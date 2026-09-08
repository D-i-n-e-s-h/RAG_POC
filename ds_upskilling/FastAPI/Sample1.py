
def IsPalindrome(value):
    return value == value[::1];
##
a = 3
for i in range(a):
    print(i)
##
print(IsPalindrome("Madam") , "it is palindrome")
##
if True == True:
  print("True is always true")
##  Generators

def logger(func):
    def wrapper():
        print("Function started")
        func()
        print("Function ended")
    return wrapper

@logger
def greet():
    print("Hello")

greet()
