from random import shuffle
# from stack import *
import time

start = time.time()
class Player:
    def __init__(self, name):
        self.name = name
        self.pocket = 500
        self.on_hand = {
                        "card": [],
                        "point": 0,
                        "bound": 1
                    }
    def hand0ut(self):
        self.on_hand["card"] = []
        self.on_hand["point"] = 0
        self.on_hand["bound"] = 1
    
    def check_point(self):
        self.on_hand["point"] = 0
        self.on_hand["bound"] = 1

        for card in self.on_hand["card"]:
            if card[0] == "A":
                self.on_hand["point"] += 1
            elif card[0] == "J" or card[0] == "Q" or card[0] == "K" or card[1] == "0":
                self.on_hand["point"] += 0
            else:
                self.on_hand["point"] += int(card[0])

        if self.on_hand["point"] > 9:
            self.on_hand["point"] -= 10

    def check_bound(self):
        count_card = len(self.on_hand["card"][0].strip())-1 
        count_card1 = len(self.on_hand["card"][1].strip())-1

        if count_card == 2 and count_card1 == 2:
            sym = self.on_hand["card"][0][1]
            sym1 = self.on_hand["card"][1][1]
            if sym == sym1:
                self.on_hand["bound"] += 1

        elif count_card == 3 and count_card1 == 2:
            sym = self.on_hand["card"][0][2]
            sym1 = self.on_hand["card"][1][1]
            if sym == sym1:
                self.on_hand["bound"] += 1

        elif count_card == 2 and count_card1 ==3:
            sym = self.on_hand["card"][0][1]
            sym1 = self.on_hand["card"][1][2]
            if sym == sym1:
                self.on_hand["bound"] += 1

        elif count_card == 3 and count_card1 == 3:
            sym = self.on_hand["card"][0][2]
            sym1 = self.on_hand["card"][1][2]
            if sym == sym1:
                self.on_hand["bound"] += 1
    
    def you_wana_play(self, call):
        if call == "y":
            self.on_hand["card"].append(deck.draw())

class Dealer:
    def who_is_the_winner(self,player1, player2):
        if player1.on_hand["point"] > player2.on_hand["point"]:
            return "player1"
        elif player1.on_hand["point"] < player2.on_hand["point"]:
            return "player2"
        elif player1.on_hand["point"] == player2.on_hand["point"]:
            if player1.on_hand["bound"] > player2.on_hand["bound"]:
                return "player1"
            elif player1.on_hand["bound"] < player2.on_hand["bound"]:
                return "player2"
            else:
                return "draw"

    def i_will_take_your_monney(self, player1, player2):
        who_is_the_winner = self.who_is_the_winner(player1, player2)
        if who_is_the_winner == "player1":
            if player1.on_hand["bound"] > 1:
                player1.pocket += (100 * player1.on_hand["bound"])
                player2.pocket -= (100 * player1.on_hand["bound"])
                print("player1 win")
            else:
                player1.pocket += 100
                player2.pocket -= 100
        elif who_is_the_winner == "player2":
            if player2.on_hand["bound"] > 1:
                player2.pocket += (100 * player1.on_hand["bound"])
                player1.pocket -= (100 * player1.on_hand["bound"])
                print("player2 win")
            else:
                player1.pocket -= 100
                player2.pocket += 100

        if player1.pocket <= 0:
            print("--------------------")
            print("player1 is bankrupt")
            print("player2 is the winner")
            print("--------------------")
            print("Good bye! see you again.")
            end = time.time()
            print("--------------------")
            print("time:",end - start)
            print("--------------------")
            print("Good bye! see you again.")
            exit()
        elif player2.pocket <= 0:
            print("--------------------")
            print("player2 is bankrupt")
            print("player1 is the winner")
            print("--------------------")
            print("Good bye! see you again.")
            end = time.time()
            print("--------------------")
            print("time:",end - start)
            print("--------------------")
            print("Good bye! see you again.")
            exit()

class Deck:
    def __init__(self):
        self.deck = []
        self.__generate_cards()

    def __cards_value(self, number, value):
        if number == 1:
            return f"A{value}"
        elif number == 11:
            return f"J{value}"
        elif number == 12:
            return f"Q{value}"
        elif number == 13:
            return f"K{value}"
        else:
            return f"{number}{value}"

    def __generate_cards(self):
        for number in range(1, 14):
            self.deck.append(self.__cards_value(number, "♣️"))
            self.deck.append(self.__cards_value(number, "♦️"))
            self.deck.append(self.__cards_value(number, "♥️"))
            self.deck.append(self.__cards_value(number, "♠️"))

    def shuffle(self):
        return shuffle(self.deck)
    
    def draw(self):
        return self.deck.pop()

    def clear(self):
        self.deck = []

    def create_new_deck(self):
        self.clear()
        self.__generate_cards()

deck = Deck()
p1 = Player("p1")
p2 = Player("p2")

play = True
while play:
    deck.shuffle()
    # print(deck.deck)
    # print("--------------------")
    for i in range(2):
        p1.on_hand["card"].append(deck.draw())
        p2.on_hand["card"].append(deck.draw())
    p1.check_point()
    p2.check_point()
    p1.check_bound()
    p2.check_bound()
    print("player1 card:", p1.on_hand["card"])
    print("Bot card:", p2.on_hand["card"])
    # call1 = input("You wana call ?(y/n) :")
    call1 = 'y'
    p1.you_wana_play(call1)
    print("--------------------")
    print("player1 card:", p1.on_hand["card"])
    print("Bot card:", p2.on_hand["card"])
    print("--------------------")
    print("player1 point:", p1.on_hand["point"])
    print("player2 point:", p2.on_hand["point"])
    print("--------------------")
    print("player1 bound:", p1.on_hand["bound"])
    print("player2 bound:", p2.on_hand["bound"])
    print("--------------------")

    dealer = Dealer()
    if dealer.who_is_the_winner(p1,p2) == "draw":
        print("this round is draw")
    else:
        print("the",dealer.who_is_the_winner(p1,p2),"is the winner in this round")
    dealer.i_will_take_your_monney(p1,p2)
    print("--------------------")
    print("player1 pocket:", p1.pocket, "$")
    print("Bot    \t pocket:", p2.pocket, "$")
    su = input("You want to play again? (y/n): ")
    if su  == "n":
        play = False
    elif su == "y":
        play = True
        deck.create_new_deck()
        p1.hand0ut()
        p2.hand0ut()
    else:
        print("--------------------")
        print("You have entered incorrectly, please try again.")
        play = False