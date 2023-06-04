from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Tutorial(object):
    def setupUi(self, Tutorial):
        Tutorial.setObjectName("Tutorial")
        Tutorial.resize(800, 600)
        Tutorial.setStyleSheet("background-color: rgb(50, 168, 82)")
        self.centralwidget = QtWidgets.QWidget(Tutorial)
        self.centralwidget.setObjectName("centralwidget")
        self.explanation_box = QtWidgets.QLabel(self.centralwidget)
        self.explanation_box.setGeometry(QtCore.QRect(40, 80, 741, 501))
        self.explanation_box.setStyleSheet("background-color: rgb(94, 189, 120);\n"
"font-family: Arial;\n"
"padding: 4px;\n"
"font-size: 17px;\n"
"")
        self.explanation_box.setObjectName("explanation_box")
        self.heading = QtWidgets.QLabel(self.centralwidget)
        self.heading.setGeometry(QtCore.QRect(230, 0, 351, 61))
        self.heading.setStyleSheet("color: white;\n"
"font-family: Monospace; \n"
"font-size: 70px;")
        self.heading.setObjectName("heading")
        Tutorial.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Tutorial)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        Tutorial.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Tutorial)
        self.statusbar.setObjectName("statusbar")
        Tutorial.setStatusBar(self.statusbar)

        self.retranslateUi(Tutorial)
        QtCore.QMetaObject.connectSlotsByName(Tutorial)

    def retranslateUi(self, Tutorial):
        _translate = QtCore.QCoreApplication.translate
        Tutorial.setWindowTitle(_translate("Tutorial", "Tutorial"))
        self.explanation_box.setText(_translate("Tutorial", "Solitaire is a card game that is known globally. It is loved by many and considered a classic game\n"
"throughout the world. It utilises a standard deck of 25 cards and is then divided and grouped \n"
"according to the foundational suits: hearts, diamonds, spades, and clubs. \n"
"This version of Solitaire is delivered in two modes: Easy and difficult. It is slightly different\n"
"and more enjoyable. \n"
"\n"
"Easy mode: \n"
"The objective of this game is to stack cards in a pile/column, where each car going from up to down\n"
"in the same number but from a different suit.  E.g, to win, the first column should be a stack of \n"
"“2 of hearts”, “2 of diamonds”, “2 of spades” and “2 of clubs”. Consequently, the same could be \n"
"said about the other piles. The first pile to be completed reaches the game objective and the \n"
"game is won. To win, a player must click the “deal cards” button at the top, which deals a card\n"
" that can be played. Be cautious though, as the number of cards to be dealt is limited!\n"
"If cards dealt reaches the end and the game objective hasn’t been met, it is game over.\n"
"The window title will display “Game Over!” at the top. \n"
"\n"
"Difficult mode:\n"
"Similar to easy mode, but a bit more advanced. This level asks you to complete ALL the cards and\n"
"place them in foundational piles, going from up to down, according to their number and suit. \n"
"However, this time, the dealing card is not limited, and players can deal with as many cards as\n"
"they want.  \n"
""))
        self.heading.setText(_translate("Tutorial", "TUTORIAL"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Tutorial = QtWidgets.QMainWindow()
    ui = Ui_Tutorial()
    ui.setupUi(Tutorial)
    Tutorial.show()
    sys.exit(app.exec_())
