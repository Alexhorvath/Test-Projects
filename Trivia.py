import time

#Asking user input for anwser
print("Who is the artist for the song: Billie Jean?")
user_anwser = input()
anwser = "Michael Jackson"

if user_anwser == anwser:
    print(user_anwser + " was the correct anwser!")
else:
    print("Sorry, " + user_anwser + " isn't the right anwser. Try again")
    time.sleep(5)