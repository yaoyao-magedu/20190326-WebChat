# coding = utf-8
"""
Author : yaoyao
Usage : Exec App
"""
from apps.webchatapp import WebChatApp
from PyQt5.QtWidgets import QApplication
import sys

web_app = QApplication(sys.argv)
chat_app = WebChatApp()
sys.exit(web_app.exec())
