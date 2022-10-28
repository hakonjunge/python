import random

suits = ["hjerter", "kløver", "ruter", "spar"]

values = {"to": 2, "tre": 3, "fire": 4, "fem": 5, "seks": 6, "syv": 7, "åtte": 8, "ni": 9,
          "ti": 10, "knekt": 10, "dame": 10, "konge": 10, "ess": 11}

ranks = ["to", "tre", "fire", "fem", "seks", "syv", "åtte", "ni", "ti", "knekt", "dame", "konge", "ess"]


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f"{self.suit} {self.rank}"


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
            if card.rank == "ess" and not found:
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
            print(f"Du har {self.money} chipper igjen")
            return False
        return True

    def gain_money(self, bet):
        self.money += bet

    def loose_money(self, bet):
        self.money -= bet

    def money_status(self):
        if self.money == 0:
            print("Du har ingen chipper igjen")
            return False
        else:
            print(f"\nDu har {self.money}\n")
            return True


class Dealer(Participent):
    def __init__(self):
        self.hand = []


def gamesetup():
    try:
        f = open("bjsave.txt", "x")
        name = input("Du har ingen lagret save-fil.\nVelg et navn: ")
        f.close()
        f = open("bjsave.txt", "w")
        f.write(name + "\n100")
        f.close()
    except:
        f = open("bjsave.txt", "r")
        name = f.readline().replace("\n", "")
        chipper = int(f.readline().replace("\n", ""))
        f.close()
        new = input(
            f"\nØnsker du å fortsette der du slapp? \nFremgang er lagret på: {name}, med {chipper} chipper igjen \n(Y/N) ").upper()
        if new == "Y":
            return Player(name, chipper)
        else:
            name = input("Hva heter du?  ")
            return Player(name)


def bet(player):
    while True:
        try:
            inp = int(input("Hvor mye ønsker du å bette "))
        except:
            print("Tallet du skrev er ugyldig, prøv igjen ")
            continue
        if not player.bet(inp) or inp < 1:
            continue

        return inp


def hit_or_stand(player, deck):
    while True:
        inp = input("\nSlå til eller stå? \n(H/S) ").upper()
        if inp == "H":
            player.deal_hand(deck.deal_one())
            hand = ""
            for x in player.hand:
                hand += f" {x}"
            print(f"Hånden din er {hand}, med en verdi på {player.hand_value()}")
        if player.hand_value() > 21:
            return False
        if inp == "S":
            return True


def play_again():
    while True:
        inp = input("\nVil du spille igjen? \n(J/N) ").upper()
        if inp in ["J", "N"]:
            if inp == "J":
                return True
            else:
                return False
        else:
            continue


def save(player_obj):
    while True:
        inp = input("\nØnsker du å lagre fremgangen din? \n(J,N) ").upper()
        if inp in ["J", "N"]:
            if inp == "J":
                f = open("bjsave.txt", "w")
                f.write(player_obj.name + "\n" + str(player_obj.money))
                f.close()
                return
            else:
                return
        else:
            continue
