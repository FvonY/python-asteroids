from constants import SHOT_SPEED, SHOT_RADIUS
from circleshape import CircleShape
import pygame

class Shot(CircleShape):
    containers = ()
    def __init__(self, x, y, rotation):
        super().__init__(x, y, SHOT_RADIUS)
        self.rotation = rotation
        self.lifetime = 0
        
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 50, 50), self.position, SHOT_RADIUS, 0)
        
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * SHOT_SPEED * dt
        
    def check_lifetime(self):
        if self.lifetime > 0.5:
            self.kill()
        
    def update(self, dt):
        self.move(dt)
        
        self.lifetime += dt
        self.check_lifetime()
        pass
    