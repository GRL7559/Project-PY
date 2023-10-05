def rectange_area(widht,height):
    S=widht*height
    return S 


def is_even(number):
    if number//2==0 :
        return True
    else:
        return False



def sum_digits(number):
    if number>10 :
         return number 
    else:
         return number%10 + sum_digits(number//10) 