from wonderwords import RandomWord
print("Welcome To Hangman")
print("By Connor Davis")
random = RandomWord()
word = "testtesttesttesttesttesttesttesttest"
currentword = ''
hangmanart = [
'''
Letters Wrong: 0
_________
|        |
|        |
|       
|        
|
|
|
|
|
|
|
''',
'''
Letters Wrong: 1
_________
|        |
|        |
|       (0)
|        
|
|
|
|
|
|
|
''',
'''
Letters Wrong: 2
_________
|        |
|        |
|       (0)
|      #####
|      #####
|      #####
|      #####
|
|
|
|
''',
'''
Letters Wrong: 3
_________
|        |
|        |
|       (0)
|     |#####
|     |#####
|     |#####
|      #####
|
|
|
|
''',
'''
Letters Wrong: 4
_________
|        |
|        |
|       (0)
|     |#####|
|     |#####|
|     |#####|
|      #####
|
|
|
|
''',
'''
Letters Wrong: 5
_________
|        |
|        |
|       (0)
|     |#####|
|     |#####|
|     |#####|
|      #####
|      |
|      |
|      |
|
''',
'''
Letters Wrong: 6
_________
|        |
|        |
|       (0)
|     |#####|
|     |#####|
|     |#####|  
|      #####
|      |   |
|      |   |
|      |   |
|
'''
]
try:
    while True:
        def get_uinput():
            while True:
                try:
                    uinput = str(input("Letter: "))
                    if len(uinput) == 1:
                        break
                    else:
                        print("Please Enter 1 Letter!")
                except ValueError:
                    print("Please Enter A Letter!")
            return(uinput)   


            
        while True:
            try:
                wordlen = int(input("Length Of Word [2-15]: "))
                if wordlen < 2:
                    wordlen = 2
                elif wordlen > 15:
                    wordlen = 15
                break
            except ValueError:
                print("You Did Not Enter A Number!")

        print("Generating Word, Please Wait.")
        word = random.word(word_min_length=wordlen, word_max_length=wordlen)
        word = word.lower()

        for num in range(wordlen):
            currentword = currentword + "_"
        num = 0
        wordswrong = 0
        while True:
            print(hangmanart[wordswrong])
            print(currentword)
            workinguinput = get_uinput()
            bdcurrentword = list(currentword)
            bdword = list(word)
            loops = 0
            prevcurrentword = currentword
            for letter in bdword:
                if letter == workinguinput:
                    bdcurrentword[loops] = workinguinput
                loops += 1
            currentword = ''.join(bdcurrentword)
            if prevcurrentword == currentword:
                wordswrong += 1
            if wordswrong == 6:
                print(hangmanart[6])
                print("Thank You For Playing!")
                print(f"The Word Was {word}")
                print(f"The Word Length Was {wordlen}")
                print("I Hope You Will Get It Next Time!")
                input("Press Enter To Exit!")
                break
            if word == currentword:
                print("Congrats! You Won!!!!!!")
                print("Thank You For Playing!")
                print(f"The Word Was {word}")
                print(f"You Guessed {wordswrong} Letters Wrong!")
                print(f"The Word Length Was {wordlen}")
                input("Press Enter To Exit!")
                break
        break
                        
except KeyboardInterrupt:
    print("\nYou Have Quited!")
    try:
        input("Press Enter To Exit!")
    except KeyboardInterrupt:
        pass
