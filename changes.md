# Changes

## Week 10 - Project part 3

4) Improve the structure of your code using the principles of abstraction and
decomposition (2 points)
    * Apply at least to some parts of the project, no need to apply to entire codebase
    * Add a document ”CHANGES.md” to the repository, describing what you have done and why

## Applied changes

In **MusicDatabase**:
* Abstraction:
    * get_library:
        here the user only sees what what we want them to see. We want them to only see the dataframe with
        its songs and information about it. Therefore, we returned the entire library formatted according
        to the filters applied to the original dataframe. This then encapsulates the loading and saving of the dataframe, as the
        user is not supposed to interact with this process.
    * get_song:
        here we only want the user to get the information relevant to them in form of a dictionairy entry.
        We do not return the entire object song object with all other information like audio_data, sample_rate,
        and states like paused or current_position.
    * add_song:
        this function searches for the id that is passed through by the user. Therefore, the user only interacts
        with the interface without having to worry about what is going on behind closed doors / in the rest of the
        dataframe.
* Decomposition:
    * creation of a .csv file to save the dataframe after shutting down the application:
        * __init__: here the init method uses the function of loading the dataframe and an instance of a dummy song-
        * load_dataframe:
            also interacts with other functions like the pandas function read_csv to check if a dataframe is already 
            existent. If that is not the case we use a helper method create_csv_file that creates a csv file with the
            according headers that are created through the dummy song instance in the __init__ function.  
        Previously, we did not have a way to upkeep a dataframe constantly, as we saved it temporarily. Through this implementation
        of a .csv file we achieved exactly that: a dynamically changeable dataframe.
    
    * updating the .csv file:
        * add_song, remove_song, and save_dataframe:
            as previously described this function adds songs to the dataframe. Furthermore, remove_song removes an entry from the dataframe.  
            These functions then use the save_dataframe function to permanently save the newly added song and update the dataframe.
            Therefore, we decomposed the function to make the code more readable and
            distribute the necessary steps to add a song and save it in its appropriate functions.

In **Player**:
* Abstraction:
    * Introduce play_song(), pause_song(), resume_song(), stop_song(), and set_volume() methods to abstract playback control operations.  
    These methods encapsulate the functionality of starting, pausing, resuming, stopping, and adjusting volume, respectively. They hide the underlying implementation details from external classes.

    * Abstract volume control functionality into the set_volume() method, allowing external classes to adjust volume without directly accessing implementation details.  
    Ensure that volume changes are applied consistently and gracefully handle invalid volume levels.


