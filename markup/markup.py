from telebot.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup,ReplyKeyboardRemove
from settings import config
from data_base.dbalchemy import DBManager


class Keyboards:
    # класс для реализации интерфейса
    def __init__(self):
        self.markup = None
        self.DB = DBManager()

    @staticmethod
    def set_btn(name, step=0, quantity=0):
        return KeyboardButton(config.KEYBOARD[name])

    def start_menu(self):
        self.markup = ReplyKeyboardMarkup(True, True)
        itm_btn_1 = self.set_btn("CHOOSE_GOODS")
        itm_btn_2 = self.set_btn("INFO")
        itm_btn_3 = self.set_btn("SETTINGS")
        # расположение кнопок
        self.markup.row(itm_btn_1)
        self.markup.row(itm_btn_2, itm_btn_3)
        return self.markup

    def info_menu(self):
        self.markup = ReplyKeyboardMarkup(True, True)
        itm_btn_1 = self.set_btn("<<")
        self.markup.row(itm_btn_1)
        return self.markup

    def settings_menu(self):
        self.markup = ReplyKeyboardMarkup(True, True)
        itm_btn_1 = self.set_btn('<<')
        # рассположение кнопок в меню
        self.markup.row(itm_btn_1)
        return self.markup

    @staticmethod
    def remove_menu():
        return ReplyKeyboardRemove()

    def category_menu(self):
        self.markup = ReplyKeyboardMarkup(True, True, row_width=1)
        self.markup.row(self.set_btn('SEMIPRODUCT'))
        self.markup.row(self.set_btn('GROCERY'))
        self.markup.row(self.set_btn('ICE_CREAM'))
        self.markup.row(self.set_btn('<<'), self.set_btn('ORDER'))
        return self.markup

    @staticmethod
    def set_inline_btn(name):
        return InlineKeyboardButton(str(name), callback_data=str(name.id))

    def set_select_category(self, category):
        self.markup = InlineKeyboardMarkup(row_width=1)
        for itm in self.DB.select_all_products_category(category):
            self.markup.add(self.set_inline_btn(itm))
        return self.markup
