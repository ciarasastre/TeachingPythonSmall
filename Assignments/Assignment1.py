'''
This is the expected code for Assignment 1
'''

#My Variables for part 1
myName = "Sally Moher"
myAge = 16
myFavFood = "Spagetti"
myZodiac = "Gemini"
myHobby = "Horse Riding"

print("My name is " + myName)
print("My favourite hobby is " + myHobby)
print("I am a " + str(myAge) +" year old")
print("I\nlove\n" + myFavFood)

#My Variables for part 2
myAnswer = str("")
numOne = 1
numTwo = 2
numTemp = 0

print("\nBefore")
print(numOne)
print(numTwo)

numTemp = numOne
numOne = numTwo
numTwo = numTemp

print("\nAfter")
print(numOne)
print(numTwo)