import MusicDatabase as mdb
import pygame               #Library to play audio files (Da chönnt me oh eifch pygame.mixer bruche lol)

pygame.mixer.init()         #Initialize the mixer module
#pygame.mixer.music.set_endevent(pygame. ?? ) #Trigger an event when the music ends (next song for example)

current_position = 0 #Current position of the song in seconds --> For a progress bar/slider (let the progress bar change this value? Or Let  user Input change it?)
paused = False     #Flag to check if the song is paused


def play_song(song: mdb.Song):      #Frage: Wie willst Du den Song übergeben? Als Objekt?
    if paused:
        pygame.mixer.music.unpause()
        paused = False
    else:
        pygame.mixer.music.load(song.path)
        pygame.mixer.music.play()
        paused = False              #zur Sicherheit

def pause_song():       #Hier kann pausiert oder fortgesetzt werden
    global paused
    if paused:
        pygame.mixer.music.unpause()
        paused = False
    else:
        pygame.mixer.music.pause()
        paused = True

def stop_song():        
    pygame.mixer.music.stop()
    # pygame.mixer.music.unload() Hier vill. song rausnehmen?

def song_queue(song: mdb.Song):
    # Hier jeweils den nächsten Song in die Queue einfügen? Oder ist das obsolet

# Position (in einer Progressbar) verändern - Achtung: geht nur für mp3
def set_position(value : float):
    global current_position
    current_position = int(value) / 100 * pygame.mixer.music.get_length()
    pygame.mixer.music.set_pos(current_position) #Hier die Progressbar rein? Oder die Current position und die Progressbar verändert die current position?

def next_song():
    pass

def previous_song():
    pass

# To set the volume
def volume(value : int):
    volume = int(value) / 100               #pygame wants a value between 0 and 1 but the slider has a range from 0 to 100
    pygame.mixer.music.set_volume(volume)