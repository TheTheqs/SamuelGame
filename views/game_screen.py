from views.base_screen import BaseScreen
import pygame


class GameScreen(BaseScreen):
    def __init__(self):
        print("Entering game screen")
        super().__init__()
        self.timer = 0  # Timer for score and control

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            from views.game_over_screen import GameOverScreen
            self.controller.set_screen(GameOverScreen(final_score=42))

    def update(self, dt):  # This test update method will end the game after 10 seconds
        self.timer += dt
        if self.timer > 10:
            from views.game_over_screen import GameOverScreen
            self.controller.set_screen(GameOverScreen(final_score=42))

    def render(self, screen):
        screen.fill((20, 20, 100))
