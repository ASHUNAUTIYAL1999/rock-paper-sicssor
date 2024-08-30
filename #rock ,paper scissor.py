#rock ,paper scissor 

import random 

def computer_output():
    choices = ['Rock', 'paper', 'scissor']
    computer=random.choice(choices)
    return computer


def user_input():
    print("Choices are - Rock ,paper scissor")
    user_choice=input("one of these choices")
    return user_choice

def comparing_input(user,computer):
    if user=="Rock":
        if computer=="Rock":
            return "tie"
        elif computer=="paper":
            return "computer wins"
        else:
            return "user wins"
    if user=="paper":
        if computer=="Rock":
            return "user wins"
        elif computer=="paper":
            return "tie"
        else:
            return "user lose"
    if user=="scissor":
        if computer=="Rock":
            return "you lost"
        elif computer=="paper":
            return "you win"
        else:
            return "tie"
                
def play():
        user=user_input()
        computer=computer_output()
        result=comparing_input(user,computer)
        print("computers choices was ", computer)
        print(result)
    
if __name__ == "__main__":
    play()