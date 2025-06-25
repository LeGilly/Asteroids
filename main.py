import sys
import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from game import Game
from player import Player
from shot import Shot


def main():
    # Init block for pygame, dt, the clock and game elements
    pygame.init()
    dt = 0.0
    clock = pygame.time.Clock()
    game = Game()

    # Sprite group creation
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Adding appropriate groups to the containers Class variable for each Class
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    # Init of screen, player and asteroid field
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) # Start at the center of the screen
    asteroid_field = AsteroidField()

    # Game loop
    while True:
        # Allows the X button to work
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Delta time used to limit framerate, converted from milliseconds to seconds
        dt = clock.tick(FRAMERATE) / 1000

        # Black background fill
        screen.fill(BLACK_COLOR)

        # Loop in updatables group and game 
        updatable.update(dt)
        game.update(dt)
        for asteroid in asteroids:
            # Check if player hit an asteroid and exits if so
            if asteroid.collision(player):
                print(f"Game over! Finished with a score of {game.score}")
                sys.exit()
            # Check if shots hit an asteroid
            for shot in shots:
                if asteroid.collision(shot):
                    asteroid.split()
                    shot.kill()
                    game.add_score(50)

        # Loop in drawables group        
        for item in drawable:
            item.draw(screen)
        
        game.draw_score(screen)

        # Update display
        pygame.display.flip()
        



if __name__ == "__main__":
    main()