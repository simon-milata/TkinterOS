import os
import json
from dataclasses import dataclass
from datetime import datetime


@dataclass()
class File:
    pos_x: int
    pos_y: int
    creation_time: str
    last_edited: str
    name: str = "New Text File"
    content: str = ""

    def __post_init__(self):
        self.pos_x = int(self.pos_x)
        self.pos_y = int(self.pos_y)

        if not self.creation_time:
            self.creation_time = datetime.now()
        if not self.last_edited:
            self.last_edited = self.creation_time


class FileManager():
    def __init__(self):
        user_path = os.path.expanduser("~")
        self.project_folder_path = os.path.join(user_path, "AppData/Local/TkinterOS")
        self.file_folder = os.path.join(self.project_folder_path, "files")

        self.file_objects = []

        self.create_file_folder()
        self.load_files()
        self.create_file_objects()


    def create_file_folder(self):
        os.makedirs(self.file_folder, exist_ok=True)


    def load_metadata(self):
        try:
            with open(os.path.join(self.file_folder, "metadata.json"), "r") as metadata_file:
                self.metadata = json.load(metadata_file)
        except FileNotFoundError:
            emtpy_metadata = {"files": []}
            with open(os.path.join(self.file_folder, "metadata.json"), "w") as metadata_file:
                self.metadata = json.dump(emtpy_metadata, metadata_file)
                


    def load_files(self):
        self.load_metadata()
        self.files = [file for file in os.listdir(self.file_folder) if os.path.isfile(os.path.join(self.file_folder, file))]
        self.files.remove("metadata.json")
        self.text_files = [file for file in self.files if ".txt" in file]


    def create_file_objects(self):
        for file in self.files:
            file_object = File(
                pos_x=self.metadata["files"][file]["x_pos"],
                pos_y=self.metadata["files"][file]["y_pos"],
                name=[file],
                last_edited=self.metadata["files"][file]["last_modified"],
                creation_time=self.metadata["files"][file]["creation_time"],
            )
            self.file_objects.append(file_object)
