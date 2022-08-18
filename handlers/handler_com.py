# импортируем класс родитель

from handlers.handler import Handler


class HandlerCommands(Handler):
    # обрабатывает вход команды
    def __init__(self, bot):
        super().__init__(bot)

    def pressed_btn_start(self, message):
        # обрабатываем /start команды
        self.bot.send_message(message.chat.id, f'{message.from_user.first_name},'
                                               f'hello! I wait for ur command.',
                              reply_markup=self.keyboards.start_menu())

    def handle(self):
        # обработчик( декоратор) сообщений
        # обр вход /start команды
        @self.bot.message_handler(commands=["start"])
        def handle(message):
            if message.text == "/start":
                self.pressed_btn_start(message)
