from typing import List
from .attachment import Attachment
from .image import Image

class Message:
    def __init__(self, content: str, attachments: List[Attachment], images: List[Image]):
        self.content = content
        self.attachments = attachments
        self.images = images
