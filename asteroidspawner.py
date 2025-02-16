from constants import *
from asteroid import Asteroid
import pygame
import random

class AsteroidSpawner(pygame.sprite.Sprite):
    containers = ()
    edges = [
        #x-range, y-range
         #top
        [(0, SCREEN_WIDTH), (SCREEN_HEIGHT, SCREEN_HEIGHT)],
         #bottom
        [(0, SCREEN_WIDTH), (0, 0)],
         #left
        [(0, 0), (0, SCREEN_HEIGHT)],
         #right
        [(SCREEN_WIDTH, SCREEN_WIDTH), (0, SCREEN_HEIGHT)]
    ]
    
    edges_rotation = [
        #top
        {"x-range": (0, SCREEN_WIDTH),
         "y-range": (SCREEN_HEIGHT, SCREEN_HEIGHT),
         "rotation-offset": 180},
        #bottom
        {"x-range": (0, SCREEN_WIDTH),
         "y-range": (0, 0),
         "rotation-offset": 0},
        #left
        {"x-range": (0, 0),
         "y-range": (0, SCREEN_HEIGHT),
         "rotation-offset": 270},
        #right
        {"x-range": (SCREEN_WIDTH, SCREEN_WIDTH),
         "y-range": (0, SCREEN_HEIGHT),
         "rotation-offset": 90},  
    ]
    
    def __init__(self):
        super().__init__(self.containers)
        self.time_since_spawn = 0
        pass
    
    def spawn(self):
        # spawn at screen edges
        # fly into the screen, not away
        
        # choose an edge to spawn at
        random_edge = random.randint(0, len(self.edges)-1)
        edge = self.edges_rotation[random_edge]
        
        x_min, x_max = edge["x-range"]
        y_min, y_max = edge["y-range"]
        rotation_offset = edge["rotation-offset"]
        
        half_angle = 30
        rotation_min = (rotation_offset - half_angle)
        rotation_max = (rotation_offset + half_angle)
        
        print(f"{rotation_min}, {rotation_max}")
        
        asteroid = Asteroid(random.randint(x_min, x_max),
                            random.randint(y_min, y_max),
                            random.randint(ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS),
                            random.randint(min(rotation_min, rotation_max), max(rotation_min, rotation_max)))
        pass
    
    def update(self, dt):
        #print("update spawner")
        self.time_since_spawn += dt
        if self.time_since_spawn > ASTEROID_SPAWN_RATE:
            self.spawn()
            self.time_since_spawn = 0
        pass
    