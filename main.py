import pygame
from player import Player
from asteroid import Asteroid
from constants import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)

    asteroid1 = Asteroid(100, 100, 30)
    asteroid2 = Asteroid(200, 150, 40)
    asteroid1.velocity = pygame.Vector2(50, 0)
    asteroid2.velocity = pygame.Vector2(-30, 20)

    player = Player(x, y, PLAYER_RADIUS, (updatable, drawable))
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        pygame.Surface.fill(screen, (0,0,0))
        dt = clock.tick(60)/1000
        
        updatable.update(dt)
        
        for sprite in drawable:
            sprite.draw(screen)
        
        # player.draw(screen)
        # asteroid1.draw(screen)
        # asteroid2.draw(screen)

        pygame.display.flip()
    
if __name__ == "__main__":
    main()
