import pygame

class Player:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.current_song = None

    def play_song(self, song):
        if self.current_song:
            pygame.mixer.music.stop()
        self.current_song = song
        pygame.mixer.music.load(song.file_path)
        pygame.mixer.music.play()

    def pause_song(self):
        pygame.mixer.music.pause()

    def resume_song(self):
        pygame.mixer.music.unpause()

    def stop_song(self):
        pygame.mixer.music.stop()

    def is_playing(self):
        return pygame.mixer.music.get_busy()