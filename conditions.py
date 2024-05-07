light=input("light :")
if(light=="red"):
    print("Stop")
elif(light=="yellow"):
    print("Look")
elif(light=="green"):
    print("Go")
else:
    print("Light Broke")

food=input("Food :")
print("Sweet")if food=="jalebi" else print("Not Sweet")

age=int(input("age :"))
vote= ("yes","no") [ age <= 18 ]
print(vote)

#nesting

age=88
if(age>=18):
    if(age>=70):
        print("can't drive")
    else:
        print("drive")
else:
    print("can't drive")
 
#find odd even no

num=int(input("Enter No :"))
if(num % 2 == 0):
    print("even")
else:
    print("odd")

#find gretest no

no1=int(input("Enter No 1:"))
no2=int(input("Enter No 2:"))
no3=int(input("Enter No 3:"))

if(no1>no2 and no1>no3):
    print(no1,"is gretest")
elif(no2>no1 and no2>no3):
    print(no2,"is gretest")
else:
    print(no3,"is gretest")

# no is multiply by 7 or not

no=int(input("Enter No :"))
if(no % 7==0):
    print("Multiplied")
else:
    print("Can't Multiply")