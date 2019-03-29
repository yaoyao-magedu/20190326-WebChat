# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_login.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ui_login(object):
    def setupUi(self, ui_login):
        ui_login.setObjectName("ui_login")
        ui_login.setWindowModality(QtCore.Qt.WindowModal)
        ui_login.resize(400, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ui_login.sizePolicy().hasHeightForWidth())
        ui_login.setSizePolicy(sizePolicy)
        ui_login.setMinimumSize(QtCore.QSize(400, 400))
        ui_login.setMaximumSize(QtCore.QSize(400, 400))
        ui_login.setCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
        ui_login.setWindowTitle("微信登陆")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../下载/1L3ryyg.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ui_login.setWindowIcon(icon)
        self.lbl_qr = QtWidgets.QLabel(ui_login)
        self.lbl_qr.setGeometry(QtCore.QRect(0, 0, 400, 400))
        font = QtGui.QFont()
        font.setFamily("STHeiti")
        font.setPointSize(24)
        self.lbl_qr.setFont(font)
        self.lbl_qr.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_qr.setObjectName("lbl_qr")

        self.retranslateUi(ui_login)
        QtCore.QMetaObject.connectSlotsByName(ui_login)

    def retranslateUi(self, ui_login):
        _translate = QtCore.QCoreApplication.translate
        self.lbl_qr.setText(_translate("ui_login", "加载二维码....."))


