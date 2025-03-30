# This is an abstract class, used to make contracts for the screen classes.
from abc import ABC, abstractmethod


class BaseScreen:
    def __init__(self):
        self.controller = None  # Will receive its value by the GameController
        self.SCREEN_WIDTH = 800
        self.SCREEN_HEIGHT = 600  # H and W from children class usage

    @abstractmethod
    def handle_event(self, event):
        pass

    @abstractmethod
    def update(self, dt):
        pass

    @abstractmethod
    def render(self, screen):
        pass
