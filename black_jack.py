import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return f"{self.rank} of {self.suit}"
    
    def value(self):
        if self.rank in ['Jack', 'Queen', 'King']:
            return 10
        elif self.rank == 'Ace':
            return 11
        else:
            return int(self.rank)

class Deck:
    def __init__(self):
        self.cards = []
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def deal_card(self):
        return self.cards.pop()

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
    
    def add_card(self, card):
        self.cards.append(card)
        self.value += card.value()
        if card.rank == 'Ace':
            self.aces += 1
    
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
    
    def show_all(self):
        print("\n--- Cards in Hand ---")
        for card in self.cards:
            print(card)
        print(f"Total Value: {self.value}")
    
    def show_some(self):
        print("\n--- Dealer's Hand ---")
        print("Hidden Card")
        print(self.cards[1])

def show_chips(chips):
    print(f"\nPlayer's chips: {chips}")

def take_bet(chips):
    while True:
        try:
            bet = int(input(f'\nHow many chips would you like to bet? (You have {chips}): '))
        except ValueError:
            print('Please provide an integer!')
        else:
            if bet > chips:
                print("Sorry, your bet can't exceed", chips)
            else:
                return bet

def hit(deck, hand):
    hand.add_card(deck.deal_card())
    hand.adjust_for_ace()

def hit_or_stand(deck, hand):
    while True:
        x = input("\nWould you like to Hit or Stand? Enter 'h' or 's': ").lower()
        if x == 'h':
            hit(deck, hand)
        elif x == 's':
            print("Player stands. Dealer is playing.")
            return False
        else:
            print("Sorry, please try again.")
            continue
        return True

def player_busts(chips, bet):
    print("Player busts!")
    return chips - bet

def player_wins(chips, bet):
    print("Player wins!")
    return chips + bet

def dealer_busts(chips, bet):
    print("Dealer busts!")
    return chips + bet

def dealer_wins(chips, bet):
    print("Dealer wins!")
    return chips - bet

def push():
    print("Dealer and Player tie! It's a push.")

def main():
    print("Welcome to BlackJack! Get as close to 21 as you can without going over!")
    print("Dealer hits until she reaches 17. Aces count as 1 or 11.")
    
    # Set up Player's chips
    player_chips = 100
    
    while True:
        # Create & shuffle the deck, deal two cards to each player
        deck = Deck()
        deck.shuffle()
        
        player_hand = Hand()
        player_hand.add_card(deck.deal_card())
        player_hand.add_card(deck.deal_card())
        
        dealer_hand = Hand()
        dealer_hand.add_card(deck.deal_card())
        dealer_hand.add_card(deck.deal_card())
        
        # Prompt the Player for their bet
        show_chips(player_chips)
        player_bet = take_bet(player_chips)
        
        # Show cards (but keep one dealer card hidden)
        dealer_hand.show_some()
        player_hand.show_all()
        
        playing = True
        while playing:  # recall this variable from our hit_or_stand function
            
            # Prompt for Player to Hit or Stand
            playing = hit_or_stand(deck, player_hand)
            
            # Show cards (but keep one dealer card hidden)
            dealer_hand.show_some()
            player_hand.show_all()
            
            # If player's hand exceeds 21, run player_busts() and break out of loop
            if player_hand.value > 21:
                player_chips = player_busts(player_chips, player_bet)
                break
        
        # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
        if player_hand.value <= 21:
            
            while dealer_hand.value < 17:
                hit(deck, dealer_hand)
            
            # Show all cards
            print("\n--- Final Results ---")
            dealer_hand.show_all()
            player_hand.show_all()
            
            # Run different winning scenarios
            if dealer_hand.value > 21:
                player_chips = dealer_busts(player_chips, player_bet)
            elif dealer_hand.value > player_hand.value:
                player_chips = dealer_wins(player_chips, player_bet)
            elif dealer_hand.value < player_hand.value:
                player_chips = player_wins(player_chips, player_bet)
            else:
                push()
        
        # Inform Player of their chips total
        show_chips(player_chips)
        
        # Check if player is out of chips
        if player_chips <= 0:
            print("Sorry, you're out of chips! Game over.")
            break
        
        # Ask to play again
        new_game = input("Would you like to play another hand? Enter 'y' or 'n': ").lower()
        if new_game != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()