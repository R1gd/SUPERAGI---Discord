from .discord_client import DiscordClient
from .message import Message
from .attachment import Attachment
from .image import Image

def send_message(bot_token: str, channel_id: str, content: str, attachment_file_name: str, attachment_file_data: bytes, image_file_name: str, image_file_data: bytes):
    discord_client = DiscordClient(bot_token)
    attachment = Attachment(attachment_file_name, attachment_file_data)
    image = Image(image_file_name, image_file_data)
    message = Message(content, [attachment], [image])
    discord_client.send_message(channel_id, message)
