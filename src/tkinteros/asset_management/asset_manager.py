import os

from PIL import Image

class AssetManager:
    def __init__(self, asset_folder: str):
        self.asset_folder = asset_folder


    def get_image(self, relative_path: str):
        return Image.open(os.path.join(self.asset_folder, relative_path))
    

    def get_sound(self, relative_path: str):
        return os.path.join(self.asset_folder, relative_path)
    

    def get_icon(self, relative_path: str):
        return os.path.join(self.asset_folder, relative_path)