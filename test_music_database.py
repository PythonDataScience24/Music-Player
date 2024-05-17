import unittest
import os
import pandas as pd
from Song import Song
from MusicDatabase import MusicDatabase

class TestMusicDatabase (unittest.TestCase):
    """This class tests the music database environment and checks if everything works appropriately

    Args:
        unittest: different kinds of unittests
    """
    # make sure that the database and .csv is clean so that we can test properly
    def setUp(self):
        self.db = MusicDatabase()
        if os.path.exists("music_library.csv"):
            os.remove("music_library.csv")
        self.db.create_csv_file()
    # clean the files again after testing
    def tearDown(self) -> None:
        if os.path.exists("music_library.csv"):
            os.remove("music_library.csv")

    #test if the creation of a dataframe is working correctly
    def test_initialization_and_csv_creation(self):
        self.assertTrue(os.path.exists("music_library.csv"))
        df = self.db.load_dataframe()
        self.assertTrue(df.empty)

    #test if adding a song works
    def test_add_song (self):
        song = Song(title="Song1", artist="Artist1", genre="Genre1", year="2024", album="Album1", file_path="test_path.wav")
        self.db.add_song(song)
        df = self.db.load_dataframe()
        #is there an entry?
        self.assertEqual(len(df), 1)
        # check if entry 1 is actually the value we assigned
        self.assertEqual(df['title'][0], "Song1")

    #test if a song can be removed by id
    def test_remove_song (self):
        #add a song
        song = Song(title="Test Song", artist="Test Artist", genre="Test Genre", year="2024", album="Test Album", file_path="test_path.wav")
        self.db.add_song(song)
        # get the id through splicing the dataframe and then grabbing the id value
        song_id = self.db.music_library['id'][0]
        # call the removal function
        self.db.remove_song(song_id)
        # fetch the newly changed csv file
        df = self.db.load_dataframe()
        self.assertTrue(df.empty)
    
    # Test filtering a dataframe and see if the output is correct
    def test_filter_df(self):
        # create 2 song instances to add to the dataframe
        song1 = Song(title="Test Song 1", artist="Test Artist", genre="Test Genre", year="2024", album="Test Album", file_path="test_path1.wav")
        song2 = Song(title="Test Song 2", artist="Test Artist", genre="Test Genre", year="2024", album="Test Album", file_path="test_path2.wav")
        # add the songs
        self.db.add_song(song1)
        self.db.add_song(song2)
        # song to filter to and save the filtered dataframe
        filter_song = Song(title="Test Song 1", artist="", genre="", year="", album="", file_path="")
        self.db.filterdf(filter_song)
        filtered_df = self.db.df
        # check if the filtered dataframe has the length one, as we removed one song
        self.assertEqual(len(filtered_df), 1)
        self.assertEqual(filtered_df['title'].iloc[0], "Test Song 1")
    
    # test if we can get the right information of the according song instance
    def test_get_song_info(self):
        # add song instance to the dataframe
        song = Song(title="Test Song", artist="Test Artist", genre="Test Genre", year="2024", album="Test Album", file_path="test_path.wav")
        self.db.add_song(song)
        # grab the song_id and _info
        song_id = self.db.music_library['id'][0]
        song_info = self.db.get_song_info(song_id)
        # check if the info is existent and if it is correct
        self.assertIsNotNone(song_info)
        self.assertEqual(song_info['title'], "Test Song")
        self.assertEqual(song_info['artist'], "Test Artist")

if __name__ == "__main__":
    unittest.main()
    