def cheese_and_crackers(cheese_count, boxes_of_crackers): # the cheese_count and boxes_of crackers are bieng replaced by the numbers 20 and 30
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket. \n")

# lines 2 and 3 are adding the numbers 20 and 30 into the variables' places
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)


print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# these lines are using the numbers from upper lines to do the math
print("We can do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

# these lines are combining the variables and math
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)