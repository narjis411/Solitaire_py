from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton
import sys
import random

class diffmode(QMainWindow):
    def __init__(self):
        super(diffmode, self).__init__()
        uic.loadUi("DifficultMode.ui", self)

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


        global firstly, secondly, thirdly, forthly, fifthly, sixthly, seventhly, eightthly, dealt
        firstly = []
        secondly = []
        thirdly = []
        forthly = []
        fifthly = []
        sixthly = []
        eightthly = []
        seventhly = []

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

        #fifth file set card
        card = random.choice(deck)
        deck.remove(card)
        fifthly.append(card)

        pixmap = QPixmap(f'cards/{card}.png')
        self.fifthlabel.setPixmap(pixmap)
        
        #sixth file set card
        card = random.choice(deck)
        deck.remove(card)
        sixthly.append(card)

        pixmap = QPixmap(f'cards/{card}.png')
        self.sixthlabel.setPixmap(pixmap)
        
        #seventh file set card
        card = random.choice(deck)
        deck.remove(card)
        seventhly.append(card)

        pixmap = QPixmap(f'cards/{card}.png')
        self.seventhlabel.setPixmap(pixmap)
        
        #eighth file set card
        card = random.choice(deck)
        deck.remove(card)
        eightthly.append(card)

        pixmap = QPixmap(f'cards/{card}.png')
        self.eightthlabel.setPixmap(pixmap)
        
     
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


        
    def setupUi(self, DifficultMode):
        DifficultMode.setObjectName("DifficultMode")
        DifficultMode.resize(800, 600)
        DifficultMode.setStyleSheet("background-color: rgb(50, 168, 82)")
        self.centralwidget = QtWidgets.QWidget(DifficultMode)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 111, 31))
        self.label.setStyleSheet("background-color: rgb(94, 189, 120);\n"
"font-family: Arial;\n"
"padding: 4px;\n"
"color: white;")
        self.label.setObjectName("label")
        DifficultMode.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(DifficultMode)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        DifficultMode.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(DifficultMode)
        self.statusbar.setObjectName("statusbar")
        DifficultMode.setStatusBar(self.statusbar)

        self.retranslateUi(DifficultMode)
        QtCore.QMetaObject.connectSlotsByName(DifficultMode)

    def retranslateUi(self, DifficultMode):
        _translate = QtCore.QCoreApplication.translate
        DifficultMode.setWindowTitle(_translate("DifficultMode", "DifficultMode"))
        self.label.setText(_translate("DifficultMode", "Player Name"))

app = QApplication(sys.argv)
UIWindow = diffmode()
app.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DifficultMode = QtWidgets.QMainWindow()
    ui = diffmode()
    ui.setupUi(DifficultMode)
    DifficultMode.show()
    sys.exit(app.exec_())
