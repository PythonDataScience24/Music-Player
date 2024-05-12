'''
Song Class:
Represents an individual song with attributes such as title, artist, genre, release year,
album, file path, and an optional unique identifier.

Attributes:
    title (str): The title of the song.
    artist (str): The artist of the song.
    genre (str): The genre of the song.
    year (int): The release year of the song.
    album (str): The album of the song.
    file_path (str): The file path of the song.
    id (int): The unique identifier of the song. Defaults to None.

Methods:
    __init__: Initializes a Song object with the provided attributes.
    play_song: play the chosen song
    pause_song: pause the song and be able to play it again
    stop_song: stop playing the song alltogether without being able to start it again
    set_position: enable the user to play a song at a certain point
    next_song: skip to the next song in a queue
    previous_song: go back to the previous song played
    volume: amplify the volume of the song playing
'''

import sounddevice as sd
import numpy as np
from scipy.io.wavfile import read

# Default sample rate for playback
DEFAULT_SAMPLE_RATE = 44100


class Song:
    def __init__ (self, title, artist, genre, year, album, file_path, id = None):
        self.title = title
        self.artist = artist
        self.genre = genre
        self.year = year
        self.album = album
        self.file_path = file_path
        self.id = id
        self.audio_data = None
        self.sample_rate = DEFAULT_SAMPLE_RATE
        self.paused = False
        self.current_position = 0


    def play_song(self):
        #check if the state of paused is false if it is so then we play the song
        if self.paused:
            sd.play(self.audio_data, self.sample_rate, start=int(self.current_position * DEFAULT_SAMPLE_RATE))
            self.paused = False
            print("Resuming playback:", self.title)
        else:
            try:
                if not self.audio_data:
                    _, self.audio_data = read(self.file_path)
                sd.play(self.audio_data, self.sample_rate)
                print("Now playing:", self.title)
            except Exception as e:
                print(f"Error occurred while playing {self.title}: {e}")

    def pause_song(self):       #Hier kann pausiert oder fortgesetzt werden
        if not self.paused:
            sd.stop()
            self.paused = True
            print("Song paused:", self.title)

    # here the song playing gets killed off
    def stop_song(self):        
        sd.stop()
        self.paused = False
        self.current_position = 0
        print("Playback stopped:", self.title)

    # Position (in einer Progressbar) verändern - Achtung: geht nur für mp3
    def set_position(self, value : float):
        if value < 0 or value > 1:
            raise ValueError("Position value must be between 0 and 1.")
        self.current_position = value
        if not self.paused:
            self.stop_song()
            self.play_song()

    
    # def song_queue(song: mdb.Song):
    # Hier jeweils den nächsten Song in die Queue einfügen? Oder ist das obsolet


    # def next_song():
    #     pass

    # def previous_song():
    #     pass

    # To set the volume
    def volume(self, value: int):
        if value < 0 or value > 100:
            raise ValueError("Volume value must be between 0 and 100.")
        scale_factor = value / 100.0
        self.audio_data = np.multiply(self.audio_data, scale_factor)
        if not self.paused:
            self.stop_song()
            self.play_song()