from dino_runner.components.obstacles.obstacles import Obstacles
from dino_runner.utils.constants import SMALL_CACTUS

import random



class Cactus(Obstacles):
    def __init__(self, image):
        self.type = random.randint(0,2)
        super().__init__(image, self.type)
        self.rect.y = 330