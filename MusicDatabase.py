'''
Hist: 
* 20240508 JC: 
    * implementation of Music.song to create for dataFrame
    * load_dataframe now creates a new dataFrame if before non existent
    * ID's are now given uniquely and never change, even if songs added or removed
'''

import pandas as pd
import csv
from Music import Song
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

    ## everything regarding the creation of the dataframe and the saving into a .csv file

    # initialize a list to temporary store the needed information to create a dataframe
    def __init__ (self):
        self.dummy_song = Song("", "", "", "", "", "", None)  # Create a dummy Song instance
        self.music_library = self.load_dataframe()

    # load the dataframe if possible and if not then create a dataframe
    def load_dataframe(self):
        """loades the most recent version of the dataframe

        Returns:
            pandas dataframe: the current version of the pandas dataframe that stores the songs
        """
        try:
        # Load the DataFrame from the CSV file
            return pd.read_csv("music_library.csv")
        except FileNotFoundError:
            # If the file doesn't exist, create empty DataFrame with defined columns
            self.create_csv_file()
            return pd.read_csv("music_library.csv")


    # save the dataframe --> use to save the newest version after adding or removing the songs
    def save_dataframe(self, df):
        """ Save the dataframe to a .csv file so that we can save the most recent state of the dataframe

        Args:
            df (pandas dataframe): music library dataframe
        """
        df.to_csv("music_library.csv", index=False)

    # create csv file or not if it already exists
    def create_csv_file(self):
        """Creates an empty music_library.csv file with headers based on the attributes of the Song class."""
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
    
    
    # every function regarding changing the dataframe, like adding and removing songs

    # add a song to the library
    def add_song(self, song: Song):

        if len(self.music_library) > 0:
            song.id = self.music_library['id'].max() + 1
        else:
            song.id = 1

         # Append the song information to the DataFrame
        self.music_library = self.music_library.append(vars(song), ignore_index=True)
        # Save the updated DataFrame
        self.save_dataframe(self.music_library)

        '''
        Old Code
        
        """Add a new song to the music library."""
    # Get user input with validation
        song_info = self.get_user_input()
        if not song_info:
            return  # User cancelled or invalid input
        # Unpack the validated song information
        title, artist, genre, year, album, file_path = song_info

        # Create a dictionary with the song information
        new_song = {'id': None,  # Will be assigned automatically by most databases
             'title': title,
             'artist': artist,
             'genre': genre,
             'year': year,
             'album': album,
             'file_path': file_path}

       # add  new song as a row to the existing DataFrame
        self.music_library = pd.concat([self.music_library, pd.DataFrame(new_song, index=[0])], ignore_index=True)

        # Assign the row index (new ID) to the 'id' column
        self.music_library['id'] = self.music_library.index

        # Save the updated DataFrame to the CSV file (important to persist changes)
        self.save_dataframe(self.music_library)

        addMore = input("do you want to add another song: y/n")
        if addMore == 'y':
            self.add_song()
        '''

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
        self.music_library = self.music_library[self.music_library['title'] != title]
        self.save_dataframe(self.music_library)

    def get_song(self, id):
        """search for a specific song depending on the id passed throuh

        Args:
            id (int): id that is specific to the song searched for

        Returns:
            dict or None: A dictionary containing the information of the song if found,
            with keys "ID", "Title", "Artist", "Genre", "Year", "Album", and "File_Path".
            Returns None if the song with the specified ID is not found.
        """
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