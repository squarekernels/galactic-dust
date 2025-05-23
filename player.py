import pygame 
from circleshape import CircleShape
from constants import *
from shot import Shot

class Player(CircleShape, pygame.sprite.Sprite):
    def __init__(self, x, y, PLAYER_RADIUS, containers):
        pygame.sprite.Sprite.__init__(self, *containers)
        CircleShape.__init__(self, x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shots = []
        self.timer = 0


    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, (255,255,255), self.triangle(), 2)
        for shot in self.shots:
            shot.draw(screen)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):        
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.timer -= dt 

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rotate(-dt)

        if keys[pygame.K_d]or keys[pygame.K_RIGHT]:
            self.rotate(dt)

        if keys[pygame.K_w]or keys[pygame.K_UP]:
            self.move(dt)

        if keys[pygame.K_s]or keys[pygame.K_DOWN]:
            self.move(-dt)
        
        if keys[pygame.K_SPACE]:
            self.shoot()

        for shot in self.shots:
            shot.update(dt)


    def shoot(self):
        if self.timer <= 0:
            direction = pygame.Vector2(0,1).rotate(self.rotation)
            shot_position = self.position + direction * (self.radius + SHOT_RADIUS)
            new_shot = Shot(shot_position.x, shot_position.y, SHOT_RADIUS)
            new_shot.velocity = direction * PLAYER_SHOOT_SPEED
            self.shots.append(new_shot)
            self.timer = PLAYER_SHOOT_COOLDOWN