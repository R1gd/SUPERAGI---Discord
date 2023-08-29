from dataclasses import dataclass

@dataclass
class Image:
    file_name: str
    file_data: bytes

    def to_dict(self):
        return {
            "filename": self.file_name,
            "content": self.file_data.decode("utf-8")
        }
