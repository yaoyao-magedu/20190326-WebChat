# coding = utf-8
"""
Author : yaoyao
Usage : Exec App
"""
import sys

from PyQt5.QtWidgets import QApplication

from apps.webchatapp import WebChatApp

web_app = QApplication(sys.argv)
chat_app = WebChatApp()
sys.exit(web_app.exec())
