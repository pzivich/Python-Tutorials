##########################################################
# Magic 8-ball that 'thinks' and sometimes gets bored
#
# Paul Zivich 2019/8/2
##########################################################

import random
import time


def magic_8_ball(delay=1):
    # Set of potential responses to draw from (makes experiences with the 8-ball different)
    questions = ["What is your question: ", "Ask your question to the all knowing: ", "What would you like to know: ",
                 "How can the magic-8 ball help: ", "Ask your question to the Wise One: "]
    think1 = ["Hmmm now let me see...", "Processing...", "Curious...", "Let me search the realm of possibilities...",
              "Peering beyond the veil of reality...", "Hmmmmmm..."]
    think2 = ["Interesting... the answer is becoming clear...", "Could it be?...", "I'm seeing something...",
              "I see...", "Ahh....", "It couldn't be..."]
    answers = ["Not so sure", "42", "Most likely", "Absolutely not", "Outlook is good", "I see good things happening",
               "Never", "Negative", "Could be", "Unclear, ask again", "Yes", "No", "Possible, but not probable"]

    # Asking user for the question
    question = input(random.choice(questions))

    # Thinking-phase of magic-8-ball
    print(random.choice(think1))
    time.sleep(delay)  # "Thinking" delay
    print(random.choice(think2))
    time.sleep(delay)  # "Thinking" delay

    # Providing the answer
    print("The answer is:", random.choice(answers))


# Calling function for initial 8-ball 'shake'
magic_8_ball()

# Creating a counter for how many questions have been asked
qcount = 1

# Asking user if they would like to ask another question
qfollowup = (input("Would you like to ask the Wise One another question? Y/N: "))

while qfollowup.upper() == str("Y"):
    # Answering question again
    magic_8_ball()
    qcount += 1  # Adding to the number of questions asked
    # Deciding if magic-8-ball gets bored of the questions
    if random.uniform(0, 1) > 0.03 * qcount**1.5:  # More questions the more likely magic-8-ball becomes bored
        qfollowup = (input("Would you like to ask the Wise One another question? Y/N: "))
    else:
        # Magic-8-ball is bored, so it ends the program
        qfollowup = 'n'
        print("The magic-8 ball is tired of your questions. Goodbye!")
