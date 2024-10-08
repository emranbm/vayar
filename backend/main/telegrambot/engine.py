from django.conf import settings
from telegram.ext import ApplicationBuilder, Application

from main.telegrambot.command_handlers.start_command_handler import StartCommandHandler


class TelegramBotEngine:
    @staticmethod
    def create_app() -> Application:
        app_builder = ApplicationBuilder().token(settings.TELEGRAM_BOT_TOKEN)
        proxy_url = settings.TELEGRAM_PROXY_URL
        if proxy_url is not None:
            app_builder = app_builder \
                .proxy_url(proxy_url) \
                .get_updates_proxy_url(proxy_url)
        return app_builder.build()

    @staticmethod
    def run() -> None:
        app = TelegramBotEngine.create_app()
        app.add_handler(StartCommandHandler())
        app.run_polling(drop_pending_updates=True)
