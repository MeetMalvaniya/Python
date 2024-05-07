t1=(56,67,78,89,90)
print(type(t1))
print(t1[1])
#t1[2]=5 # not allowed

t2=(2) #determine as integer
print(type(t2))
t3=(2,) #determine as tuple
print(type(t3))

t4=(1,2,3,1)
print(t4.index(2)) # return first occurence
print(t4.count(1)) # Count total occurence
