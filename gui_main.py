import sys
import pyglet
from pyglet.window import Window

from ptimer.gui.gui_version import Ptimer

time_settings = [25, 5, 20]
if len(sys.argv) == 4:
    time_settings = sys.argv[1:]
else:
    if len(sys.argv) != 1:
        print(":::::::::::::::::::::::::::::")
        print("Usage: python gui_main.py [round length in minutes] [break length in minutes] [long break length in minutes]")
        print("example: python gui_main 20.1 5.2 12")
        print("Inputting no args will use default values")
        print(":::::::::::::::::::::::::::::")
        sys.exit(1)


game = Ptimer(time_settings)
window = Window(700, 500)
pyglet.gl.glClearColor(.8, .8, .8, 1)


def update(self):
    game.update()


@window.event
def on_mouse_release(x, y, button, modifiers):
    game.on_mouse_release(x, y, button, modifiers)


@window.event
def on_mouse_press(x, y, button, modifiers):
    game.on_mouse_press(x, y, button, modifiers)


@window.event
def on_draw():
    window.clear()
    game.draw()


if __name__ == '__main__':

    pyglet.clock.schedule(update)
    pyglet.app.run()
