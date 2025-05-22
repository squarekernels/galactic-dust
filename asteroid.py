import pygame
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self,x,y, PLAYER_RADIUS):
        CircleShape.__init__(self, x, y, PLAYER_RADIUS)
        self.radius = PLAYER_RADIUS
        self.velocity = pygame.Vector2(0,0)
    
    def draw(self, screen):
        return pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt
