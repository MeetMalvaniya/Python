coll={1,2,3,4,5}
print(coll)
print(type(coll))

s1={1,1,2,3,"hi","hi"}
print(s1) #ignre duplicate values

s2=set()
s2.add(1)
s2.add(2)
s2.add(3)

print(s2)
s2.remove(1)
print(s2)
s2.pop()
print(s2)

s4={1,2,3}
s5={3,4,5,6}
print(s4.union(s5)) # return combine values
print(s4.intersection(s5)) #returm common values

s6={"python","java","c++","python","javascript","java","python","java","c++","c"}
print(len(s6))

x=float(9.0)
s7={9,x}
print(s7)