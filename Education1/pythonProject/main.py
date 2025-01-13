people = "ребятишки"
count = 25

a = 2

while a < count:
    a += 1
    if a < 10:
        print("Дорова "  +  people + ". вас",  a)
    elif a > 20:
        print("Привет "  +  people + ". вас",  a)

def dorovaFunc(x:int):
    print("cifra", x)

def getAge(a:int):
    a += 5
    return a

length1 = 3
for x in range(length1):
    print("----------------------------")
    for x2 in range(3):
        dorovaFunc(x*length1+x2)

ageString = "10"
b = getAge(int(ageString))
dorovaFunc(b)

def decorator(input_function):
    def out_func():
        print("dorova")
        input_function()
        print("______________poka")
    return out_func()

@decorator
def go_go():
    print(1)

@decorator
def go_go1():
    print(2)

@decorator
def go_go2():
    print(3)

go_go()
go_go1()
go_go2()

