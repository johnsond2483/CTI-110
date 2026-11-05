# Cti-110
# LLMLab1
# Darion J
# 10/22/2026

# Create a simple python project using a Largely used AI model

import random


import random

print("==========================")
print("     ADDITION QUIZ")
print("==========================")

# Keep the game running
while True:

    # Generate two random numbers
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)

    # Calculate the correct answer
    correct_answer = num1 + num2

    # Ask the player
    print("\nWhat is the answer to:")
    print(num1, "+", num2)

    player_answer = int(input("Your answer: "))

    # Check the answer
    if player_answer == correct_answer:
        print("Correct! Great job!")
    else:
        print("Sorry, that's incorrect!")
        print("The correct answer is:", correct_answer)

    # Ask if the player wants to play again
    play_again = input("\nDo you want to play again? (yes/no): ")

    if play_again.lower() == "yes":
        print("\nLet's play again!")
    else:
        print("\nThanks for playing!")
        break


#questions:
#Was the generated code correct and complete?
#What parts did you have to fix or improve?
#How would you rephrase your prompt to get better results?
#What are the benefits and risks of using AI for coding?

# Yes all of the code that the AI generated was running very perfectly and it was almost 100% complete the first time I ran it.
# Although the code did run almost perfectly, it didnt give me what I wanted, which was a replayability option. So the second time I had to run it, I asked it to give the user and option to answer another question
# If I had to rephrase this prompt I would most likely ask it to make it into an actual quiz with a grade and multiple questions.
# The benefits is that it gives a lot of helpful ways to use its knowledge and can solve a lot of problems you may create for youself.
# The risks is that it can replace the way you think of coding and start to abuse it, also it can give false information sometimes as it only knows as much as you tell and as much as it knows, meaning to get what you want you have to be more specific.