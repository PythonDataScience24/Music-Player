### we store all the information of how the music needs to be structured here. isolated class for clarity:
class Music:
    """this class represents one song and all the info this object can carry
    """
    def __init__ (self, title, artistName, genre, date, album ):
        self.title = title
        self.artistName = artistName
        self.genre = genre
        self.date = date
        self.album = album