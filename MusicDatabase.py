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
        self.music_library = self.load_dataframe()


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

    def add_song(self): #TODO probably best if function can be called with a Music object as argument.
        """use user input to save a song and create a Music Object"""
        user_input = self.get_user_input()
        if user_input:
            title, artist, genre, year, album, file_path = user_input
            new_id = len(self.music_library) + 1  # generate ID for song
            new_song = Music(title, artist, genre, year, album, file_path)
            self.music_library = self.music_library.append(pd.DataFrame([{
                "ID": new_id,
                "Title": new_song.title,
                "Artist": new_song.artist,
                "Genre": new_song.genre,
                "Year": new_song.year,
                "Album": new_song.album,
                "File_Path": new_song.file_path
            }]), ignore_index=True)
            self.save_dataframe(self.music_library)

    def remove_song(self, title): #TODO delete by id instead of title
        """removes song from dataframe and saves the current dataframe after removing

        Args:
            title (string): title of the song to be removed
        """
        self.music_library = self.music_library[self.music_library['Title'] != title]
        self.save_dataframe(self.music_library)


    def create_dataframe(self):
        """Creates a DataFrame from the Music objects in the library."""
        data = [
            {"ID": i + 1,  # Adding 1 to make IDs start from 1
             "Title": song.title, 
             "Artist": song.artist, 
             "Genre": song.genre,
             "Year": song.year, 
             "Album": song.album, 
             "File_Path": song.file_path}
            for i, song in enumerate(self.music_library)
        ]
        return pd.DataFrame(data)
    
    
    def remove_song (self, title):
        self.music_library = self.music_library[self.music_library['Title'] != title]
        return self.save_dataframe (self.music_library)
    
    def save_dataframe(self, df):
        """ Save the dataframe to a .csv file so that we can save the most recent state of the dataframe

        Args:
            df (pandas dataframe): music library dataframe
        """
        df.to_csv("music_library.csv", index=False)

    def load_dataframe(self):
        """loades the most recent version of the dataframe

        Returns:
            pandas dataframe: the current version of the pandas dataframe that stores the songs
        """
        try:
            return pd.read_csv("music_library.csv")
        except:
            return pd.DataFrame()


    def get_song(self, id):
        """search for a specific song depending on the id passed throuh

        Args:
            id (int): id that is specific to the song searched for

        Returns:
            dict or None: A dictionary containing the information of the song if found,
            with keys "ID", "Title", "Artist", "Genre", "Year", "Album", and "File_Path".
            Returns None if the song with the specified ID is not found.
        """
        song = self.music_library[self.music_library['ID'] == id]
        if not song.empty:
            return {
                "Title": song['Title'].iloc[0],
                "Artist": song['Artist'].iloc[0],
                "Genre": song['Genre'].iloc[0],
                "Year": song['Year'].iloc[0],
                "Album": song['Album'].iloc[0],
                "File_Path": song['File_Path'].iloc[0]
            }
        else:
            return None