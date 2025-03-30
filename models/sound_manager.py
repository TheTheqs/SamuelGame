# Sound effects dealer
import pygame
import os


class SoundManager:
    # Constructor
    def __init__(self, instrument="piano"):  # Piano is the default instrument
        self.sounds = {}
        self.instrument = instrument
        self.load_sounds()

    # Play instrument
    def load_sounds(self):
        base_path = f"assets/sounds/{self.instrument}"
        notes = ['C', 'D', 'E', 'F']

        for note in notes:
            path = os.path.join(base_path, f"{note}.wav")  # Wav format for pygame optimization
            self.sounds[note] = pygame.mixer.Sound(path)

    # Change instrument
    def change_instrument(self, new_instrument):
        self.instrument = new_instrument
        self.load_sounds()
