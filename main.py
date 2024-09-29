import sys
import os.path
from asteroid import Asteroid
from AsteroidField import AsteroidField
from constants import *;
from player import Player;
import pygame;
from shot import Shot
from ui import ScoreUI


def scoring():
    pass
    #Text Sprite
    #Calculate number of
def main():
    pygame.init();
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT));
    clock = pygame.time.Clock();
    delta_time:int = 0;
    background = pygame.image.load(os.path.join('assets','images','background.jpg'))
    running: bool = True

    updateable = pygame.sprite.Group();
    drawable = pygame.sprite.Group();
    asteroids = pygame.sprite.Group();
    shots = pygame.sprite.Group();

    AsteroidField.containers = updateable
    Asteroid.containers = (asteroids,drawable,updateable)
    Player.containers = (updateable,drawable)
    Shot.containers = (shots,updateable,drawable)
    ScoreUI.containers = (updateable,drawable)

    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()
    score = ScoreUI()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.blit(background,(0,0))
        for sprite in updateable:
            sprite.update(delta_time)

        for asteroid in asteroids:
            if asteroid.collide(player):
                print('Game Over!')
                running = False

            for shot in shots:
                if asteroid.collide(shot):
                    asteroid.split()
                    shot.kill()
                    score.score_text += 1

        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip();
        delta_time = clock.tick(60)/1000;

if __name__ == "__main__":
    main();
