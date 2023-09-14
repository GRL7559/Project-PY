#Практическая работа №1 Мартынов Н.А.
import math
stop=0
while stop==0 :
    print("Введите наименование операции из приведенного ниже списка,которую вы хотите выполнить (Ввод производится с учётом регистра) \n Сложение  \n Вычитание \n Умножение \n Деление \n Степень \n Квадратный корень \n Факториал \n Синус  \n Косинус \n Тангенс \n Завершить работу ")
    a=input()
    match a :
        case 'Сложение': 
            Sum1=float(input("Введите первое слагаемое "))
            Sum2=float(input("Введите первое слагаемое "))
            SumTotal=Sum1+Sum2
            print("Результат: ",SumTotal)
        case "Вычитание": 
            Sub1=float(input("Введите уменьшаемое "))
            Sub2=float(input("Введите вычитаемое "))
            SubTotal=Sub1-Sub2
            print("Результат: ",SubTotal)
        case "Умножение":
            Mul1=float(input("Введите первый множитель "))
            Mul2=float(input("Введите второй множитель "))
            MulTotal=Mul1*Mul2
            print("Результат: ",MulTotal)
        case "Деление":
            Div1=float(input("Введите делимое  "))
            Div2=float(input("Введите делитель "))
            if Div2==0 :
                print("Деление на 0 недопустимо")
            else:
                DivTotal=Div1/Div2
                print("Результат: ",DivTotal)
        case "Степнь" :
            NumD=float(input("Введите число возводимое в степнь  "))
            Deg=float(input("Введите показатель степни  "))
            DegNum=NumD**Deg
            print(DegNum)
        case "Квадратный корень":
            NumR=float(input("Введите число из которого тербуеся извлечь квадратный корень  "))
            Root=math.sqrt(NumR)
            print("Результат: ",Root)
        case "Факториал":
            NumF=float(input("Введите число факториал которого требуется вычислить   "))
            Fac= math.factorial(NumF)
            print(Fac)
        case "Синус":
            NumS=float(input("Введите угол(в радианах) синус из которого требуется вычислить  "))
            Sin=math.sin(NumS)
            print("Результат: ",Sin)
        case "Косинус":
            NumC=float(input("Введите угол(в радианах) косинус из которого требуется вычислить  "))
            Cos=math.cos(NumC)
            print("Результат: ",Cos)
        case "Тангенс":
            NumT=float(input("Введите угол(в радианах) тангенс из которого требуется вычислить  "))
            Tan=math.tan(NumT)
            print("Результат: ",Tan)
        case "Завершить работу":
            stop=1
        case _:
            print("Вы ввели некорректное значение")
