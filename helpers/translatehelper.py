import base64
import os.path
import xml.etree.ElementTree as et

import requests


class TranslateHelper:
    def __init__(self, kw):
        self.kw = kw
        # self.mp3file = os.path.join(
        #     tempfile.gettempdir(), "WechatQtTranslate", "tmp.mp3")
        self.mp3file = "tmp/{}.mp3".format(kw)

    def webxml(self):
        req = requests.post(
            url="http://fy.webxml.com.cn/webservices/EnglishChinese.asmx/TranslatorString",
            data={"wordKey": self.kw},
        )
        try:
            doc = et.ElementTree(et.fromstring(req.text))
            root = doc.getroot()
            array = []
            for x in root.iter():
                array.append(x.text)
            os.mkdir("tmp")
            req = requests.post(
                url="http://fy.webxml.com.cn/webservices/EnglishChinese.asmx/GetMp3",
                data={"Mp3": array[5]},
            )
            for _ in et.ElementTree(et.fromstring(req.text)).getroot().iter():
                array.append(_.text)
            mp3 = base64.b64decode(array[6])
            # print(mp3)
            mp3file = open(self.mp3file, "wb")
            mp3file.write(mp3)
            mp3file.close()
            return array[4] # mp3
        except:
            return "错误，请重试"


if __name__ == '__main__':
    a = TranslateHelper("kw")
    print(a.webxml())
