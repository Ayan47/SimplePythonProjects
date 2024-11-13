# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import random
def tryAgain():
    choice = input("Would you like to try again? ==>").lower()
    if "y" in choice:
        game()
    else:
        print("Thank you for your time")
        return


def randomNumberGenerator():
    return random.randrange(1,11)

def game():
    print("")
    computersChoice = randomNumberGenerator()
    N = 5
    for i in range(0,N):
        print("Remember, you get ",N-i," more choices")
        print("=====================================================")
        yourChoice = input("Choose a Number between 1 and 10 and let's see if it matches the Computer's choice as well: ")
        print("")
        
        if(not yourChoice.isdigit()):
            cussItOut = ["Enter A FUCKING NUMBER!!", "Are you an Idiot? You don't know what a Number is?", "Can you read you clown? You're a pathetic waste of semen!", "What did you enter? What are you blind?? JEEZUZ!!!", "My God! You're a dissapointment!"]

            print(random.choice(cussItOut))
            print("")
        elif(int(yourChoice)<1 or int(yourChoice)>10):
            cussItOutAgain = ["Are you a retard? You were supposed to choose between 1 and 10, I deduct a point for this!!!", "JESUS!!! You dickhead, you chose this? Haven't I wrote the rules enough?", "My God! You have to be the dumbest motherfucker in town!", "No, No, That's not how it works, you gotta read this shit", "I didn't know you have ADHD! Your attention span is weaker than a sloth, and it's an insult to a sloth!"]

            print(random.choice(cussItOutAgain))
            print("")
        else:
            yourChoice=int(yourChoice)
            if yourChoice == computersChoice:
                print("Ding! Ding! Ding!...You chose the right Number!!! ", yourChoice, " was absolutely correct!!!!!!")
                tryAgain()
                return
            elif yourChoice > computersChoice:
                print("Maybe a little lower")
                print("")
            else:
                print("Maybe a little higher")
                print("")
    print("Badd-Tmm-Tiss!!")
    print("Awwww!!! you're out of turns now!")
    tryAgain()

print("Welcome to the Number Choosing Game!!")
game()



    
    
        
        
    
