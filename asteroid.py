from circleshape import CircleShape
from constants import *
import pygame

class Asteroid(CircleShape):
    containers = ()
    def __init__(self, x, y, radius, rotation=0):
        super().__init__(x, y, radius)
        self.rotation = rotation
        
    def draw(self, screen):
        pygame.draw.circle(screen, (120, 255, 125), self.position, self.radius, 0)
        pass
    
    def move(self, dt):
        print("move asteroid")
        self.position += pygame.Vector2(0, 1).rotate(self.rotation) * ASTEROID_SPEED * dt
    
    def update(self, dt):
        self.move(dt)
        pass
