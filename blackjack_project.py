############### Blackjack Project #####################
from art import logo
import random

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.

# Uses the List below to *return* a random card.
#11 is the Ace.
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

# Takes a List of cards as input and returns the score. 
def calculate_score(cards):
     
    # Check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    # Check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. 
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(user_score, computer_score):
    if computer_score > 21 and user_score > 21:
        return "You went over. You lose."
    
    if computer_score == user_score:
        return "Draw."
    elif computer_score == 0:
        return "Opponent has Blackjack. You lose."
    elif user_score == 0:
        return "Blackjack. You win."
    elif user_score > 21:
        return "You went over. You lose."
    elif computer_score > 21:
        return "Opponent went over. You win."
    elif user_score > computer_score:
        return "You win."
    else:
        return "You lose."
            



def play_game():
    print(logo)

    user_cards = []
    computer_cards = []
    game_over = False

    for card in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not game_over:
      # Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
      user_score = calculate_score(user_cards)
      computer_score = calculate_score(computer_cards)

      print(f"Your cards: {user_cards}, current score: {user_score}")
      print(f"Computer's first card: {computer_cards[0]}")

      if user_score == 0 or computer_score == 0 or user_score > 21:
          game_over = True
      
      else:
          user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")

          if user_should_deal == "y":
              user_cards.append(deal_card())
          
          else:
              game_over = True

    # Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

    user_continue = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if user_continue == "y":
        play_game()


play_game()