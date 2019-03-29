from sys import argv

ex14.py, user_name = argv
prompt = '> '

print(f"Hi {user_name}, I'm the {script} script.") # the variables user_name and script are replaced with argv
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)
# f means formatting strings
print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""") # this shows that this string is adding the variables's values into the text