import pygame
from Vector import Vector
from states import GameState, PlayState, MenuState


def Update():
    global circle_vel
    global circle_pos

    if circle_follow_mouse:
        mouse_pos_vect = Vector(mouse_pos[0], mouse_pos[1])
        diff_vect = mouse_pos_vect - circle_pos
        normalized_dir = diff_vect.normalize()

        circle_vel += normalized_dir * circle_speed * dt
    circle_pos += circle_vel * dt

def Draw():
    screen.fill((50, 50, 50))
    pygame.draw.circle(screen, (255, 255, 255), circle_pos.make_int_tuple(), 10)

# -----------------------------------------------

pygame.init()
screen = pygame.display.set_mode((720, 410))
dt = 0.0
clock = pygame.time.Clock()
mouse_pos = (0, 0)

# ------------------------------------------------
circle_pos = Vector(0, 0)
circle_vel = Vector(0, 0)
circle_speed = 10000
circle_follow_mouse = False
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
            elif event.key == pygame.K_SPACE:
                circle_follow_mouse = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                circle_follow_mouse = False

    Update()
    Draw()

    pygame.display.flip()
    dt = 0.001 * clock.tick(144)

pygame.quit()


"""
from functools import lru_cache

def foo1():
    @lru_cache(maxsize=5) # stores the  lastest values
    def fib(n):
        if n<= 1:
            return n
        return fib(n-1) + fib(n-2)

    for i in range(400):
        print(i, fib(i))
    print("done")

def main():
    x = 1
    y = 3
    z = x | y
    print(z)

if __name__ == '__main__':
    main()
"""
