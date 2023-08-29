import requests

class DiscordClient:
    def __init__(self, bot_token):
        self.bot_token = bot_token

    def send_message(self, channel_id, message):
        url = f"https://discord.com/api/v9/channels/{channel_id}/messages"
        headers = {
            "Authorization": f"Bot {self.bot_token}",
            "Content-Type": "application/json"
        }
        data = {
            "content": message.content,
            "attachments": [attachment.to_dict() for attachment in message.attachments],
            "embeds": [image.to_dict() for image in message.images]
        }
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
