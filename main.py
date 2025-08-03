import pygame
import constants
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    clock =pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids=pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    player = Player(constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2)
    field = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        for item in asteroids:
            if item.collision(player):
                print("Game over!")
                exit(0)
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()
        clock.tick(60)
        dt = clock.tick(60)/1000
if __name__ == "__main__":
    main()
