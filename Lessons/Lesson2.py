'''
In this example you will be presented with two choices
using pythons if(): elif(): and else(): function.

The user will reply with pythons input() function
'''

#My Variables
myAnswer = str()
myName = ""
myNumber = 0

#print("num pls")
#myNumber = input()
#print("your number is" + myNumber)

print("What is your name?")
myName = input()
print("Hello " + myName)

print("Do you like programming in Python? Answer yes/no.")

myAnswer = input()

# Now to reply based off choices
if (myAnswer == "yes"):
    print("Yes? Thats great!")

elif (myAnswer == "no"):
    print("No? But you are so good at it!")

else:
    print(
        "That wasnt a yes or a no!\nCould you restart and answer with yes or no?"
    )
'''
Have extra time?
Write a program that takes the users input
and replys if it is higher/lower or the same as 5.

Other useful operators are
==
!=
>
<

'''

print("Enter in a number")
myNumber = int(input())

if (myNumber < 5):
    print("Your number is less than five")

elif (myNumber > 5):
    print("Your number is greater than five")

elif (myNumber == 5):
    print("Your number is 5")


'''
myName = str("Sastre")
elif(myNumber == 5 and myName == "Sastre"):
  print("Your number is 5")
'''
