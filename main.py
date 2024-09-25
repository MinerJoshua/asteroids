from constants import *;
from player import Player;
import pygame;

def main():
    pygame.init();
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT));
    clock = pygame.time.Clock();
    delta_time:int = 0;
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    updateable = pygame.sprite.Group();
    drawable = pygame.sprite.Group();
    updateable.add(player)
    drawable.add(player)

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
