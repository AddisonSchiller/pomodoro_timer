import os

from pyglet.image import load as pload

BASE = os.path.dirname(os.path.abspath(__file__))
FOLDER = 'images'


class ImageAssets(object):

    def __init__(self):
        self.image_dict = {}

    def _load_image(self, image, anchor=True):

        img = pload(os.path.join(BASE, FOLDER, image))
        if anchor:
            img.anchor_x = img.width // 2
            img.anchor_y = img.height // 2
        self.image_dict[image] = img
        return img

    def __getitem__(self, image):
        image += '.png'
        if image in self.image_dict:
            return self.image_dict[image]
        else:
            return self._load_image(image)

IMAGE_ASSETS = ImageAssets()
