import random
import time
def unscramble(list_of_words):    
    max = len(list_of_words)    
    l = list(range(0, max))    
    random.shuffle(l)

    for i in range(len(list_of_words)):
        print("Guess the word: ", end='')
        index=l.pop()
        word = list_of_words[index]
        word=''.join(random.sample(word,len(word)))
        print(word)
        for i in range(1,11):
            time.sleep(1)
        print(list_of_words[index])        

text_file = open("1000_Words.txt", "r")
lines = text_file.read().split('\n')
print(lines)
list_of_words = ["ability","able","about","above","accept","according","account","across"]    
unscramble(list_of_words)
