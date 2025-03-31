# This is an abstract class, used to make contracts for the screen classes.
from abc import ABC, abstractmethod
from utils.decorators import with_background
import pygame


class BaseScreen:
    def __init__(self):
        self.controller = None  # Will receive its value by the GameController
        self.SCREEN_WIDTH = 800
        self.SCREEN_HEIGHT = 600  # H and W from children class usage
        self.background = pygame.image.load("assets/images/background/background.png").convert()  # Background
        self.font = pygame.font.Font("assets/fonts/font.ttf", 30)  # font Load
        self.title_font = pygame.font.Font("assets/fonts/font.ttf", 40)
        self.footer_font = pygame.font.Font("assets/fonts/font.ttf", 20)

    @abstractmethod
    def handle_event(self, event):
        pass

    @abstractmethod
    def update(self, dt):
        pass

    @with_background  # Using decorator for background recycle
    def render(self, screen):
        self.render_content(screen)

    @abstractmethod
    def render_content(self, screen):
        pass

    # Play ambient theme// A static method
    @staticmethod
    def play_theme(play):
        if play:
            if not pygame.mixer.music.get_busy():
                pygame.mixer.music.load("assets/sounds/system/ambient.wav")
                pygame.mixer.music.set_volume(0.3)
                pygame.mixer.music.play(loops=-1)
        else:
            pygame.mixer.music.stop()
