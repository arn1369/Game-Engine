from Component import Component

class Transform(Component):
    def __init__():
        pass

    class Position(Transform):
        def __init__(self):
            self.pos = (0, 0, 0)

    class Rotation(Transform):
        def __init__(self):
            pass

    class Scale(Transform):
        ## WARNING: scale the mesh here or in 'Mesh.py' ?
        def __init__(self):
            ## OPTIMIZE: cleaner
            self.scale_x = 0.0
            self.scale_y = 0.0
            self.scale_z = 0.0
            self.scale = (self.scale_x, self.scale_y, self.scale_z)

        def ScaleX(self, new_scale):
            pass
