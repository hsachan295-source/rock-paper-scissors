import random
l=["rock","scissor","paper"]

while True:
    ccount=0
    ucount=0
    uc=int(input('''
    Game start....
    1 yes
    2 No| Exist
    '''))
    if uc==1:
        for a in range(1,6):
            userInput=int(input( #''' ''' 3 tripal coma ish liye le ke chalte code kerne me problem na ho
                '''
            1. Rock
            2. scissor
            3.paper
            '''
            ))
            if userInput==1:
                uchoice="rock"
            elif userInput==2:
                uchoice="scissor"
            elif userInput==3:
                uchoice = "paper"
            else:
                print("Invalid input")
                continue



            cchoice=random.choice(l)


            if   cchoice == uchoice:
                    print("user choice:---", uchoice)
                    print("computer choice:---", cchoice)
                    print("Game Draw")

                    ucount=ucount+1
                    ccount=ccount+1
            elif (uchoice=="rock" and cchoice=="scissor") or \
                    (uchoice=="paper" and cchoice=="rock") or \
                    (uchoice=="scissor" and cchoice=="paper"):
                    print("user choice:---", uchoice)
                    print("computer choice:---", cchoice)
                    ucount+=1
                    print("you win")
            else:
                    ccount=ccount+1
                    print("computer win")

        if ucount==ccount:
            print("final game draw...")
            print("user score",ucount)
            print("computer score",ccount)
        elif ucount>ccount:
            print("user win the game..")
            print("user score",ucount)
            print("computer score",ccount)
        else:
            print("computer win the game..")
            print("user score", ucount)
            print("computer score", ccount)

    else:
     break
