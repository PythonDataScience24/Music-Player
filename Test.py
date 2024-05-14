import pandas as pd
import time
from MusicDatabase import MusicDatabase
from dataframeManipulation import filter_dataframe

# Create a MusicDatabase instance
music_db = MusicDatabase()

def checkIfDataframeExists (): 
    # Check if a dataframe is created and has expected columns 
    if isinstance(music_db.music_library, pd.DataFrame):
        # Check if the dataframe has the expected columns
        if all(col in music_db.music_library.columns for col in ['id', 'title', 'artist', 'genre', 'year', 'album', 'file_path']):
          print("Dataframe created successfully!")
        else:
           print("Dataframe has incorrect columns.")
    else:
       print("Failed to create dataframe.")

def DataframeManipulation ():
    keep_loop = True

    while keep_loop:
       
        # # Add the song to the database
        song = music_db.get_song_to_add()
        music_db.add_song(song= song)

        # Print the entire dataframe to verify the song was added
        print(music_db.music_library)
        # songToRemove = input('Enter the ID of the song you want to remove: ')
        # music_db.remove_song(songToRemove)
        # print(music_db.music_library)

        filtered_df = filter_dataframe(music_db.music_library)
        print(filtered_df)

        decision = input("you want to keep testing? (y/n)")
        if decision == 'n':
          keep_loop = False


def play_function_tests ():
    try:
        # Retrieve song object from database (assuming successful retrieval)
        song = music_db.get_song(1)

        # Check if song has a valid file path
        if song.file_path:
            song.play_song()
        else:
          print("Song object doesn't have a valid file path")
    except Exception as e:
      print(f"Error occurred while getting or playing song: {e}")




# checkIfDataframeExists()
# DataframeManipulation()
play_function_tests()
