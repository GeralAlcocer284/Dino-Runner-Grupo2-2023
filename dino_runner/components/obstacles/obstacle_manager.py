
import pygame
import random
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import BIRD, SMALL_CACTUS, LARGE_CACTUS




class ObstacleManager():
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            obstacle = random.randint(0,2)
            if obstacle == 0: 
                self.obstacles.append(Cactus(SMALL_CACTUS))  
            elif obstacle == 1:
                self.obstacles.append(Cactus(LARGE_CACTUS))
            elif obstacle == 2:
                self.obstacles.append(Bird(BIRD))
                

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if not game.player.shield:              
                    pygame.time.delay(1000)
                    game.playing = False
                    pygame.mixer.music.stop()
                    break         
                elif game.player.shield:
                    self.obstacles.remove(obstacle)    



    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
        
        for obstacle in self.obstacles:
            obstacle.draw(screen)    

    def reset_obstacles(self):
        self.obstacles = []        