import random

# variables
computer_score = 0
your_score = 0
break_score = 0

while True:
    # stop program
    if break_score == 1:
        break
    # input for your number
    computer_num = random.randint(1, 5)
    your_num = int(input("Enter a number between 1 and 5: "))

    while True:
        if your_num in range(1, 6):
            # check if someone has won
            if computer_score - your_score >= 11:
                print("computer wins")
                break_score += 1
                break
            elif your_score - computer_score >= 11:
                print("You win")
                break_score += 1
                break
            else:
                # check for undercut
                print("The computers number is", computer_num,)
                if computer_num - your_num == 1:
                    your_score += computer_num
                    print("You undercut the computer")
                    print("Your score is", your_score, "The computers score is", computer_score, )
                    break
                elif your_num - computer_num == 1:
                    computer_score += your_num
                    print("The computer undercut you")
                    print("Your score is", your_score, "The computers score is", computer_score, )
                    break
                else:
                    # number check and adding
                    if computer_num > your_num:
                        computer_score += (computer_num - your_num)
                        print("Your score is", your_score, "The computers score is", computer_score,)
                        break
                    elif your_num > computer_num:
                        your_score += (your_num - computer_num)
                        print("Your score is", your_score, "The computers score is", computer_score, )
                        break
        else:
            print("PICK A NUMBER BETWEEN 1 AND 5: ")
            your_num = int(input("Enter a number between 1 and 5: "))
