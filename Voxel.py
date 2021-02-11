from ursina import *
from ursina import mouse

import global_parameters as param

punch_sound = Audio('assets/punch_sound.wav', loop=False, autoplay=False)
grass_texture = load_texture('assets/grass_block.png')
brick_texture = load_texture('assets/brick_block.png')
dirt_texture = load_texture('assets/dirt_block.png')
stone_texture = load_texture('assets/stone_block.png')
block_textures = {'grass': grass_texture,
                  'brick': brick_texture,
                  'dirt': dirt_texture,
                  'stone': stone_texture,
                  }


class Voxel(Button):
    def __init__(self, type, position=(0, 0, 0)):
        super().__init__(
            parent=scene,
            position=position,
            model='assets/block',
            texture=block_textures[type],
            color=color.color(0, 0, random.uniform(0.9, 1)),
            highlight_color=(0.8, 0.8, 0.8, 1),
            scale=0.5,
            origin_y=0.5
        )

    # designated func name
    def input(self, key):
        if self.hovered:
            if key == 'right mouse down':
                punch_sound.play()
                voxel = Voxel(type=param.block_pick,
                              position=self.position + mouse.normal)

            if key == 'left mouse down':
                punch_sound.play()
                destroy(self)
