from ursina import *

if __name__ == "__main__":
    from ursina.prefabs.first_person_controller import FirstPersonController
    game = Ursina()
    player = FirstPersonController()
    alien=load_texture('assets/alien.png')


class BlockMesh(Button):
    def __init__(self, position=(0, 0, 0)):
        super().__init__(
            parent=scene,
            position=position,
            model='quad',
            texture=alien,
            color=color.color(0, 0, random.uniform(0.9, 1)),
            highlight_color=(0.8, 0.8, 0.8, 1),
            scale=1,
            double_sided=True
        )

class Block:
    def __init__(pos=Vec3(0, 0, 0)) -> None:

        pass

map_size = 16
for z in range(map_size):
    for x in range(map_size):
        y = 5
        for i in range(-1, y, 2):
            blockmesh = BlockMesh(
                position=(
                    x - map_size / 2,
                    i,
                    z - map_size / 2
                )
            )


def update():
    if held_keys['escape']:
        application.quit()

if __name__ == "__main__":
    game.run()

