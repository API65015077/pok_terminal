from collections import deque
from random import shuffle
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.pocket = 500
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
            if self.__class__.__name__ == "Player":
                time.sleep(1.25)
                self.on_hand["card"].append(deck.draw())
                print(self.name, "draw a card")
                if self.on_hand["card"][0][1] == "0" and self.on_hand["card"][1][1] == "0" and self.on_hand["card"][2][1] == "0":
                    self.cards_terminal_3(str(self.on_hand["card"][0][0])+str(self.on_hand["card"][0][1]), self.on_hand["card"][0][-2], str(self.on_hand["card"][1][0])+str(self.on_hand["card"][1][1]), self.on_hand["card"][1][-2], str(self.on_hand["card"][2][0])+str(self.on_hand["card"][2][1]), self.on_hand["card"][2][-2])
                    # 10 10 10
                elif self.on_hand["card"][0][1] != "0" and self.on_hand["card"][1][1] == "0" and self.on_hand["card"][2][1] == "0":
                    self.cards_terminal_3(self.on_hand["card"][0][0], self.on_hand["card"][0][-2], str(self.on_hand["card"][1][0])+str(self.on_hand["card"][1][1]), self.on_hand["card"][1][-2], str(self.on_hand["card"][2][0])+str(self.on_hand["card"][2][1]), self.on_hand["card"][2][-2])
                    # 0 10 10
                elif self.on_hand["card"][0][1] == "0" and self.on_hand["card"][1][1] != "0" and self.on_hand["card"][2][1] == "0":
                    self.cards_terminal_3(str(self.on_hand["card"][0][0])+str(self.on_hand["card"][0][1]), self.on_hand["card"][0][-2], self.on_hand["card"][1][0], self.on_hand["card"][1][-2], str(self.on_hand["card"][2][0])+str(self.on_hand["card"][2][1]), self.on_hand["card"][2][-2])
                    # 10 0 10
                elif self.on_hand["card"][0][1] == "0" and self.on_hand["card"][1][1] == "0" and self.on_hand["card"][2][1] != "0":
                    self.cards_terminal_3(str(self.on_hand["card"][0][0])+str(self.on_hand["card"][0][1]), self.on_hand["card"][0][-2], str(self.on_hand["card"][1][0])+str(self.on_hand["card"][1][1]), self.on_hand["card"][1][-2], self.on_hand["card"][2][0], self.on_hand["card"][2][-2])
                    # 10 10 0
                elif self.on_hand["card"][0][1] != "0" and self.on_hand["card"][1][1] != "0" and self.on_hand["card"][2][1] == "0":
                    self.cards_terminal_3(self.on_hand["card"][0][0], self.on_hand["card"][0][-2], self.on_hand["card"][1][0], self.on_hand["card"][1][-2], str(self.on_hand["card"][2][0])+str(self.on_hand["card"][2][1]), self.on_hand["card"][2][-2])
                    # 0 0 10
                elif self.on_hand["card"][0][1] != "0" and self.on_hand["card"][1][1] == "0" and self.on_hand["card"][2][1] != "0":
                    self.cards_terminal_3(self.on_hand["card"][0][0], self.on_hand["card"][0][-2], str(self.on_hand["card"][1][0])+str(self.on_hand["card"][1][1]), self.on_hand["card"][1][-2], self.on_hand["card"][2][0], self.on_hand["card"][2][-2])
                    # 0 10 0
                elif self.on_hand["card"][0][1] == "0" and self.on_hand["card"][1][1] != "0" and self.on_hand["card"][2][1] != "0":
                    self.cards_terminal_3(str(self.on_hand["card"][0][0])+str(self.on_hand["card"][0][1]), self.on_hand["card"][0][-2], self.on_hand["card"][1][0], self.on_hand["card"][1][-2], self.on_hand["card"][2][0], self.on_hand["card"][2][-2])
                    # 10 0 0
                else:
                    self.cards_terminal_3(self.on_hand["card"][0][0], self.on_hand["card"][0][-2], self.on_hand["card"][1][0], self.on_hand["card"][1][-2], self.on_hand["card"][2][0], self.on_hand["card"][2][-2])
                self.call_check()

    def call_check(self):
        self.check_point()
        self.check_bound()

    def show_point(self, point, bound):
        print("\t     ____________________")
        print("\t    |                    |")
        if self.__class__.__name__ == "Player":
            print("\t    |     Name  = {}     |".format(self.name))
        elif self.__class__.__name__ == "Bot":
            print("\t    |   Name  = {} |".format(self.name))
        if point >= 10:
            print("\t    |     Point = {}     |".format(point))
        else:   
            print("\t    |     Point = {}      |".format(point))
        print("\t    |     Bound = {}      |".format(bound))  
        print("\t    |____________________|")
    
    def cards_terminal_1(self, prev_card, prev_face):
        # print()
        print("\t ________________      ")
        print("\t|                |     ")
        if prev_card == '10':
            print("\t|  {}            |    ".format(prev_card)) 
        else:
            print("\t|  {}             |    ".format(prev_card))  
        print("\t|                |    ")
        print("\t|                |    ")
        print("\t|                |    ")
        print("\t|                |    ")
        print("\t|       {}        |    ".format(prev_face))
        print("\t|                |    ")
        print("\t|                |    ")
        print("\t|                |    ")
        print("\t|                |    ")
        if prev_card == '10':
            print("\t|            {}  |    ".format(prev_card))
        else:
            print("\t|            {}   |    ".format(prev_card))  
        print("\t|________________|    ")
        print()

    def cards_terminal_2(self, prev_card, prev_face , current_card, current_face):
        # print()
        print("\t ________________      ________________     ")
        print("\t|                |    |                |    ")
        if prev_card == '10' and current_card == '10':
            print("\t|  {}            |    |  {}            |    ".format(prev_card,current_card))
        elif prev_card == '10': 
            print("\t|  {}            |    |  {}             |   ".format(prev_card,current_card))   
        elif current_card == '10':
            print("\t|  {}             |    |  {}            |   ".format(prev_card,current_card))   
        else:
            print("\t|  {}             |    |  {}             |   ".format(prev_card,current_card))  
        print("\t|                |    |                |    ")
        print("\t|                |    |                |    ")
        print("\t|                |    |                |    ")
        print("\t|                |    |                |    ")
        print("\t|       {}        |    |       {}        |    ".format(prev_face, current_face))
        print("\t|                |    |                |    ")
        print("\t|                |    |                |    ")
        print("\t|                |    |                |    ")
        print("\t|                |    |                |    ")
        if prev_card == '10' and current_card == '10':
            print("\t|            {}  |    |            {}  |    ".format(prev_card,current_card))
        elif prev_card == '10': 
            print("\t|            {}  |    |            {}   |    ".format(prev_card,current_card))   
        elif current_card == '10':
            print("\t|            {}   |    |            {}  |    ".format(prev_card,current_card))   
        else:
            print("\t|            {}   |    |            {}   |    ".format(prev_card,current_card))  
        print("\t|________________|    |________________|    ")
        print()

    def cards_terminal_3(self, prev_card, prev_face, current_card, current_face, next_card, next_face):
        # print()
        print("\t ________________      ________________      ________________")
        print("\t|                |    |                |    |                |")
        if prev_card == '10' and current_card == '10' and next_card == '10':
            print("\t|  {}            |    |  {}            |    |  {}            |".format(prev_card,current_card,next_card))
        elif prev_card == '10' and current_card == '10':
            print("\t|  {}            |    |  {}            |    |  {}             |".format(prev_card,current_card,next_card))
        elif prev_card == '10' and next_card == '10':
            print("\t|  {}            |    |  {}             |    |  {}            |".format(prev_card,current_card,next_card))
        elif current_card == '10' and next_card == '10':
            print("\t|  {}             |    |  {}            |    |  {}            |".format(prev_card,current_card,next_card))
        elif prev_card == '10': 
            print("\t|  {}            |    |  {}             |    |  {}             |".format(prev_card,current_card,next_card))   
        elif current_card == '10':
            print("\t|  {}             |    |  {}            |    |  {}             |".format(prev_card,current_card,next_card))   
        elif next_card == '10':
            print("\t|  {}             |    |  {}             |    |  {}            |".format(prev_card,current_card,next_card))
        else:
            print("\t|  {}             |    |  {}             |    |  {}             |".format(prev_card,current_card,next_card))  
        print("\t|                |    |                |    |                |")
        print("\t|                |    |                |    |                |")
        print("\t|                |    |                |    |                |")
        print("\t|                |    |                |    |                |")
        print("\t|       {}        |    |       {}        |    |       {}        |".format(prev_face, current_face, next_face))
        print("\t|                |    |                |    |                |")
        print("\t|                |    |                |    |                |")
        print("\t|                |    |                |    |                |")
        print("\t|                |    |                |    |                |")
        if prev_card == '10' and current_card == '10' and next_card == '10':
            print("\t|            {}  |    |            {}  |    |            {}  |".format(prev_card,current_card,next_card))
        elif prev_card == '10' and current_card == '10':
            print("\t|            {}  |    |            {}  |    |             {}  |".format(prev_card,current_card,next_card))
        elif prev_card == '10' and next_card == '10':
            print("\t|            {}  |    |            {}   |    |            {}  |".format(prev_card,current_card,next_card))
        elif prev_card == '10': 
            print("\t|            {}  |    |            {}   |    |             {}  |".format(prev_card,current_card,next_card))   
        elif current_card == '10':
            print("\t|            {}   |    |            {}  |    |             {}  |".format(prev_card,current_card,next_card))   
        elif next_card == '10':
            print("\t|            {}   |    |            {}   |    |            {}  |".format(prev_card,current_card,next_card))
        else:
            print("\t|            {}   |    |            {}   |    |            {}   |".format(prev_card,current_card,next_card))  
        print("\t|________________|    |________________|    |________________|")
        print()

