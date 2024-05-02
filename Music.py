### we store all the information of how the music needs to be structured here. isolated class for clarity:
class Music:
    """this class represents one song and all the info this object can carry """
    def __init__ (self, title, artist, genre, year, album, file_path):
        self.title = title
        self.artist = artist
        self.genre = genre
        self.year = year
        self.album = album
        self.file_path = file_path