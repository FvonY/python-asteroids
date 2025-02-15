import pygame
from constants import *

def main():
    print(f"Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while(True):
        screen.fill((0,0,0))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT():
                return
            pass
        pass


if __name__ == "__main__":
    main()
    