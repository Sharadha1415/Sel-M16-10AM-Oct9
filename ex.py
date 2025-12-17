# def outer(func):
#     def wrapper(*args, **kwargs):
#         print("Good morning")
#         func(*args, **kwargs)       ## main func call
#         print("Good evening")
#     return wrapper
#
# @outer                  ## add = outer(add)
# def add(a, b):
#     print(a + b)
#
# add(10, 20)         ## wrapper func call
#
# '''
# func --> main func
# main func --> wrapper address
# '''
#
# @outer                  ## login = outer(login)
# def login():
#     print("login executing")
#
# login()

####################################################################


# num1 = 100              ## global var
#
# def sample():
#     num2 = 200          ## local var
#     num1 += 200
#     print(num1)
#     print(num2)
#
# sample()
#
# ## UnboundLocalError

#####################################################

# num1 = 100              ## global var
#
# def sample():
#     num2 = 200          ## local var
#     global num1
#     num1 += 200
#     print(num1)
#     print(num2)
#
# sample()

#####################################################

# a = 10              ## global
#
# def outer():
#     b = 20          ## local
#     def inner():
#         c = 30      ## local
#         nonlocal b
#         b += 10
#         print(b)
#     inner()
#
# outer()

#############################################################

#
# a = 10              ## global
#
# def outer():
#     b = 20          ## local
#     def inner():
#         c = 30      ## local
#         print(b)
#         print(a)
#         def wrapper():
#             d = 100
#             print(a, b, c)
#
























