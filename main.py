import random

l = ["rock", "scissor", "paper"]

while True:
    ccount = 0
    ucount = 0
    uc = int(input('''
    Game start....
    1. Yes
    2. No | Exit
    '''))

    if uc == 1:
        for a in range(1, 6):
            userInput = int(input(  # Triple quotes used to allow multiline input
                '''
            1. Rock
            2. Scissor
            3. Paper
            Enter your choice: '''
            ))

            if userInput == 1:
                uchoice = "rock"
            elif userInput == 2:
                uchoice = "scissor"
            elif userInput == 3:
                uchoice = "paper"
            else:
                print("Invalid input")
                continue  # Skip this round

            cchoice = random.choice(l)  # ✅ Always generate computer's choice after valid input

            print("User choice: ---", uchoice)
            print("Computer choice: ---", cchoice)

            if cchoice == uchoice:
                print("Result: Game Draw")
                ucount += 1
                ccount += 1
            elif (uchoice == "rock" and cchoice == "scissor") or \
                    (uchoice == "paper" and cchoice == "rock") or \
                    (uchoice == "scissor" and cchoice == "paper"):
                print("Result: You win this round!")
                ucount += 1
            else:
                print("Result: Computer wins this round!")
                ccount += 1

        # Final game result after 5 rounds
        print("\nFinal Score after 5 rounds:")
        print("Your Score:", ucount)
        print("Computer Score:", ccount)

        if ucount > ccount:
            print("🎉 You won the game!")
        elif ccount > ucount:
            print("😞 Computer won the game!")
        else:
            print("😐 The game is a draw!")

    else:
        print("Thanks for playing!")
        break

