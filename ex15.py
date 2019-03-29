from sys import argv
# script is the ex15.py and the filename is ex15_sample.txt
script, filename = argv

txt = open(filename)
# the filename is replaced by ex15_sample.txt
print(f"Here's your file {filename}:")
print(txt.read()) # the txt.read tells the computer to print what ex15_sample.txt says
# thi tells the computer to print ex15_sample.txt says again
print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())