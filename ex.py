def outer(func):
    def wrapper(*args, **kwargs):
        print("Good morning")
        func(*args, **kwargs)       ## main func call
        print("Good evening")
    return wrapper

@outer                  ## add = outer(add)
def add(a, b):
    print(a + b)

add(10, 20)         ## wrapper func call

'''
func --> main func
main func --> wrapper address
'''

@outer                  ## login = outer(login)
def login():
    print("login executing")

login()


















