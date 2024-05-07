student = {
    "name" : "meet",
    "age" : 20,
    "subject" : {
        "py" : 80,
        "dw" : 88,
        "and" : 90
    }
}
print(student)
print(student["subject"])
print(student["subject"]["and"])

#methods

print(student.keys())
print(student.values())
print(student.items())
print(student.get("age"))
print(student.update({"age" : 22}))
print(student)

#practice

dic = {"table" : ["a piece of forniture","list of fact and figures"],
       "cat":"a small animal "}
print(dic)

dic1={}

py =int(input("Enter py Marks :"))
android = int(input("Enter And Marks :"))
dataw = int(input("Enter dw Marks :"))

dic1.update({"python" : py})
dic1.update({"Android" : android})
dic1.update({"DW" : dataw})

print(dic1)