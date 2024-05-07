import random

target = random.randint(1,100)
#print(target)

# guss = int(input("Enter Number :"))
# if(guss==target):
#     print("congrats you gess right")
# elif(guss>target):
#     print("Guess smaller Number")
# elif(guss<target):
#     print("Guess big Number")
# else:
#     print("Pls enter Number")

while True:
    userchoice=int(input("Enter no :"))
    if(userchoice==target):
        print("Congrats")
        break
    elif(userchoice>target):
        print("Choose Smaller")
    else:
        print("Choose Bigger")
     