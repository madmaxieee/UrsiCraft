# from ursina import *
# from ursina.prefabs.first_person_controller import FirstPersonController


# class Test_cube(Entity):
#     def __init__(self):
#         super().__init__(
#             model='cube',
#             color=color.white,
#             rotation=Vec3(45, 45, 45),
#             texture='white_cube',
#             position=(0, 2)
#         )


# class Test_button(Button):
#     def __init__(self):
#         super().__init__(
#             parent=scene,
#             model='cube',
#             color=color.green,
#             texture='brick',
#             highlight_color=(0, 1, 1, 1),
#             pressed_color=color.red
#         )


# def update():
#     if held_keys['5']:
#         square.x += 1 * time.dt


# app = Ursina()

# sans_texture = load_texture('assets/alien.png')
# sans = Entity(model='quad', texture=sans_texture, position=(2, 0))

# square = Entity(model='quad', color=(255, 0, 0, 255),
#                 scale=(1, 4), position=(-2, 0))

# cube = Test_cube()
# button = Test_button()

# player = FirstPersonController()

# app.run()
