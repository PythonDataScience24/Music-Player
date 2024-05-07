import tkinter as tk
import customtkinter as ctk

#pip install customtkinter

#import pd

from Music import Music
import MusicDatabase

#This script creates a basic GUI to display and manage the list of songs and control the playback.
#At this point, the list is static and the buttons do not have any functionality yet.



#Define custom widgets
class ScrollableListbox(tk.Frame):

    def __init__(self, parent, musicDB: MusicDatabase.MusicDatabase,  *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.scrollbar = tk.Scrollbar(self)
        self.listbox = tk.Listbox(self, yscrollcommand=self.scrollbar.set)

        self.scrollbar.config(command=self.listbox.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.listbox.bind("<Double-1>", self.on_double_click)

        self.musicDB = musicDB

        self.update_listbox()

    def update_listbox(self):
        self.listbox.delete(0, tk.END)

        self.library = self.musicDB.get_musicLibrary()

        if (len(self.library) > 0):
            for song in self.library:
                self.listbox.insert(tk.END, song.title)

    """ def add_item(self, item):
        self.listbox.insert(tk.END, item)

    def remove_item(self, item):
        self.listbox.delete(self.listbox.get(0, tk.END).index(item)) """

    def get_selected(self):
        #return the identifier of the selected
        index = self.listbox.curselection()
        if index:  # if there is a selection
            return self.library[index[0]] # return the song at index
        else:
            return None
    
    def on_double_click(self, event):
        index = self.listbox.nearest(event.y)
        song = self.library[index]
        print(f"You double-clicked {song}!")
    

class CustomProgressBar(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.progressbar = tk.ttk.Progressbar(self, orient="horizontal", length=200, mode="determinate", style="TProgressbar")
        self.progressbar.pack(fill=tk.X, expand=True)

    def update_progress(self, value):
        self.progressbar["value"] = value




#Create the main application
class  App(tk.Tk):


    #initialize the main application
    def __init__(self):
        super().__init__()

        self.geometry("800x600")
        self.title("Custom Tkinter")

        self.musicDB = MusicDatabase.MusicDatabase()


        self.listview = ScrollableListbox(self, self.musicDB)
        self.listview.place(relx=0.1, rely=0.1, relwidth=0.8)

        #add some items to the list view
        #self.musicDB.add_song("Song1")

        #add progressbar to bottom
        self.progressbar = CustomProgressBar(self)
        self.progressbar.place(relx=0.1, rely=0.9, relwidth=0.8)
        self.progressbar.update_progress(50)


        playButton = ctk.CTkButton(self, text="Play", command=lambda: print("Play button clicked!"), width=20)
        ForwardButton = ctk.CTkButton(self, text="Forward", command=lambda: print("Forward button clicked!"), width=20)
        BackwardButton = ctk.CTkButton(self, text="Backward", command=lambda: print("Backward button clicked!"), width=20)
        AddButton = ctk.CTkButton(self, text="Add", command=lambda: self.add_item_with_popup(), width=20)
        InfoButton = ctk.CTkButton(self, text="Info", command=lambda: print(f"Selected item: {self.listview.get_selected()}"), width=20)
        RemoveButton = ctk.CTkButton(self, text="Remove", command=lambda: self.remove_item_with_confirmation(), width=20)

        #place all buttons below the progressbar. play in the middle, forward and backward around it. add, info and remove on the left side
        playButton.place(relx=0.5, rely=0.8, anchor=tk.CENTER)
        ForwardButton.place(relx=0.6, rely=0.8, anchor=tk.CENTER)
        BackwardButton.place(relx=0.4, rely=0.8, anchor=tk.CENTER)
        AddButton.place(relx=0.25, rely=0.8, anchor=tk.W)
        InfoButton.place(relx=0.2, rely=0.8, anchor=tk.W)
        RemoveButton.place(relx=0.1, rely=0.8, anchor=tk.W)






        self.mainloop()


    #define the functions for the buttons
    def remove_item_with_confirmation(self):
            selected_item = self.listview.get_selected()

            def confirm_delete():
                #self.listview.remove_item(selected_item)
                self.musicDB.remove_song(selected_item.id)
                self.listview.update_listbox()
                popup.destroy()

            popup = tk.Toplevel()
            #popup.overrideredirect(True)
            popup.title("Confirmation")

            message_label = tk.Label(popup, text=f"Are you sure you want to delete {selected_item}?")
            message_label.pack()

            yes_button = ctk.CTkButton(popup, text="Yes", command=confirm_delete)
            yes_button.pack()

            no_button = ctk.CTkButton(popup, text="No", command=popup.destroy)
            no_button.pack()

    def add_item_with_popup(self):

        def add_item():
            song = Music(title.get(), artist.get(), genre.get(), year.get(), album.get(), file_path.get())

            
            self.musicDB.add_song()
            self.listview.update_listbox()
            popup.destroy()
            


        popup = tk.Toplevel()
        #popup.overrideredirect(True)
        popup.title("Add Item")


        #create entries for song = Music(title.get(), artist.get(), genre.get(), year.get(), album.get(), file_path.get())
        
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


    def updateView(self):



        pass



#Run the application
if __name__ == "__main__":
    app = App()
    app.mainloop()

