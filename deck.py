from PyQt5.QtWidgets import QMainWindow, QApplication,QLabel,QTextEdit,QPushButton, QWidget, QLineEdit
from PyQt5 import QtCore, uic
from PyQt5.QtGui import QPixmap
import sys
import random

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        #load the ui file
        uic.loadUi("deck.ui", self)
        self.setWindowTitle("Cards")

        #define Widgets
        self.dealer_label = self.findChild(QLabel,"dealerLabel")
        self.player_label = self.findChild(QLabel,"playerLabel")
        self.dealer_head_label = self.findChild(QLabel,"dealerHeaderLabel")
        self.player_head_label = self.findChild(QLabel,"playerHeaderLabel")
        self.shuffle_button = self.findChild(QPushButton,"spushButton")
        self.deal_button = self.findChild(QPushButton,"dpushButton")

        #shuffle cards
        self.shuffle()

        #action to be taken when button is clicked
        self.shuffle_button.clicked.connect(self.shuffle)
        self.deal_button.clicked.connect(self.deal_cards)

        #show the app
        self.show()

    def shuffle(self):
        #define our deck
        suits = ["diamonds", "clubs", "hearts", "spades"]
        # 11 = J 12=Queen 13 = K ,14=Ace
        values = range (2,15)

        #Create Deck
        #global deck
        self.deck = []

        for suit in suits:
            for value in values:
                self.deck.append(f'{value}_of_{suit}')

        #Create our player
        #global dealer, player
        self.dealer = []
        self.player = []

        #Grab a random card for dealer
        card = random.choice(self.deck)
        #remove that card from deck
        self.deck.remove(card)
        #Add that card to dealer list
        self.dealer.append(card)
        #Output card to screen
        pixmap = QPixmap(f'D:\PyQt5 Project\cards\{card}.png')
        self.dealer_label.setPixmap(pixmap)

        #Grab a random card for player
        card = random.choice(self.deck)
        #remove that card from deck
        self.deck.remove(card)
        #Add that card to dealer list
        self.player.append(card)
        #Output card to screen
        pixmap = QPixmap(f'D:\PyQt5 Project\cards\{card}.png')
        self.player_label.setPixmap(pixmap)
        #update titlebar
        self.setWindowTitle(f'{len(self.deck)} Cards left in Deck')

    def deal_cards(self):
        try:
            #Grab a random card for dealer
            card = random.choice(self.deck)
            #remove that card from deck
            self.deck.remove(card)
            #Add that card to dealer list
            self.dealer.append(card)
            #Output card to screen
            pixmap = QPixmap(f'D:\PyQt5 Project\cards\{card}.png')
            self.dealer_label.setPixmap(pixmap)

            #Grab a random card for player
            card = random.choice(self.deck)
            #remove that card from deck
            self.deck.remove(card)
            #Add that card to dealer list
            self.player.append(card)
            #Output card to screen
            pixmap = QPixmap(f'D:\PyQt5 Project\cards\{card}.png')
            self.player_label.setPixmap(pixmap)
            #update titlebar
            self.setWindowTitle(f'{len(self.deck)} Cards left in Deck')
        
        except:
            self.setWindowTitle("Game Over!!")

#Initalize the app 
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()