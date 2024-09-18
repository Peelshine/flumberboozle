###################
# LIBRARY IMPORTS #
###################
import glfw

# placeholder config variables, in future will be loaded from file
# game resolution will be 120x90 4:3, but until i figure out how
# i want to do upscaling it will be 1920x1080 as placeholder
RESOLUTION_X = 1920
RESOLUTION_Y = 1080


def init(
) -> None:
    print('Initializing window...')
    if not glfw.init():
        return

    window = glfw.create_window(
        RESOLUTION_X,
        RESOLUTION_Y,
        'flumberboozle',
        None,
        None
    )

    if not window:
        glfw.terminate()
        return

    print('Window initialized! Yippee!')

    glfw.make_context_current(window)

    while not glfw.window_should_close(window):
        # RENDER HERE

        glfw.swap_buffers(window)

        glfw.poll_events()

    close()


def close(
) -> None:
    glfw.terminate
