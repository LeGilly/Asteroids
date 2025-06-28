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

    # Game loop
    while True:
        # Init of screen, player, asteroid field and running states
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        player = Player(SCREEN_CENTER_X, SCREEN_CENTER_Y) # Start at the center of the screen
        game.reset()
        clock = pygame.time.Clock()
        dt = 0.0
        asteroid_field = AsteroidField()
        running = True

        while running:
            need_reset = False
            # Allows the X button to work
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
            
            # Delta time used to limit framerate, converted from milliseconds to seconds
            dt = clock.tick(FRAMERATE) / 1000

            # Black background fill
            screen.fill(BLACK_COLOR)

            # Loop in updatables and game group
            updatable.update(dt)
            game.update(dt)
            for asteroid in asteroids:
                # Check if player hit an asteroid and respawns or exits
                if asteroid.collision(player):
                    player.lives -= 1
                    print(f"Lives remaining : {player.lives}")
                    if player.lives == 0:
                        running = False
                    else:
                        player.reset()
                        need_reset = True
                    break
                # Check if shots hit an asteroid
                for shot in shots:
                    if asteroid.collision(shot):
                        asteroid.split()
                        shot.kill()
                        game.add_score(50)
            
            # Apply the reset if needed
            if need_reset:
                for asteroid in asteroids:
                    asteroid.kill()
                for shot in shots:
                    shot.kill()

            # Loop in drawables group        
            for item in drawable:
                item.draw(screen)
            
            game.draw_score(screen)
            for life in range(0, player.lives):
                game.draw_lives_remaining(screen, (30 * (life + 1), 55))

            # Update display
            pygame.display.flip()
        
        choice = game_over_screen(screen, game.score)
        if choice == "restart":
            player.kill()
            for asteroid in asteroids:
                asteroid.kill()
            for shot in shots:
                shot.kill()
            for sprite in updatable:
                sprite.kill()
            for sprite in drawable:
                sprite.kill()
            continue
        else:
            break


def game_over_screen(surface, final_score):
    # Render each text surface
    large_font = pygame.font.SysFont(None, 72)
    small_font = pygame.font.SysFont(None, 36)

    game_over_text = large_font.render("GAME OVER", True, WHITE_COLOR)
    score_text = small_font.render(f"Score: {final_score}", True, WHITE_COLOR)
    prompt_text = small_font.render("Press SPACE to play again, ESC to quit", True, (200, 200, 200))

    # Get their rectangles and center the x position
    game_over_rect = game_over_text.get_rect(center=(SCREEN_CENTER_X, SCREEN_CENTER_Y - 60))
    score_rect = score_text.get_rect(center=(SCREEN_CENTER_X, SCREEN_CENTER_Y))
    prompt_rect = prompt_text.get_rect(center=(SCREEN_CENTER_X, SCREEN_CENTER_Y + 40))

    # Blit each one using its rect
    surface.blit(game_over_text, game_over_rect)
    surface.blit(score_text, score_rect)
    surface.blit(prompt_text, prompt_rect)
    pygame.display.flip()

    # Input loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return "restart"
                elif event.key in (pygame.K_ESCAPE, pygame.K_q):
                    sys.exit()
        


if __name__ == "__main__":
    main()