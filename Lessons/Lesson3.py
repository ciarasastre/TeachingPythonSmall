stringData = str(3) #will be "3"
intData = int(3) #will be 3
floatData = float(3) #will be 3.0
zooAnimals = ["Seal", "Bear", "Penguin"]
A1, A2, A3 = zooAnimals
replyX = "great!" # global var
#globalKey = "Global"

#Printing out different data types
print(type(stringData))
print(type(intData))
print(type(floatData))

print(A1)
print(A2)
print(A3)

'''
New function to explain
how variables work regardless if inside or outside a function
'''

def myfunc():
  replyX = "fantastic!"
  #global = globalKey

  #globalKey = "Not Global"
  
  print("Programming is " + replyX) #This will use the local variable Fantastic
  print("My favourite animal is a " + A2)

myfunc()

print("Programming is so " + replyX) # This will use the global var Great!


