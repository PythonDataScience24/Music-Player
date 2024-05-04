import pandas as pd
from Music import Music
from dataframeManipulation import filter_dataframe

# in this file we set up the database/dataframe and save it. This will be the anchor point of the other files/functions

# to dos:
# create a way to play the songs
# filtering options --> can be expanded on --> bare bones works
# skip and rewind options
# amplifying of songs
# eq's (?)
# maybe even implement the album covers? user must upload .jpg/.png file themselves --> else if they dont do that add a placeholder

class MusicDatabase:
    # initialize a list to temporary store the needed information to create a dataframe
    def __init__ (self):
        self.music_library = []

    def get_user_input(self):
        """Prompts the user for song information and performs basic validation."""
        title = input("Enter title: ")
        # make sure that it is not empty
        if not title:
            print("Title cannot be empty.")
            return None
        # get further information
        artist = input("Enter artist name: ")
        genre = input("Enter genre: ")
        year = input("Enter year (leave blank if unknown): ")
        # make sure that the year is an int, so that the data manipulation is easier
        try:
            year = int(year) if year else None  # Convert to int if provided
        except ValueError:
            print("Invalid year format.")
            return None

        album = input("Enter the album: ")
        file_path = input("Enter path to the music file: ")

        # Additional checks for file existence could be added here
        return title, artist, genre, year, album, file_path

    def add_song(self):
        """use user input to save a song and create a Music Object"""
        user_input = self.get_user_input()
        if user_input:
            title, artist, genre, year, album, file_path = user_input
            new_song = Music(title, artist, genre, year, album, file_path)
            self.music_library.append(new_song)

    def remove_song(self):
        """TODO: Remove a song from the music library."""
        #title = input("Enter the title of the song to remove: ")
        #self.music_library = [song for song in self.music_library if song.title != title]


    def create_dataframe(self):
        """Creates a DataFrame from the Music objects in the library."""
        data = [
            {"Title": song.title, "Artist": song.artist, "Genre": song.genre,
             "Year": song.year, "Album": song.album, "File_Path": song.file_path}
            for song in self.music_library
        ]
        return pd.DataFrame(data)
    
    def save_dataframe(self, df):
        """TODO: Saves the DataFrame to a CSV file."""
        #df.to_csv("music_library.csv", index=False)

    def load_dataframe(self):
        """TODO: Load the DataFrame from a CSV file."""
        #return pd.read_csv("music_library.csv")

    def get_song(self, id):
        """TODO: Retrieve a song from the library by its ID."""
        #return song.title, song.artist, song.genre, song.year, song.album, song.file_path

