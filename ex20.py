from sys import argv

script, input_file = argv
# I'm guessing lines 4 to 12 are ignored, or they read something because of the command 'print'
def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline())
# this tells the computer to, I think, to use this in another line, or to ignore it
current_file = open(input_file)

print("First let's print the whole file:\n")
# this line tells the computer to show the current file on the screen
print_all(current_file)

print("Now let's rewind, kind of like a tape.")
# I believe rewind is just another variable that is being used, unless it's another command?
rewind(current_file)
# after this line, the current_line and other variables are combining sentances
print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
.0