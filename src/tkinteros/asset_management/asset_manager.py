import os
from typing import Tuple
import tempfile
import logging

from PIL import Image, ImageColor, ImageTk


class AssetManager:
    def __init__(self, asset_folder: str, appearance_mode: str):
        self.asset_folder = asset_folder
        self.temp_files = []
        
        self.window_background_color = (240, 240, 240) if appearance_mode == "light" else (32, 32, 32)


    def get_image(self, relative_path: str, hex_color: str | None = None, resize: bool = True):
        image = Image.open(os.path.join(self.asset_folder, relative_path))

        if resize:
            image = self.resize_image(image=image)
        if hex_color:
            image = self.color_image(image=image, rgb_new_color=ImageColor.getrgb(hex_color))

        return image
    

    def get_sound(self, relative_path: str):
        return os.path.join(self.asset_folder, relative_path)
    

    def get_icon(self, relative_path: str, hex_color: str | None = None):
        image = self.get_image(relative_path=relative_path, hex_color=hex_color)

        # Flatten transparency onto a background
        background = Image.new("RGB", image.size, self.window_background_color)
        background.paste(image, mask=image.split()[3] if image.mode == "RGBA" else None)

        with tempfile.NamedTemporaryFile(suffix=".ico", delete=False) as tmp:
            background.save(tmp, format="ICO", sizes=[(32, 32)])
            ico_path = tmp.name

        self.temp_files.append(ico_path)

        return ico_path
    

    def resize_image(self, image: Image.Image, size: Tuple[int, int] = (64, 64)):
        return image.resize((size[0], size[1]), resample=Image.LANCZOS)
    

    def color_image(self, image: Image.Image, rgb_new_color: tuple[int, int, int]):
        image = image.convert("RGBA")
        pixel_list = list(image.getdata())

        modified_pixels = [
            (*rgb_new_color, pixel[3]) if pixel[:3] == (0, 0, 0) else pixel
            for pixel in pixel_list
        ]

        colored_image = Image.new(mode="RGBA", size=image.size)
        colored_image.putdata(modified_pixels)
        return colored_image


    def delete_temp_files(self):
        for file_path in self.temp_files:
            logging.debug(f"Deleting temp file {file_path}...")
            os.remove(file_path)