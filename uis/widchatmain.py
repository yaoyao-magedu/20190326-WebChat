# coding = utf-8
import datetime
import os
import shutil
import subprocess

import itchat
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtMultimedia import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import *

from helpers.translatehelper import *
from uis.ui_webchatmain import Ui_Form


class WidChatMain(QWidget):
    def __init__(self, chat_):
        super().__init__()
        self.allchat = {}
        self.chatlists = {}
        self.chat = chat_
        self.form = Ui_Form()
        self.form.setupUi(self)
        self.form.tabWidget.setWindowFlags(Qt.FramelessWindowHint)
        self.chat.sign_coming_msg.connect(self.get_msg)
        self.friendmodel = QStandardItemModel()
        self.currentmodel = QStandardItemModel()
        self.form.friends.setModel(self.friendmodel)
        self.form.friends.clicked.connect(self.select_user)
        self.mpmodel = QStandardItemModel()
        self.form.mplist.setModel(self.mpmodel)
        self.form.mplist.clicked.connect(self.select_mp)
        self.form.current.setModel(self.currentmodel)
        self.form.current.clicked.connect(self.select_current)
        self.form.send.clicked.connect(self.send_msg)
        self.form.closeButton.clicked.connect(self.exit)
        self.form.searchButton.clicked.connect(self.search)
        self.form.searchmpButton.clicked.connect(self.searchmp)
        self.message_label = QLabel()
        self.form.scrollArea.setWidget(self.message_label)
        self.current_user = None
        self.current = set()
        self.form.clean.clicked.connect(lambda: self.form.textEdit.setText(""))
        self.form.send.setShortcut("Ctrl+Return")
        self.form.min.clicked.connect(lambda: self.showMinimized())
        self.m_flag = False
        self.setWindowTitle("微信Qt")
        self.message_label.setGeometry(QRect(
            self.message_label.x() + 10,
            self.message_label.y(),
            310,
            self.message_label.height()))
        self.message_label.setScaledContents(True)

        font = QFont()
        font.setPointSize(10)
        self.message_label.setFont(font)
        self.message_label.setWordWrap(True)
        self.mpview1 = QWebEngineView(self.form.mpframe)
        self.mpview = QWebEnginePage(self.mpview1)
        self.mpview1.setGeometry(QRect(0, 0, 441, 391))
        self.mpview.setObjectName("mpview")
        self.mpview.urlChanged.connect(self.reload)
        self.mpb = QPushButton(self.form.mpframe)
        self.mpb.setGeometry(QRect(420, 0, 21, 21))
        self.mpb.setObjectName("mpb")
        self.mpb.setText("刷")
        # self.mpview.link_clicked().connect(lambda x:print(x))

        self.form.tabWidget.setCurrentIndex(1)
        self.form.mpframe.hide()
        self.mpb.clicked.connect(
            lambda: self.mpview.runJavaScript("""
        var list = document.getElementsByTagName("a")
        for (var i= list.length; i-->0;)
            list[i].removeAttribute("target");
        """))
        self.form.friendsound.setTristate(False)
        self.form.groupsound.setTristate(False)
        # self.recapture = uis.recapture.recap()
        # self.recapture.show()
        self.form.translateButton.clicked.connect(self.translate)
        # self.form.translatesoundButton.clicked.connect(self.translatesound)

    def exit(self):
        shutil.rmtree("tmp", ignore_errors=True)
        QApplication.quit()

    def reload(self):
        self.mpview.load(self.mpview.url())
        # self.mpview.
        # time.sleep(2)
        self.mpview.loadFinished.connect(
            lambda: self.mpview.runJavaScript("""
         var list = document.getElementsByTagName("a")
         for (var i= list.length; i-->0;)
             list[i].removeAttribute("target");
         """))
        # self.mpview1.setPage(self.mpview)

    def mousePressEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.LeftButton and \
                (QMouseEvent.globalPos() - self.pos()).x() < 700 and \
                (QMouseEvent.globalPos() - self.pos()).y() < 60:
            self.m_flag = True
            self.m_Position = QMouseEvent.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            QMouseEvent.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))  # 更改鼠标图标
        else:
            super().mousePressEvent(QMouseEvent)

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()
        else:
            super().mouseMoveEvent(QMouseEvent)

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))
        super().mouseReleaseEvent(QMouseEvent)

    def search(self):
        search_string = self.form.searchbar.text()
        items = self.friendmodel.findItems(search_string, Qt.MatchStartsWith)
        for item in items:
            if search_string:
                self.friendmodel.takeRow(item.row())
                self.friendmodel.insertRow(0, item)

    def searchmp(self):
        search_string = self.form.searchmp.text()
        items = self.mpmodel.findItems(search_string, Qt.MatchStartsWith)
        for item in items:
            if search_string:
                self.mpmodel.takeRow(item.row())
                self.mpmodel.insertRow(0, item)

    def show_message(self):
        try:
            a = ""
            for _ in self.chatlists.get(self.current_user):
                a += _
            self.message_label.setText(a)
            self.message_label.setTextInteractionFlags(Qt.TextSelectableByMouse)
            self.form.scrollArea.verticalScrollBar().setValue(9999)
        except Exception as e:
            self.message_label.setText("无消息")

    def select_user(self, index):
        self.form.mpframe.hide()
        row = index.row()
        self.form.chatname.setText(self.allchat[self.friendmodel.item(row).data()])
        self.current_user = self.friendmodel.item(row).data()
        self.show_message()

    def select_current(self, index):
        self.form.mpframe.hide()
        row = index.row()
        self.form.chatname.setText(self.allchat[self.currentmodel.item(row).data()])
        self.current_user = self.currentmodel.item(row).data()
        self.current.remove(self.current_user)
        self.currentmodel.removeRow(row)
        self.show_message()

    def select_mp(self, index):
        row = index.row()
        self.form.mpframe.show()
        self.form.chatname.setText(self.allchat[self.mpmodel.item(row).data()])
        self.current_user = self.mpmodel.item(row).data()
        name = self.allchat[self.mpmodel.item(row).data()]
        a = "http://www.sogou.com/web?ie=utf8&query={} 公众号".format(
            name)
        self.mpview.load(QUrl(a))
        self.mpview1.setPage(self.mpview)

    def send_msg(self):
        msg = self.form.textEdit.toPlainText().strip()
        if msg:
            if self.current_user:
                self.chat.send_msg(self.current_user, msg)
                self.form.textEdit.setText("")
                if self.chatlists.get(self.current_user):
                    self.chatlists[self.current_user].append("<p style='color:red;'>{}---------------</p>".format(
                        datetime.datetime.now().strftime("%m-%d %H:%M:%S")) + msg)
                else:
                    self.chatlists[self.current_user] = ["<p style='color:red;'>{}---------------</p>".format(
                        datetime.datetime.now().strftime("%m-%d %H:%M:%S")) + msg]
                self.show_message()
        else:
            QMessageBox.about(self, "错误", "请输入内容")

    def get_msg(self, msg):
        if self.chatlists.get(msg[0]):
            self.chatlists[msg[0]].append("<p style='color:green;'>{}--{}-------------</p>".format(
                datetime.datetime.now().strftime("%m-%d %H:%M:%S"), msg[2]) + msg[1], )
        else:
            self.chatlists[msg[0]] = ["<p style='color:green;'>{}--{}-------------</p>".format(
                datetime.datetime.now().strftime("%m-%d %H:%M:%S"), msg[2]) + msg[1]]
        if msg[0].startswith("@@"):
            msg[2] = itchat.search_chatrooms(userName=msg[0])["NickName"]
            icon_head = QIcon("imgs/group.png")
            if self.form.groupsound.checkState():
                QSound.play("sounds/notice.wav")
        else:
            msg[2] = itchat.search_friends(userName=msg[0])["NickName"]
            icon_head = QIcon("imgs/friends.png")
            if self.form.friendsound.checkState():
                QSound.play("sounds/notice.wav")

        if msg[0] not in self.current and msg[0] != self.current_user:
            user_name = msg[0]
            nick_name = msg[2]
            item_ = QStandardItem(icon_head, nick_name)
            item_.setData(user_name)
            self.currentmodel.appendRow(item_)
            self.current.add(msg[0])
        self.show_message()

    def show_user_list(self):
        lst_group = self.chat.get_groups()
        for user_ in lst_group:
            user_name = user_["UserName"]
            nick_name = user_["NickName"]
            icon_head = QIcon("imgs/group.png")
            item_ = QStandardItem(icon_head, nick_name)
            item_.setData(user_name)
            self.friendmodel.appendRow(item_)
            self.allchat[user_name] = nick_name
        lst_user = self.chat.get_friends()
        for user_ in lst_user:
            user_name = user_["UserName"]
            nick_name = user_["NickName"]
            icon_head = QIcon("imgs/friends.png")
            item_ = QStandardItem(icon_head, nick_name)
            item_.setData(user_name)
            self.friendmodel.appendRow(item_)
            self.allchat[user_name] = nick_name
        myimg = itchat.get_head_img(userName=itchat.search_friends()["UserName"])
        self_img = QPixmap.fromImage(QImage.fromData(myimg))
        self.form.selfpic.setPixmap(self_img)
        self.form.selfpic.setScaledContents(True)

    def show_mp_list(self):
        lst_mp = self.chat.get_mp()
        for user_ in lst_mp:
            user_name = user_["UserName"]
            nick_name = user_["NickName"]
            icon_head = QIcon("imgs/mps.png")
            item_ = QStandardItem(icon_head, nick_name)
            item_.setData(user_name)
            self.mpmodel.appendRow(item_)
            self.allchat[user_name] = nick_name

    def translate(self):
        trans = TranslateHelper(self.form.translateText.text())
        self.form.translateResult.setText(trans.webxml())
        self.form.translatesoundButton.clicked.connect(self.translateplay)

    def translateplay(self):
        try:
            os.startfile("tmp/{}.mp3".format(self.form.translateText.text()))
        except AttributeError:
            subprocess.call(['xdg-open', "tmp/{}.mp3".format(self.form.translateText.text())])
