###
script: GUI.py line 224


`
try:
    figure = self.parent.musicDB.plot_song_frame(self.song) 

    canvas = FigureCanvasTkAgg(figure, master=popup)    
    canvas.draw()

    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

except Exception as e:
    texto = f"Error plotting song: {e}" 
    errormessage = tk.Label(popup, text=texto, fg="red")
    errormessage.pack()
    
`

The `plot_song_frame` function requires the song to be in 32-bit WAV format because it utilizes the `scipy.io.wavfile` library, which only supports this format. For other file types, such as 24-bit WAV or MP3, the function is unable to generate a plot because it cannot retrieve the necessary data using `scipy.io.wavfile`.

The exception catches the error and shows the error as a red label
