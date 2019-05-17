i = 0
numbers = []

while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i)
    
    i = i + 1
    print("Numbers now: ", numbers)
    print(f"Ar the bottom i is {i}")
    

print("The numbers: ")

for num in numbers:
    print(num)
# I explained this already in my Google Doc, but I'll explain again
# while-loop is acting as an if-statement, so it'll repeat until the expression is False