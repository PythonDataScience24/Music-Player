"""
MusicDatabase Class:
A class representing a music database. This class provides methods for managing a music library stored in a DataFrame.

Attributes:
    csv_file_path (str): The file path to the CSV file storing the music library.
    dummy_song (Song): A dummy Song instance used for initializing the music library DataFrame.
    music_library (pandas DataFrame): The DataFrame storing the music library.
    df (pandas DataFrame): A reference to the filtered DataFrame used for querying.

Methods:
    __init__: Initializes a MusicDatabase instance and loads the music library DataFrame.
    load_dataframe: Loads the most recent version of the DataFrame.
    save_dataframe: Saves the DataFrame to a .csv file.
    create_csv_file: Creates an empty music_library.csv file with headers based on the attributes of the Song class.
    add_song: Adds a song to the music library DataFrame.
    remove_song: Removes a song from the DataFrame and saves the current DataFrame after removing.
    get_library: Retrieves an array of Song objects representing the songs in the music library DataFrame.
    filterdf: Filters the music library DataFrame based on the provided Song object.
    plot_song_frame: Plots the waveform of a song.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import read
import csv
import pandas as pd
from Song import Song 
import os

class MusicDatabase:
    

    def __init__ (self):
        '''
        Initializes a MusicDatabase instance.

        This method creates a dummy Song instance and loads the music library DataFrame.
        '''
        self.csv_file_path = os.path.dirname(os.path.abspath(__file__)) + "/music_library.csv"
        self.dummy_song = Song(title="", artist= "", genre="", year="", album="", file_path="", id=None)
        self.music_library = self.load_dataframe()
        self.df = self.music_library
        self.filterdf(self.dummy_song)

    def load_dataframe(self):
        '''
        Loads the most recent version of the DataFrame.

        This method attempts to load the DataFrame from the CSV file.
        If the file doesn't exist, it creates an empty DataFrame with defined columns.

        Returns:
            pandas dataframe: The current version of the DataFrame that stores the songs.
        '''
        try:
            return pd.read_csv(self.csv_file_path)
        except FileNotFoundError:
            self.create_csv_file()
            return pd.read_csv(self.csv_file_path)

    def save_dataframe(self, df):
        '''
        Saves the DataFrame to a .csv file.

        Args:
            df (pandas dataframe): The music library DataFrame.
        '''
        df.to_csv(self.csv_file_path, index=False)

    def create_csv_file(self):
        '''
        Creates an empty music_library.csv file with headers based on the attributes of the Song class.
        '''
        headers = vars(self.dummy_song).keys()
        try:
            with open(self.csv_file_path, 'x', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=headers)
                writer.writeheader()
        except FileExistsError:
            with open(self.csv_file_path, 'r') as file:
                if not file.read(1):
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
        if len(self.music_library) > 0:
            song.id = self.music_library['id'].max() + 1
        else:
            song.id = 1
        new_row = pd.DataFrame([vars(song)], columns=vars(self.dummy_song).keys())
        self.music_library = pd.concat([self.music_library, new_row], ignore_index=True)
        self.save_dataframe(self.music_library)

    def remove_song(self, id):
        '''
        Removes a song from the DataFrame and saves the current DataFrame after removing.

        Args:
            id (int): The ID of the song to be removed.
        '''
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
        '''
        Filters the music library DataFrame based on the provided Song object.

        Args:
            song (Song): The Song object used for filtering.
        '''
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

    def plot_song_frame(self, song):
        '''
        Plots the waveform of a song.

        Args:
            song (Song): The Song object for which the waveform will be plotted.

        Returns:
            matplotlib figure: The plotted waveform.
        '''
        max_time = 10
        song.audio_data = read(song.file_path)[1]
        sound_data = song.audio_data
        song_length = len(sound_data) / song.sample_rate
        num_samples = int(min(song_length, max_time) * song.sample_rate)
        plot_data = sound_data[:num_samples]
        time_axis = np.linspace(0, max_time, len(plot_data))
        fig, ax = plt.subplots()
        ax.plot(time_axis, plot_data)
        ax.set_xlabel("Time (seconds)")
        ax.set_ylabel("Amplitude")
        ax.set_title(f"Waveform of {song.title} (Limited to {max_time} seconds)")
        ax.set_xlim(0, max_time)
        ax.grid(True)
        return fig
