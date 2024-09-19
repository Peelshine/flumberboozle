import pyglet

# placeholder config variables, in future will be loaded from file
# game resolution will be 120x90 4:3, but until i figure out how
# i want to do upscaling it will be 1920x1080 as placeholder
RESOLUTION_X = 1920
RESOLUTION_Y = 1080


def init(
) -> None:
    print('Initializing window...')

    window = pyglet.window.Window()

    label = pyglet.text.Label(
        'Hello, world',
        font_name='Times New Roman',
        font_size=36,
        x=window.width//2, y=window.height//2,
        anchor_x='center', anchor_y='center'
    )

    @window.event
    def on_draw():
        window.clear()
        label.draw()

    pyglet.app.run()


def close(
) -> None:
    print('haha no lol')
