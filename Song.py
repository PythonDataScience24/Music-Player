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

''' use player instead of this so no need for later uses
import sounddevice as sd
import numpy as np
from scipy.io.wavfile import read

    # this is a super long method so i just used helper methods for increased readablity
    # def play_song(self):
    #     #check if the state of paused is false if it is so then we play the song
    #     if self.paused:
    #         sd.play(self.audio_data, self.sample_rate, start=int(self.current_position * DEFAULT_SAMPLE_RATE))
    #         self.paused = False
    #         print("Resuming playback:", self.title)
    #     else:
    #         try:
    #             if not self.audio_data:
    #                 sample_rate, audio_data = read(self.file_path)
    #                 self.audio_data = audio_data.astype(np.float32)  # Convert to float32 for compatibility with sounddevice
    #                 self.sample_rate = sample_rate
    #             sd.play(self.audio_data, self.sample_rate)
    #             print("Now playing:", self.title)

    #              # Calculate duration of the audio file
    #             duration_seconds = len(self.audio_data) / self.sample_rate

    #             # Wait for the duration of the song
    #             time.sleep(duration_seconds)
    #         except Exception as e:
    #             print(f"Error occurred while playing {self.title}: {e}")

    def play_song(self):
        """Handle how a song should be played. Resume it or start an entirely new song. play a song using the helper methods to load data
        and play it
        """
        if self.paused:
            # If song is paused, resume playback from current position
            start_sample = int(self.current_position * self.sample_rate)
            sd.play(self.audio_data[start_sample:], self.sample_rate)
            self.paused = False
            print("Resuming playback:", self.title)
        else:
            # if there is no song paused start up a new song and play it!
            self.load_audio_data()  # Load audio data if not already loaded
            self.play_audio()  # Play the song

    def load_audio_data(self):
        """this method loads the audio data and normalizes it. It converts the data to 32float.
        """
        try:
            if not self.audio_data:
                # Reads the audio file
                sample_rate, audio_data = read(self.file_path)
                # convert the audio data to a float32 to assure the compatibility with the sounddevice extension
                self.audio_data = audio_data.astype(np.float32)
                self.sample_rate = sample_rate

                # Normalize the audio data to the range [-1, 1]
                # we normalize to prevent clipping of the sound and to regulate the noise to sound ratio to regulate the clarity of the playback
                max_val = np.max(np.abs(self.audio_data))
                if max_val > 1:
                    self.audio_data /= max_val

        except Exception as e:
            print(f"Error occurred while loading audio data for {self.title}: {e}")
    
    # def play_audio(self):
    #     """this method plays the audio of a song instance.
    #     """
    #     try:
    #         # play the audio using sounddevice play function 
    #         sd.play(self.audio_data, self.sample_rate)
    #         print("Now playing:", self.title)

    #         # Calculate duration of the audio file
    #         duration_seconds = len(self.audio_data) / self.sample_rate

    #         # Wait for the duration of the song
    #         time.sleep(duration_seconds)

    #     except Exception as e:
    #         print(f"Error occurred while playing {self.title}: {e}")
    def play_audio(self):
        """This method plays the audio of a song instance."""
        try:
            # Play the audio using sounddevice play function
            sd.play(self.audio_data, self.sample_rate)
            print("Now playing:", self.title)
        except Exception as e:
            print(f"Error occurred while playing {self.title}: {e}")


    def pause_song(self):       #Hier kann pausiert oder fortgesetzt werden
        """pause the currently playing song!
        """
        if not self.paused:
            sd.stop()
            self.paused = True
            print("Song paused:", self.title)

    # here the song playing gets killed off
    def stop_song(self):
        """playback of a song is terminated without the ability to resume the song
        """
        sd.stop()
        self.paused = False
        self.current_position = 0
        print("Playback stopped:", self.title)

    # Position (in einer Progressbar) verändern - Achtung: geht nur für mp3
    def set_position(self, value : float):
        """set position of playback and make the song playback skip to that point

        Args:
            value (float): value where we want to start the new playback

        Raises:
            ValueError: if the value is not within the bounds we cannot skip the song position to that part
        """
        if value < 0 or value > 1:
            raise ValueError("Position value must be between 0 and 1.")
        position_samples = int(value * len(self.audio_data))
        # Set the current position
        self.current_position = position_samples / self.sample_rate
        if not self.paused:
            self.pause_song()  # Pause the song at the current position
            self.play_song()   # Resume playback from the new position

    # def song_queue(song: mdb.Song):
    # Hier jeweils den nächsten Song in die Queue einfügen? Oder ist das obsolet


    # def next_song():
    #     pass

    # def previous_song():
    #     pass

    # To set the volume
    def volume(self, value: int):
        """increase or decrease the volume of the playback

        Args:
            value (int): how much to increase of decrease the value

        Raises:
            ValueError: error if the value is not within the proper range
        """
        if value < 0 or value > 100:
            raise ValueError("Volume value must be between 0 and 100.")
        scale_factor = value / 100.0
        self.audio_data = np.multiply(self.audio_data, scale_factor)
        if not self.paused:
            self.stop_song()
            self.play_song()
'''