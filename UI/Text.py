import pygame


class Text():
    def __init__(self,
                 text: str,
                 font: str,
                 size: float,
                 color: tuple,
                 w_size: tuple,
                 antialias: bool,
                 scale: tuple=(1, 1),
                 pos: tuple=(0, 0)):
        self.x = pos[0]
        self.y = pos[1]
        self._text = text
        self._color = color
        self.w_size = w_size
        # create the font of the text
        self._size = size
        self._height, self._width = self._size, self._size
        self._font = pygame.font.SysFont(font, self._size)
        self.img = self._font.render(self._text, antialias, self._color)
        self.rect = self.img.get_rect()
        # apply the scale to the text (keep resolution)
        txt_w, txt_h = self.img.get_size()
        #self.img = pygame.transform.scale(self.img, (txt_w*w_size[0] // 1080, txt_h*w_size[1] // 720))

    def show(self, window):
        # if the text is in the window we chosen
        if self.x < self.w_size[0] and self.y < self.w_size[1]:
            # display it on the window
            window.blit(self.img, (self.x, self.y))

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, _new_text: str):
        self._text = _new_text

    @property
    def font(self):
        return self._font

    @font.setter
    def font(self, _new_font: 'font'):
        self._font = _new_font

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, _new_size: float):
        self._size = _new_size

    @property
    def position(self):
        return self.x, self.y

    @position.setter
    def position(self, _new_pos: tuple):
        self.x, self.y = _new_pos[0], _new_pos[1]

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, _new_color: tuple):
        self._color = _new_color
