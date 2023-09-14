from PyQt5.QtWidgets import QMainWindow, QApplication,QLabel,QTextEdit,QPushButton, QWidget, QLineEdit
from PyQt5 import QtCore, uic
from PyQt5.QtGui import QPixmap
import sys
import random

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        #load the ui file
        uic.loadUi("war.ui", self)
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

        #keep tack of scores
        self.dealer_score = 0
        self.player_score = 0

        #Grab a random card for dealer
        self.dealer_card = random.choice(self.deck)
        #remove that card from deck
        self.deck.remove(self.dealer_card )
        #Add that card to dealer list
        self.dealer.append(self.dealer_card )
        #Output card to screen
        pixmap = QPixmap(f'D:\PyQt5 Project\cards\{self.dealer_card }.png')
        self.dealer_label.setPixmap(pixmap)

        #Grab a random card for player
        self.player_card = random.choice(self.deck)
        #remove that card from deck
        self.deck.remove(self.player_card)
        #Add that card to dealer list
        self.player.append(self.player_card)
        #Output card to screen
        pixmap = QPixmap(f'D:\PyQt5 Project\cards\{self.player_card}.png')
        self.player_label.setPixmap(pixmap)
        #update titlebar
        self.setWindowTitle(f'{len(self.deck)} Cards left in Deck')

        #Determin score
        self.score()

    def deal_cards(self):
        try:
            #Grab a random card for dealer
            self.dealer_card  = random.choice(self.deck)
            #remove that card from deck
            self.deck.remove(self.dealer_card )
            #Add that card to dealer list
            self.dealer.append(self.dealer_card )
            #Output card to screen
            pixmap = QPixmap(f'D:\PyQt5 Project\cards\{self.dealer_card }.png')
            self.dealer_label.setPixmap(pixmap)

            #Grab a random card for player
            self.player_card = random.choice(self.deck)
            #remove that card from deck
            self.deck.remove(self.player_card)
            #Add that card to dealer list
            self.player.append(self.player_card)
            #Output card to screen
            pixmap = QPixmap(f'D:\PyQt5 Project\cards\{self.player_card}.png')
            self.player_label.setPixmap(pixmap)
            #update titlebar
            self.setWindowTitle(f'{len(self.deck)} Cards left in Deck')

            #Determin score
            self.score()
        
        except:
            if self.dealer_score == self.player_score:
                self.setWindowTitle("Game Over!!  || TIE!|| {self.dealer_score} to {self.player_score} ")
            #Dealer Wins
            elif self.dealer_score > self.player_score:
                self.setWindowTitle(f"Game Over!!  || Dealer Wins! ||  {self.dealer_score} to {self.player_score} ")
            else:
                self.setWindowTitle(f"Game Over!!  || Player Wins! ||  {self.player_score} to {self.dealer_score} ")

    def score(self):
        #strip out cards number
        self.dealer_card = int(str(self.dealer_card).split("_", 1)[0])
        self.player_card = int(str(self.player_card).split("_", 1)[0])

        #compare the card number
        if self.dealer_card == self.player_card:
            self.dealer_head_label.setText("Tie!")
            self.player_head_label.setText("Tie!")
            #update titlebar
            self.setWindowTitle(f'{len(self.deck)} Cards left in Deck  ||  Dealer:{self.dealer_score} Player:{self.player_score} ')
        #dealer wins
        elif self.dealer_card > self.player_card:
            self.dealer_head_label.setText("Dealer Wins!")
            self.player_head_label.setText("Player Loses..")
            #update score
            self.dealer_score+=1
            #update titlebar
            self.setWindowTitle(f'{len(self.deck)} Cards left in Deck  ||  Dealer:{self.dealer_score} Player:{self.player_score} ')
        #Player wins
        else:
            self.dealer_head_label.setText("Dealer Loses..")
            self.player_head_label.setText("Player Wins!")
            #update score
            self.player_score+=1
            #update titlebar
            self.setWindowTitle(f'{len(self.deck)} Cards left in Deck  ||  Dealer:{self.dealer_score} Player:{self.player_score} ')

#Initalize the app 
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()