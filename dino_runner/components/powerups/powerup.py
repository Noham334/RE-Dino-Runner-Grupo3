import random
from dino_runner.utils.constants import SCREEN_HEIGHT
from pygame.sprite import Sprite


class PowerUp(Sprite):
    def __init__(self, image, type):
        self.image = image
        self.rect = self.image.get_rect()
        self.type = type
        self.rect_x = SCREEN_HEIGHT + random.randint(800, 1000)
        self.rect_y = random.randint(100, 150)

        self.start_time = 0

        self.width = self.image.get_width()

    def update(self, game_speed, powerups):
        self.rect_x -= game_speed
        if self.rect.x < -self.rect.width:
            powerups.pop()

    def draw(self, screen):
        screen.blit(self.image, (self.rect_x, self.rect_y))
