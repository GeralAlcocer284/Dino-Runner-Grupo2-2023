import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import SCREEN_HEIGHT






class Cactus(Obstacle):


    def __init__(self, image):
        self.type = random.randint(0,5)
        super().__init__(image, self.type)
        self.rect.y = 325

   
  