def add(a, b): # lines 1 to 15 help the computer to do the math by saying 'return' as the answer to the math problem itself
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b


print("Let's do some math with just functions!")
# these 4 lines are being used by the computer to do the math
age = add(7, 8)
height = subtract(67, 4)
weight = multiply(55, 2)
iq = divide(100, 2)
# this line will use the answers from the numbers above and add it to this string
print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")


# a puzzle for the extra credit, type it in anyway
print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")