'''
Hist: 
* 20240508 JC: 
    * implementation of Music.song to create for dataFrame
    * load_dataframe now creates a new dataFrame if before non existent
    * ID's are now given uniquely and never change, even if songs added or removed
    * remove_song takes the unique ID
    * new def get_library(self): returns all the songs in the current dataFrame as Song objects
'''

import pandas as pd
import csv
from Song import Song

# in this file we set up the database/dataframe and save it. This will be the anchor point of the other files/functions

# to dos:
# create a way to play the songs
# filtering options --> can be expanded on --> bare bones works
# skip and rewind options
# amplifying of songs
# eq's (?)
# maybe even implement the album covers? user must upload .jpg/.png file themselves --> else if they dont do that add a placeholder

class MusicDatabase:
    '''
    Initializes a MusicDatabase instance.

    This method creates a dummy Song instance and loads the music library DataFrame.
    '''
    def __init__ (self):
        # create a dummy song with empty values
        self.dummy_song = Song(title="", artist= "", genre="", year="", album="", file_path="", id=None)  # Create a dummy Song instance
        # set up the music library --> load an existing dataframe or create a new one
        self.music_library = self.load_dataframe()

    # load the dataframe if possible and if not then create a dataframe
    def load_dataframe(self):
        '''
        Loads the most recent version of the DataFrame.

        This method attempts to load the DataFrame from the CSV file.
        If the file doesn't exist, it creates an empty DataFrame with defined columns.

        Returns:
            pandas dataframe: The current version of the DataFrame that stores the songs.
        '''
        try:
        # Load the DataFrame from the CSV file
            return pd.read_csv("music_library.csv")
        except FileNotFoundError:
            # If the file doesn't exist, create empty DataFrame with defined columns
            self.create_csv_file()
            return pd.read_csv("music_library.csv")


    # save the dataframe --> use to save the newest version after adding or removing the songs
    def save_dataframe(self, df):
        '''
        Saves the DataFrame to a .csv file.

        Args:
            df (pandas dataframe): The music library DataFrame.
        '''
        df.to_csv("music_library.csv", index=False)

    # create csv file or not if it already exists
    def create_csv_file(self):
        '''
        Creates an empty music_library.csv file with headers based on the attributes of the Song class
        '''
        headers = vars(self.dummy_song).keys()  # Get attributes of the dummy Song instance
        try:
            with open("music_library.csv", 'x', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=headers)
                writer.writeheader()
        except FileExistsError:
            # Check if the file is empty
            with open("music_library.csv", 'r') as file:
                if not file.read(1):
                    # File is empty, write headers
                    with open("music_library.csv", 'w', newline='') as file:
                        writer = csv.DictWriter(file, fieldnames=headers)
                        writer.writeheader()
    
    
    ## Functions for changing the DataFrame

    def add_song(self, song: Song):
        '''
        Adds a song to the music library DataFrame.

        Args:
            song (Song): The Song object to be added to the music library.
        '''

        # Assign a unique ID to the song
        if len(self.music_library) > 0:
            song.id = self.music_library['id'].max() + 1
        else:
            song.id = 1
           
        # Create a new DataFrame with the song data
        new_row = pd.DataFrame([vars(song)], columns=vars(self.dummy_song).keys())
        
        # Append the new row to the music_library DataFrame
        self.music_library = pd.concat([self.music_library, new_row], ignore_index=True)
        
        # Save the updated DataFrame
        self.save_dataframe(self.music_library)
      
    # function that gets information from the user to add a certain song. will be used in combination with add_song
    def get_song_to_add(self):
        """ Prompts the user to input the file path of a .wav file and returns a Song instance with metadata.

        Returns:
            _type_: _description_
        """
        
        file_path = input("Enter the file path of the .wav file: ")
        song = Song(title="", artist="", genre="", year="", album="", file_path=file_path)

        # Prompt user for missing information
        song.title = input("Enter the song title (or leave blank): ")
        song.artist = input("Enter the artist name (or leave blank): ")
        song.genre = input("Enter the genre (or leave blank): ")
        song.year = input("Enter the release year (or leave blank): ")
        song.album = input("Enter the album name (or leave blank): ")

        return song


    def remove_song(self, id):
        '''
        Removes a song from the DataFrame and saves the current DataFrame after removing.

        Args:
            id (int): The ID of the song to be removed.
        '''
        # create an int out of the string that is passed through, so that the comparison works properly
        id = int(id)
        self.music_library = self.music_library[self.music_library['id'] != id]
        self.save_dataframe(self.music_library)

    def get_library(self):
        '''
        Retrieves an array of Song objects representing the songs in the music library DataFrame.

        Returns:
            List[Song]: An array of Song objects.
        '''
        library = []
        for index, row in self.music_library.iterrows():
            song = Song(
                row['title'],
                row['artist'],
                row['genre'],
                row['year'],
                row['album'],
                row['file_path'],
                row['id']
            )
            library.append(song)
        return library

    def get_song(self, id):
        '''
        Searches for a specific song based on the ID.

        Args:
            id (int): The ID of the song to be searched.

        Returns:
            dict or None: A dictionary containing the information of the song if found.
            Returns None if the song with the specified ID is not found.
        '''
        song = self.music_library[self.music_library['id'] == id]
        if not song.empty:
            return {
                "title": song['title'].iloc[0],
                "artist": song['artist'].iloc[0],
                "genre": song['genre'].iloc[0],
                "year": song['year'].iloc[0],
                "album": song['album'].iloc[0],
                "file_path": song['file_path'].iloc[0]
            }
        else:
            return None