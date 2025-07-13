import os
import json
from dataclasses import dataclass
from datetime import datetime


@dataclass()
class File:
    x_pos: int
    y_pos: int
    creation_time: datetime
    last_modified: datetime
    name: str = "New Text File"
    content: str = ""

    def __post_init__(self):
        self.x_pos = int(self.x_pos)
        self.y_pos = int(self.y_pos)

        if not self.name.endswith(".txt"):
            self.name += ".txt"
        if not self.creation_time:
            self.creation_time = datetime.now()
        if not self.last_modified:
            self.last_modified = self.creation_time


    def update_content(self, new_content):
        self.content = new_content
        self.last_modified = datetime.now()


class FileManager():
    def __init__(self):
        user_path = os.path.expanduser("~")
        self.project_folder_path = os.path.join(user_path, "AppData/Local/TkinterOS")
        self.file_folder = os.path.join(self.project_folder_path, "files")
        self.metadata_path = os.path.join(self.file_folder, "metadata.json")

        self.file_objects = []

        self.create_file_folder()
        self.load_files()
        self.create_file_objects()


    def create_file_folder(self):
        os.makedirs(self.file_folder, exist_ok=True)


    def load_metadata(self):
        try:
            with open(self.metadata_path, "r") as metadata_file:
                self.metadata = json.load(metadata_file)
        except FileNotFoundError:
            emtpy_metadata = {"files": {}}
            with open(self.metadata_path, "w") as metadata_file:
                json.dump(emtpy_metadata, metadata_file)
                self.metadata = emtpy_metadata
                


    def load_files(self):
        self.load_metadata()
        self.files = [file for file in os.listdir(self.file_folder) if os.path.isfile(os.path.join(self.file_folder, file))]
        self.files.remove("metadata.json")
        self.text_files = [file for file in self.files if ".txt" in file]


    def create_file_metadata(self, file: File) -> None:
        with open(self.metadata_path, "r") as metadata_file: 
            self.metadata = json.load(metadata_file)

        self.metadata["files"][file.name] = {
            "x_pos": file.x_pos,
            "y_pos": file.y_pos,
            "creation_time": file.creation_time.isoformat(),
            "last_modified": file.last_modified.isoformat()
        }

        with open(self.metadata_path, "w") as metadata_file:
            json.dump(self.metadata, metadata_file)
        
        print(f"metadata for file {file.name} created.")


    def create_actual_file(self, file: File):
        """Checks if a physical file exists and if not creates it"""
        file_path = os.path.join(self.file_folder, file.name)
        if not os.path.exists(file_path):
            open(file_path, "w").close()
            self.create_file_metadata(file)


    def create_file_object(self, x_pos: int, y_pos: int, name: str, last_modified: datetime | None, creation_time: datetime | None) -> File:
        file_object = File(
            x_pos=x_pos,
            y_pos=y_pos,
            name=name,
            last_modified=last_modified,
            creation_time=creation_time,
        )

        self.create_actual_file(file_object)
    
        self.file_objects.append(file_object)
        return file_object


    def create_file_objects(self):
        for file in self.files:
            if not file in self.metadata["files"]:
                continue
            
            self.create_file_object(
                x_pos=self.metadata["files"][file]["x_pos"],
                y_pos=self.metadata["files"][file]["y_pos"],
                name=file,
                last_modified=datetime.fromisoformat(self.metadata["files"][file]["last_modified"]),
                creation_time=datetime.fromisoformat(self.metadata["files"][file]["creation_time"]),
            )


    def get_file_content(self, name: str) -> str:
        file_path = os.path.join(self.file_folder, name)
        with open(file_path, "r") as file:
            content = file.read()
        print(f"{content=}")
        return content
    

    def save_file_content(self, name: str, updated_content: str) -> None:
        file_path = os.path.join(self.file_folder, name)
        print(f"{updated_content=}")
        with open(file_path, "w") as file:
            file.writelines(updated_content)