import random
PlayerName = "Bryan"
question = "Will I win the lottery" 

random_number = random.randint(1,12)
print(random_number)
if random_number == 1:
  eightBall = "Yes - definitely."
elif random_number == 2:
  eightBall = " It is decidedly so."
elif random_number == 3:
  eightBall = " Without a doubt."
elif random_number == 4:
  eightBall = " Reply hazy, try again."
elif random_number == 5:
  eightBall = "Reply hazy, try again."
elif random_number == 6:
  eightBall = "Better not tell you now."
elif random_number == 7:
  eightBall = "My source say no."
elif random_number == 8:
  eightBall = "Outlook not so good."
elif random_number == 9:
  eightBall = "Very doubtful."
elif random_number == 10:
  eightBall = "You are very lucky."
elif random_number == 11:
  eightBall = "You are not very lucky."
elif random_number == 12:
  eightBall = "You will die in 5 day."
else: 
  eightBall = "Error"

print( PlayerName + " asks: " + question)

print("Magic 8-Ball's answer: " + eightBall)