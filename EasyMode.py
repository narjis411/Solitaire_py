from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton
import sys
import random

class easymode(QMainWindow):
    def __init__(self):
        super(easymode, self).__init__()
        uic.loadUi("EasyMode.ui", self)

        self.firstlabel = self.findChild(QLabel, "hearts2label")
        self.secondlabel = self.findChild(QLabel, "diamonds2label")
        self.thirdlabel = self.findChild(QLabel, "clubs2label")
        self.fourthlabel = self.findChild(QLabel, "spades2label")
        self.fifthlabel = self.findChild(QLabel, "heart3label")
        self.sixthlabel = self.findChild(QLabel, "diamonds3label")
        self.seventhlabel = self.findChild(QLabel, "clubs3label")
        self.eightthlabel = self.findChild(QLabel, "spades3label")
        self.ninthlabel = self.findChild(QLabel, "hearts4label")
        self.tenthlabel = self.findChild(QLabel, "diamonds4label")
        self.eleventhlabel = self.findChild(QLabel, "clubs4label")
        self.twelvethlabel = self.findChild(QLabel, "spades4label")
        self.thirteenthlabel = self.findChild(QLabel, "hearts5label")
        self.fourteenthlabel = self.findChild(QLabel, "diamonds5label")
        self.fifteenthlabel = self.findChild(QLabel, "clubs5label")
        self.sixteenthlabel = self.findChild(QLabel, "spades5label")
        self.dealtcardlabel = self.findChild(QLabel, "dealtcardlabel")
        self.StartButton = self.findChild(QPushButton, "StartButton")
        self.DealButton = self.findChild(QPushButton, "DealButton")

#shuffle cards before we open window
        self.shuffle()