class Bot(Player):
    def __init__(self, name):
        super().__init__(name)

    def check_my_hand(self):
        self.check_point()
        if self.on_hand["point"] < 5:
            self.you_wana_play("y")
            self.check_point()
            self.check_bound()

    def card_terminal_q2(self):
        # print()
        print("\t ________________      ________________ ")
        print("\t|                |    |                |")
        print("\t|                |    |                |")
        print("\t|      * *       |    |      * *       |")
        print("\t|    *     *     |    |    *     *     |")
        print("\t|   *       *    |    |   *       *    |")
        print("\t|   *       *    |    |   *       *    |")
        print("\t|          *     |    |          *     |")
        print("\t|         *      |    |         *      |")
        print("\t|        *       |    |        *       |")
        print("\t|                |    |                |")
        print("\t|                |    |                |")
        print("\t|        *       |    |        *       |")
        print("\t|________________|    |________________|")
        # print()

    def card_terminal_q1(self):
        # print()
        print("\t ________________")
        print("\t|                |")
        print("\t|                |")
        print("\t|      * *       |")
        print("\t|    *     *     |")
        print("\t|   *       *    |")
        print("\t|   *       *    |")
        print("\t|          *     |")
        print("\t|         *      |")
        print("\t|        *       |")
        print("\t|                |")
        print("\t|                |")
        print("\t|        *       |")
        print("\t|________________|")
        # print()

    def show_card(self):
        print(self.name, "have")
        if len(self.on_hand["card"]) == 1:
            if self.on_hand["card"][0][1] == "0":
                self.cards_terminal_1(str(self.on_hand["card"][0][0])+str(self.on_hand["card"][0][1]) , self.on_hand["card"][0][-2])
            else:
                self.cards_terminal_1(self.on_hand["card"][0][0], self.on_hand["card"][0][-2])
        elif len(self.on_hand["card"]) == 2:
            if self.on_hand["card"][0][1] == "0" and self.on_hand["card"][1][1] != "0":
                self.cards_terminal_2(str(self.on_hand["card"][0][0])+str(self.on_hand["card"][0][1]) , self.on_hand["card"][0][-2] , self.on_hand["card"][1][0], self.on_hand["card"][1][-2])
            elif self.on_hand["card"][0][1] == "0" and self.on_hand["card"][1][1] == "0":
                self.cards_terminal_2(str(self.on_hand["card"][0][0])+str(self.on_hand["card"][0][1]), self.on_hand["card"][0][-2] , str(self.on_hand["card"][1][0])+str(self.on_hand["card"][1][1]), self.on_hand["card"][1][-2])
            else:
                self.cards_terminal_2(self.on_hand["card"][0][0], self.on_hand["card"][0][-2], self.on_hand["card"][1][0], self.on_hand["card"][1][-2])
        elif len(self.on_hand["card"]) == 3:
            if self.on_hand["card"][0][1] == "0" and self.on_hand["card"][1][1] == "0" and self.on_hand["card"][2][1] == "0":
                    self.cards_terminal_3(str(self.on_hand["card"][0][0])+str(self.on_hand["card"][0][1]), self.on_hand["card"][0][-2], str(self.on_hand["card"][1][0])+str(self.on_hand["card"][1][1]), self.on_hand["card"][1][-2], str(self.on_hand["card"][2][0])+str(self.on_hand["card"][2][1]), self.on_hand["card"][2][-2])
                    # 10 10 10
            elif self.on_hand["card"][0][1] != "0" and self.on_hand["card"][1][1] == "0" and self.on_hand["card"][2][1] == "0":
                self.cards_terminal_3(self.on_hand["card"][0][0], self.on_hand["card"][0][-2], str(self.on_hand["card"][1][0])+str(self.on_hand["card"][1][1]), self.on_hand["card"][1][-2], str(self.on_hand["card"][2][0])+str(self.on_hand["card"][2][1]), self.on_hand["card"][2][-2])
                # 0 10 10
            elif self.on_hand["card"][0][1] == "0" and self.on_hand["card"][1][1] != "0" and self.on_hand["card"][2][1] == "0":
                self.cards_terminal_3(str(self.on_hand["card"][0][0])+str(self.on_hand["card"][0][1]), self.on_hand["card"][0][-2], self.on_hand["card"][1][0], self.on_hand["card"][1][-2], str(self.on_hand["card"][2][0])+str(self.on_hand["card"][2][1]), self.on_hand["card"][2][-2])
                # 10 0 10
            elif self.on_hand["card"][0][1] == "0" and self.on_hand["card"][1][1] == "0" and self.on_hand["card"][2][1] != "0":
                self.cards_terminal_3(str(self.on_hand["card"][0][0])+str(self.on_hand["card"][0][1]), self.on_hand["card"][0][-2], str(self.on_hand["card"][1][0])+str(self.on_hand["card"][1][1]), self.on_hand["card"][1][-2], self.on_hand["card"][2][0], self.on_hand["card"][2][-2])
                # 10 10 0
            elif self.on_hand["card"][0][1] != "0" and self.on_hand["card"][1][1] != "0" and self.on_hand["card"][2][1] == "0":
                self.cards_terminal_3(self.on_hand["card"][0][0], self.on_hand["card"][0][-2], self.on_hand["card"][1][0], self.on_hand["card"][1][-2], str(self.on_hand["card"][2][0])+str(self.on_hand["card"][2][1]), self.on_hand["card"][2][-2])
                # 0 0 10
            elif self.on_hand["card"][0][1] != "0" and self.on_hand["card"][1][1] == "0" and self.on_hand["card"][2][1] != "0":
                self.cards_terminal_3(self.on_hand["card"][0][0], self.on_hand["card"][0][-2], str(self.on_hand["card"][1][0])+str(self.on_hand["card"][1][1]), self.on_hand["card"][1][-2], self.on_hand["card"][2][0], self.on_hand["card"][2][-2])
                # 0 10 0
            elif self.on_hand["card"][0][1] == "0" and self.on_hand["card"][1][1] != "0" and self.on_hand["card"][2][1] != "0":
                self.cards_terminal_3(str(self.on_hand["card"][0][0])+str(self.on_hand["card"][0][1]), self.on_hand["card"][0][-2], self.on_hand["card"][1][0], self.on_hand["card"][1][-2], self.on_hand["card"][2][0], self.on_hand["card"][2][-2])
                # 10 0 0
            else:
                self.cards_terminal_3(self.on_hand["card"][0][0], self.on_hand["card"][0][-2], self.on_hand["card"][1][0], self.on_hand["card"][1][-2], self.on_hand["card"][2][0], self.on_hand["card"][2][-2])
                


