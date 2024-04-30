from Music import Music
import pandas as pd

# to dos:
# create a way to play the songs
# filtering options
# skip and rewind options
# amplifying of songs
# eq's (?)
# maybe even implement the album covers? user must upload .jpg/.png file themselves --> else if they dont do that add a placeholder

class MusicDatabase:
    # initialize a list to temporary store the needed information to create a dataframe
    def __init__ (self):
        self.music_library = []

    def add_song(self):
        """use user input to save a song and create a Music Object"""
        # gather the information we need for a Music Object
        title = input("Enter title: ")
        artist = input("Enter artist name: ")
        genre = input("Enter genre: ")
        year = input("Enter year (leave blank if unknown): ")
        file_path = input("Enter path to the music file: ")

        new_song = Music(title, artist, genre, year, file_path)
        self.music_library.append(new_song)

    def create_dataframe(self):
        """create a dataframe out of the created library"""
        data = {
            "Title": [],
            "Artist": [],
            "Genre": [],
            "Year": [],
            "File_Path": []
        }
        # append the data
        for song in self.music_library:
            data["Title"].append(song.title)
            data["Artist"].append(song.artist)
            data["Genre"].append(song.genre)
            data["Year"].append(song.year)
            data["File_Path"].append(song.file_path)
        
        df = pd.DataFrame(data= data)
        return df


if __name__ == "__main__":
    # Code inside this block will only execute when the script is run directly
    music_db = MusicDatabase()

    # Add multiple songs
    num_songs = int(input("Enter the number of songs you want to add: "))
    for _ in range(num_songs):
        music_db.add_song()

    # Create DataFrame
    music_df = music_db.create_dataframe()
    print("\nDataFrame created:")
    print(music_df)