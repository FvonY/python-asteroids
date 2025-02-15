import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from shot import Shot

def main():
    print(f"Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (drawable)
    Shot.containers = (updatable, drawable)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid = Asteroid(100, 100, ASTEROID_MAX_RADIUS)
    shot = Shot(500, SCREEN_HEIGHT / 2, 0)

    while(True):
        # event
        dt = clock.tick(60)/1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            pass
        pass
    
        # update
        for entity in updatable:
            entity.update(dt)

        # draw
        screen.fill((0,0,0))
        
        for entity in drawable:
            entity.draw(screen)
        
        pygame.display.flip()
    pass

if __name__ == "__main__":
    main()
    