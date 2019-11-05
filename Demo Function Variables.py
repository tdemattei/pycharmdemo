
def update(lst):
    print(id(lst))
    lst[1] = 8
    print("x ", lst)

lst = [10, 20, 30]
print(id(lst))
update(lst)
print("a ", lst)

