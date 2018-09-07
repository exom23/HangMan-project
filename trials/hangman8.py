def main():
    print("Welocme to Hangman!")
    word = "SWAHILIBOX"
    letters_tried = []
    a = ["_" for i in range(len(word))]
    print(" ".join(a))
    
    while True:
        letter = input("Guess your letter: ").upper()
        count = 0

        if letter not in letters_tried:
            for i in range(len(word)):
                if letter == word[i] and a[i] == "_":
                    a[i] = letter
                    print(" ".join(a))
                    break
                else:
                    count += 1
        else:
            print("Letter already tried")

        if count == len(word):
                letters_tried.append(letter)

        if "_" not in a:
            print("You found the word: ", "".join(a))
            break


if __name__ == "__main__":
    main()
