import time
import pyglet

from .button import Button
from .image_assets import IMAGE_ASSETS


class Ptimer(object):
    def __init__(self, times=[25, 5, 20]):
        self.sequence = [
            'round', 'break',
            'round', 'break',
            'round', 'break',
            'round', 'long break']
        self.sequence_times = {
            'round': float(times[0]) * 60,
            'break': float(times[1]) * 60,
            'long break': float(times[2]) * 60
        }

        self.buttons = []
        self.buttons.append(Button(IMAGE_ASSETS['button'], 225, 100, label="Start/Pause"))
        self.buttons[0].set_action(self.toggle_pause)
        self.buttons.append(Button(IMAGE_ASSETS['button'], 475, 100, label="Reset"))
        self.buttons[1].set_action(self.reset)

        self.time_label = pyglet.text.Label(
            '',
            font_name='Times New Roman',
            font_size=40,
            color=(0, 0, 0, 255),
            x=350,
            y=250,
            anchor_x='center',
            anchor_y='center',
        )

        self.round_label = pyglet.text.Label(
            'round 1',
            font_name='Times New Roman',
            font_size=40,
            color=(0, 0, 0, 255),
            x=350,
            y=370,
            anchor_x='center',
            anchor_y='center',
        )
        self.reset()

    def toggle_pause(self):

        self.started = not self.started
        if self.started:
            self.last_time = time.time()

    def update(self):
        if self.started:
            c_time = time.time()
            self.time_elapsed += c_time - self.last_time
            self.last_time = c_time

            if self.time_elapsed < self.sequence_times[self.sequence[self.round]]:
                message = str(int((self.sequence_times[self.sequence[self.round]] - self.time_elapsed) // 60)) + ":"
                message += str(int((self.sequence_times[self.sequence[self.round]] - self.time_elapsed) % 60))
                self.time_label.text = message
            else:
                self.round += 1
                if self.round < len(self.sequence):
                    self.round_label.text = self.sequence[self.round] + " " + str((self.round // 2) + 1)
                    self.time_elapsed = 0
                    self.last_time = time.time()
                else:
                    self.started = False
                    self.round = 0
                    self.time_elapsed = 0
                    self.round_label.text = "round 1"
                    self.time_label.text = "Sequence over! Good job!"
        else:
            pass

    def reset(self):
        self.round_label.text = "round 1"
        self.time_label.text = ''
        self.started = False
        self.round = 0
        self.last_time = 0
        self.time_elapsed = 0

    def draw(self):
        for b in self.buttons:
            b.draw()
        self.time_label.draw()
        self.round_label.draw()

    def on_mouse_release(self, x, y, button, modifiers):
        for b in self.buttons:
            b.on_mouse_release(x, y, button, modifiers)

    def on_mouse_press(self, x, y, button, modifiers):
        for b in self.buttons:
            b.on_mouse_press(x, y, button, modifiers)
