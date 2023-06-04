from PyQt5 import QtCore, QtGui, QtWidgets
from tutorial import Ui_Tutorial
from EasyMode import easymode
from DifficultMode import diffmode

class Ui_solitaire(object):
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Tutorial()
        self.ui.setupUi(self.window)
        self.window.show()

    def openeasymode(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = easymode()
        self.ui.setupUi(self.window)
        self.window.show()

    def opendiffmode(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = diffmode()
        self.ui.setupUi(self.window)
        self.window.show()


    def clicker(self):
        txt = self.enter_name_field.text()
        self.ui.label.setText(txt)

    
    def setupUi(self, solitaire):
        solitaire.setObjectName("solitaire")
        solitaire.resize(808, 606)
        solitaire.setAutoFillBackground(False)
        solitaire.setStyleSheet("background-color: rgb(50, 168, 82)\n""")
        self.centralwidget = QtWidgets.QWidget(solitaire)
        self.centralwidget.setObjectName("centralwidget")
        self.enter_name_field = QtWidgets.QLineEdit(self.centralwidget)
        self.enter_name_field.setGeometry(QtCore.QRect(200, 190, 261, 91))
        self.enter_name_field.setStyleSheet("color : white;\n"
"background-color: rgb(54, 153, 81);\n"
"padding: 20px;\n"
"border-style: none;\n"
"border-radius: 25px;\n"
"hover background-color: rgb(52, 140, 76);\n"
"\n"
"")
        self.enter_name_field.setObjectName("enter_name_field")
        self.easy_mode_btn = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.openeasymode())
        self.easy_mode_btn.setGeometry(QtCore.QRect(320, 310, 171, 71))
        self.easy_mode_btn.setStyleSheet("color : white;\n"
"background-color: rgb(54, 153, 81);\n"
"padding: 20px;\n"
"text-align: center;\n"
"border-style: none;\n"
"border-radius: 25px;\n"
"hover background-color: rgb(52, 140, 76);")
        self.easy_mode_btn.setObjectName("easy_mode_btn")
        self.hard_mode_btn = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.opendiffmode())
        self.hard_mode_btn.setGeometry(QtCore.QRect(320, 400, 171, 71))
        self.hard_mode_btn.setStyleSheet("color : white;\n"
"background-color: rgb(54, 153, 81);\n"
"padding: 20px;\n"
"text-align: center;\n"
"border-style: none;\n"
"border-radius: 25px;\n"
"hover background-color: rgb(52, 140, 76);")
        self.hard_mode_btn.setObjectName("hard_mode_btn")
        self.tutorial_btn = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.openWindow())
        self.tutorial_btn.setGeometry(QtCore.QRect(320, 490, 171, 61))
        self.tutorial_btn.setStyleSheet("color : white;\n"
"background-color: rgb(54, 153, 81);\n"
"padding: 20px;\n"
"text-align: center;\n"
"border-style: none;\n"
"border-radius: 25px;\n"
"hover background-color: rgb(52, 140, 76);")
        self.tutorial_btn.setObjectName("tutorial_btn")
        self.logo_txt = QtWidgets.QLabel(self.centralwidget)
        self.logo_txt.setGeometry(QtCore.QRect(190, 50, 471, 91))
        self.logo_txt.setStyleSheet("color: white;\n"
"font-family: Monospace; \n"
"font-size: 70px;")
        self.logo_txt.setObjectName("logo_txt")
        self.submit = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.clicker())
        self.submit.setGeometry(QtCore.QRect(470, 190, 121, 91))
        self.submit.setStyleSheet("color : white;\n"
"background-color: rgb(54, 153, 81);\n"
"padding: 20px;\n"
"text-align: center;\n"
"border-style: none;\n"
"border-radius: 25px;\n"
"hover background-color: rgb(52, 140, 76);")
        self.submit.setObjectName("submit")
        solitaire.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(solitaire)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 808, 21))
        self.menubar.setObjectName("menubar")
        solitaire.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(solitaire)
        self.statusbar.setObjectName("statusbar")
        solitaire.setStatusBar(self.statusbar)

        self.retranslateUi(solitaire)
        QtCore.QMetaObject.connectSlotsByName(solitaire)

    def retranslateUi(self, solitaire):
        _translate = QtCore.QCoreApplication.translate
        solitaire.setWindowTitle(_translate("solitaire", "Solitaire"))
        self.enter_name_field.setText(_translate("solitaire", "Enter Player Name here! "))
        self.easy_mode_btn.setText(_translate("solitaire", "Play Easy Mode"))
        self.hard_mode_btn.setText(_translate("solitaire", "Play Difficult Mode"))
        self.tutorial_btn.setText(_translate("solitaire", "See Tutorial"))
        self.logo_txt.setText(_translate("solitaire", "SOLITAIRE ♧"))
        self.submit.setText(_translate("solitaire", "SUBMIT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    solitaire = QtWidgets.QMainWindow()
    ui = Ui_solitaire()
    ui.setupUi(solitaire)
    solitaire.show()
    sys.exit(app.exec_())