#click buttons to start and deal
        self.StartButton.clicked.connect(self.shuffle)
        self.DealButton.clicked.connect(self.deal)
        self.show()


    def shuffle(self):
        suits = ["diamonds", "clubs", "hearts", "spades"]
        values = range(2, 11)

        global deck

        deck = []

        for suit in suits:
            for value in values:
                deck.append(f"{value}_of_{suit}")


        global firstly, secondly, thirdly, forthly, dealt
        firstly = []
        secondly = []
        thirdly = []
        forthly = []
        dealt = []

        #first file set card
        card = random.choice(deck)
        deck.remove(card)
        firstly.append(card)

        pixmap = QPixmap(f'cards/{card}.png')
        self.firstlabel.setPixmap(pixmap)
        
       
        #second pile set card
        card = random.choice(deck)
        deck.remove(card)
        secondly.append(card)

        pixmap = QPixmap(f'cards/{card}.png')
        self.secondlabel.setPixmap(pixmap)

        #third pile set card
        card = random.choice(deck)
        deck.remove(card)
        thirdly.append(card)

        pixmap = QPixmap(f'cards/{card}.png')
        self.thirdlabel.setPixmap(pixmap)

        #fourth pile set card
        card = random.choice(deck)
        deck.remove(card)
        forthly.append(card)

        pixmap = QPixmap(f'cards/{card}.png')
        self.fourthlabel.setPixmap(pixmap)


    def deal(self):
        try:
            card = random.choice(deck)
            deck.remove(card)
            dealt.append(card)
            pixmap = QPixmap(f'cards/{card}.png')
            self.dealtcardlabel.setPixmap(pixmap)


        except:
            
            self.setWindowTitle("game is Over!")

    #decide end of game
    def win(self):
        if self.firstlabel == "2_of_hearts.png" and self.fifthlabel == "2_of_diamonds.png" and self.ninthlabel == "2_of_clubs.png" and self.thirteenthlabel == "2_of_spades.png":
            self.gamestate.setTex("You won!")

        elif self.secondlabel == "3_of_hearts.png" and self.sixthlabel == "3_of_diamonds.png" and self.tenthlabel == "3_of_clubs.png" and self.fourteenthlabel == "3_of_spades.png":
            self.gamestate.setTex("You won!")
            
        elif self.thirdlabel == "4_of_hearts.png" and self.seventhlabel == "4_of_diamonds.png" and self.eleventhlabel == "4_of_clubs.png" and self.fifteenthlabel == "4_of_spades.png":
            self.gamestate.setTex("You won!")

        elif self.fourthlabel == "5_of_hearts.png" and self.eightthlabel == "5_of_diamonds.png" and self.twelvethlabel == "5_of_clubs.png" and self.sixteenthlabel == "5_of_spades.png":
            self.gamestate.setTex("You won!")

        else: 

            self.gamestate.setTex("Game Ongoing...")


        



    def setupUi(self, EasyMode):
        EasyMode.setObjectName("EasyMode")
        EasyMode.resize(832, 933)
        EasyMode.setStyleSheet("background-color: rgb(50, 168, 82)")
        self.centralwidget = QtWidgets.QWidget(EasyMode)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(340, 10, 91, 21))
        self.label.setStyleSheet("background-color: rgb(94, 189, 120);\n"
"font-family: Arial;\n"
"padding: 4px;\n"
"color: white;")
        self.label.setObjectName("label")
        self.re_start = QtWidgets.QPushButton(self.centralwidget)
        self.re_start.setGeometry(QtCore.QRect(140, 10, 111, 21))
        self.re_start.setStyleSheet("background-color: rgb(94, 189, 120);\n"
"font-family: Arial;\n"
"padding: 4px;\n"
"color: white;")
        self.re_start.setObjectName("re_start")
        self.deal = QtWidgets.QPushButton(self.centralwidget)
        self.deal.setGeometry(QtCore.QRect(520, 10, 111, 21))
        self.deal.setStyleSheet("background-color: rgb(94, 189, 120);\n"
"font-family: Arial;\n"
"padding: 4px;\n"
"color: white;")
        self.deal.setObjectName("deal")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 70, 101, 141))
        self.label_2.setStyleSheet("background-color: rgb(20, 159, 36);")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("cards/2_of_clubs.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(250, 70, 101, 141))
        self.label_18.setStyleSheet("background-color: rgb(20, 159, 36);")
        self.label_18.setText("")
        self.label_18.setPixmap(QtGui.QPixmap("cards/2_of_diamonds.png"))
        self.label_18.setScaledContents(True)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(430, 70, 101, 141))
        self.label_19.setStyleSheet("background-color: rgb(20, 159, 36);")
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(600, 70, 101, 141))
        self.label_20.setStyleSheet("background-color: rgb(20, 159, 36);")
        self.label_20.setObjectName("label_20")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 230, 101, 141))
        self.label_3.setStyleSheet("background-color: rgb(20, 159, 36);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(250, 230, 101, 141))
        self.label_4.setStyleSheet("background-color: rgb(20, 159, 36);")
        self.label_4.setObjectName("label_4")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(430, 230, 101, 141))
        self.label_21.setStyleSheet("background-color: rgb(20, 159, 36);")
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(600, 230, 101, 141))
        self.label_22.setStyleSheet("background-color: rgb(20, 159, 36);")
        self.label_22.setObjectName("label_22")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(60, 390, 101, 141))
        self.label_5.setStyleSheet("background-color: rgb(20, 159, 36);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(250, 390, 101, 141))
        self.label_6.setStyleSheet("background-color: rgb(20, 159, 36);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(430, 390, 101, 141))
        self.label_7.setStyleSheet("background-color: rgb(20, 159, 36);")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(600, 390, 101, 141))
        self.label_8.setStyleSheet("background-color: rgb(20, 159, 36);")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(60, 560, 101, 141))
        self.label_9.setStyleSheet("background-color: rgb(20, 159, 36);")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(250, 550, 101, 141))
        self.label_10.setStyleSheet("background-color: rgb(20, 159, 36);")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(430, 550, 101, 141))
        self.label_11.setStyleSheet("background-color: rgb(20, 159, 36);")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(600, 550, 101, 141))
        self.label_12.setStyleSheet("background-color: rgb(20, 159, 36);")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(350, 740, 101, 141))
        self.label_13.setStyleSheet("background-color: rgb(20, 159, 36);")
        self.label_13.setObjectName("label_13")
        EasyMode.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(EasyMode)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 832, 21))
        self.menubar.setObjectName("menubar")
        EasyMode.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(EasyMode)
        self.statusbar.setObjectName("statusbar")
        EasyMode.setStatusBar(self.statusbar)

        self.retranslateUi(EasyMode)
        QtCore.QMetaObject.connectSlotsByName(EasyMode)

    def retranslateUi(self, EasyMode):
        _translate = QtCore.QCoreApplication.translate
        EasyMode.setWindowTitle(_translate("EasyMode", "EasyMode"))
        self.label.setText(_translate("EasyMode", "Player Name"))
        self.re_start.setText(_translate("EasyMode", "Start/Restart"))
        self.deal.setText(_translate("EasyMode", "Deal Cards"))
        self.label_19.setText(_translate("EasyMode", "TextLabel"))
        self.label_20.setText(_translate("EasyMode", "TextLabel"))
        self.label_3.setText(_translate("EasyMode", "TextLabel"))
        self.label_4.setText(_translate("EasyMode", "TextLabel"))
        self.label_21.setText(_translate("EasyMode", "TextLabel"))
        self.label_22.setText(_translate("EasyMode", "TextLabel"))
        self.label_5.setText(_translate("EasyMode", "TextLabel"))
        self.label_6.setText(_translate("EasyMode", "TextLabel"))
        self.label_7.setText(_translate("EasyMode", "TextLabel"))
        self.label_8.setText(_translate("EasyMode", "TextLabel"))
        self.label_9.setText(_translate("EasyMode", "TextLabel"))
        self.label_10.setText(_translate("EasyMode", "TextLabel"))
        self.label_11.setText(_translate("EasyMode", "TextLabel"))
        self.label_12.setText(_translate("EasyMode", "TextLabel"))
        self.label_13.setText(_translate("EasyMode", "TextLabel"))


app = QApplication(sys.argv)
UIWindow = easymode()
app.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EasyMode = QtWidgets.QMainWindow()
    ui = easymode()
    ui.setupUi(EasyMode)
    EasyMode.show()
    sys.exit(app.exec_())
