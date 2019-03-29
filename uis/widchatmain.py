# coding = utf-8
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from uis.ui_webchatmain import Ui_Form
import itchat

class WidChatMain(QWidget):
    def __init__(self, chat_):
        super().__init__()
        self.chat = chat_
        self.form = Ui_Form()
        self.form.setupUi(self)

        self.chat.sign_coming_msg.connect(self.show_msg)

        self.model = QStandardItemModel()
        self.form.listView.setModel(self.model)

        self.form.listView.clicked.connect(self.select_user)
        self.form.pushButton.clicked.connect(self.send_msg)

    def select_user(self, index):
        # print(index, type(index))
        # get current user
        row = index.row()
        # data1 = index.data()
        # self.current_user.append(data1)
        self.form.chatname.setText(self.model.item(row).data())
        self.current_user = self.model.item(row).data()

    def send_msg(self):
        msg = self.form.lineEdit.text()
        # send(Assistant Class)
        if self.current_user:
            self.chat.send_msg(self.current_user, msg)

    def show_msg(self, msg):
        self.setWindowTitle(msg)
        # self.form.scrollArea

    def show_user_list(self):
        # 调用辅助
        lst_user = self.chat.get_friends()

        for user_ in lst_user:
            user_name = user_["UserName"]
            nick_name = user_["NickName"]
            icon = itchat.get_head_img(userName==[user_name])
            icon_head = QIcon("imgs/user.png")
            item_ = QStandardItem(icon_head, nick_name)
            item_.setData(user_name)
            self.form.friend_lable.appendRow(item_)

    def show_group_list(self):
        # 调用辅助
        lst_group = self.chat.get_groups()

        for user_ in lst_group:
            user_name = user_["UserName"]
            nick_name = user_["NickName"]
            icon = itchat.get_head_img(chatroomUserName=[user_name])
            icon_head = QIcon("imgs/user.png")
            item_ = QStandardItem(icon_head, nick_name)
            item_.setData(user_name)
            self.form.group_lable.appendRow(item_)