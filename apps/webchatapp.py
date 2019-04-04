# coding=utf-8
from PyQt5.QtCore import *

from helpers.webchathelper import WebChatHelper
from uis.dlgqrlogin import DlgQRLogin
from uis.widchatmain import WidChatMain


class WebChatApp(QObject):

    def __init__(self):
        super().__init__()
        self.chat = WebChatHelper()

        self.ui_login = DlgQRLogin(self.chat)
        self.ui_login.show()
        self.ui_main = WidChatMain(self.chat)
        # self.ui_main.show()

        self.chat.start()
        self.chat.sign_login_ok.connect(self.show_chat_main)
        self.chat.sign_login_fail.connect(self.show_error)

    def show_chat_main(self):
        self.ui_login.hide()
        self.ui_login.destroy()
        self.ui_main.show_user_list()
        self.ui_main.show_mp_list()
        self.ui_main.setWindowFlags(Qt.FramelessWindowHint)
        self.ui_main.show()

    def show_error(self):
        self.ui_login.error()
