from collections import deque
from random import shuffle
import time
# import os

# start = time.time()
class Player:
    def __init__(self, name):
        self.name = name
        self.pocket = 100
        self.on_hand = {
                        "card": [],
                        "point": 0,
                        "bound": 1
                    }

    def hand0ut(self, deck ):
        if len(self.on_hand["card"]) == 2:
            deck.deck.append(self.on_hand["card"].pop())
            deck.deck.append(self.on_hand["card"].pop())
        elif len(self.on_hand["card"]) == 3:
            deck.deck.append(self.on_hand["card"].pop())
            deck.deck.append(self.on_hand["card"].pop())
            deck.deck.append(self.on_hand["card"].pop())
        self.on_hand["point"] = 0
        self.on_hand["bound"] = 1
        deck.shuffle()

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
        elif self.on_hand["point"] < 0 or self.on_hand["point"] == 10:
            self.on_hand["point"] = 0

    def check_bound(self):
        count_card = len(self.on_hand["card"][0].strip())-1  
        count_card1 = len(self.on_hand["card"][1].strip())-1

        if count_card == 2 and count_card1 == 2: # 2 2
            sym = self.on_hand["card"][0][1]
            sym1 = self.on_hand["card"][1][1]
            if sym == sym1:
                self.on_hand["bound"] += 1
        elif count_card == 3 and count_card1 == 2: # 3 2
            sym = self.on_hand["card"][0][2]
            sym1 = self.on_hand["card"][1][1]
            if sym == sym1:
                self.on_hand["bound"] += 1
        elif count_card == 2 and count_card1 == 3: # 2 3
            sym = self.on_hand["card"][0][1]
            sym1 = self.on_hand["card"][1][2]
            if sym == sym1:
                self.on_hand["bound"] += 1
        elif count_card == 3 and count_card1 == 3: # 3 3
            sym = self.on_hand["card"][0][2]
            sym1 = self.on_hand["card"][1][2]
            if sym == sym1:
                self.on_hand["bound"] += 1

    def you_wana_play(self, call):
        if call == "y":
            self.on_hand["card"].append(deck.draw())
            self.call_check()

    def call_check(self):
        self.check_point()
        self.check_bound()


class Bot(Player):
    def __init__(self, name):
        super().__init__(name)

    def check_my_hand(self):
        self.check_point()
        if self.on_hand["point"] < 5:
            self.you_wana_play("y")
            self.check_point()
            self.check_bound()
        # os.system('cls')


class Dealer:
    def do_you_wanna_play_with_my_bot(self, answer):
        pass

    def who_is_the_winner(self, player1, player2):
        if len(player1.on_hand["card"]) == 2 and len(player2.on_hand["card"]) == 2 or\
        len(player1.on_hand["card"]) == 3 and len(player2.on_hand["card"]) == 3:
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

        elif len(player1.on_hand["card"]) == 3 and len(player2.on_hand["card"]) == 2:
            if player2.on_hand["point"] > player1.on_hand["point"]:
                return "player2"
            elif player1.on_hand["point"] == player2.on_hand["point"]:
                return "player2"
            else:
                return "player1"
            
        elif len(player1.on_hand["card"]) == 2 and len(player2.on_hand["card"]) == 3:
            if player1.on_hand["point"] > player2.on_hand["point"]:
                return "player1"
            elif player1.on_hand["point"] == player2.on_hand["point"]:
                return "player1"
            else:
                return "player2"

    def i_will_take_your_monney(self, player1, player2):
        who_is_the_winner = self.who_is_the_winner(player1, player2)
        if who_is_the_winner == "player1":
            if player1.on_hand["bound"] > 1:
                player1.pocket += (100 * player1.on_hand["bound"])
                player2.pocket -= (100 * player1.on_hand["bound"])
            else:
                player1.pocket += 100
                player2.pocket -= 100
        elif who_is_the_winner == "player2":
            if player2.on_hand["bound"] > 1:
                player2.pocket += (100 * player1.on_hand["bound"])
                player1.pocket -= (100 * player1.on_hand["bound"])
            else:
                player1.pocket -= 100
                player2.pocket += 100

        self.check_pocket(player1, player2)

    def check_pocket(self, player1, player2):
        if player1.pocket <= 0:
            print("--------------------")
            print(player1.name, "is bankrupt")
            print(player2.name, "is the winner")
            print("--------------------")
            print("Good bye! see you again.")
            exit()
        elif player2.pocket <= 0:
            print("--------------------")
            print(player2.name,"is bankrupt")
            print(player1.name, "is the winner")
            print("--------------------")
            print("Good bye! see you again.")
            exit()

    def money_for_your_enemy(self, player1, player2):
        pass


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

    def sent_card_to_player(self, player ): 
        player.on_hand["card"].append(self.draw())
        if player.__class__.__name__ == "Player":
            print(player.name ,"card:",player.on_hand["card"])
        elif player.__class__.__name__ == "Bot":
            print(player.name ,"card:","??")
        time.sleep(0.5)
        

deck = Deck()
# p1 = Player(input("Enter your name: "))
p1 = Player("su")
bot = Bot("Nong Bot")
dealer = Dealer()
my_turn = deque()
max_size = 3
my_turn.append(p1)
my_turn.append(bot)



play = True
while play:
    deck.shuffle()
    # print("deck:",deck.deck)
    deck.sent_card_to_player(my_turn[1])
    my_turn.rotate(-1) #bot
    deck.sent_card_to_player(my_turn[1])
    my_turn.rotate(-1)  #player
    deck.sent_card_to_player(my_turn[1])
    my_turn.rotate(-1) #bot
    deck.sent_card_to_player(my_turn[1])

    my_turn.rotate(-1) #player
    my_turn[1].check_my_hand()
    my_turn.rotate(-1) #bot
    my_turn[1].call_check()

    my_turn.rotate(-1) #player
    my_turn[0].you_wana_play(input("Do you want to draw a card? (y/n): "))
    print(my_turn[0].name ,"card:",my_turn[0].on_hand["card"])
    time.sleep(1)
    print(my_turn[1].name ,"card:",my_turn[1].on_hand["card"])
    time.sleep(1)
    print(my_turn[0].name ,"point:",my_turn[0].on_hand["point"])
    time.sleep(1)
    print(my_turn[1].name ,"point:",my_turn[1].on_hand["point"])
    time.sleep(1)
    print(my_turn[0].name ,"bound:",my_turn[0].on_hand["bound"])
    time.sleep(1)
    print(my_turn[1].name ,"bound:",my_turn[1].on_hand["bound"])
    time.sleep(1)
    print("--------------------")

    print("The winner is",dealer.who_is_the_winner(my_turn[0], my_turn[1]))
    dealer.i_will_take_your_monney(my_turn[0], my_turn[1])
    print(my_turn[0].name ,"pocket:",my_turn[0].pocket)
    print(my_turn[1].name ,"pocket:",my_turn[1].pocket)
    my_turn[0].hand0ut(deck) 
    my_turn[1].hand0ut(deck)

    want_to_play = input("do you want to play again? (y/n): ")
    if want_to_play != "y":
        print("--------------------")
        if want_to_play != "n":
            print("Your Answer is not correct")
        print("Good bye! see you again.")
        exit()
    

