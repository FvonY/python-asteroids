from constants import *
from asteroid import Asteroid
import pygame
import random

class AsteroidSpawner(pygame.sprite.Sprite):
    containers = ()
    
    def __init__(self):
        super().__init__(self.containers)
        self.time_since_spawn = 0
        pass
    
    def spawn(self):
        asteroid = Asteroid(random.randint(0, SCREEN_WIDTH),
                            random.randint(0, SCREEN_HEIGHT),
                            random.randint(ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS),
                            random.randint(0,359))
        pass
    
    def update(self, dt):
        print("update spawner")
        self.time_since_spawn += dt
        if self.time_since_spawn > ASTEROID_SPAWN_RATE:
            self.spawn()
            self.time_since_spawn = 0
        pass
    