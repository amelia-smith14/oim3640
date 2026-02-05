for i in range(1, 6, 2):
    print(i)

name= "Amelia"
print(name*3)
print(name + "3")

a=5
#int is immutable
a = [1, 2, 3]
#list is mutable
print(a)
a.append(4)
print(a)
#add to list

"""
🧱🧱🧱
🧱🧱🧱
🧱🧱🧱
"""

def draw_square(size):
    for i in range(size):
        print("🧱"*size)

draw_square(3)

def draw_triangle(size):
    for i in range(size):
        print("🧱" * (i+1))

draw_triangle(4)

def draw_righttriangle(size):
    for i in range(size):
        print(" " * (size-i-1), "#" * (i+1))

draw_righttriangle(4)

def draw_pyramid(size):
    for i in range(size):
        print(" " * (size - i - 1)), print ("#" * (i+1)), print(" " * (size - i - 1))

draw_pyramid(5)