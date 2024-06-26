import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import read
import csv
import pandas as pd
from Song import Song
import os

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
        self.csv_file_path = os.path.dirname(os.path.abspath(__file__)) + "/music_library.csv"
        self.dummy_song = Song(title="", artist= "", genre="", year="", album="", file_path="", id=None)  # Create a dummy Song instance
        # set up the music library --> load an existing dataframe or create a new one
        self.music_library = self.load_dataframe()
        self.df = self.music_library
        self.filterdf(self.dummy_song)
        

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
            return pd.read_csv(self.csv_file_path)
        except FileNotFoundError:
            # If the file doesn't exist, create empty DataFrame with defined columns
            self.create_csv_file()
            return pd.read_csv(self.csv_file_path)


    # save the dataframe --> use to save the newest version after adding or removing the songs
    def save_dataframe(self, df):
        '''
        Saves the DataFrame to a .csv file.

        Args:
            df (pandas dataframe): The music library DataFrame.
        '''
        df.to_csv(self.csv_file_path, index=False)

    # create csv file or not if it already exists
    def create_csv_file(self):
        '''
        Creates an empty music_library.csv file with headers based on the attributes of the Song class
        '''
        headers = vars(self.dummy_song).keys()  # Get attributes of the dummy Song instance
        try:
            with open(self.csv_file_path, 'x', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=headers)
                writer.writeheader()
        except FileExistsError:
            # Check if the file is empty
            with open(self.csv_file_path, 'r') as file:
                if not file.read(1):
                    # File is empty, write headers
                    with open(self.csv_file_path, 'w', newline='') as file:
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
      
    # only terminal (later uses not needed)
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
        self.filterdf(self.dummy_song)
        for _, row in self.df.iterrows():
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
    
    def filterdf(self, song: Song):
        self.df = self.music_library
        self.dummy_song = song
        if song.title is not None and song.title != "":
            self.df = self.df[self.df['title'] == song.title]
        if song.artist is not None and song.artist != "":
            self.df = self.df[self.df['artist'] == song.artist]
        if song.genre is not None and song.genre != "":
            self.df = self.df[self.df['genre'] == song.genre]
        if song.year is not None and song.year != "":
            self.df = self.df[self.df['year'] == song.year]
        if song.album is not None and song.album != "":
            self.df = self.df[self.df['album'] == song.album]

    def get_song_info(self, id):
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
        
    # don't think we need this method
    def get_song (self, id):
        """this method fetches the requested song

        Args:
            id (int): id of a song that corresponds to an id within the dataframe

        Returns:
            song (Song): song object that matches the id
        """
        id = int(id)
    
        # Search for the song with the given ID in the music library DataFrame
        song_data = self.music_library[self.music_library['id'] == id]
    
        # Check if the song exists
        if not song_data.empty:
            # Extract song attributes from the DataFrame
            song_attributes = song_data.iloc[0].to_dict()
        
            # Create and return a Song object
            return Song(
                title=song_attributes['title'],
                artist=song_attributes['artist'],
                genre=song_attributes['genre'],
                year=song_attributes['year'],
                album=song_attributes['album'],
                file_path=song_attributes['file_path'],
                id=song_attributes['id']
            )
        return None
    
    def plot_song (self, song):
        # max time of 10 seconds to be plotted
        max_time = 10
        # assign audio_data to the song object and then assign it to the data to plot
        song.audio_data = read(song.file_path)
        sound_data = song.audio_data
        # calculate the length of the song
        song_length = len(sound_data) / song.sample_rate

        # Select data for plotting based on max_time
        num_samples = int(min(song_length, max_time) * song.sample_rate)
        plot_data = sound_data[:num_samples]

        # define time_axis based on max_time
        time_axis = np.linspace(0, max_time, len(plot_data))
        
        #create the plot
        # Create the plot
        plt.plot(time_axis, plot_data)
        plt.xlabel("Time (seconds)")
        plt.ylabel("Amplitude")
        plt.title(f"Waveform of {song.title} (Limited to {max_time} seconds)")
        plt.xlim(0, max_time)
        plt.grid(True)
        plt.show()


    def plot_song_frame(self, song):
        # max time of 10 seconds to be plotted
        max_time = 10

        # assign audio_data to the song object and then assign it to the data to plot
        song.audio_data = read(song.file_path)[1]
        sound_data = song.audio_data

        # calculate the length of the song
        song_length = len(sound_data) / song.sample_rate

        # Select data for plotting based on max_time
        num_samples = int(min(song_length, max_time) * song.sample_rate)
        plot_data = sound_data[:num_samples]

        # define time_axis based on max_time
        time_axis = np.linspace(0, max_time, len(plot_data))

        # Create the plot
        fig, ax = plt.subplots()
        ax.plot(time_axis, plot_data)
        ax.set_xlabel("Time (seconds)")
        ax.set_ylabel("Amplitude")
        ax.set_title(f"Waveform of {song.title} (Limited to {max_time} seconds)")
        ax.set_xlim(0, max_time)
        ax.grid(True)

        return fig
