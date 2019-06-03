# peer programming by: Faith Pham and Allana Richardson
from sys import exit

def room_1():
    print("Welcome to the 7 Rooms of Death, where you will die unless you solve all our riddles.")
    print("To exit this room please solve the riddle before you.")
    answer = "hermes"
    print("You: ECOJCP <- (use lowercase), ? What does that even mean?")
    H = input("> ")
    if( answer == H ):
        print("You guessed correctly! Step into your next challenge.")
        print("Remember number 9.")
        print("You walk into the next room.")
        room_2()
    else:
        print("Incorrect. Now die please.")
        dead("You are killed by carbon poisoning.")

def dead(why):
    print(why, "Good job!")
    exit(0)
        
def room_2():
    print("Please solve this riddle.")
    answer2 = "calender"
    print("""You: No matter how little or how much you use me, you change me every month. What am I?
    I wonder what this is.""")
    C = input("> ")
    if ( answer2 == C ):
        print("Congrats! You made it to the next room. You don't die...yet.")
        print("Please remember this OTHER number 3.")
        print("You walk into the 3rd room.")
        room_3()
    
    else:
        print("Oh how unfortunate. That's incorrect. Now die.")
        dead("You get squashed by a giant grandfather clock. ")
        
def room_3():
    answer3 = "coffin"
    print("""You: Who makes it, but has no need for it? 
    Who buys it, but does not want it? Who uses it, but can neither see nor feel it?
    What am I?""")
    F = input("> ")
    if( answer3 == F ):
        print("Wonderful. That's correct. You get to live a little longer...sadly.")
        print("Remember this number which is 5.")
        print("You walk, well actuall run, into the next room.")
        room_4()
        
    else:
        print("Wrong. Time to die!")
        dead("You die because you are burried alive.")
        
def room_4():
    answer4 = "river"
    print("""You: What can run, but never walks? Has a mouth, but never talks?
    Has a head, but never weeps? Has a bed, but never sleeps? What am I?""")
    R = input("> ")
    if( answer4 == R ):
        print("Oh when are you ever going to lose? I just want to see you die.")
        print("Anyways, the next number to remember is 8.")
        print("You enter room 5.")
        room_5()
        
    else:
        print("YAY! FINALLY YOU ARE DEAD!")
        dead("Death by snake 'hug.'")
        
def room_5():
    answer5 = "Ragnarok"
    print("You: In Norse mythology, what is the doom of the gods called?")
    M = input("> ")
    if( answer5 == M ):
        print("Aw dang...I thought you would die.")
        print("Remembering number time! Chosen number: 3.")
        print("You walk into the next room.")
        room_6()
        
    else:
        print("Enjoy death.")
        dead("You are squashed by a giant version of Mjolnir.")
        
def room_6():
    answer6 = "water flows to the west"
    print("You: L'acqua scorre ad ovest. What?")
    print("Gotta love languages in Europe.")
    W = input("> ")
    if( answer6 == W ):
        print("DARN IT! I THOUGHT FOR SURE IT WOULD GET YOU!")
        print("Remember the number 2.")
        print("You walk into the last room.")
        room_7()
        
    else:
        print("Aw there was only one room left. OH well. Now perish.")
        dead("Poisonous gas fills the room.")
        
def room_7():
    answer7 = "935832"
    print("You: The heck! The room is flooding! I need to get out of here!")
    print("You run back to the door through you entered, and find it locked.")
    print("""Did I forget to tell you? You need to enter the pin number. Oh and the room will fill with water.
    Good luck.""")
    P = input("> ")
    if( answer7 == P ):
        print("DANG IT! GO TO HELL YOU NERD! GO LIVE YOUR PATHETIC LIFE!")
        print("You leave the room at once.")
    else:
        print("So clse yet so far.")
        dead("Die from drowning.")
room_1()

