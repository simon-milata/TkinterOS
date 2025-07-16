from datetime import datetime
from dataclasses import dataclass

@dataclass()
class File:
    x_pos: int
    y_pos: int
    creation_time: datetime | None
    last_modified: datetime | None
    name: str = "New Text File"
    content: str = ""

    def __repr__(self):
        return f"Name: {self.name}, X: {self.x_pos}, Y: {self.y_pos}, Created: {self.creation_time.strftime("%d/%m/%Y %H:%M:%S")}, Last Modified: {self.last_modified.strftime("%d/%m/%Y %H:%M:%S")}"

    def __post_init__(self):
        self.x_pos = int(self.x_pos)
        self.y_pos = int(self.y_pos)

        if self.name and not self.name.endswith(".txt"):
            self.name += ".txt"
        if not self.creation_time:
            self.creation_time = datetime.now()
        if not self.last_modified:
            self.last_modified = self.creation_time


    def update_content(self, new_content):
        self.content = new_content
        self.last_modified = datetime.now()