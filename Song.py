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

# Current position of the song in seconds
current_position = 0

# Flag to check if the song is paused
paused = False

current_position = 0 #Current position of the song in seconds --> For a progress bar/slider (let the progress bar change this value? Or Let  user Input change it?)
paused = False     #Flag to check if the song is paused

class Song:
    def __init__ (self, title, artist, genre, year, album, file_path, id = None):
        self.title = title
        self.artist = artist
        self.genre = genre
        self.year = year
        self.album = album
        self.file_path = file_path
        self.id = id


    def play_song(self):
        global paused, current_position
        #check if the state of paused is false if it is so then we play the song
        if paused:
            sd.play(self.audio_data, self.sample_rate, start=int(current_position * self.sample_rate))
            paused = False
        else:
        # Read audio data from file and assign it to song.audio_data
        # Discard the sample rate returned by read() using the underscore 
            _, self.audio_data = read(self.file_path)
            self.sample_rate = DEFAULT_SAMPLE_RATE  # Set default sample rate
            sd.play(self.audio_data, self.sample_rate)
            paused = False
        print("Now playing:", self.title)

    def pause_song(self):       #Hier kann pausiert oder fortgesetzt werden
        global paused
        if paused:
            sd.resume()
            paused = False
        else:
            sd.pause()
            paused = True

    # here the song playing gets killed off
    def stop_song(self):        
        sd.stop()

    # Position (in einer Progressbar) verändern - Achtung: geht nur für mp3
    def set_position(self, value : float):
        global current_position
        current_position = value
        if not paused:
            sd.stop()
            self.play_song()

    
    # def song_queue(song: mdb.Song):
    # Hier jeweils den nächsten Song in die Queue einfügen? Oder ist das obsolet


    def next_song():
        pass

    def previous_song():
        pass

    # To set the volume
    def volume(self, value : int):
        # check the value if it is possible to amplify it that far 
        #--> restriction so that the user cannot make misinputs --> ask the user how many percent they want to increase it
        if value < 0 or value > 100:
            raise ValueError("Volume value must be between 0 and 100.")
    
        # Convert volume percentage to a scale factor
        scale_factor = value / 100.0
    
        # Amplify the audio data using numpy
        self.audio_data = np.multiply(self.audio_data, scale_factor)

        #   If the song is currently playing, restart playback with the new volume
        if not paused:
            sd.stop()
            self.play_song()