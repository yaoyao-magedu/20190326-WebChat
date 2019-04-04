import os.path

import itchat
from PyQt5.QtCore import *
from itchat.content import *


class WebChatHelper(QThread):
    sign_qr = pyqtSignal(bytes)
    sign_login_ok = pyqtSignal()
    sign_login_fail = pyqtSignal()
    sign_coming_msg = pyqtSignal(list)

    def __init__(self):
        super().__init__()

    def run(self):
        print("Start Login")
        msgtype = {3: "图片", 47: "表情"}

        @itchat.msg_register(msgType=[TEXT, SHARING, PICTURE, RECORDING, VOICE, ATTACHMENT, VIDEO], isFriendChat=True, isGroupChat=True)
        def recv_msg(msg):
            if msg['MsgType'] == 1:
                self.sign_coming_msg.emit([msg["FromUserName"],
                                           msg['Content'],
                                           msg["ActualNickName"] if msg.get("ActualNickName") else
                                           itchat.search_friends(userName=msg["FromUserName"])["NickName"],
                                           ""])

            elif msg['MsgType'] == 49:
                try:
                    os.mkdir("Download")
                except:
                    pass
                self.sign_coming_msg.emit([msg["FromUserName"],
                                           "请在 Download 文件夹查看收到的文件消息，文件名{}".format(msg['FileName']),
                                           msg["ActualNickName"] if msg.get("ActualNickName") else
                                           itchat.search_friends(userName=msg["FromUserName"])["NickName"],
                                           msg["Text"](str(os.path.join("Download", msg['FileName'])))])

            elif msg['MsgType'] == 3:
                try:
                    os.mkdir("DownloadImg")
                except:
                    pass
                nickname = msg["ActualNickName"] if msg.get("ActualNickName") else \
                    itchat.search_friends(userName=msg["FromUserName"])["NickName"]
                path = os.path.join("DownloadImg", nickname + msg['FileName'])
                self.sign_coming_msg.emit([msg["FromUserName"],
                                           "<img style=\"width:150px;\" src=\"{}\"></img>".format(str(path)),
                                           nickname,
                                           msg["Text"](path)])

            elif msg['MsgType'] == 43 or msg["MsgType"] == 62:
                try:
                    os.mkdir("DownloadVid")
                except:
                    pass
                nickname = msg["ActualNickName"] if msg.get("ActualNickName") else \
                    itchat.search_friends(userName=msg["FromUserName"])["NickName"]
                path = os.path.join("DownloadVid", nickname + msg['FileName'])
                self.sign_coming_msg.emit([msg["FromUserName"],
                                           "请在 DownloadVid 文件夹查看收到的视频消息，文件名{}".format(msg['FileName']),
                                           nickname,
                                           msg["Text"](path)])
            else:
                self.sign_coming_msg.emit([msg["FromUserName"],
                                           "请在手机查看" + msgtype.get(msg["MsgType"], str(msg["MsgType"])) + "消息",
                                           msg["ActualNickName"] if msg.get("ActualNickName") else
                                           itchat.search_friends(userName=msg["FromUserName"])["NickName"],
                                           ""])

        # Login
        itchat.login(qrCallback=self.qr_callback, loginCallback=self.login_callback)

        itchat.run()

    def qr_callback(self, uuid, status, qrcode):
        self.sign_qr.emit(qrcode)
        if status == "400":
            self.sign_login_fail.emit()

    def login_callback(self):
        self.sign_login_ok.emit()

    def get_friends(self):
        lst_user = []
        friends = itchat.get_friends()
        for friend_ in friends:
            user = {}
            user["NickName"] = friend_["NickName"]
            user["UserName"] = friend_["UserName"]
            # user["HeadImg"] = itchat.get_head_img(chatroomUserName=user["UserName"])
            lst_user.append(user)
        return lst_user

    def get_groups(self):
        lst_group = []
        groups = itchat.get_chatrooms()
        for group_ in groups:
            user = {}
            user["NickName"] = group_["NickName"]
            user["UserName"] = group_["UserName"]
            # user["HeadImg"] = itchat.get_head_img(chatroomUserName=user["UserName"])
            lst_group.append(user)

        return lst_group

    def get_mp(self):
        lst_mp = []
        mps = itchat.get_mps()
        for mp_ in mps:
            user = {}
            user["NickName"] = mp_["NickName"]
            user["UserName"] = mp_["UserName"]
            # user["HeadImg"] = itchat.get_head_img(chatroomUserName=user["UserName"])
            lst_mp.append(user)

        return lst_mp

    def send_msg(self, user_, msg_):
        itchat.send_msg(msg=msg_, toUserName=user_)
