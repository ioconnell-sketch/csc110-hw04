# ------------------------------------------------------
#        Name: (Issy O'Connell)
#       Peers: (N/A)
#  References: (N/A)
# ------------------------------------------------------
import sys
secret_word = "food"


# Task 1
def check_text():
    """Ask for sentences until one has the secret word or dog/Dog."""
    while True:
        text = input("Give me a word (hint is a pet): ")
        # secret word is checked first
        if secret_word in text:
            print("You used the secret word!")
            return
        if "dog" in text or "Dog" in text:
            print('You used the word "dog" or the word "Dog"!')
            return
        print("Try again")


# Task 2
def check_greater():
    """Ask for two integers until they differ, then say which is greater."""
    while True:
        first = int(input("Give me a first integer: "))
        second = int(input("Give me a second integer: "))
        if first > second:
            print("First is Greater")
            return
        elif second > first:
            print("Second is Greater")
            return
        else:
            print("Try again")


# Task 3
def get_special_numbers():
    """Print numbers 1-40 that are odd, multiples of 3, and not multiples of 5."""
    for num in range(1, 41):
        # skip even numbers
        if num % 2 == 0:
            continue
        # skip numbers that are not multiples of 3
        if num % 3 != 0:
            continue
        # skip multiples of 5
        if num % 5 == 0:
            continue
        print(num)


# Task 4.a
def my_for_loop():
    """Read a word and say whether each letter is a vowel or consonant."""
    word = input("Give me a string: ")
    # length must be 2 to 5 and there must be no spaces
    if len(word) < 2 or len(word) > 5 or " " in word:
        print("bad word")
        return
    for letter in word:
        if letter in "aeiouAEIOU":
            print("letter " + letter + " is a vowel")
        else:
            print("letter " + letter + " is a consonant")


# Task 4.b
def my_while_loop():
    """Show a menu: a repeats, b says Goodbye and returns, c exits the program."""
    while True:
        choice = input("Choose one option: a, b, or c: ")
        if choice == "a":
            continue
        if choice == "b":
            print("Goodbye")
            return
        if choice == "c":
            sys.exit()
        print("try again")

# ---------------------------------------
# Do not modify anything below this line
# ---------------------------------------

def main():

    # Task 1 calls
    check_text()

    # Task 2 calls
    check_greater()

    # Task 3 calls
    get_special_numbers()

    # Task 4 calls
    my_for_loop()
    my_while_loop()

if __name__ == "__main__":
    main()
    print("The End")
