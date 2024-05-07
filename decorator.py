# def startend(fun):
#     def dec(*args,**kwargs):
#         print("start")
#         res=fun(*args,**kwargs)
#         print("end")
#         return res
#     return dec

# @startend
# def add(x):
#     return x+5 

# res=add(10)
# print(res)


# import functools

# def repeat(num):
#     def dec_repeat(fun):
#         @functools.wraps(fun)
#         def wrapper(*args,**kwargs):
#             for _ in range(num):
#                 result = fun(*args,**kwargs)
#             return result
#         return wrapper
#     return dec_repeat

# @repeat(num=5)
# def print1(name):
#     print(f"hello {name}")

# print1("meet")


def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1) # calculate all trirec from 1 to 4
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(4)
