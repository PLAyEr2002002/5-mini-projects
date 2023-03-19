print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    print("aww , ok some other time then ")
    quit()
    
print("Okay! Let's play :)")
score = 0

name= input('What is your name? ')

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct! you got it right, ' + name)
    score += 1
else:
    print("Incorrect! :( Try again, " +name)
    
answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('Correct! you got it right, ' + name)
    score += 1
else:
    print("Incorrect! :( Try again, " +name)

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct! you got it right, ' + name)
    score += 1
else:
    print("Incorrect! :( Try again, " +name)

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print('Correct! you got it right, ' + name)
    score += 1
else:
    print("Incorrect! :( Try again, " +name)
    
print("You got " + str(score) + " questions correct!")