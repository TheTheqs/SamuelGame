import pygame


# Main controller
class GameController:
    # Constructor
    def __init__(self, screen):
        self.screen = screen
        self.current_screen = None
        self.running = True
        self.clock = pygame.time.Clock()

    # Screen control, change and set
    def set_screen(self, new_screen):
        self.current_screen = new_screen
        self.current_screen.controller = self

    # Main function, runs the game
    def run(self):
        while self.running:
            dt = self.clock.tick(60) / 1000.0  # set frame rate.

            # Event dealer
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif self.current_screen:
                    self.current_screen.handle_event(event)

            # Screen render and update
            if self.current_screen:
                self.current_screen.update(dt)
                self.current_screen.render(self.screen)

            pygame.display.flip()
