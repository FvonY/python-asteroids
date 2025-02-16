from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_MOVE_SPEED
from shot import Shot
import pygame

class Player(CircleShape):
    containers = ()
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shots = []
        self.shot_lock = False
        
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        #right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        
        a = self.position + forward * self.radius
        b = self.position + forward.rotate(140) * self.radius
        c = self.position + forward.rotate(-140) * self.radius
        #b = self.position - forward * self.radius - right
        #c = self.position - forward * self.radius + right
        
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)
        #pygame.draw.circle(screen, (255,100,100),self.position,self.radius,1)
        pass
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_MOVE_SPEED * dt
        pass
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
        pass
    
    def shoot(self):
        shot = Shot(self.position.x, self.position.y, self.rotation)
        return None  
    
    def update(self, dt):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_SPACE] and not self.shot_lock:
            self.shots = self.shoot()
            self.shot_lock = True
        if not keys[pygame.K_SPACE]:
            self.shot_lock = False
        pass
    