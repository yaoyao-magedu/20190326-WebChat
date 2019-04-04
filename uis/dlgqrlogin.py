# coding = utf-8
"""
A
"""
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from uis.ui_login import Ui_ui_login


class DlgQRLogin(QDialog):
    def __init__(self, chat_):
        super().__init__()
        self.chat = chat_
        self.ui = Ui_ui_login()
        self.ui.setupUi(self)
        self.ui.lbl_qr.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.ui.closeButton.clicked.connect(QApplication.quit)

        # Get QR Code
        self.chat.sign_qr.connect(self.show_qr)

    def show_qr(self, qrcode):
        img_qr = QImage.fromData(qrcode)
        pix_qr = QPixmap.fromImage(img_qr)
        self.ui.lbl_qr.setPixmap(pix_qr)
        self.ui.lbl_qr.setScaledContents(True)
        self.ui.lbl_qr.setCursor(QCursor(Qt.ArrowCursor))

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))

    def error(self):
        errBox = QMessageBox()
        errBox.setWindowFlags(Qt.FramelessWindowHint)
        errBox.setText("登录失败，可能该账号被禁止登录")
        errBoxRun = errBox.exec_()
        if errBoxRun:
            QApplication.quit()
