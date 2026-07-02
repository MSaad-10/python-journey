''' 
    - A function is a reusable block of code that performs a specific task. 
'''


# ===== Simple Example =====
def greet():
    print("Hello")

greet()


# ===== Function with Single Parameter =====
def show_name(name):
    print(f"Hello {name}")

name = input("Enter your name: ")
show_name(name)


# ===== Function with Return Value =====
def add(a, b):
    return a + b

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
print(f"Sum: {add(n1,n2)}")


# ===== Default Parameters =====
def greet_msg(name="Guest"):    # add default parameter at the end 
    print(f"Hello {name}!!")

greet_msg()
greet_msg("Saad")


# ===== Multiple Parameters =====
def show_info(name, age):
    print(f"Hello {name}!! You are {age} years old")

name = input("Enter your name: ")
age = int(input("Enter your age: "))
show_info(name,age)


# ===== Keyword Arguments =====
def key_info(age, name="Saad"): 
    print(f"Hello {name}!! your age is {age}")

key_info(18)


# ===== Local Variables =====
def test():
    x = 10   # cannot be used outside function
    print("Inside function:", x)

test()
# print("Outside function:", x)    ❌ ERROR


# ===== Alteration of Global & Local Variables =====
x = 5
def func():
    global x    
    x = 7   # changes made in global
    return x

print(x)      
print(func())    
print(x)    # 'x' chnaged after func() call