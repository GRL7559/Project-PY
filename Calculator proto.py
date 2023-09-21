#Практическая работа №1 Мартынов Н.А.
import math

stop=0
while stop==0 :
    print("Введите наименование операции из приведенного ниже списка,которую вы хотите выполнить (Ввод производится с учётом регистра) \n Сложение  \n Вычитание \n Умножение \n Деление \n Степень \n Квадратный корень \n Факториал \n Синус  \n Косинус \n Тангенс \n Завершить работу ")
    a=input()
    match a :
        case 'Сложение': 
            test=True
            while test==True :
                try:
                    Sum1=float(input("Введите первое слагаемое "))
                    Sum2=float(input("Введите второе слагаемое "))
                except Exception:
                    print("Введите целое или вещественное число ")
                else:
                    SumTotal=Sum1+Sum2
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
                    SubTotal=Sub1-Sub2
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
                    MulTotal=Mul1*Mul2
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
                        DivTotal=Div1/Div2
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
                    DegNum=NumD**Deg
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
                        Root=math.sqrt(NumR)
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
                        Fac=math.factorial(NumF)
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
                    Sin=math.sin(NumS)
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
                    Cos=math.cos(NumC)
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
                    Tan=math.tan(NumT)
                    print("Результат: ",Tan)
                    test9=False
        case "Завершить работу":
            stop=1
        case _:
            print("Вы ввели некорректное значение")
