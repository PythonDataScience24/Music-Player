# in this file every function that manipulates the data frame in any shape or form

def filter_dataframe (df):
    """filter the dataframe according to user input and return the dataframe 
    according to the filter expected

        Args:
            df (pandas dataframe): the dataframe that saved all the information of the local music library

        Returns:
            sortedDataFrame (dataframe): the dataframe sorted by the users choice
        """
    # initialise an origin state so that our while loop can later stop accordingly!
    origin_state = 0
    # grab the choice through the helper method!
    choice = askFilters()

    while choice != origin_state:
        if choice == 1:
            genre = input("Enter the genre of choice: ")
            sorted_dataframe = df[df['genre'] == genre]
            choice = 0
        elif choice == 2:
            artist = input("Enter the artist you're searching for: ")
            sorted_dataframe = df[df['artist'] == artist]
            choice = 0
        elif choice == 3:
            year = input("Enter the year from the songs you want to listen to: ")
            sorted_dataframe = df[df['year'] == year]
            choice = 0
        elif choice == 4:
            sorted_dataframe = df
            choice = 0
        else:
            # throws me out without giving print message but this error message: " ValueError: invalid literal for int() with base 10: '' "
            print('invalid choice! please enter again')
            choice = 0
    return sorted_dataframe

# helper methods for the filtering   
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
