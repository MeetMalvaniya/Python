"""marks=[98,89,78,86,90]
print(len(marks))
print(marks[2])

student=["meet",20,93,"surat"]
print(student)
student[2]=96
print(student)

#list slicing

list1=[45,56,67,78,89]
print(list1[0:3])
print(list1[0:])
print(list1[:4])
print(list1[-3:-1])

#Methods

list2=[3,2,1]
list2.append(4)
print(list2)
list2.sort()
print(list2)
list2.sort(reverse=True)
print(list2)
list2.reverse()
print(list2)
list2.insert(1,5)
print(list2)
list2.remove(1) #here 1 is value
print(list2)
list2.pop(3) # here 3 is index
print(list2)


#enter 3 movies name and store in list

movies=[]
movies.append(input("Enter Movie 1 :"))
movies.append(input("Enter Movie 2 :"))
movies.append(input("Enter Movie 3 :"))
print(movies)"""

#check palingdrom or not

pal=[1,2,3,2,1]
copy=pal.copy()
copy.reverse()
if(copy==pal):
    print("Palingdrom")
else:
    print("Not Palingdrom")