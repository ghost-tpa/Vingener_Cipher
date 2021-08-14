import sys
from pyperclip import copy
from PyQt5.QtWidgets import *
import funcVigener
import random


"""
13.08.2021 - done 
Đã hoàn thành chức năng pentest code chạy 
"""



class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.initUI()
        self.setMinimumWidth(700)
        self.setMinimumHeight(900)

    def initUI(self):  # phần này làm việc với widget
        self.setWindowTitle("Chương trình mã hóa Vigener")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.labeltemp = QLabel("CHƯƠNG TRÌNH MÃ HÓA VIGENER CƠ BẢN")
        self.layout.addWidget(self.labeltemp)
        self.lineeditinput = QLineEdit()
        self.lineeditinput.setPlaceholderText("Nhập văn bản vào đây")
        self.lineeditinput.returnPressed.connect(self.setinput)
        self.layout.addWidget(self.lineeditinput)
        self.lineeditkey = QLineEdit()
        self.lineeditkey.setPlaceholderText("Nhập key vào đây")
        self.layout.addWidget(self.lineeditkey)
        self.enpbutton = QPushButton("Mã hóa")
        self.enpbutton.clicked.connect(self.encryptfunc)
        self.layout.addWidget(self.enpbutton)
        self.depbutton = QPushButton("Giải mã")
        self.depbutton.clicked.connect(self.decryptfunc)
        self.layout.addWidget(self.depbutton)
        self.lineeditresult = QLineEdit()
        self.lineeditresult.setPlaceholderText("Chỗ này chứa kết quả: (readonly)")
        self.lineeditresult.setReadOnly(True)
        self.layout.addWidget(self.lineeditresult)
        self.lboutput = QLabel()
        self.layout.addWidget(self.lboutput)
        self.resetbutton = QPushButton("Reset")
        self.resetbutton.clicked.connect(self.resetfuc)
        self.layout.addWidget(self.resetbutton)
        self.testcodebutton = QPushButton("Test Code")
        self.testcodebutton.clicked.connect(self.func_test_code)
        self.layout.addWidget(self.testcodebutton)
        exitbutton = QPushButton("Exit")
        exitbutton.clicked.connect(self.exitfun)
        self.layout.addWidget(exitbutton)


    def exitfun(self):
        exit(0)

    def setinput(self):
        return self.lineeditinput.text()
    def encryptfunc(self):
        message = self.lineeditinput.text()
        key = self.lineeditkey.text()
        encryptext = funcVigener.translateMessage(key, message, "encrypt")
        copy(encryptext)
        self.lineeditresult.setText(encryptext)
        self.lboutput.setText("Bản mã đã được coppy vào clipboard")

    def decryptfunc(self):
        message = self.lineeditinput.text()
        key = self.lineeditkey.text()
        plainttext = funcVigener.translateMessage(key, message, "decrypt")
        copy(plainttext)
        self.lineeditresult.setText(plainttext)
        self.lboutput.setText("Bản mã đã được coppy vào clipboard")

    def resetfuc(self):
        self.lineeditinput.setText("")
        self.lineeditkey.setText("")
        self.lineeditresult.setText("")

    def func_test_code(self):
        random.seed()
        for i in range(20):
            message = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" * random.randint(4, 40)
            message = list(message)
            random.shuffle(message)
            message = "".join(message)
            label = QLabel("Test #%s: %s..." % (i+1, message[:50]))
            self.layout.addWidget(label)
            for i in range(50):
                key = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" * random.randint(2, 4)
                key = list(key)
                random.shuffle(key)
                key = "".join(key)
                encrypted = funcVigener.translateMessage(key, message, "encrypt")
                decrypted = funcVigener.translateMessage(key, encrypted, "decrypt")

                if message != decrypted:
                    label = QLabel("Mismath with key %s and message %s" % (key, message))
                    self.layout.addWidget(label)
                    label = QLabel("Decrypted as : " + decrypted)
                    self.layout.addWidget(label)
        label = QLabel("Test passed ")
        self.layout.addWidget(label)


def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    exit(app.exec_())

if __name__ == '__main__':
    main()
