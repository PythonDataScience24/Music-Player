from Music import Music
import pandas as pd

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
        self.music_library = []

    def add_song(self):
        """use user input to save a song and create a Music Object"""
        # gather the information we need for a Music Object
        title = input("Enter title: ")
        artist = input("Enter artist name: ")
        genre = input("Enter genre: ")
        year = input("Enter year (leave blank if unknown): ")
        album = input("Enter the album: ")
        file_path = input("Enter path to the music file: ")

        new_song = Music(title, artist, genre, year, album, file_path)
        self.music_library.append(new_song)

    def create_dataframe(self):
        """create a dataframe out of the created library"""
        data = {
            "Title": [],
            "Artist": [],
            "Genre": [],
            "Year": [],
            "Album": [],
            "File_Path": []
        }
        # append the data
        for song in self.music_library:
            data["Title"].append(song.title)
            data["Artist"].append(song.artist)
            data["Genre"].append(song.genre)
            data["Year"].append(song.year)
            data["Album"].append(song.album)
            data["File_Path"].append(song.file_path)
        
        df = pd.DataFrame(data= data)
        return df


def filter_dataframe (df):
        """filter the dataframe according to user input and return the dataframe according to the filter expected

        Args:
            df (pandas dataframe): the dataframe that saved all the information of the local music library

        Returns:
            sortedDataFrame (dataframe): the dataframe sorted by the users choice
        """
        # initialise an origin state so that our while loop can later stop accordingly!
        originState = 0
        # grab the choice through the helper method!
        choice = askFilters()
    

        while choice != originState:
            if choice == 1:
                genre = input("Enter the genre of choice: ")
                sortedDataframe = df[df['Genre'] == genre]
                choice = 0
            elif choice == 2:
                artist = input("Enter the artist you're searching for: ")
                sortedDataframe = df[df['Artist'] == artist]
                choice = 0
            elif choice == 3:
                year = input("Enter the year from the songs you want to listen to: ")
                sortedDataframe = df[df['Year'] == year]
                choice = 0
            elif choice == 4:
                choice = 0
            else:
                print('invalid choice! please enter again')
                choice = 0
        return sortedDataframe
    
def askFilters ():
    """helper method that displays the possible filters and asks the user for their choice
    Returns:
        int choice: the chosen filter that the user wants to apply"""
    # show the options
    print("Filter options:")
    print("1. Filter by genre")
    print("2. Filter by artist")
    print("3. Filter by year")
    print("4. Exit filter menu")
    # save the input of the user
    choice = int(input("Please enter your choice by typing 1-4: "))
    return choice


# test
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

sortedDf = filter_dataframe(music_df)
print(sortedDf)