import pygame


class Anchor():
    def __init__(self, pos: tuple, height: int, width: int, window_size: tuple):
        self.x, self.y = pos[0], pos[1]
        self.height, self.width = height, width
        self.w_width = window_size[0]
        self.w_height = window_size[1]

    def set_anchor_center(self):
        # go make an image
        self.x = (self.w_width[0]/2) - (self.width/2)
        self.y = (self.w_height[1]/2) - (self.height/2)
        self.align_top_left()

    def set_anchor_edge(self, side: str):
        if side != None:
            if side == 'right':
                self.x = self.w_width - (self.width/2)         # x_right
                self.y = self.w_height/2                       # y_center
            elif side == 'left':
                self.x = self.width/2                          # x_left
                self.y = self.w_height/2                       # y_center
            elif side == 'top':
                self.x = self.w_width/2                        # x_center
                self.y = self.height/2                         # y_top
            elif side == 'bottom':
                self.x = self.w_width/2                        # x_center
                self.y = self.w_height - (self.height/2)       # y_bottom
            else:
                raise Exception(f"HaloWarning: You must have a valid anchor : {side}.")
                return
        self.align_top_left()

    def set_anchor_corner(self, corner: str):
        if corner != None:
            if corner == 'top_left':
                self.x = self.width/2
                self.y = self.height/2
            elif corner == 'top_right':
                self.x = self.w_width - self.width/2
                self.y = self.height/2
            elif corner == 'bottom_left':
                self.x = self.width/2
                self.y = self.w_height - self.height/2
            elif corner == 'bottom_right':
                self.x = self.w_width - self.width/2
                self.y = self.w_height - self.height/2
            else:
                raise Exception(f"HaloWarning: You must have a valid anchor : {corner}.")
                return
        self.align_top_left()

    def align_top_left(self):
        '''This func align the ui to the topleft of it so i can
           calculate in this class with the center
           -> more readable & simple'''
        # translate to width/2 left and height/2 up
        self.x -= self.width/2
        self.y -= self.height/2
