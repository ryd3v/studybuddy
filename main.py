# Program: Study Buddy
# Author: R.
# Original creation date: 2020-12-19
# Version: Final
# Updated: 2020-12-31
#!/usr/bin/env python3
import random
import time
import subprocess as s

def countdown(mins, secs=0):
    t = (mins*60) + secs
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

print("Let's Study!"),
print("The topics are:\n"),
study_topics = ["Books[1]", "Cyber Security[2]", "Programming[3]"]

for topic in study_topics:
    print(topic)
    print()
question = input("Select topic: ")

if question == "1":
    books = []
    with open("books.txt", "r") as f:
        books = f.readlines()
        print("How about?:", random.choice(books)),

elif question == "2":
    cybersecurity = []
    with open("cybersecurity.txt", "r") as f:
        cybersecurity = f.readlines()
        print("How about?:", random.choice(cybersecurity)),

elif question == "3":
    programming = []
    with open("programming.txt", "r") as f:
        programming = f.readlines()
        print("How about?:", random.choice(programming)),

else:
    print("Topic entered not in the list!")
    print("Goodbye")
    exit()

input("Press Enter to Start timer")
countdown(30),
s.call(['notify-send','Well done!, Have a Great Day!']),print('\a')
