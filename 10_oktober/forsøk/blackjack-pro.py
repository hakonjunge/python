import random

suits = ["hearts", "clubs", "dimond", "spades"]

values = {"two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
          "ten": 10, "jack": 10, "queen": 10, "king": 10, "ace": 11}

ranks = ["two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king", "ace"]


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    def __init__(self, ):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()


class Participent:
    def setup(self, deck):
        self.hand.append(deck.deal_one())
        self.hand.append(deck.deal_one())

    def deal_hand(self, deal):
        self.hand.append(deal)

    def hand_value(self):
        value = 0
        found = False
        for card in self.hand:
            if card.rank == "ace" and not found:
                found = True
                continue
            value += card.value
        if found:
            if value + 11 <= 21:
                value += 11
            else:
                value += 1
        return value

    def print_hand(self):
        y = ""
        for x in self.hand:
            y += f"{x} "
        return y


class Player(Participent):
    def __init__(self, name, money=100):
        self.hand = []
        self.name = name
        self.money = money

    def bet(self, bet):
        if bet > self.money:
            print(f"You have {self.money}$ left")
            return False
        return True

    def gain_money(self, bet):
        self.money += bet

    def loose_money(self, bet):
        self.money -= bet

    def money_status(self):
        if self.money == 0:
            print("You have no money left.")
            return False
        else:
            print(f"\nYou have {self.money}$.\n")
            return True


class Dealer(Participent):
    def __init__(self):
        self.hand = []


def gamesetup():
    try:
        f = open("bjsave.txt", "x")
        name = input("you have no save files pick a name: ")
        f.close()
        f = open("bjsave.txt", "w")
        f.write(name + "\n100")
        f.close()
    except:
        f = open("bjsave.txt", "r")
        name = f.readline().replace("\n", "")
        cash = int(f.readline().replace("\n", ""))
        f.close()
        new = input(f"do you want to laod the saved file: name: {name}, $:{cash}: ").upper()
        if new == "Y":
            return Player(name, cash)
        else:
            name = input("what is your name?: ")
            return Player(name)


def bet(player):
    while True:
        try:
            inp = int(input("how much do you want to bet?: "))
        except:
            print("give a valid number")
            continue
        if not player.bet(inp) or inp < 1:
            continue

        return inp


def hit_or_stand(player, deck):
    while True:
        inp = input("Do You want to hit or stand?(H/S):").upper()
        if inp == "H":
            player.deal_hand(deck.deal_one())
            hand = ""
            for x in player.hand:
                hand += f" {x}"
            print(f"your hand is {hand}, with a value of {player.hand_value()}")
        if player.hand_value() > 21:
            return False
        if inp == "S":
            return True


def play_again():
    while True:
        inp = input("do you want to play again?(Y,N): ").upper()
        if inp in ["Y", "N"]:
            if inp == "Y":
                return True
            else:
                return False
        else:
            continue


def save(player_obj):
    while True:
        inp = input("do you want to save your progress?(Y,N): ").upper()
        if inp in ["Y", "N"]:
            if inp == "Y":
                f = open("bjsave.txt", "w")
                f.write(player_obj.name + "\n" + str(player_obj.money))
                f.close()
                return
            else:
                return
        else:
            continue


""""""

player_obj = gamesetup()
print(f"ok you are playing as {player_obj.name} you have {player_obj.money}$. \n")

game_on = True
while game_on:
    player_obj.hand = []

    dealer_obj = Dealer()

    my_deck = Deck()

    my_deck.shuffle()

    player_bet = bet(player_obj)

    dealer_obj.setup(my_deck)

    player_obj.setup(my_deck)

    print(f"Dealers first card is {dealer_obj.hand[0]} with a value of {dealer_obj.hand[0].value}")

    print(f"You'r cards are {player_obj.hand[0]} and {player_obj.hand[1]} with a value of {player_obj.hand_value()}")

    if player_obj.hand_value() == dealer_obj.hand_value() == 21:
        print("Blackjack!! but the dealer had aswell so its a draw :(")
        continue
    elif player_obj.hand_value() == 21 != dealer_obj.hand_value():
        print("Blackjack!!")
        player_obj.gain_money(player_bet)
    else:
        if not hit_or_stand(player_obj, my_deck):
            print("you lose!")
            player_obj.loose_money(player_bet)
        else:
            print("dealers cards are:")
            print(dealer_obj.print_hand())
            while True:
                if dealer_obj.hand_value() < 17:
                    print("dealer is drawing card:")
                    dealer_obj.deal_hand(my_deck.deal_one())
                    print(dealer_obj.print_hand())
                else:
                    break
            print(f"dealers cards are valued {dealer_obj.hand_value()} ")

            if player_obj.hand_value() > dealer_obj.hand_value() and player_obj.hand_value() <= 21 or dealer_obj.hand_value() > 21:
                print("You win!")
                player_obj.gain_money(player_bet)
            else:
                print("You lose!")
                player_obj.loose_money(player_bet)

    if not player_obj.money_status():
        break
    game_on = play_again()

save(player_obj)
print(f"GG's {player_obj.name}")
