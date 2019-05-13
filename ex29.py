people = 20
cats = 30
dogs = 15
# the numbers help the computer know how to respond even though the print has what the computer to say

if people < cats:
    print("Too many cats! The world is doomed!")

if people > cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:
    print("The world is dry!")
# like in line 4, the computer is helped out with what to say

dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")
    
if people <= dogs:
    print("People are less than or equal to dogs.")


if people == dogs:
    print("People are dogs.")
# here the computer is being told that people are either equal, less than or greater than dogs    