class Dealer:
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
            print("\t------------------------------")
            print("\t", player1.name, "is bankrupt")
            print("\t", player2.name, "is the winner")
            print("\t--------------------")
            print("\tGood bye! see you again.")
            exit()
        elif player2.pocket <= 0:
            print("\t------------------------------")
            print("\t", player2.name,"is bankrupt")
            print("\t", player1.name, "is the winner")
            print("\t--------------------")
            print("\tGood bye! see you again.")
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

    def sent_card_to_player(self, player ): 
        player.on_hand["card"].append(self.draw())
        if player.__class__.__name__ == "Player":
            # print(player.name ,"card:",player.on_hand["card"])
            if len(player.on_hand["card"]) == 1:
                if player.on_hand["card"][0][1] == "0":
                    player.cards_terminal_1(str(player.on_hand["card"][0][0])+str(player.on_hand["card"][0][1]) , player.on_hand["card"][0][-2])
                else:
                    player.cards_terminal_1(player.on_hand["card"][0][0], player.on_hand["card"][0][-2])
            elif len(player.on_hand["card"]) == 2:
                if player.on_hand["card"][0][1] == "0" and player.on_hand["card"][1][1] != "0":
                    player.cards_terminal_2(str(player.on_hand["card"][0][0])+str(player.on_hand["card"][0][1]) , player.on_hand["card"][0][-2] , player.on_hand["card"][1][0], player.on_hand["card"][1][-2])
                elif player.on_hand["card"][0][1] == "0" and player.on_hand["card"][1][1] == "0":
                    player.cards_terminal_2(str(player.on_hand["card"][0][0])+str(player.on_hand["card"][0][1]), player.on_hand["card"][0][-2] , str(player.on_hand["card"][1][0])+str(player.on_hand["card"][1][1]), player.on_hand["card"][1][-2])
                else:
                    player.cards_terminal_2(player.on_hand["card"][0][0], player.on_hand["card"][0][-2], player.on_hand["card"][1][0], player.on_hand["card"][1][-2])
            
        # elif player.__class__.__name__ == "Bot":
        #     print(player.name ,"card:","??")
        #     if len(player.on_hand["card"]) == 1:
        #         player.card_terminal_q1()
        #     elif len(player.on_hand["card"]) == 2:
        #         player.card_terminal_q2()
        time.sleep(1.25)

