import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0
        self.lives = PLAYER_INITIAL_LIVES
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position - forward * self.radius
        b = self.position + forward * self.radius - right
        c = self.position + forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, WHITE_COLOR, self.triangle(), DRAW_LINE_WIDTH)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def update(self, dt):
        self.timer -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_q]:
            self.rotate(-dt)

        if keys[pygame.K_d]:
            self.rotate(dt)
        
        if keys[pygame.K_z]:
            self.move(-dt)

        if keys[pygame.K_s]:
            self.move(dt)
        
        if keys[pygame.K_SPACE] and self.timer <= 0:
            self.shoot(dt)

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    def shoot(self, dt):
        shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation + 180) * PLAYER_SHOT_SPEED
        self.timer = PLAYER_SHOT_COOLDOWN
    
    def reset(self):
        self.position = pygame.Vector2(SCREEN_CENTER_X, SCREEN_CENTER_Y)
        self.rotation = 0
        self.timer = 0