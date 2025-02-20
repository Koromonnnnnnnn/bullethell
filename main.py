import sys
import pygame
from player import Player

pygame.init()
pygame.display.set_caption("Bullet Hell")
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

FPS = 60

p1 = Player(375, 375, (50, 150, 250), 50, 50)


def main():
    running = True
    while running:
        delta_time = clock.tick(FPS) / 1000.0
        keys_pressed = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        p1.update(delta_time, keys_pressed)

        screen.fill((0, 0, 0))

        p1.draw(screen)

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
