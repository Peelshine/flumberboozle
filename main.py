import pyglet
import input
import update



RESOLUTION_X = 1920
RESOLUTION_Y = 1080


def close(
) -> None:
    print('haha no lol')


def main(
) -> None:
    global window
    window = pyglet.window.Window()

    label = pyglet.text.Label(
        'Hello, world!',
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




if __name__ == '__main__':
    main()
