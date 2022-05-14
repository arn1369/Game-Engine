import pygame
from .Text import Text


class Button:
    def __init__(self,
                 text: Text,
                 pos: tuple,
                 color: tuple,
                 background_color: tuple,
                 default_state: bool=False,):
        self.x, self.y = pos[0], pos[1]
        self._text = text
        self.state = default_state
        # get the size of the text
        self.size = self._text._width, self._text._height
        # get the surface of the rect
        self.surface = pygame.Surface(self.size)
        # fill the surface with the background
        self.surface.fill(background_color)
        # add the text to the surface
        """if we want margin, it's here"""
        self.surface.blit(self.surface, (0, 0))
        # get the rect of the text
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, _new_text: Text):
        self._text = _new_text

    def click(self, event, action: 'function'):
        mouse_pos: tuple = pygame.mouse.get_pos()
        # if we press the left click of the mouse
        if pygame.mouse.get_pressed()[0]:
            # was that click in the button ?
            if self.rect.collidepoint(mouse_pos):
                # do the action
                action()

    def show(self, window):
        window.blit(self.surface, (self.x, self.y))

    def highlight(self):
        pass

    def update(self):
        pass
