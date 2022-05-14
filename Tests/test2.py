from Button import Button
import pygame

pygame.init()

screen = pygame.display.set_mode((720, 460))
clock = pygame.time.Clock()

# ---------------------------------------------
but = Button("Text", (0, 0), 12)
# ---------------------------------------------


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click(event)

    pygame.display.flip()
    dt = 0.0001 * clock.tick(144)
