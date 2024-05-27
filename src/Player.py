"""
Player Class:
A music player class that uses the pygame library to manage song playback. It provides
functionality to play, pause, resume, stop, and control the volume and position of the
currently playing song.

Attributes:
    current_song (Song): The currently loaded song object.
    slider_position (int): The position of the playback slider (for UI integration).
    song_length (float): The length of the current song in seconds.
    offset (float): The offset used to calculate the current position in the song.

Methods:
    __init__: Initializes the Player object and sets up the pygame mixer.
    play_song(song): Loads and plays the specified song.
    pause_song(): Pauses the currently playing song.
    resume_song(): Resumes playback of the paused song.
    stop_song(): Stops the currently playing song.
    is_playing(): Checks if a song is currently playing.
    set_volume(volume): Sets the playback volume (0 to 100 scale).
    set_position(value): Sets the playback position to a specific point.
    get_position(): Gets the current playback position as a percentage.
"""

import pygame.mixer
# pylint: disable=no-member
import pygame


class Player:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.current_song = None
        self.slider_position = 0
        self.song_length = 0
        self.offset = 0


    def play_song(self, song):
        self.offset = 0
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

    def is_playing(self):
        return pygame.mixer.music.get_busy()
    
    def set_volume(self, volume):
        pygame.mixer.music.set_volume(volume/100)

    def set_position(self, value):
        if self.current_song:
            try:
                self.offset = value - ((100/(self.song_length*1000)) * pygame.mixer.music.get_pos())
                pygame.mixer.music.set_pos(value * (self.song_length/100))
            except pygame.error:
                pass

    def get_position(self):
        if self.current_song:
            return ((100/(self.song_length*1000)) * pygame.mixer.music.get_pos()) + self.offset
