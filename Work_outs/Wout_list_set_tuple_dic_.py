def otr1():
    numbers=[]
    N=int(input())
    for i in range (0 , N):
        a=int(input())
        numbers.append(a)
    numbers.sort
    print(numbers[-1],numbers[0])

def otr2():
    words=["ум","придаток","вирус"]
    words.sort


def otr3():
    students={"Петров":5 , "Иванов":3 , "Галкина" : 4 , "Полижайкина":2}
    corteges=students.items

def otr4():
    txt=input()
    uniq=set(txt.split())
    print (uniq)

def otr5():
    fruits={"яблоко","помидор", "лимон"}
    fruits1={"лимон","манго","памело"}
    result=fruits.intersection(fruits1)

def otr6():
    employees=["Дмитрий Иванович","Константин Вятчесловович","Сергей Губин"]
    del employees[1]
    employees.append("Соня Галкина")
    print(employees)
    
