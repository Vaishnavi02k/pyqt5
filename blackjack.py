from PyQt5.QtWidgets import QMainWindow, QApplication,QLabel,QPushButton,QMessageBox
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
import sys
import random

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        #load the ui file
        uic.loadUi("blackjack.ui", self)
        self.setWindowTitle("BlackJack!")

        #define Widgets
        self.dealer_card1 = self.findChild(QLabel,"dealerCard1")
        self.dealer_card2 = self.findChild(QLabel,"dealerCard2")
        self.dealer_card3 = self.findChild(QLabel,"dealerCard3")
        self.dealer_card4 = self.findChild(QLabel,"dealerCard4")
        self.dealer_card5 = self.findChild(QLabel,"dealerCard5")

        self.player_card1 = self.findChild(QLabel,"playerCard1")
        self.player_card2 = self.findChild(QLabel,"playerCard2")
        self.player_card3 = self.findChild(QLabel,"playerCard3")
        self.player_card4 = self.findChild(QLabel,"playerCard4")
        self.player_card5 = self.findChild(QLabel,"playerCard5")

        self.dealer_head_label = self.findChild(QLabel,"dealerHeaderLabel")
        self.player_head_label = self.findChild(QLabel,"playerHeaderLabel")
        
        self.shuffle_button = self.findChild(QPushButton,"spushButton")
        self.hit_me_button = self.findChild(QPushButton,"hitMeButton")
        self.stand_button = self.findChild(QPushButton,"standButton")

        #shuffle cards
        self.shuffle()

        #action to be taken when button is clicked
        self.shuffle_button.clicked.connect(self.shuffle)
        self.hit_me_button.clicked.connect(self.player_hit)
        self.stand_button.clicked.connect(self.stand)

        #show the app
        self.show()

    #stand
    def stand(self):
        #Disable buttons
        self.hit_me_button.setEnabled(False)
        self.stand_button.setEnabled(False)

        #just to make sure its a current score
        self.player_total = 0
        self.dealer_total = 0
        #get the player score
        for score in self.player_score:
            self.player_total += score
        #get the dealer score
        for score in self.dealer_score:
            self.dealer_total += score

        #logic: if dealer has point greater than 17 they have to stand, if its below 17 they have to get another card
        if self.dealer_total >= 17:
            #check for bust 
            if self.dealer_total >21:
                #Winner Message
                QMessageBox.about(self,"Player Wins!", f"Player Wins! Dealer:{self.dealer_total} || Player:{self.player_total}")
            elif self.dealer_total == self.player_total:
                #tie Message
                QMessageBox.about(self,"Tie!", f"Its a Tie! Dealer:{self.dealer_total} || Player:{self.player_total}")
            elif self.dealer_total > self.player_total :
                #Winner Message
                QMessageBox.about(self,"Dealer Wins!", f"Dealer Wins! Dealer:{self.dealer_total} || Player:{self.player_total}")
            else:
                #player wins (Winner Message)
                QMessageBox.about(self,"Player Wins!", f"Player Wins! Dealer:{self.dealer_total} || Player:{self.player_total}")
               
        else:
            #dealer needs another card
            self.dealer_hit()
            self.stand()
    
    #check for blackjack
    def blackjack_check(self,player):
        #keep track of score totals
        self.player_total = 0
        self.dealer_total = 0

        if player == "dealer":
            if len(self.dealer_score) == 2:
                if self.dealer_score[0]+self.dealer_score[1] == 21:
                    #Change black jack status to yes for dealer
                    self.blackjack_status["dealer"] = "yes"

        if player == "player":
            if len(self.player_score) == 2:
                if self.player_score[0]+self.player_score[1] == 21:
                    #Change black jack status to yes for dealer
                    self.blackjack_status["player"] = "yes"
            else:
                #loop through players list and add up cards
                for score in self.player_score:
                    #add up the score
                    self.player_total+=score
                #check for win or lose
                if self.player_total == 21:
                    self.blackjack_status["player"]="yes"
                elif self.player_total > 21:
                    #check for ace conversion
                    for card_num, card in enumerate(self.player_score):
                        if card == 11:
                            #change 11 to 1
                            self.player_score[card_num] = 1

                            #update totals
                            self.player_total =0
                            for score in self.player_score:
                                self.player_total+= score
                            #check for bust
                            if self.player_total > 21:
                                self.blackjack_status["player"]= "bust"
                    else:
                        #check for win or bust
                        if self.player_total == 21:
                            self.blackjack_status["player"]= "yes"
                        if self.player_total > 21:
                            self.blackjack_status["player"]= "bust"
                    

        #check for blackjack
        if len(self.player_score)==2 and len(self.dealer_score)==2:
            #check for tie and we are making sure there are only two cards in both section
            if self.blackjack_status["dealer"] =="yes" and self.blackjack_status["player"] == "yes":
                #Winner Message
                QMessageBox.about(self,"Push!", "Its a Tie!! Start Over!")
                #Disable buttons
                self.hit_me_button.setEnabled(False)
                self.stand_button.setEnabled(False)

            #check for dealer wins
            elif self.blackjack_status["dealer"] == "yes":
                #Winner Message
                QMessageBox.about(self,"Dealer Wins!", "Blackjack! Dealer wins!")
                #Disable buttons
                self.hit_me_button.setEnabled(False)
                self.stand_button.setEnabled(False)

            #check for player wins
            elif self.blackjack_status["player"] == "yes":
                #Winner Message
                QMessageBox.about(self,"player Wins!", "Blackjack! player wins!")
                #Disable buttons
                self.hit_me_button.setEnabled(False)
                self.stand_button.setEnabled(False)
        else:
            if self.blackjack_status["dealer"] =="yes" and self.blackjack_status["player"] == "yes":
                #Winner Message
                QMessageBox.about(self,"Push!", "Its a Tie!!")
                #Disable buttons
                self.hit_me_button.setEnabled(False)
                self.stand_button.setEnabled(False)

            #check for dealer wins
            elif self.blackjack_status["dealer"] == "yes":
                #Winner Message
                QMessageBox.about(self,"Dealer Wins!", "21! Dealer wins!")
                #Disable buttons
                self.hit_me_button.setEnabled(False)
                self.stand_button.setEnabled(False)

            #check for player wins
            elif self.blackjack_status["player"] == "yes":
                #Winner Message
                QMessageBox.about(self,"player Wins!", "21! player wins!")
                #Disable buttons
                self.hit_me_button.setEnabled(False)
                self.stand_button.setEnabled(False)
        
        #check for player bust
        if self.blackjack_status["player"] == "bust":
            #Bust Message
            QMessageBox.about(self,"Bust!", f"Player loses:{self.player_total}")
            #Disable buttons
            self.hit_me_button.setEnabled(False)
            self.stand_button.setEnabled(False)


    def shuffle(self):
        #keep track of score totals
        self.player_total = 0
        self.dealer_total = 0

        #create a dictionary to keep track of blackjack status
        self.blackjack_status = {"dealer":"no", "player":"no"}
        #Enable Buttons
        self.hit_me_button.setEnabled(True)
        self.stand_button.setEnabled(True)

        # Reset Card Images
        pixmap = QPixmap("D:\PyQt5 Project\cards\green.jpg")
        self.dealer_card1.setPixmap(pixmap)
        self.dealer_card2.setPixmap(pixmap)
        self.dealer_card3.setPixmap(pixmap)
        self.dealer_card4.setPixmap(pixmap)
        self.dealer_card5.setPixmap(pixmap)

        self.player_card1.setPixmap(pixmap)
        self.player_card2.setPixmap(pixmap)
        self.player_card3.setPixmap(pixmap)
        self.player_card4.setPixmap(pixmap)
        self.player_card5.setPixmap(pixmap)

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
        #keeping track of positions
        self.players_position = 0
        self.dealers_position = 0
        #keeping track of score 
        #all face cards have value 10 and ace can be 1 or 11 based on your choice
        self.dealer_score = []
        self.player_score = []

        self.dealer_hit()
        self.dealer_hit()

        self.player_hit()
        self.player_hit()

    def deal_cards(self):
        try:
            #Grab a random card for dealer
            card  = random.choice(self.deck)
            #remove that card from deck
            self.deck.remove(card )
            #Add that card to dealer list
            self.dealer.append(card)
            #Output card to screen
            pixmap = QPixmap(f'D:\PyQt5 Project\cards\{card }.png')
            self.dealer_card1.setPixmap(pixmap)

            #Grab a random card for player
            card = random.choice(self.deck)
            #remove that card from deck
            self.deck.remove(card)
            #Add that card to dealer list
            self.player.append(card)
            #Output card to screen
            pixmap = QPixmap(f'D:\PyQt5 Project\cards\{card}.png')
            self.player_card1.setPixmap(pixmap)
            #update titlebar
            self.setWindowTitle(f'{len(self.deck)} Cards left in Deck')    
        
        except:
            self.setWindowTitle("Game Over deaaler card!!")
    
    def dealer_hit(self):
        if self.dealers_position <= 5 :
            try:
                #Grab a random card for dealer
                card  = random.choice(self.deck)
                #remove that card from deck
                self.deck.remove(card )
                #Add that card to dealer list
                self.dealer.append(card )
                
                # add cards to dealer score
                #11_of_heart is saved as 10 same for all face cards
                #and 8_of_spade is saved as 8 and all the less or equal to 10
                self.dcard = int(card.split("_",1)[0])
                if self.dcard == 14:
                    self.dealer_score.append(11)
                elif self.dcard == 11 or self.dcard == 12 or self.dcard == 13:
                    self.dealer_score.append(10)
                else:
                    self.dealer_score.append(self.dcard)
                #now dealer score will look like this : dealer_score = [10,7,3]  its a list

                #Output card to screen
                pixmap = QPixmap(f'D:\PyQt5 Project\cards\{card }.png')
                if self.dealers_position == 0:
                    self.dealer_card1.setPixmap(pixmap)
                    self.dealers_position+=1
                elif self.dealers_position == 1:
                    self.dealer_card2.setPixmap(pixmap)
                    self.dealers_position+=1
                elif self.dealers_position == 2:
                    self.dealer_card3.setPixmap(pixmap)
                    self.dealers_position+=1
                elif self.dealers_position == 3:
                    self.dealer_card4.setPixmap(pixmap)
                    self.dealers_position+=1
                elif self.dealers_position == 4:
                    self.dealer_card5.setPixmap(pixmap)
                    self.dealers_position+=1

                    #check for bust
                    #just to make sure its a current score
                    self.player_total = 0
                    self.dealer_total = 0
                    #get the player score
                    for score in self.player_score:
                        self.player_total += score
                    #get the dealer score
                    for score in self.dealer_score:
                        self.dealer_total += score
                    #check to see player score is less than equal to 21
                    if self.dealer_total <= 21:
                        #Win!
                        #Disable buttons
                        self.hit_me_button.setEnabled(False)
                        self.stand_button.setEnabled(False)
                        #flash win messagw
                        QMessageBox.about(self,"dealer Wins!",f"Dealer Wins! Player:{self.player_total} Dealer{self.player_total}")
                #update titlebar
                self.setWindowTitle(f'{len(self.deck)} Cards left in Deck')
            
            except:
                    self.setWindowTitle("Game Over dealer hit!!")
            
            #check for blackjack
            self.blackjack_check("dealer")

    def player_hit(self):
        if self.players_position <= 5 :
            try:
                #Grab a random card for player
                card = random.choice(self.deck)
                #remove that card from deck
                self.deck.remove(card)
                #Add that card to dealer list
                self.player.append(card)

                # add cards to player score
                #11_of_heart is saved as 10 same for all face cards
                #and 8_of_spade is saved as 8 and all the less or equal to 10
                self.pcard = int(card.split("_",1)[0])
                if self.pcard == 14:
                    self.player_score.append(11)
                elif self.pcard == 11 or self.pcard == 12 or self.pcard == 13:
                    self.player_score.append(10)
                else:
                    self.player_score.append(self.pcard)
                #now player score will look like this : player_score = [2,8,7]  its a list

                #Output card to screen
                pixmap = QPixmap(f'D:\PyQt5 Project\cards\{card}.png')    
                if self.players_position == 0:
                    self.player_card1.setPixmap(pixmap)
                    self.players_position += 1
                elif self.players_position == 1:
                    self.player_card2.setPixmap(pixmap)
                    self.players_position+=1
                elif self.players_position == 2:
                    self.player_card3.setPixmap(pixmap)
                    self.players_position+=1
                elif self.players_position == 3:
                    self.player_card4.setPixmap(pixmap)
                    self.players_position+=1
                elif self.players_position == 4:
                    self.player_card5.setPixmap(pixmap)
                    self.players_position+=1

                    #check for bust
                    #just to make sure its a current score
                    self.player_total = 0
                    self.dealer_total = 0
                    #get the player score
                    for score in self.player_score:
                        self.player_total += score
                    #get the dealer score
                    for score in self.dealer_score:
                        self.dealer_total += score
                    #check to see player score is less than equal to 21
                    if self.player_total <= 21:
                        #Win!
                        #Disable buttons
                        self.hit_me_button.setEnabled(False)
                        self.stand_button.setEnabled(False)
                        #flash win messagw
                        QMessageBox.about(self,"Player Wins!",f"player Wins! Player:{self.player_total} Dealer{self.player_total}")

                #update titlebar
                self.setWindowTitle(f'{len(self.deck)} Cards left in Deck')
            
            except:
                    self.setWindowTitle("Game Over player hit!!")
            
            #check for blackjack
            self.blackjack_check("player")


#Initalize the app 
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()