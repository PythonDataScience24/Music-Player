"""
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
    audio_data (numpy.ndarray): The audio data of the song, initialized as None.
    sample_rate (int): The sample rate of the song, defaulting to 44100 Hz.
    paused (bool): A flag indicating if the song is currently paused.
    current_position (int): The current playback position in the audio data.

Methods:
    __init__: Initializes a Song object with the provided attributes.
    play_song: Plays the chosen song from the current position.
    pause_song: Pauses the song and can resume playback from the same position.
    stop_song: Stops playing the song altogether and resets the position.
    set_position: Sets the playback position to a specific point in the song.
    next_song: Skips to the next song in a queue.
    previous_song: Goes back to the previous song played.
    volume: Adjusts the volume of the song playing.
"""

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
