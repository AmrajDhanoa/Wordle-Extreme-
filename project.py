from spellchecker import SpellChecker
from colorama import init,Fore, Style
import random
import sys


init(autoreset=True)

def main(): # call all functions
    print(game_instructions())
    board = create_board()
    print(print_board(board))
    main_word, words = generate_word()
    score = 6
    index = 0
    while score != 0:
        user_input = input(Fore.WHITE + 'Guess a word: ').lower()
        valid = validate_input(user_input,words,board)
        if valid == True:
            print(check_input(user_input,main_word,board,index))
            score -= 1
            index +=1
        else:
            continue
        if score == 0:
            print(Style.BRIGHT + Fore.WHITE + f"Better luck next time! The word was {main_word}!")

def game_instructions():
    instructions = [Style.BRIGHT + 'Welcome to Wordle! You have 6 chances to guess the mystery 5-letter word, good luck!',
                    Fore.GREEN + 'Green character(s) mean the letter(s) are in the correct spot in the word',
                    Fore.YELLOW + 'Yellow character(s) mean the letter(s) are in the word but in the wrong spot',
                    Fore.LIGHTBLACK_EX + 'Grey character(s) mean the letter(s) are not in the word'
    ]
    lines = '\n'.join(instructions)
    return lines


def create_board(colm=5, row=6):
    return[['_' for _ in range(colm)] for _ in range(row)]


def print_board(board):
    return('\n'.join(' '.join(row) for row in board))

# create_board()

def generate_word():
    spell = SpellChecker()
    List = list(spell.word_frequency)
    words = []
    for word in List:
        if len(word) == 5 and "'" not in word:
            words.append(word)
    main_word = random.choice(words)
    return main_word, words


def validate_input(user_input,words,board):
    if len(user_input) > 5:
        print('word is too long, try again')
        print(print_board(board))
        return False
    elif len(user_input) < 5:
        print("word is too short, try again")
        print(print_board(board))
        return False
    elif user_input not in words:
        print("Word doesn't exist, try again!")
        print(print_board(board))
        return False
    else:
        return True

def check_input(user_input, main_word, board, index):
    coloured_letters = []
    if user_input == main_word:
        coloured_letters.append(Fore.GREEN + ' '.join(user_input))
        board[index] = coloured_letters
        print(print_board(board))
        sys.exit("Congratulations! You guess the word!")
    check_word = list(main_word)
    for i,char in enumerate(user_input):
        if char == check_word[i]:
            check_word[i] = None
            coloured_letters.append(Fore.GREEN + char + Fore.RESET)
        elif char in check_word:
            i = check_word.index(char)
            check_word[i] = None
            coloured_letters.append(Fore.YELLOW + char + Fore.RESET)
        elif char not in check_word:
            coloured_letters.append(Fore.LIGHTBLACK_EX + char + Fore.RESET)
    board[index] = coloured_letters
    return print_board(board)



if __name__ == '__main__':
    main()


