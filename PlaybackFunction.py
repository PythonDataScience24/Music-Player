import MusicDatabase as mdb
import sounddevice as sd
import numpy as np
from scipy.io.wavfile import read

# Default sample rate for playback
DEFAULT_SAMPLE_RATE = 44100

# Current position of the song in seconds
current_position = 0

# Flag to check if the song is paused
paused = False

current_position = 0 #Current position of the song in seconds --> For a progress bar/slider (let the progress bar change this value? Or Let  user Input change it?)
paused = False     #Flag to check if the song is paused


def play_song(song: mdb.Song):
    global paused, current_position
    #check if the state of paused is false if it is so then we play the song
    if paused:
        sd.play(song.audio_data, song.sample_rate, start=int(current_position * song.sample_rate))
        paused = False
    else:
        # Read audio data from file and assign it to song.audio_data
        # Discard the sample rate returned by read() using the underscore 
        _, song.audio_data = read(song.file_path)
        song.sample_rate = DEFAULT_SAMPLE_RATE  # Set default sample rate
        sd.play(song.audio_data, song.sample_rate)
        paused = False
    print("Now playing:", song.title)

def pause_song():       #Hier kann pausiert oder fortgesetzt werden
    global paused
    if paused:
        sd.resume()
        paused = False
    else:
        sd.pause()
        paused = True

def stop_song():        
    sd.stop()

# def song_queue(song: mdb.Song):
#     # Hier jeweils den nächsten Song in die Queue einfügen? Oder ist das obsolet

# Position (in einer Progressbar) verändern - Achtung: geht nur für mp3
def set_position(song: mdb.Song, value : float):
    global current_position
    current_position = value
    if not paused:
        sd.stop()
        play_song(song)

def next_song():
    pass

def previous_song():
    pass

# To set the volume
def volume(song: mdb.Song, value : int):
    # check the value if it is possible to amplify it that far 
    #--> restriction so that the user cannot make misinputs --> ask the user how many percent they want to increase it
    if value < 0 or value > 100:
        raise ValueError("Volume value must be between 0 and 100.")
    
    # Convert volume percentage to a scale factor
    scale_factor = value / 100.0
    
    # Amplify the audio data using numpy
    song.audio_data = np.multiply(song.audio_data, scale_factor)

    # If the song is currently playing, restart playback with the new volume
    if not paused:
        sd.stop()
        play_song(song)