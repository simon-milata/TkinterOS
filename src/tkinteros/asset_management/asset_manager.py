import os
from typing import Tuple

from PIL import Image, ImageColor

class AssetManager:
    def __init__(self, asset_folder: str):
        self.asset_folder = asset_folder


    def get_image(self, relative_path: str, hex_color: str | None = None, resize: bool = True):
        image = Image.open(os.path.join(self.asset_folder, relative_path))

        if resize:
            image = self.resize_image(image=image)

        if not hex_color:
            return image

        colored_image = self.color_image(image, rgb_new_color=ImageColor.getrgb(hex_color))

        return colored_image
    

    def get_sound(self, relative_path: str):
        return os.path.join(self.asset_folder, relative_path)
    

    def get_icon(self, relative_path: str):
        return os.path.join(self.asset_folder, relative_path)
    

    def resize_image(self, image: Image.Image, size: Tuple[int, int] = (64, 64)):
        return image.resize((size[0], size[1]), resample=Image.LANCZOS)
    

    def color_image(self, image: Image.Image, rgb_new_color: tuple[int, int, int]):
        pixel_list = list(image.getdata())

        modified_pixels = [
            (*rgb_new_color, pixel[3]) if pixel[:3] == (0, 0, 0) else pixel
            for pixel in pixel_list
        ]

        colored_image = Image.new(mode="RGBA", size=image.size)
        colored_image.putdata(modified_pixels)

        return colored_image
