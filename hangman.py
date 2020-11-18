import random
word= ['python', 'java', 'kotlin', 'javascript']
n = random.randint(0,len(word)-1)
words = word[n]
heard = 0
i = len(words)
print(i)
while heard < 8 :
        inpy = input("input a letter: > ")
        if inpy in  words :
                print("df")
        elif inpy not in words :
                 print("No such letter in the word ")
                 heard +=1



