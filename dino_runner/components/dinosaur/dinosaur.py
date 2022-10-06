import pygame
from dino_runner.utils.constants import RUNNING, DUCKING, JUMPING
from pygame.sprite import Sprite


class Dinosaur(Sprite):
    X_POS = 80
    Y_POS = 310
    Y_POS_DUCK = 340
    JUMP_LEVEL = 8.5

    def __init__(self):
        self.image = RUNNING[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.dino_run = True
        self.dino_duck = False
        self.dino_jump = False
        self.jump_vel = self.JUMP_LEVEL
        self.step_index = 0

    def update(self, user_input):
        if self.dino_run:
            self.dino_running()
        if self.dino_duck:
            self.dino_ducking()
        if self.dino_jump:
            self.dino_jumping()
        if self.step_index >= 10:
            self.step_index = 0

        if (user_input[pygame.K_UP] or user_input[pygame.K_SPACE]) and not self.dino_jump:
            self.dino_duck = False
            self.dino_run = False
            self.dino_jump = True
        elif user_input[pygame.K_DOWN] or user_input[pygame.K_s] and not self.dino_jump:
            self.dino_run = False
            self.dino_duck = True
            self.dino_jump = False
        elif not (self.dino_jump or user_input[pygame.K_DOWN]):
            self.dino_duck = False
            self.dino_run = True
            self.dino_jump = False

    def dino_running(self):
        self.image = RUNNING[0] if self.step_index < 5 else RUNNING[1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index = self.step_index + 1

    def dino_ducking(self):
        self.image = DUCKING[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS_DUCK
        self.step_index = self.step_index + 1

    def dino_jumping(self):
        self.image = JUMPING
        if (self.dino_jump):
            self.dino_rect.y = self.dino_rect.y - (self.jump_vel * 4)
            self.jump_vel = self.jump_vel - 0.8

        if (self.jump_vel < -self.JUMP_LEVEL):
            self.dino_jump = False
            self.jump_vel = self.JUMP_LEVEL
            self.dino_rect.y = self.Y_POS

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))
