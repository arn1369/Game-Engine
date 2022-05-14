import pygame
import UI


SCREEN_WIDTH, SCREEN_HEIGHT = 1080, 720

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# -----------------------------------------------------------------------------
background = (128, 128, 128)
text1 = UI.Text(text="Text",
         font='Arial',
         size=50,
         color=(0, 0, 0),
         w_size=(SCREEN_WIDTH, SCREEN_HEIGHT),
         antialias=True,
         pos=(500, 500))
button1 = UI.Button(text=text1,
                 pos=(500, 500),
                 color=(100, 100, 100),
                 background_color=(100, 100, 100))
def but():
    print("Pressed !")

# -----------------------------------------------------------------------------
#                                  HIERARCHY
# -----------------------------------------------------------------------------

# create the window and add the image
hierarchy_win = UI.Panel(pos=(0, 0),
          background_color=(150, 150, 150),
          size=(300, 720))
hierarchy_win.add_image(pos=(0, 0),
            path="C:/Users/arnul/OneDrive/Documents/Développement/Programmation/Python/Projets/Pygame Projects/Chess/Assets/test_image.jpg",
            size=(786, 443),
            scale=(1, 1))
path_font1 = "C:/Users/arnul/OneDrive/Documents/Développement/Programmation/Python/Projets/Pygame Projects/Chess/Assets/liberation_sans/LiberationSans-Regular.ttf"
hierarchy_win.add_text(_text="Vector2D",
                       font='Arial',
                       size=30,
                       color=(0, 0, 0),
                       antialias=False,
                       scale=(1, 1),
                       pos=(0, 300))

# -----------------------------------------------------------------------------
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            button1.click(event, but)
            pass

    screen.fill(background)
    button1.show(screen)
    text1.show(screen)
    hierarchy_win.show(screen)
    pygame.display.update()
    dt = 0.0001 * clock.tick(60)

pygame.quit()
