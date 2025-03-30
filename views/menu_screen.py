from views.base_screen import BaseScreen
import pygame


class MenuScreen(BaseScreen):
    def __init__(self):
        # Buttons banners
        self.button_image = pygame.image.load("assets/images/UI/menu_banner.png").convert_alpha()
        self.title_image = pygame.image.load("assets/images/UI/title_banner.png").convert_alpha()
        super().__init__()
        # Buttons config
        self.menu_options = [
            {"text": "Samuel Game!", "y": 70, "action": lambda: None},
            {"text": "Play", "y": 210, "action": lambda: self.change_screen(1)},
            {"text": "Scores", "y": 330, "action": lambda: self.change_screen(2)},
            {"text": "Exit", "y": 450, "action": lambda: setattr(self.controller, "running", False)},
        ]
        self.buttons = []

        self.font = pygame.font.Font("assets/fonts/font.ttf", 30)  # font Load

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()

            for button in self.buttons:
                if button["rect"].collidepoint(mouse_pos):
                    button["action"]()  # Take Button action

    def update(self, dt):
        pass

    def render(self, screen):
        screen.fill((0, 0, 0))  # Background

        self.buttons.clear()  # Reset button list

        for i, option in enumerate(self.menu_options):
            text_surface = self.font.render(option["text"], True, (30, 30, 30))
            y = option["y"]

            rect = text_surface.get_rect(centerx=self.SCREEN_WIDTH // 2, y=y)

            # Take the correct banner
            current_banner = self.title_image if i == 0 else self.button_image
            banner_rect = current_banner.get_rect(center=rect.center)

            # Draw button + text
            screen.blit(current_banner, banner_rect)
            screen.blit(text_surface, rect)

            # Button action config
            self.buttons.append({
                "rect": banner_rect,
                "action": option["action"]
            })

    def change_screen(self, command):
        from views.game_screen import GameScreen
        from views.score_screen import ScoreScreen
        if command == 1:
            self.controller.set_screen(GameScreen())
        else:
            self.controller.set_screen(ScoreScreen([]))
