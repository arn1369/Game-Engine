import pygame


class UI:
    def __init__(self, pos, height, width):
        self.x = pos[0]
        self.y = pos[1]
        self._height = height
        self._width = width

    def __str__(self):
        return f"\n \
                 width : {self._width}, \n \
                 height : {self._height}, \n \
                 pos_x : {self.x}, \n \
                 pos_y : {self.y} \n \
                "

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, __new_width):
        self._width = __new_width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, __new_height):
        self._height = __new_height

    @property
    def position(self):
        return self.x, self.y

    @position.setter
    def position(self, pos):
        self.x = pos[0]
        self.y = pos[1]
