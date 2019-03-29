# coding = utf-8

from PyQt5.QtCore import *
import itchat


class WebChatHelper(QThread):

    sign_qr = pyqtSignal(bytes)
    sign_login_ok = pyqtSignal()
    sign_coming_msg = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def run(self):
        print("Start Login")
        # Login

        @itchat.msg_register(msgType=itchat.content.TEXT, isFriendChat=True, isGroupChat=True)
        def recv_msg(self, msg):
            if msg["MsgType"] == 1:
                self.sign.coming_msg.emit(msg["Content"])

        itchat.login(qrCallback=self.qr_callback, loginCallback=self.login_callback)

        itchat.run()

    def qr_callback(self, uuid, status, qrcode):
        self.sign_qr.emit(qrcode)

    def login_callback(self):
        print("Login OK")
        self.sign_login_ok.emit()

    def get_friends(self):

        lst_user = []
        friends = itchat.get_friends()
        for friend_ in friends:
            user = {}
            user["NickName"] = friend_["NickName"]
            user["UserName"] = friend_["UserName"]
            lst_user.append(user)

    def get_groups(self):
        lst_group = []
        groups = itchat.get_chatrooms()
        for group_ in groups:
            user = {}
            user["NickName"] = group_["NickName"]
            user["UserName"] = group_["UserName"]
            lst_group.append(user)

        return lst_user

    def send_msg(self, user_, msg_):
        itchat.send_msg(msg=msg_, toUserName=user_)
