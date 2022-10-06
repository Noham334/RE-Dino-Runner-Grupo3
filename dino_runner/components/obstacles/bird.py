import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD


class Bird(Obstacle):
    BIRDS = [250, 290, 320]

    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = random.choice(self.BIRDS)
        self.index = 0

    def draw(self, screen):
        if self.index >= 10:
            self.index = 0

        screen.blit(BIRD[0] if self.index < 5 else BIRD[1], self.rect)
        self.index += 1
