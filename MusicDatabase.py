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
        self.music_library = self.create_dataframe()
        self.create_csv_file()


    # set up the dataframe:
    def create_dataframe(self):
        """Creates an empty DataFrame library."""
        columns = ['id', 'title', 'artist', 'genre', 'year', 'album', 'file_path']
        df = pd.DataFrame(columns=columns)
        return df
    
    # create csv file or not if it already exists
    def create_csv_file(self):
        """Creates an empty music_library.csv file if it doesn't exist."""
        try:
            with open("music_library.csv", 'x'):
                pass  # Create the file if it doesn't exist
        except FileExistsError:
            pass  # File already exists, do nothing
    
    # add a song to the library
    def add_song(self):
        """Add a new song to the music library."""
        user_input = self.get_user_input()
        if user_input:
            title, artist, genre, year, album, file_path = user_input
            new_id = len(self.music_library) + 1  # Generate ID for song
            new_song_data = {
                "id": new_id,
                "title": title,
                "artist": artist,
                "genre": genre,
                "year": year,
                "album": album,
                "file_path": file_path
            }
            # Append the new song data to the music library DataFrame
            self.music_library = self.music_library.append(new_song_data, ignore_index=True)
            # Save the updated DataFrame
            self.save_dataframe(self.music_library)

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

    def remove_song(self, title):
        """removes song from dataframe and saves the current dataframe after removing
        Args:
            title (string): title of the song to be removed
        """
        self.music_library = self.music_library[self.music_library['Title'] != title]
        self.save_dataframe(self.music_library)
    
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
        # Load the DataFrame from the CSV file
            df = pd.read_csv("music_library.csv")
            return df
        except FileNotFoundError:
            # If the file doesn't exist, return an empty DataFrame with defined columns
            return pd.DataFrame(columns=["ID", "Title", "Artist", "Genre", "Year", "Album", "File_Path"])


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