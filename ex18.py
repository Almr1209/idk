# this one is like your scripts with argv, this is just one way to run arguements
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# ok, that *args is actually pointless, we can just do this, this is another way
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# this just takes one argument, I was going to say that but you know
def print_one(arg1):
    print(f"arg1: {arg1}")

# this one takes no arguments
def print_none():
    print("I got nothin'.")

# these next lines replaces print_two, print_none, print_two_again, and print_one
print_two("Allana","Richardson")
print_two_again("Allana","Richardson")
print_one("First!")
print_none()