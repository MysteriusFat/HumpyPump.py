import requests
from config import headers

class TriggerBot:
    def __init__(self, channel_id, separator):
        self.url = 'https://discord.com/api/v8/channels/{}/messages?limit=5'.format(channel_id)
        self.separator = separator
        self.coin = ''

    def GetMessages(self):
        r = requests.get(self.url, headers=headers)
        return r.json()

    def IsValidMessage(self, message):
        if self.separator in message:
            return True
        return False

    def GetCoinFromMessage(self, message):
        index = message.index(self.separator)
        self.coin = message[index+1:index+4]

