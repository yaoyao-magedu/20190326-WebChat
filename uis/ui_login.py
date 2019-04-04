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
        ui_login.setWindowModality(QtCore.Qt.ApplicationModal)
        ui_login.resize(350, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ui_login.sizePolicy().hasHeightForWidth())
        ui_login.setSizePolicy(sizePolicy)
        ui_login.setMinimumSize(QtCore.QSize(350, 400))
        ui_login.setMaximumSize(QtCore.QSize(350, 400))
        ui_login.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        ui_login.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        ui_login.setWindowTitle("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../下载/1L3ryyg.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ui_login.setWindowIcon(icon)
        ui_login.setStyleSheet("background:rgb(255, 255, 255);")
        ui_login.setSizeGripEnabled(False)
        ui_login.setModal(False)
        self.lbl_qr = QtWidgets.QLabel(ui_login)
        self.lbl_qr.setGeometry(QtCore.QRect(0, 50, 350, 350))
        font = QtGui.QFont()
        font.setFamily("STHeiti")
        font.setPointSize(24)
        self.lbl_qr.setFont(font)
        self.lbl_qr.setCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
        self.lbl_qr.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_qr.setObjectName("lbl_qr")
        self.windowTitleBar = QtWidgets.QFrame(ui_login)
        self.windowTitleBar.setGeometry(QtCore.QRect(0, 0, 351, 41))
        self.windowTitleBar.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.windowTitleBar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.windowTitleBar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.windowTitleBar.setObjectName("windowTitleBar")
        self.titleName = QtWidgets.QLabel(self.windowTitleBar)
        self.titleName.setGeometry(QtCore.QRect(30, 0, 61, 43))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Arabic")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.titleName.setFont(font)
        self.titleName.setAutoFillBackground(False)
        self.titleName.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.titleName.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.titleName.setObjectName("titleName")
        self.closeButton = QtWidgets.QPushButton(self.windowTitleBar)
        self.closeButton.setGeometry(QtCore.QRect(290, -5, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.closeButton.setFont(font)
        self.closeButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.closeButton.setCheckable(False)
        self.closeButton.setAutoDefault(False)
        self.closeButton.setFlat(True)
        self.closeButton.setObjectName("closeButton")

        self.retranslateUi(ui_login)
        QtCore.QMetaObject.connectSlotsByName(ui_login)

    def retranslateUi(self, ui_login):
        _translate = QtCore.QCoreApplication.translate
        self.lbl_qr.setText(_translate("ui_login", "加载二维码....."))
        self.titleName.setText(_translate("ui_login", "微信QT"))
        self.closeButton.setText(_translate("ui_login", "×"))
