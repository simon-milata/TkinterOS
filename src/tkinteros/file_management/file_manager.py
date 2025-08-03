import os
import json
import logging
from datetime import datetime
from string import punctuation
import re

from tkinteros.file_management.file import File


class FileManager():
    def run(self):
        user_path = os.path.expanduser("~")
        self.project_folder_path = os.path.join(user_path, "AppData/Local/TkinterOS")
        self.file_folder = os.path.join(self.project_folder_path, "files")
        self.metadata_path = os.path.join(self.file_folder, "metadata.json")

        self.file_objects = []

        self.create_file_folder()
        self.load_files()
        self.load_file_objects()


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
        
        logging.debug(f"Metadata for {file.name} created.")


    def create_actual_file(self, file: File):
        """Checks if a physical file exists and if not creates it"""
        file_path = os.path.join(self.file_folder, file.name)
        if not os.path.exists(file_path):
            open(file_path, "w").close()

            logging.debug(f"Physical file ({file}) created.")

            self.create_file_metadata(file)
        self.load_files()


    def create_file_object(self, x_pos: int, y_pos: int, name: str, last_modified: datetime | None, creation_time: datetime | None) -> File:
        file_object = File(
            x_pos=x_pos,
            y_pos=y_pos,
            name=name,
            last_modified=last_modified,
            creation_time=creation_time,
        )

        logging.debug(f"Loading file ({file_object}).")

        self.create_actual_file(file_object)
    
        self.file_objects.append(file_object)
        return file_object


    def load_file_objects(self):
        """Creates file objects from files + metadata and adds them to a list"""

        logging.debug(f"Loading file objects...")

        for file in self.files:
            if not file in self.metadata["files"]:
                continue

            file_metadata = self.metadata["files"][file]
            
            self.create_file_object(
                x_pos=file_metadata["x_pos"],
                y_pos=file_metadata["y_pos"],
                name=file,
                last_modified=datetime.fromisoformat(file_metadata["last_modified"]),
                creation_time=datetime.fromisoformat(file_metadata["creation_time"]),
            )


    def get_file_content(self, name: str) -> str:
        file_path = os.path.join(self.file_folder, name)
        with open(file_path, "r") as file:
            content = file.read()

        logging.debug(f"Loading file content:\n'{content}' from {name}.")

        return content
    

    def save_file_content(self, name: str, updated_content: str) -> None:
        file_path = os.path.join(self.file_folder, name)
        with open(file_path, "w") as file:
            file.writelines(updated_content)

        logging.debug(f"Saving file content:\n'{updated_content}' to {name}.")


    def validate_file_name_on_creation(self, file_name: str, files: list[str]) -> bool:
        """Returns True if the length of filename is in set range and filename is unique."""
        base_file_name = self.get_file_basename(file_name)

        if file_name.startswith(tuple(punctuation)):
            logging.debug(f"Validation for '{file_name}' failed! File name mustn't start with a special character.")
            return False
        
        if not re.match(r"^(?:[^a-zA-Z0-9]*[a-zA-Z0-9]){2,}.*$", file_name):
            logging.debug(f"Validation for '{file_name}' failed! File name must contain at least 2 characters.")
            return False

        if not 1 < len(base_file_name) < 11:
            logging.debug(f"Validation for '{file_name}' failed! File name not in length range [2, 10].")
            return False
        
        if base_file_name in map(self.get_file_basename, files):
            logging.debug(f"Validation for '{file_name}' failed! Base filename already exists.")
            return False
        
        logging.debug(f"Validation for '{file_name}' succeded.")
        return True
    

    def get_file_basename(self, file_name: str) -> str:
        return os.path.splitext(os.path.basename(file_name))[0]