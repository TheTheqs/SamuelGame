import pygame
from controllers.game_controller import GameController
from views.menu_screen import MenuScreen  # Temporary, for test


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))  # Dimensions
    pygame.display.set_caption("SamuelGame")

    controller = GameController(screen)  # Start controller with the test screen
    controller.set_screen(MenuScreen())  # Start from menu
    controller.run()  # Start loop

    pygame.quit()  # Close game


if __name__ == "__main__":
    main()
