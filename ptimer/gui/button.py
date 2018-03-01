import pyglet
from pyglet.sprite import Sprite


class Button(Sprite):
    def __init__(self, img, x, y, label="", **kwargs):
        """Instantiate `Button`."""
        super(Button, self).__init__(img, x, y, **kwargs)
        self.clicked = False
        self.label = pyglet.text.Label(
            label,
            font_name='Times New Roman',
            font_size=25,
            color=(0, 0, 0, 255),
            x=x,
            y=y,
            anchor_x='center',
            anchor_y='center',
        )

    def draw(self):
        super(Button, self).draw()
        self.label.draw()

    def set_action(self, action):
        self.action = action

    def check_click(self, x, y):
        if (x in range(self.x - self.width // 2, self.x + self.width // 2) and
                y in range(self.y - self.height // 2, self.y + self.height // 2)):
                return True

        return False

    def on_mouse_press(self, x, y, button, modifiers):
        if self.check_click(x, y):
            self.clicked = True

    def on_mouse_release(self, x, y, button, modifiers):
        if self.clicked:
            self.clicked = False
            if self.check_click(x, y):
                self.action()
