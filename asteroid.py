from circleshape import CircleShape
import pygame

class Asteroid(CircleShape):
    containers = ()
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, (120, 255, 125), self.position, self.radius, 0)
        pass
