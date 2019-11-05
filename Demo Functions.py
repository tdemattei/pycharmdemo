
def greet():
    print("Hello")
    print("Good Morning")

def add_sub(x, y):
    c = x + y
    d = x - y
    return c, d

result1, result2 = add_sub(5, 4)

if result1 >= 10:
    print(result1)
else:
    print(result2)