deck = Deck()
# p1 = Player(input("Enter your name: "))
p1 = Player("su")
bot = Bot("Nong Bot")
dealer = Dealer()
my_turn = deque()
max_size = 3
my_turn.append(p1)
my_turn.append(bot)

# for test
# deck.deck.append("10♣️")
# deck.deck.append("1♣️")
# deck.deck.append("1♦️")
# deck.sent_card_to_player(my_turn[0])
# deck.sent_card_to_player(my_turn[0])
# my_turn[0].you_wana_play("y")

play = True
while play:
    deck.shuffle()
    print("On",my_turn[0].name,"hand and poacket", my_turn[0].pocket)
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
    time.sleep(1.25)
    my_turn[0].you_wana_play(input("Do you want to draw a card? (y/n): "))
    time.sleep(1.25)
    my_turn[1].show_card()
    time.sleep(1.25)
    my_turn[1].show_point(my_turn[1].on_hand["point"], my_turn[1].on_hand["bound"])
    time.sleep(1.25)
    my_turn[0].show_point(my_turn[0].on_hand["point"], my_turn[0].on_hand["bound"])
    time.sleep(1.25)
    print("\t------------------------------")

    print("\tThe winner is",dealer.who_is_the_winner(my_turn[0], my_turn[1]))
    dealer.i_will_take_your_monney(my_turn[0], my_turn[1])
    print("\t", my_turn[0].name ,"pocket:",my_turn[0].pocket)
    print("\t", my_turn[1].name ,"pocket:",my_turn[1].pocket)
    my_turn[0].hand0ut(deck) 
    my_turn[1].hand0ut(deck)

    want_to_play = input("do you want to play again? (y/n): ")
    if want_to_play != "y":
        print("\t------------------------------")
        if want_to_play != "n":
            print("\tYour Answer is not correct")
        print("\tGood bye! see you again.")
        exit()
    elif want_to_play == "y":
        print("\t------------------------------")
    else:
        print("\tyour answer is not correct")
        print("\tGood bye! see you again.")
        exit() 