import pygame
from constants import *
from player import Player

def main():
    print(f"Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    pygame.init()
    clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while(True):
        dt = clock.tick(60)/1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            pass
        pass

        screen.fill((0,0,0))
        player.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
    