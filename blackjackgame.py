import random
import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


logo = """
 _     _            _            _    
| |__ | | __ _  ___| | _____  __| |   
| '_ \| |/ _` |/ __| |/ / _ \/ _` |   
| |_) | | (_| | (__|   <  __/ (_| |_  
|_.__/|_|\__,_|\___|_|\_\___|\__,_(_)
"""


def deal():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
    return random.choice(cards)


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user, computer):
    if user > 21 and computer > 21:
        return "You lose"
    elif user == computer:
        return "It's a draw"
    elif computer == 0:
        return "Computer won with Blackjack"
    elif user == 0:
        return "You won with Blackjack"
    elif user > 21:
        return "You lose"
    elif computer > 21:
        return "You win"
    elif user > computer:
        return "You win"
    else:
        return "You lose"

def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal())
        computer_cards.append(deal())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            choice = input("Type 'y' to get another card, 'n' to pass: ")
            if choice.lower() == 'y':
                user_cards.append(deal())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal())
        computer_score = calculate_score(computer_cards)

    print(f"\nYour final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Type any letter to play Blackjack, or press Enter to quit: "):
    clear()
    play_game()

