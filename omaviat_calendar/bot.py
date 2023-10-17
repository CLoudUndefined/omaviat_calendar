from telebot.async_telebot import AsyncTeleBot


class TelegramBot(AsyncTeleBot):
    def __init__(self, token: str, **kwargs) -> None:
        super().__init__(token, **kwargs)

