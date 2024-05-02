import pandas as pd
from Music import Music
from MusicDatabase import get_user_input, add_song
from dataframeManipulation import filter_dataframe


# Test data for Music class
test_data = [
    ("Song1", "Artist1", "Genre1", 2020, "Album1", "path/to/song1.mp3"),
    ("Song2", "Artist2", "Genre2", 2021, "Album2", "path/to/song2.mp3"),
    ("Song3", "Artist1", "Genre1", 2019, "Album3", "path/to/song3.mp3"),
]

# Create a list of Music objects
music_library = []
for title, artist, genre, year, album, file_path in test_data:
    music_library.append(Music(title, artist, genre, year, album, file_path))


def create_test_dataframe():
    """Creates a test dataframe from the music_library"""
    data = {
        "Title": [],
        "Artist": [],
        "Genre": [],
        "Year": [],
        "Album": [],
        "File_Path": [],
    }

    for song in music_library:
        data["Title"].append(song.title)
        data["Artist"].append(song.artist)
        data["Genre"].append(song.genre)
        data["Year"].append(song.year)
        data["Album"].append(song.album)
        data["File_Path"].append(song.file_path)

    return pd.DataFrame(data=data)


def test_filter():
    """Tests exiting the filter menu"""
    df = create_test_dataframe()
    original_df = df.copy()
    filtered_df = filter_dataframe(df.copy())
    print("Original Dataframe:")
    print(original_df)
    print("\nDataframe after exiting filter menu:")
    print(filtered_df)
    # add_more_songs(df=df)
    # print(df)
    # print(filtered_df)

# def add_more_songs(df):
#     """Allows adding more songs to the existing dataframe

#     Args:
#         df (pandas.DataFrame): The existing dataframe containing song information

#     Returns:
#         pandas.DataFrame: The updated dataframe with new songs added
#     """
#     while True:
#         add_song = input("Do you want to add another song? (y/n): ")
#         if add_song.lower() != "y":
#             break

#         title, artist, genre, year, album, file_path = get_user_input()

#         # Create a new Music object with the user input
#         new_song = Music(title, artist, genre, year, album, file_path)
#         music_library.append(new_song)  # Add the new song to the music_library list

#         # Create a new dictionary to store the new song information
#         new_song_data = {
#             "Title": [new_song.title],
#             "Artist": [new_song.artist],
#             "Genre": [new_song.genre],
#             "Year": [new_song.year],
#             "Album": [new_song.album],
#             "File_Path": [new_song.file_path],
#         }

#         # Append the new song data to the existing dataframe using pd.concat
#         df = pd.concat([df, pd.DataFrame(new_song_data)], ignore_index=True)

#     return df

test_filter()