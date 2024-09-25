from asteroid import Asteroid
from AsteroidField import AsteroidField
from constants import *;
from player import Player;
import pygame;

def main():
    pygame.init();
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT));
    clock = pygame.time.Clock();
    delta_time:int = 0;

    updateable = pygame.sprite.Group();
    drawable = pygame.sprite.Group();
    asteroids = pygame.sprite.Group();

    AsteroidField.containers = updateable
    Asteroid.containers = (asteroids,drawable,updateable)
    Player.containers = (updateable,drawable)

    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()
    #updateable.add(player)
    #drawable.add(player)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black");
        for sprite in updateable:
            sprite.update(delta_time)

        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip();
        delta_time = clock.tick(60)/1000;

if __name__ == "__main__":
    main();
