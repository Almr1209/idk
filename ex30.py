people = 30
cars = 40
trucks = 15
# this is like exercise 29; therefore, I will not explain.

if cars < people:
    print("We should take the cars.")
elif cars <people:
    print("We should not take the cars.")
else:
    print("We can't decide.")
# I have no clue what an elif is so don't ask. I think it's just a combination of the words else and if    
if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's just stay home then.")
# I believe elif and else are telling the computer to show this or that.
# I mean if you look at the book, his says, "We should take the cars. Maybe we could take the trucks. Alright, let's just take the trucks."
# Maybe these commands tell the computer to chose what to show then show it.