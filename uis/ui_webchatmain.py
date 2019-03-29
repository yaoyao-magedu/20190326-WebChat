# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_webchatmain.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(600, 400))
        Form.setMaximumSize(QtCore.QSize(600, 400))
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 240, 400))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.groups = QtWidgets.QListView(self.frame)
        self.groups.setGeometry(QtCore.QRect(0, 230, 238, 171))
        self.groups.setObjectName("groups")
        self.friend_lable = QtWidgets.QLabel(self.frame)
        self.friend_lable.setGeometry(QtCore.QRect(0, 0, 241, 31))
        self.friend_lable.setAlignment(QtCore.Qt.AlignCenter)
        self.friend_lable.setObjectName("friend_lable")
        self.friends = QtWidgets.QListView(self.frame)
        self.friends.setGeometry(QtCore.QRect(0, 30, 238, 171))
        self.friends.setObjectName("friends")
        self.group_lable = QtWidgets.QLabel(self.frame)
        self.group_lable.setGeometry(QtCore.QRect(0, 200, 241, 31))
        self.group_lable.setAlignment(QtCore.Qt.AlignCenter)
        self.group_lable.setObjectName("group_lable")
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setGeometry(QtCore.QRect(250, 50, 341, 291))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.chatdetail = QtWidgets.QWidget()
        self.chatdetail.setGeometry(QtCore.QRect(0, 0, 339, 289))
        self.chatdetail.setObjectName("chatdetail")
        self.scrollArea.setWidget(self.chatdetail)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(250, 360, 271, 30))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(530, 360, 60, 30))
        self.pushButton.setObjectName("pushButton")
        self.chatname = QtWidgets.QLabel(Form)
        self.chatname.setGeometry(QtCore.QRect(250, 10, 341, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chatname.sizePolicy().hasHeightForWidth())
        self.chatname.setSizePolicy(sizePolicy)
        self.chatname.setAlignment(QtCore.Qt.AlignCenter)
        self.chatname.setObjectName("chatname")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.friend_lable.setText(_translate("Form", "好友"))
        self.group_lable.setText(_translate("Form", "群组"))
        self.pushButton.setText(_translate("Form", "发送"))
        self.chatname.setText(_translate("Form", "选择聊天"))


