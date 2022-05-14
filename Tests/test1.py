import pygame
from func import Update, Draw
from Vector import Vector
from states import GameState, PlayState, MenuState

def main():
	# ------------------------------------------------
	pygame.init()
	screen = pygame.display.set_mode((720, 410))
	dt = 0.0
	clock = pygame.time.Clock()
	mouse_pos = (0, 0)
	# ------------------------------------------------
	
	# ------------------------------------------------
	running = True
	while running:
		mouse_pos = pygame.mouse.get_pos()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					running = False

		Update()
		Draw()
		screen.fill((50, 50, 50))
		pygame.display.flip()
		dt = 0.001 * clock.tick(144)

	pygame.quit()

if __name__ == '__main__':
	main()
