from ursina import *

sky_texture = load_texture('assets/skybox.png')


class mySky(Entity):
    def __init__(self):
        super().__init__(
            parent=scene,
            model='sphere',
            texture=sky_texture,
            scale=100,
            double_sided=True
        )
