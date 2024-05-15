import tkinter as tk
import customtkinter as ctk
from Player import Player
from Song import Song
import MusicDatabase
import threading
import time

#pip install customtkinter


#This script creates a basic GUI to display and manage the list of songs and control the playback.
#At this point, the list is static and the buttons do not have any functionality yet.

#The GUI is structured as follows:
#- The main application is an instance of the App class
#- The App class contains a ScrollableListbox and a SongPlayer

#- The ScrollableListbox contains a Listbox widget to display the list of songs
#- The SongPlayer contains labels for the song title and artist, buttons for playback control, and a progress bar


#ScrollableListbox class
class ScrollableListbox(tk.Frame):

    def __init__(self, parent, musicDB: MusicDatabase.MusicDatabase, songPlayer,  *args, **kwargs):
        '''
        This class creates a scrollable listbox that displays the songs in the music database.
        It allows the user to select a song by clicking on it and play it using the songPlayer.

        Args:
            parent (tk.Tk): The parent Tkinter window.
            musicDB (MusicDatabase): An instance of the MusicDatabase class.
            songPlayer (SongPlayer): An instance of the SongPlayer class.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.


        '''


        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.scrollbar = tk.Scrollbar(self)
        self.listbox = tk.Listbox(self, yscrollcommand=self.scrollbar.set)

        self.scrollbar.config(command=self.listbox.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        #songs can be clicked 
        #if double clicked, the song will be assigned to the songplayer and playback starts.
        #if songplayer is assigned to a song, clicking once on another song should not change the song unless its a double click
        self.listbox.bind("<Double-1>", self.on_double_click) #binds the double click event to the listbox

        self.musicDB = musicDB
        self.songPlayer = songPlayer
        self.library = []

        self.update_listbox()

    def update_listbox(self):
        self.listbox.delete(0, tk.END)

        self.library = self.musicDB.get_library()

        #temporary library
        #self.library = [Song("Song1", "Artist1", "Genre1", 2021, "Album1", "path1"), Song("Song2", "Artist2", "Genre2", 2022, "Album2", "path2")]

        #do a for loop that does self.musicDB.get_length() times. if 0 times, it will not do anything
        for song in self.library:

            self.listbox.insert(tk.END, song.title)
            

    def get_selected(self):
        #return the identifier of the selected
        index = self.listbox.curselection()
        if index:  # if there is a selection
            return self.library[index] # return the song at index
        else:
            return None
    
    def on_double_click(self, event):
        index = self.listbox.nearest(event.y)
        song = self.library[index]
        print(f"You double-clicked {song}!")
        self.songPlayer.select_song(song)   
        #self.songPlayer.play_song()
 

#SongPlayer class
class SongPlayer(tk.Frame):
    
        def __init__(self, parent, *args, **kwargs):
            '''
            This class creates a song player widget that displays the currently selected song and allows the user to control playback.

            Args:
                parent (tk.Tk): The parent Tkinter window.
                *args: Variable length argument list.
                **kwargs: Arbitrary keyword arguments.
            '''

            tk.Frame.__init__(self, parent, *args, **kwargs)

            self.song = None
            self.parent = parent
            self.player = Player()



            #add volume slider
            self.volumeSlider = ctk.CTkSlider(self, from_=0, to=100, command=self.set_volume)
            self.volumeSlider.set(10)
            self.volumeSlider.grid(row=3, column=0, columnspan=6)

            self.set_volume(self.volumeSlider.get())

            #add playback position slider
            self.playbackSlider = ctk.CTkSlider(self, from_=0, to=100, command=self.set_playback)
            self.playbackSlider.set(0)
            self.playbackSlider.grid(row=4, column=0, columnspan=6)

            #player updatePositionEvent = setPlaybackSliderPosition
            self.update_thread = threading.Thread(target=self.update_slider)
            self.update_thread.start()


    
            self.titleLabel = ctk.CTkLabel(self, text="No Song Selected", width=20, font=("Arial", 12, "bold"))
            self.artistLabel = ctk.CTkLabel(self, text="Unkown Artist", width=20, font=("Arial", 10))

            self.playButton = ctk.CTkButton(self, text="Play", command=self.play_song, width=20)
            self.ForwardButton = ctk.CTkButton(self, text="Forward", command=self.forward_song, width=20)
            self.BackwardButton = ctk.CTkButton(self, text="Backward", command=self.backward_song, width=20)
            self.AddButton = ctk.CTkButton(self, text="Add", command=self.add_song, width=20)
            self.InfoButton = ctk.CTkButton(self, text="Info", command=self.get_song_info, width=20)
            self.RemoveButton = ctk.CTkButton(self, text="Remove", command=self.remove_song, width=20)
    
            self.titleLabel.grid(row=0, column=2)
            self.artistLabel.grid(row=1, column=2)

            self.BackwardButton.grid(row=2, column=1)
            self.playButton.grid(row=2, column=2)
            self.ForwardButton.grid(row=2, column=3)
            
            self.AddButton.grid(row=1, column=0)
            self.RemoveButton.grid(row=2, column=0)
            self.InfoButton.grid(row=2, column=4)
    

        def setPlaybackSliderPosition(self, position):
            self.playbackSlider.set(position)


        def select_song(self, song: Song):
            self.song = song
            self.titleLabel.configure(text=song.title)
            self.artistLabel.configure(text=song.artist)
            self.player.play_song(song)

          
        def get_song_info(self):
            if self.song:
                print("Info button clicked!")

                #open a popup window with the song info
                popup = tk.Toplevel()
                popup.title("Song Info")
                popup.geometry("200x200")

                title_label = tk.Label(popup, text=f"Title: {self.song.title}")
                title_label.pack()

                artist_label = tk.Label(popup, text=f"Artist: {self.song.artist}")
                artist_label.pack()

                genre_label = tk.Label(popup, text=f"Genre: {self.song.genre}")
                genre_label.pack()

                year_label = tk.Label(popup, text=f"Year: {self.song.year}")
                year_label.pack()


                album_label = tk.Label(popup, text=f"Album: {self.song.album}")
                album_label.pack()

                file_path_label = tk.Label(popup, text=f"File Path: {self.song.file_path}")
                file_path_label.pack()

                close_button = ctk.CTkButton(popup, text="Close", command=popup.destroy)
                close_button.pack()


                return self.song
            else:  
                print("No song selected!")
    
        def play_song(self):
            # check if song selected and if playing or not
            if self.song:
                if self.player.is_playing():
                    self.player.pause_song()
                else:
                    self.player.resume_song()
                
            else:
                print("No song selected!")
                
    
        def forward_song(self):
            if self.song:
                print(f"Playing next song after {self.song}")   

            else:
                print("No song selected!")
    
        def backward_song(self):
            if self.song:
                print(f"Playing next song after {self.song}")   

            else:
                print("No song selected!")
    
        def add_song(self):
            self.add_item_with_popup()

    
        def remove_song(self):
            if self.song:
                self.remove_item_with_confirmation()
            else:
                print("No song selected!")


        def remove_item_with_confirmation(self):
            #selected_item = self.listview.get_selected()

            def confirm_delete():
                #self.listview.remove_item(selected_item)
                self.parent.musicDB.remove_song(self.song.id)
                self.parent.listview.update_listbox()
                popup.destroy()

            popup = tk.Toplevel()
            #popup.overrideredirect(True)
            popup.title("Confirmation")

            message_label = tk.Label(popup, text=f"Are you sure you want to delete {self.song}?")
            message_label.pack()

            yes_button = ctk.CTkButton(popup, text="Yes", command=confirm_delete)
            yes_button.pack()

            no_button = ctk.CTkButton(popup, text="No", command=popup.destroy)
            no_button.pack()


        def add_item_with_popup(self):

            def add_item():
                song = Song(title.get(), artist.get(), genre.get(), year.get(), album.get(), file_path.get(), None)

                self.parent.musicDB.add_song(song)# needs to add possiblity to add arguments
                self.parent.listview.update_listbox()
                popup.destroy()
                

            popup = tk.Toplevel()
            #popup.overrideredirect(True)
            popup.title("Add Item")
            
            def add_labels_and_entries(text):
                frame = tk.Frame(popup)
                frame.pack()

                label = tk.Label(frame, text=text)
                label.pack(side=tk.LEFT)

                entry = tk.Entry(frame)
                entry.pack(side=tk.RIGHT)

                return entry

            title = add_labels_and_entries("Title")
            artist = add_labels_and_entries("Artist")
            genre = add_labels_and_entries("Genre")
            year = add_labels_and_entries("Year")
            album = add_labels_and_entries("Album")
            file_path = add_labels_and_entries("File Path")

            add_button = ctk.CTkButton(popup, text="Add", command=add_item)
            add_button.pack()

            cancel_button = ctk.CTkButton(popup, text="Cancel", command=popup.destroy)
            cancel_button.pack()

        def set_volume(self, value):
            self.player.set_volume(value)
            #player.setVolume(volume)
            """ if self.song:
                self.song.volume = self.volume """
            
        def set_playback(self, value):
            self.player.set_position(value)

        def update_slider(self):
            while not self.player.stop_update_thread.is_set():
                if self.player.is_playing():
                    self.playbackSlider.set(self.player.get_position())
                time.sleep(1)  # Adjust the sleep duration as needed for smoother updating

        def stop_thread(self):
            self.player.stop_update_thread.set()  # Set the flag to stop the thread
            self.update_thread.join()  # Wait for the thread to finish


#Create the main application
class  App(tk.Tk):
    # func for closing thread
    def cleanup(self):
        self.songplayer.stop_thread()  # Stop the update thread before closing
        self.destroy()  # Destroy the Tkinter window

    #initialize the main application
    def __init__(self):
        super().__init__()

        self.geometry("800x600")
        self.title("Custom Tkinter")

        self.musicDB = MusicDatabase.MusicDatabase()

        self.songplayer = SongPlayer(self)
        self.songplayer.place(relx=0.3, rely=0.8, relwidth=2)

        self.listview = ScrollableListbox(self, self.musicDB, self.songplayer)
        self.listview.place(relx=0.1, rely=0.1, relwidth=0.8)

        self.protocol("WM_DELETE_WINDOW", self.cleanup)  # Call cleanup when the window is closed

        self.mainloop()

    #define the functions for the buttons


#Run the application
if __name__ == "__main__":
    app = App()
    app.mainloop()

