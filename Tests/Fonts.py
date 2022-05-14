"""Draw text to the screen."""
import pygame
import time

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)

pygame.init()
screen = pygame.display.set_mode((640, 240))

sysfont = pygame.font.get_default_font()
print('system font :', sysfont)

t0 = time.time()
font = pygame.font.SysFont(None, 48)
print('time needed for Font creation :', time.time()-t0)

img = font.render(sysfont, True, RED)
rect = img.get_rect()
pygame.draw.rect(img, BLUE, rect, 1)

font1 = pygame.font.SysFont('chalkduster.ttf', 72)
img1 = font1.render('hi', True, BLUE)

running = True
background = GRAY
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(background)
    screen.blit(img, (20, 20))
    screen.blit(img1, (20, 50))
    pygame.display.update()

pygame.quit()
