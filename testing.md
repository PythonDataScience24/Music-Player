# testing

## Week 11 - Project part 4

3) Implement a unit test with at least four test cases (3 Points)
    * Create a seperate file dedicated to uni tests
    * Write a unit test that tests a function in your code that could produce an unexpected ouptut. Provide a description of how this function might produce an unexpected result and how you tested it in a "testing.md" file.
    * You can implement more than one unit test, but this is optional

* Task 1: can be found in test_music_database.py

* Task 2:
1. test_initialization_and_csv_creation : tests if the database/dataframe and .csv file are created properly. One unexpected output could have been that the dataframe creation creates multiple instances instead of just one with all the necessary information. Therefore, we set aan assertions that test there exists only one .csv file with the dataframe. Another concern was that the dataframe might not be clean from the beginning but might have residue contents from previous dataframes, therefore, we asserted that it must be empty right after creation.
2. test_add_song: here we test that only one instance is added for each call of the add_song function and that the added song is properly and permanently added to the dataframe until removal. To test that behaviour we have placed 2 assertEqual statements that check if the added song is placed correctly and that the length of the dataframe is correct.
3. test_remove_song: here we test if the song is removed appropriately. The main concern was that the song cannot be removed properly even if we use the id of the song in the dataframe. To test this procedure we added one song to the dataframe, thus only having one entry. After that instantly we removed it this song instance and checked if the dataframe is empty (as it should be after removing the one entry).
4. test_filter_df: in this test we check if the filtering of the dataframe works correctly. Of course, the main concern was that the dataframe does not filter correctly, meaning that instances of songs are in the filtered dataframe that should not be there. We tested this behaviour through adding 2 mock songs and then define a filter_song template by which the dataframe should be sorted by. As only one song of the 2 added mock songs conforms to that template the dataframe that was filtered should only include that song. Therefore, we assertEqual the length of the dataframe to be one and assertEqual to check if the title of the entry in the dataframe conforms to the expected song.
5. test_get_song_info: in this test we check if we get the appropriate information of the desired song. The main unexpected output would either be no output at all or false output about a song with the according id that was searched for. To test this we have added a song to the dataframe and then used two kinds of asserts. The first assertIsNotNone check if the information exists. As this one passes the next 2 assertEquals check if the title and artist information are correct, therefore, ensuring that our method works accordingly.