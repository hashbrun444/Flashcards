import card_sets
import random
import os
import sys


# Display all values inside a tuple nested in a dictionary, allowing the user to go through the flashcards.
def display_cards(input_dict):
    for key, value in input_dict.items():
        print(f"{key}.{value[0]}")
        input()
        print(f"{value[1]}\n\n\n")
     
    while True:
        play_again_input = input("Finished the set! Play it again? [Y/n]")
        if play_again_input == 'n':
            return False
        elif play_again_input in ('Y', 'y', ''):
            return True


# Shuffles the terms in a card
# 1. Assigns the values of a dictionary to a temporary variable
# 2. Shuffles the list using random.shuffle
# 3. Uses the zip function to combine the shuffled values with the original keys, allowing for the questions and answers to stay paired but for the order to be shuffled.
def shuffle_terms(card_set):
    original_values = list(card_set.values())
    random.shuffle(original_values)
    return(dict(zip(card_set, original_values)))


# Shuffler logic to allow for the program to run multiple times. 
# Works by prompting the user, then returning the current_flashcards that are either shuffled or unshuffled, depending on the user's input. 
def shuffler(input_set):
        while True:
            shuffle_determine = input("Would you like to shuffle the cards? [Y/n]")
            if shuffle_determine == 'n':
                print("\nCards won't be shuffled.")
                current_flashcard = input_set
                break
            elif shuffle_determine in ('Y', 'y', ''):
                print("\nCards will be shuffled.\n")
                buffer = shuffle_terms(input_set)
                current_flashcard = buffer
                break
        return current_flashcard


# Main program code
def main():
    print("\nWelcome to CSP Cards, an AP CSP MCQ Exam Practice tool written in Python!\nTo begin, select a flashcard set number:\n")
    # Lists out all flashcards in the 'db' variable.
    for index, value in enumerate(card_sets.db):
        print(f"{index + 1}: {value[0]}")
    print("\n0: Exit")

    while True:
        # Input validation for every possible case.
        try:
            user_selection = int(input())
            # Assigns the flashcard selected to a new variable for ease-of-accesss.
            current_flashcard = card_sets.db[user_selection - 1][1]
            if user_selection == 0:
                # Allows user to exit the program without using a keyboard interrupt (Ctrl+C) or an EOF (Ctrl+D).
                sys.exit()
            break
        except ValueError:
            print("Please enter a single number!\n")
        except IndexError:
            print("Please select a flashcard number in the database!\n")
    print(f'You have selected "{card_sets.db[user_selection - 1][0]}"')
    
    # Shuffles flashcards using a buffer. 
    # This method allows the user to be asked every single time.
    buffer = shuffler(current_flashcard)
    current_flashcard = buffer
    # Dummy code to test:
    # print(type(current_flashcard)) 
    print("Let's play!\n")

    # Prints out flashcards using display_cards().
    # display_cards() returns the user's play again input, so this loop determines whether the flashcard set is repeated or if the program starts again.
    # If the user selects to play again, the shuffler runs again to determine if the user still wants to shuffle.
    # The newly shuffled or unshuffled cards are reassigned to current_flashcard, and the display_cards() function runs again. 
    # If the user decides not to play again, the entire main() function runs again, and the screen is cleared.
    while True: 
        if display_cards(current_flashcard):
            print()
            buffer = shuffler(card_sets.db[user_selection - 1][1])
            current_flashcard = buffer
        else:
            print()
            return 0
    
    

if __name__ == '__main__':
    # Using this convention prevents the main() function from running if this file is imported. 
    # This allows for scalability such as implementing a GUI mode.
    while True:
        # Clear screen, command obtained from StackOverflow: 
        # https://stackoverflow.com/questions/2084508/clear-the-terminal-in-python
        os.system('cls' if os.name == 'nt' else 'clear')
        # Allows main code to be looped through the use of return statements.
        main()