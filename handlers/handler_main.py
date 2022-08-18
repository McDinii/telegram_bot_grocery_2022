from handlers.handler_com import HandlerCommands
from handlers.handler_all_text import HandlerAllText


class HandlerMain:
    # класс компановщик
    def __init__(self, bot):
        # бота получаем
        self.bot = bot  # инициализ обработчики
        self.handler_commands = HandlerCommands(self.bot)
        self.handler_all_text = HandlerAllText(self.bot)

    def handle(self):
        # запускаем обработчики
        self.handler_commands.handle()
        self.handler_all_text.handle()
