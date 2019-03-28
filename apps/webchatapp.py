# coding = utf-8
"""
Usage: compress UI and API
"""
from PyQt5.QtCore import *
from uis.dlgqrlogin import DlgQRLogin
from uis.widchatmain import WidChatMain
from helpers.webchathelper import WebChatHelper


class WebChatApp(QObject):
    """
    Usage : compress Wechat ,UI for login , chat
    """
    def __init__(self):
        super().__init__()
        self.chat = WebChatHelper()

        self.ui_login = DlgQRLogin(self.chat)
        self.ui_login.show()
        self.ui_main = WidChatMain(self.chat)
        # self.ui_main.show()
        # 调用辅助类实现登陆

        self.chat.start()
        self.chat.sign_login_ok.connect(self.show_chat_main)

    def show_chat_main(self):
        # hide login gui
        self.ui_login.hide()
        # destroy login UI
        self.ui_login.destroy()
        # List Users
        self.ui_main.show_user_list()
        # show chat form
        self.ui_main.show()
