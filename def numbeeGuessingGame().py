
import random 

print("Number guessing game")

number = random.randint(1,9)

chances = 0

print("Guess a number(between1 and 9):")

while chances < 5:
             
    guess =int(input("Enter your guess:-"))


if guess == number :
  print  ("congratulation you won!!")
  

elif guess < number :
    print("yours guess was too low :Guessa number higher than ", guess)

else:
     print("your guesswas too high :guess a number lower than ",guess)

chances += 1

if  not chances <5 :
   print("you lose!! the number is",number)
