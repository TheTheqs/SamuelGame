# Sound effects dealer
import pygame
import os


class SoundManager:
    # Constructor
    def __init__(self, instrument="piano"):  # Piano is the default instrument
        self.last_channel = None  # For busy verification
        self.sounds = {}
        self.instrument = instrument
        self.load_sounds()
        # For FX
        self.effects = {}
        self.load_effects()

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
        self.sounds['D'].play()

    def play_note(self, note):
        self.sounds[note].play()
        sound = self.sounds.get(note)
        if sound:
            self.last_channel = sound.play()

    def is_playing(self):
        return self.last_channel is not None and self.last_channel.get_busy()

    # FX load
    def load_effects(self):
        fx_path = "assets/sounds/system"
        self.effects["round_finished"] = pygame.mixer.Sound(os.path.join(fx_path, "round_finished.wav"))
        self.effects["fail"] = pygame.mixer.Sound(os.path.join(fx_path, "fail.wav"))

    def play_round_finished(self):
        self.effects["round_finished"].play()

    def play_fail(self):
        self.effects["fail"].play()
