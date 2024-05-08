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
'''

class Song:
    def __init__ (self, title, artist, genre, year, album, file_path, id = None):
        self.title = title
        self.artist = artist
        self.genre = genre
        self.year = year
        self.album = album
        self.file_path = file_path
        self.id = id