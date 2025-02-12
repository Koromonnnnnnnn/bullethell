import sys
import pygame

pygame.init()
pygame.display.set_caption("bullet hell")
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()


def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    screen.fill((0, 0, 0))

    pygame.display.flip()


pygame.quit()
sys.exit()

if __name__ == "__main__":
    main()
