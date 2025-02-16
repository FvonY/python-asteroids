from circleshape import CircleShape
from constants import *
import pygame

class Asteroid(CircleShape):
    containers = ()
    def __init__(self, x, y, radius, rotation=0, sizeclass=2):
        super().__init__(x, y, radius)
        self.rotation = rotation
        self.size_class = sizeclass
        
    def draw(self, screen):
        pygame.draw.circle(screen, (80, 80, 80), self.position, self.radius+4, 2)
        pygame.draw.circle(screen, (120, 120, 125), self.position, self.radius, 0)
        pass
    
    def move(self, dt):
        #print("move asteroid")
        self.position += pygame.Vector2(0, 1).rotate(self.rotation) * ASTEROID_SPEED * dt
        
    def split(self):
        if self.size_class == 1:
            return
        
        new_asteroid = Asteroid(self.position.x, self.position.y, radius=self.radius/2, rotation=self.rotation+20, sizeclass=self.size_class-1)
        new_asteroid = Asteroid(self.position.x, self.position.y, radius=self.radius/2, rotation=self.rotation-20, sizeclass=self.size_class-1)
    
    def update(self, dt):
        self.move(dt)
        pass
