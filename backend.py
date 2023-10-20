from random import *

class functionality:

    def __init__(self):
        self.valid_words = []
        self.filename = 'sgb-words.txt'
        
        # handles file not found
        try:
            e = open(self.filename)
        except FileNotFoundError:
            print(f"FileNotFoundError for file {self.filename}")
        else:
            with open (self.filename) as lines:
                for line in lines:
                    word = line.strip('\n').lower()
                    if len(word) == 5:
                        self.valid_words.append(word)
            lines.close()

        wordleTargetWordIndex = randint(0, len(self.valid_words))
        self.wordleTargetWord = self.valid_words[wordleTargetWordIndex]

    def inputted(self):
        while True:
            wordInputted = input("Enter a five letter word: ").lower()
            if len(wordInputted) != 5:
                print("word needs to be 5 letters long, enter a valid word" + "\n")
            
            elif not self.validateWord(wordInputted):
                print("word is not valid, enter a valid word" + "\n")
                
            else:
                break

        return wordInputted
    
    def hint(self):
        pass

    def validateWord(self, word):
        return word in self.valid_words

    def afterValidation(self, word):
        if word == self.wordleTargetWord:
            return True
        return False
    
    def pattern(self, word):
        chars = {
            'rightSpot' : "",
            'wrongSpot' : '',
            'notIn' : ''
        }

        for x in range(len(word)):
            el = word[x]
            if el in self.wordleTargetWord and el == self.wordleTargetWord[x]:
                chars['rightSpot'] += el
            elif el in self.wordleTargetWord and el != self.wordleTargetWord[x]:
                chars['wrongSpot'] += el
            else:
                chars['notIn'] += el

        print("LETTERS IN THE RIGHT SPOT: " + " ".join(chars['rightSpot']) + "\n")
        print("LETTERS IN THE WRONG SPOT: " + " ".join(chars['wrongSpot']) + "\n")
        print("LETTERS NOT IN THE WORD: " + " ".join(chars['notIn']) + "\n")

    def win(self):
        print('YOU HAVE GUESSED THE WORD!')
        exit()

    def lose(self):
        print("YOU HAVE USED ALL OF YOUR GUESSES, YOU LOSE")
        print(self.wordleTargetWord)
    
    def runGame(self):
        for x in range(5):
            word = self.inputted()
            print("\n" + word + "\n")
            check = self.afterValidation(word)
            if check:
                self.win()
            else:
                self.pattern(word)
        self.lose()

    def getTargetWord(self):
        return self.wordleTargetWord



