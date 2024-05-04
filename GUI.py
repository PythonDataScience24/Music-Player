import tkinter as tk
import customtkinter as ctk

#pip install customtkinter



#This script creates a basic GUI to display and manage the list of songs and control the playback.
#At this point, the list is static and the buttons do not have any functionality yet.



#Define custom widgets
class ScrollableListbox(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.scrollbar = tk.Scrollbar(self)
        self.listbox = tk.Listbox(self, yscrollcommand=self.scrollbar.set)

        self.scrollbar.config(command=self.listbox.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.listbox.bind("<Double-1>", self.on_double_click)

    def add_item(self, item):
        self.listbox.insert(tk.END, item)

    def remove_item(self, item):
        self.listbox.delete(self.listbox.get(0, tk.END).index(item))

    def get_selected(self):
        return self.listbox.get(tk.ACTIVE)
    
    def on_double_click(self, event):
        index = self.listbox.nearest(event.y)
        item = self.listbox.get(index)
        print(f"You double-clicked {item}!")
    

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

        self.listview = ScrollableListbox(self)
        self.listview.place(relx=0.1, rely=0.1, relwidth=0.8)

        #add some items to the list view
        self.listview.add_item("Song 1 - Artist 1 - Album 1 - 3:00")
        self.listview.add_item("Song 2 - Artist 2 - Album 2 - 4:00")

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
                self.listview.remove_item(selected_item)
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
            new_item = entry.get()
            if new_item:  # Only add if the entry is not empty
                self.listview.add_item(new_item)
            popup.destroy()

        popup = tk.Toplevel()
        #popup.overrideredirect(True)
        popup.title("Add Item")

        entry = tk.Entry(popup)
        entry.pack()

        add_button = ctk.CTkButton(popup, text="Add", command=add_item)
        add_button.pack()

        cancel_button = ctk.CTkButton(popup, text="Cancel", command=popup.destroy)
        cancel_button.pack()



#Run the application
if __name__ == "__main__":
    app = App()
    app.mainloop()

