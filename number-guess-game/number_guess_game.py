import random
import math

lower = int(input("Enter the Lowest number: "))
upper = int(input("Enter the Upper number: "))

x = random.randint(lower, upper)
print(
    "\n\tYou have only ",
    round(math.log(upper - lower + 1, 2)),
    " Chances to guess the integer!\n",
)
count = 0

while count < math.log(upper - lower + 1, 2):
    count += 1
    guess = int(input("Guess a numebr: "))
    if x == guess:
        print("Congratulations! You did it.",
              count, "try")
        break
    elif x < guess:
        print("Your guess is to High!")
    elif x > guess:
        print("Your guess is too Low!")

    if count >= math.log(upper - lower + 1, 2):
        print("\nThe number is %d" % x)
        print("\tBetter Luck Next time!") 

