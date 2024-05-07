# s1="this is string 1"
# s2='this is string 2'
# s3="""this is string 3"""

# #ascape sequence char 
# #\n for new line
# #\t for tab

# s4=s1+" "+s2
# print(s4)
# print(len(s4))

# #indexing

# print(s4[3])

# #slicing
# #[Starting index : Ending index]

# s5="How are you"
# print(s5[1:6])
# print(s5[4:])
# print(s5[:4])#[0:4]

# #negative indexing starts with at the end of str with -1 index
# #ending index didn't count

# print(s5[-3:-1])

# #Functions

# s6="My name is Meet"
# print(s6.endswith("et")) # return true if str end with et

# print(s6.capitalize()) # capatalize first word

# print(s6.replace("is","are")) # replace word or char

# print(s6.find("e")) # find e and return first e's index value

# print(s6.count("e")) # count e word

defa="{} {} {}".format("today","is","sunday")
print(defa)

defa="{1} {0} {2}".format("today","is","sunday")
print(defa)