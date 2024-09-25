from constants import *;
from player import Player;
import pygame;

def main():
    pygame.init();
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT));
    clock = pygame.time.Clock();
    delta_time:int = 0;
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black");
        player.update(delta_time);
        player.draw(screen);
        pygame.display.flip();
        delta_time = clock.tick(60)/1000;

if __name__ == "__main__":
	main();
