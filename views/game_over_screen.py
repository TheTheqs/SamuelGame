from views.base_screen import BaseScreen
from models.score_manager import ScoreManager
from models.sound_manager import SoundManager
import pygame


class GameOverScreen(BaseScreen):
    def __init__(self, final_score):
        super().__init__()
        self.escore_manager = ScoreManager()
        self.final_score = final_score
        self.play_theme(False)
        self.input_text = ""
        self.input_active = True
        self.input_max_length = 8
        self.input_placeholder = "Player"
        self.sound = SoundManager()
        self.sound.play_fail()

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and self.input_active:
            if event.key == pygame.K_BACKSPACE:
                self.input_text = self.input_text[:-1]
            elif event.key == pygame.K_RETURN:
                print(f"Saving score: {self.final_score} for {self.input_text or self.input_placeholder}")
                self.back_to_menu()
            elif len(self.input_text) < self.input_max_length:
                if event.unicode.isalnum() or event.unicode == " ":
                    self.input_text += event.unicode

    def update(self, dt):
        pass

    def render_content(self, screen):
        elements = ["GAME OVER", f"Score: {self.final_score}", "Type your name!"]

        # Input
        display_input = self.input_text if self.input_text else self.input_placeholder
        elements.append(f"[ {display_input} ]")

        spacing = 80
        total_height = len(elements) * spacing
        start_y = (self.SCREEN_HEIGHT - total_height) // 2

        for i, text in enumerate(elements):
            color = (30, 30, 30) if not (text.startswith("[") and self.input_text == "") else (150, 150, 150)
            surface = self.font.render(text, True, color) if i != 0 else (
                self.title_font.render(text, True, color))
            rect = surface.get_rect(center=(self.SCREEN_WIDTH // 2, start_y + i * spacing))
            screen.blit(surface, rect)

    def back_to_menu(self):
        from views.menu_screen import MenuScreen
        self.controller.set_screen(MenuScreen())
