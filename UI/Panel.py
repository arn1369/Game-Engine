import pygame
from .Text import Text

class Panel:
    def __init__(self,
                 pos: tuple,
                 background_color: tuple,
                 size: tuple):
        # the positions of the window on the screen
        self.x, self.y = pos[0], pos[1]
        # the size of the window
        self.size = size
        # create the surface where we can blit images, text, ...
        self.surface = pygame.Surface((self.size[0], self.size[1]))
        self.surface.fill(background_color)

        self.images = [[], # theses are surfaces
                       []] # theses are positions
        self.texts = [[],  # theses are Texts
                      []]  # theses are positions
    def add_text(self,
                 _text: str,
                 font: str,
                 size: tuple,
                 color: tuple,
                 antialias: bool,
                 scale: tuple=(1, 1),
                 pos: tuple=(0, 0)):
        text = Text(_text, font, size, color, self.size, antialias, scale=(1, 1), pos=(0, 0))
        # if the text is in the window
        if pos[0] <= self.surface.get_size()[0] and pos[1] <= self.surface.get_size()[1]:
            self.texts[0].append(text)
            self.texts[1].append(pos)
        else:
            raise Exception(f'HaloDebug >>> The text added {text} is not on the window {self}')

    def add_image(self, pos: tuple, path: str, size: tuple, scale: tuple):
        # create the image, the rect and the surface of the image
        img = pygame.image.load(path)
        rect = img.get_rect(topleft=(pos[0], pos[1]))
        # if the image is in the window
        if pos[0] <= self.surface.get_size()[0] and pos[1] <= self.surface.get_size()[1]:
            # add the image and the positions to the arrays of all
            # the images added on the window
            self.images[0].append(img)
            self.images[1].append((pos[0], pos[1]))
        else:
            # if the image is outsite of the window
            raise Exception(f'HaloDebug >>> The image added {img} is not on the window {self}')

    def show(self, screen):
        # self.images[i].get_rect() = (0, 0) => ALWAYS
        # show the images on the window
        for i in range(len(self.images[0])):
            # blit on the window we create and at positions of the image
            self.surface.blit(self.images[0][i], self.images[1][i])
        # show the texts on the window
        for i in range(len(self.texts[0])):
            # blit on the window we created and at positions of the text
            self.surface.blit(self.texts[0][i].img, self.texts[1][i])
        # show the window on the screen
        screen.blit(self.surface, (self.x, self.y))
