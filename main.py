import pygame

from game import BSP


def main():
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    screen.fill((0, 0, 0))

    running = True
    clock = pygame.Clock()

    b = BSP(3)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))

        b.draw(screen, 500, 500)

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
