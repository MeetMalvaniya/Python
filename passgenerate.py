import random
import string

pass_len=int(input("Enter pass len :"))
char=string.ascii_lowercase + string.ascii_uppercase +string.punctuation
password = ""
for i in range(pass_len):
    password += random.choice(char)
print(password)

# List compherension used for multiple time call fun
# [function for i in range(n)]

res = "".join([random.choice(char) for i in range(pass_len)]) #used to concat string
print(res)