from views.base_screen import BaseScreen
from models.sound_manager import SoundManager
from models.game_state import GameState
import pygame


class GameScreen(BaseScreen):
    def __init__(self):
        super().__init__()
        self.sound = SoundManager()
        self.state = GameState()
        self.instrument_buttons = self.build_instrument_buttons()
        self.color_buttons = self.build_color_buttons()
        self.play_theme(False)
        self.current_instrument = "piano"
        self.play_queue = []
        # Game State Interface
        self.round_image = pygame.image.load("assets/images/UI/score_banner.png").convert_alpha()
        self.round_image = pygame.transform.scale(self.round_image, (64, 64))

        # PLayer, Machine and timer display
        color = (30, 30, 30)
        self.ui_elements = {"you": {
            "text": "You",
            "color": color,
            "pos": "topleft",
            "coords": (20, 10)
        }, "samuel": {
            "text": "Samuel",
            "color": color,
            "pos": "topright",
            "coords": (self.SCREEN_WIDTH - 20, 10)
        }}

        self.timer = 0  # Timer for score and control

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()

            for button in self.instrument_buttons + self.color_buttons:
                if button["rect"].collidepoint(mouse_pos):
                    button["action"]()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:  # Only for debug
            self.end_game()

    # Check if there is something on queue to be played.
    def update(self, dt):
        if not self.sound.is_playing():
            self.set_all_buttons_ready()  # reset buttons images

        if self.play_queue and not self.sound.is_playing():
            next_color = self.play_queue.pop(0)
            self.play_color(next_color)

    def render_content(self, screen):
        # Instrument buttons
        for button in self.instrument_buttons:
            screen.blit(button["image"], (button["x"], button["y"]))

            if button["name"] == self.current_instrument:
                rect = button["rect"]
                pygame.draw.rect(screen, (255, 255, 0), rect.inflate(4, 4), 3)

        # Color buttons
        for button in self.color_buttons:
            image_path = f"assets/images/buttons/{button['name']}_{button['state']}.png"
            image = pygame.image.load(image_path).convert_alpha()
            image = pygame.transform.scale(image, (192, 128))
            screen.blit(image, button["rect"])

        # Round interface
        round_rect = self.round_image.get_rect(center=(self.SCREEN_WIDTH // 2, self.SCREEN_HEIGHT // 2 - 40))
        screen.blit(self.round_image, round_rect)
        round_text = self.font.render(str(self.state.round), True, (30, 30, 30))
        text_rect = round_text.get_rect(center=round_rect.center)
        screen.blit(round_text, text_rect)

        # UI elements
        for key, element in self.ui_elements.items():
            if "visible" in element and not element["visible"]:
                continue

            text_surface = self.font.render(element["text"], True, element["color"])
            text_rect = text_surface.get_rect(**{element["pos"]: element["coords"]})
            screen.blit(text_surface, text_rect)

    # Create instruments button on screen
    def build_instrument_buttons(self):
        instrument_names = ["piano", "drum", "guitar", "flute", "synth"]
        button_width = 64
        button_height = 64
        space = 80
        y = self.SCREEN_HEIGHT - button_height - 20

        buttons = []

        for i, name in enumerate(instrument_names):
            x = space + i * (button_width + space)
            image_path = f"assets/images/icons/{name}.png"
            image = pygame.image.load(image_path).convert_alpha()

            action = self.make_instrument_action(name)
            rect = pygame.Rect(x, y, button_width, button_height)

            buttons.append({
                "name": name,
                "x": x,
                "y": y,
                "image": image,
                "action": action,
                "rect": rect
            })

        return buttons

    # Create color buttons on screen
    def build_color_buttons(self):
        button_width = 192
        button_height = 128
        vertical_offset = -40  # for vertical adjustment
        spacing = 20

        center_x = (self.SCREEN_WIDTH - button_width) // 2
        center_y = (self.SCREEN_HEIGHT - button_height) // 2 + vertical_offset

        buttons = []

        color_data = [
            {"name": "red", "note": "C", "x": center_x, "y": 100 + vertical_offset},
            {"name": "yellow", "note": "D", "x": center_x, "y": 372 + vertical_offset},
            {"name": "green", "note": "E", "x": center_x - button_width - spacing, "y": center_y},
            {"name": "blue", "note": "F", "x": center_x + button_width + spacing, "y": center_y},
        ]

        for color in color_data:
            rect = pygame.Rect(color["x"], color["y"], button_width, button_height)

            action = self.make_color_action(color)

            buttons.append({
                "name": color["name"],
                "rect": rect,
                "action": action,
                "state": "ready"
            })

        return buttons

    # Editable lambda actions
    def make_instrument_action(self, instrument_name):
        def action():
            if not self.play_queue and not self.sound.is_playing():
                self.current_instrument = instrument_name
                SoundManager.change_instrument(self.sound, instrument_name)

        return action

    def make_color_action(self, color):
        def action():
            if self.sound.is_playing():
                self.play_queue.append(color)
            else:
                self.play_color(color)

        return action

    def play_color(self, color):
        self.set_button_pressed(color["name"])
        self.sound.play_note(color["note"])

    # Reset button sprite
    def set_all_buttons_ready(self):
        for button in self.color_buttons:
            if button["state"] == "pressed":
                button["state"] = "ready"

    # Pressed effect
    def set_button_pressed(self, color):
        for button in self.color_buttons:
            if button["name"] == color:
                button["state"] = "pressed"

    # Game over call
    def end_game(self):
        from views.game_over_screen import GameOverScreen
        self.controller.set_screen(GameOverScreen(3))
