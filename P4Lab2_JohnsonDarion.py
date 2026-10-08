# Cti-110
# 
# 10/8/26
# Darion J

# warmups
"""
for count in (1, 2, 3, 4):
    print (number)
for number in range(5):
    print(number)
for beer in range(99,0, -1):
    print(beer,"bottles of beer on the wall.")
# counting loop
print("7's times tables:")
for mult in range(1,13):
    print (7 * mult)
"""

# Set up variables
# START THE MAIN LOOP
again = "yes"
while again == "yes":
    # Ask the user for their chosen integer (0-12)
    multiplier = int(input("Enter a number 0-12: "))
    # validate (loop) - number must be between 0 and 12
    while multiplier < 0 or multiplier > 12:
        print("That is not valid answer.")
        multiplier = int(input("Enter a number 0-12: "))

    # print the times table header
    print("Multiplication Table")
    print("-"*20)
    # print the times table (loop)
    for number in range (1, 13):
        # print (multiplier, "*", number, "=" number*multiplier)
        print(f"{multiplier} * {number} = {number * multiplier}")
    # Finally, ask if they want to repeat
    again = input("Run again? (yes/no) ")

# outside the loop
print()
print("Exciting program...")