import random
import os
from sys import platform

# sets up terminal clear
if(platform == "win32"):    # for windows
    clear = lambda: os.system('cls')
elif platform == "darwin":  # for mac
    clear = lambda: os.system('clear')

clear()

Magic8BallResponses = [
    "It is certain.",
    "It is decidedly so.",
    "Without a doubt.",
    "Yes definitely.",
    "You may rely on it.",
    "As I see it, yes.",
    "Most likely.",
    "Outlook good.",
    "Yes.",
    "Signs point to yes.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
    "Don't count on it.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful."
]

question = input("Consult the Magic 8 Ball: ")

clear()

print("QUESTION: " + question + ("" if question.endswith("?") else "?"))

print("ANSWER: " + Magic8BallResponses[random.randint(1,len(Magic8BallResponses))] + "\n")