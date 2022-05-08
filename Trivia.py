import time

# Asking user input for answer
print("Who is the artist for the song: Billie Jean?")
user_answer = input()
answer = "Michael Jackson"

if user_answer == answer:
    print(user_answer + " was the correct answer!")
else:
    print("Sorry, " + user_answer + " isn't the right answer. Try again")
    time.sleep(5)


