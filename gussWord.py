import random 

words= ['crazy', 'light', 'range', 'love']
count= 0

for word in words: 
    newWord= list(word)
    random.shuffle(newWord)
    scrambled = '-'.join(newWord)
    print('guess this word: ',scrambled)
    guess= input("write here : ")
    if guess== word:
        print("correct ! ")
        count+=1
    else : 
        print("wrong !")
        print("here is the correct: ", word)

if count >= int(len(words)/2): print(f"Your points are {count}/{len(words)}. You win!\n")
else: print("Your points are {count}/{len(words)}. You failed!\n")
