#Практическая работа №1 Мартынов Н.А.
import math
def calculator(a):
    match a:
        case "Сложение": 
            result=Sum1+Sum2
            return result
        case "Вычитание": 
            result=Sub1-Sub2
            return result
        case "Умножение":
            result=Mul1*Mul2
            return result
        case "Деление":
            result=Div1/Div2
            return result
        case "Степень" :
            result=NumD**Deg
            return result
        case "Квадратный корень":
            result=math.sqrt(NumR)
            return result
        case "Факториал":
            result=math.factorial(NumF)
            return result
        case "Синус":
            result=math.sin(NumS)
            return result
        case "Конус":
            result=math.cos(NumC)
            return result
        case "Тангенс": 
            result=math.tan(NumT)
            return result

stop=True
while stop==True :
    print("Введите наименование операции из приведенного ниже списка,которую вы хотите выполнить (Ввод производится с учётом регистра) \n Сложение  \n Вычитание \n Умножение \n Деление \n Степень \n Квадратный корень \n Факториал \n Синус  \n Косинус \n Тангенс \n Завершить работу ")
    a=input()
    match a:
        case "Сложение": 
            test=True
            while test==True :
                try:
                    Sum1=float(input("Введите первое слагаемое "))
                    Sum2=float(input("Введите второе слагаемое "))
                except Exception:
                    print("Введите целое или вещественное число ")
                else:
                    SumTotal=calculator(a)
                    print("Результат: ",SumTotal)
                    test=False 
        case "Вычитание": 
            test1=True
            while test1==True :
                try:
                    Sub1=float(input("Введите уменьшаемое "))
                    Sub2=float(input("Введите вычитаемое "))
                except Exception:
                    print("Введите целое или вещественное число ")
                else:
                    SubTotal=calculator(a)
                    print("Результат: ",SubTotal)
                    test1=False
        case "Умножение":
            test2=True
            while test2==True :
                try:
                    Mul1=float(input("Введите первый множитель "))
                    Mul2=float(input("Введите второй множитель "))
                except Exception:
                    print("Введите целое или вещественное число ")
                else:
                    MulTotal=calculator(a)
                    print("Результат: ",MulTotal)
                    test2=False
        case "Деление":
            test3=True
            while test3==True :
                try:
                    Div1=float(input("Введите делимое  "))
                    Div2=float(input("Введите делитель "))
                except Exception:
                    print("Введите целое или вещественное число")
                else:
                    if Div2==0 :
                        print("деление на 0 невозможно")
                    else:
                        DivTotal=calculator(a)
                        print("Результат: ",DivTotal)
                        test3=False
        case "Степень" :
            test4=True
            while test4==True :
                try:
                    NumD=float(input("Введите число возводимое в степнь  "))
                    Deg=float(input("Введите показатель степни  "))
                except Exception:
                    print("Введите целое или вещественное число ")
                else:
                    DegNum=calculator(a)
                    print(DegNum)
                    test4=False
        case "Квадратный корень":
            test5=True
            while test5==True :
                try:
                    NumR=float(input("Введите число из которого тербуеся извлечь квадратный корень  "))
                except Exception:
                    print("Введите целое или вещественное число ")
                else:
                    if NumR < 0 :
                        print("Подкоренное выражение не может быть отрицательным")
                    else:
                        Root=calculator(a)
                        print("Результат: ",Root)
                        test5=False
        case "Факториал":
            test6=True
            while test6==True :
                try:
                    NumF=int(input("Введите число ,факториал которого требуется вычислить   "))
                except Exception:
                    print("Введите целое число ")
                else:
                    if NumF < 0 :
                        print("Факториала отрицательных чисел не существует")
                    else:
                        Fac=calculator(a)
                        print(Fac)
                        test6=False
        case "Синус":
            test7=True
            while test7==True :
                try:
                    NumS=float(input("Введите угол(в радианах) синус из которого требуется вычислить  "))
                except Exception:
                    print("Введите целое или вещественное число ")
                else:
                    Sin=calculator(a)
                    print("Результат: ",Sin)
                    test7=False
        case "Косинус":
            test8=True
            while test8==True :
                try:
                    NumC=float(input("Введите угол(в радианах) косинус из которого требуется вычислить  "))
                except Exception:
                    print("Введите целое или вещественное число ")
                else:
                    Cos=calculator(a)
                    print("Результат: ",Cos)
                    test8=False
        case "Тангенс":
            test9=True
            while test9==True :
                try:
                    NumT=float(input("Введите угол(в радианах) тангенс из которого требуется вычислить  "))
                except Exception:
                    print("Введите целое или вещественное число ")
                else:
                    Tan=calculator(a)
                    print("Результат: ",Tan)
                    test9=False
        case "Завершить работу":
            stop=False
        case _:
            print("Вы ввели некорректное значение")
