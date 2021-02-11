from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from perlin_noise import PerlinNoise

import global_parameters as param

game = Ursina()

from Voxel import *
from Sky import *
from Hand import *

window.fps_counter.enabled = True
window.exit_button.visible = False

noise = PerlinNoise(octaves=2, seed=round(time.time()))

map_size = 8 * 3
lower_bound = -10

for z in range(map_size):
    for x in range(map_size):
        y = round(noise([x / map_size, z / map_size]) * 5)
        for i in range(lower_bound, y + 1):
            voxel = Voxel(
                type='grass' if i == y else ('dirt' if i > y - 3 else 'stone'),
                position=(
                    x - map_size / 2,
                    i,
                    z - map_size / 2
                )
            )

hand = Hand()
sky = mySky()
player = FirstPersonController()

def update():
    if held_keys['escape']:
        application.quit()
    if held_keys['1']:
        param.block_pick = 'stone'
    if held_keys['2']:
        param.block_pick = 'grass'
    if held_keys['3']:
        param.block_pick = 'dirt'
    if held_keys['4']:
        param.block_pick = 'brick'
    if held_keys['left mouse'] or held_keys['right mouse']:
        hand.active()
    else:
        hand.passive()

game.run()
