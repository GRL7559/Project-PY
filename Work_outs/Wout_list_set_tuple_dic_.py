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
    print(words)


def otr3():
    vegetables  = {"Петров": 5, "Иванов": 3, "Галкина": 4, "Полижайкина": 2}
    corteges = []
    for student in vegetables.items():
        corteges.append(student)
    print(corteges)

def otr4():
    txt=input()
    uniq=set(txt.split())
    print (uniq)

def otr5():
    fruits={"яблоко","помидор", "лимон"}
    fruits1={"лимон","манго","памело"}
    result=fruits.intersection(fruits1)
    print(result)

def otr6():
    employees={"уволен":"Дмитрий Иванович" ,"уволен":"Константин Вятчесловович","действующий":"Сергей Губин"}
    del employees["уволен"]
    employees["стажировка"]="Соня Галкина"
    print(employees)
        
