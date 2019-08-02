###################################################################################################################
# Problem Set 01: Logic, Loops, Functions
#
# Advice: if an error occurs and you aren't sure why, you can always comment out that code and try to fix it later
#         If you still can't figure it out, you can open an Issue on the GitHub page
###################################################################################################################

#############
# Question 1:
print('Question 1:')
# Review from previous. Add the missing mathematical operators to the dictionary object. Do this by creating new keys
#   and values (DON'T edit the dictionary directly). The dictionary should contain 7 key-value pairs
d = {'addition': '+',
     'subtraction': '-',
     'division': '/',
     'modulo': '%'}
# WRITE CODE BELOW

print(d)

#############
# Question 2:
print('\nQuestion 2:')
# Review from previous. For the following list of lists, print the second and third items from the fourth list
l = [[1],
     [2, 4],
     [3, 9, 12],
     [4, 8, 12, 16],
     [5, 10, 15, 20, 25],
     [6, 12, 18, 24, 30, 36]]
# WRITE CODE BELOW
print()

#############
# Question 3:
print('\nQuestion 3:')
# Below is some conditional logic code. For x=36, I would expect the logic to print 'x is divisible by 2 and 3' but
#   it doesn't. Fix the below code to print what is expected

x = 36

if x % 5 == 0:
    print("x is divisible by 5")
elif x % 2 == 0:
    print("x is divisible by 2 only")
elif x % 3 == 0:
    print("x is divisible by 3 only")
elif x % 2 == 0 and x % 3 == 0:
    print("x is divisible by 2 and 3")
else:
    print("x is NOT divisible by 2, 3, or 5")

#############
# Question 4:
print('\nQuestion 4:')
# Write a for loop that counts from 3 to 27 by 3's. Hint: remember the range() function

# WRITE CODE BELOW


#############
# Question 5:
print('\nQuestion 5:')
# Write a function that finds ax**2 + bx + c = 0 for inputs of a, b, c. If you still have numbers from your math class,
#   try out your function on those. Do they match?
#   If not try: a=5, b=10, c=0 and a=10, b=3, c=1

# WRITE CODE BELOW


#############
# Question 6:
print('\nQuestion 6:')
# For this question, we will use concepts learned from the magic-8-ball coding. It will use functions, logic, and loops.
# Create a dice-rolling program. The program should 'roll' a sided dice and tell the user what number was rolled and
# ask if they would like to roll again
#   Requirements: 1) write a function that 'rolls' a 6-sided die (remember lists and the random library)
#                 2) ask the user if they would like to roll a die
#                 3) after the die roll, it should ask the user if they would like to roll again
#                       a) if user wants to roll again, then repeat the process
#                       b) if not, the program should end

# BONUS CHALLENGE: Allow the dice function to have 2, 4, 6, 10, 12, 20, or 100 sides. The user can choose which to use
#       Have the function check that the number of sides corresponds to one of the above. If not, then the function
#           should say that option isn't available. You will need to add some extra logic
#           HINT: the following line would help to check if the input is valid `if sides in [2, 4, 6, 10, 12, 20, 100]:`

# WRITE CODE BELOW
