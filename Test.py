from MusicDatabase import MusicDatabase
import pandas as pd

# Create a MusicDatabase instance
music_db = MusicDatabase()

# Check if a dataframe is created and has expected columns
if isinstance(music_db.music_library, pd.DataFrame):
    # Check if the dataframe has the expected columns
    if all(col in music_db.music_library.columns for col in ['id', 'title', 'artist', 'genre', 'year', 'album', 'file_path']):
        print("Dataframe created successfully!")
    else:
        print("Dataframe has incorrect columns.")
else:
    print("Failed to create dataframe.")

# Add the song to the database
music_db.add_song()

# Print the entire dataframe to verify the song was added
print(music_db.music_library)
