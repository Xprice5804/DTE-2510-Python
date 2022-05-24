import random

# Generate a lottery with two digits
lottery = str(random.randint(0, 9)) + str(random.randint(0, 9))

# Prompt the user to enter a guess
guess = input("Enter your lottery pick (two digits): ")

print("The lottery number is", lottery)

# Check the guess
if guess == lottery:
    print("Exact match: you win $10,000")
elif guess[1] == lottery[0] and guess[0] == lottery[1]:
    print("Match all digits: you win $3,000")
elif guess[0] == lottery[0] or guess[0] == lottery[1] \
        or guess[1] == lottery[0] or guess[1] == lottery[1]:
    print("Match one digit: you win $1,000")
else:
    print("Sorry, no match")
