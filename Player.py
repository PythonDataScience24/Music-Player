import pygame.midi
import pygame.mixer
import pygame
import time
import threading

class Player:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.current_song = None
        self.slider_position = 0
        self.song_length = 0
        self.stop_update_thread = threading.Event()

    def play_song(self, song):
        if self.current_song:
            pygame.mixer.music.stop()
        self.current_song = song
        pygame.mixer.music.load(song.file_path)
        pygame.mixer.music.play()
        self.song_length = pygame.mixer.Sound(song.file_path).get_length()

    def pause_song(self):
        pygame.mixer.music.pause()

    def resume_song(self):
        pygame.mixer.music.unpause()

    def stop_song(self):
        pygame.mixer.music.stop()
        self.stop_update_thread.set()  # Signal the update thread to stop

    def is_playing(self):
        return pygame.mixer.music.get_busy()
    
    def set_volume(self, volume):
        pygame.mixer.music.set_volume(volume/100)

    def set_position(self, value):
        if self.current_song:
            song_length = pygame.mixer.Sound(self.current_song.file_path).get_length()
            pygame.mixer.music.set_pos(value * (song_length/100))

    def get_position(self):
        return pygame.mixer.music.get_pos() / 1000 / self.song_length * 100