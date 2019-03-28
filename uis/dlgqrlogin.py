# coding = utf-8
"""
A
"""
from PyQt5.QtWidgets import *
from uis.ui_login import Ui_ui_login
from PyQt5.QtGui import *


class DlgQRLogin(QDialog):
    def __init__(self, chat_):
        super().__init__()
        self.chat = chat_
        self.ui = Ui_ui_login()
        self.ui.setupUi(self)

        # Get QR Code
        self.chat.sign_qr.connect(self.show_qr)

    def show_qr(self, qrcode):
        img_qr = QImage.fromData(qrcode)
        pix_qr = QPixmap.fromImage(img_qr)
        self.ui.lbl_qr.setPixmap(pix_qr)
        self.ui.lbl_qr.setScaledContents(True)
