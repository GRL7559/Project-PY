import random
"""
def Invenory_add(item_add):
    inventory={"руки":"факел","тело":"лохмотья","ноги":"ничего"}
    inventory[всумке]=item
 
def Equip(item):
    print() 

def Unequip(item):
    print()

def Leveling(XP):
    match XP:
        case 3:
            LVL=2
            ATK=ATK+2
            DEF=DEF+1
        case 5:
            fsf
"""
def Ivents():
    random_ivent={"Бой" ,"Интересная находка" ,"Продовольственный ящик"}      
    ivent=random_ivent.pop(random.randint(0,2)) #не работает 
    random_ivent.add(ivent)                                                 
    return ivent
        
def Enimies():
    enimies=["волк","скорпион" ,"перекати поле"]               #наименования врагов 
    HP_enimies={"волк":20 ,"скорпион":5 ,"перекати поле":10}   #hp врагов
    ATK_enimies={"волк":12 ,"скорпион":10 ,"перекати поле":1}  #atk врагов
    enimie=enimies.pop                                         
    enimies.append(enimie)                                     #взятие рандомного врага и обновление списка              
    HP_enimi=HP_enimies.get(enimie)
    ATK_enimi=ATK_enimies.get(enimie)                          #присваивание статов конкретного врага
    return [enimie,HP_enimi,ATK_enimi]

def Battle():
    move=input()
    match move:
        case "Защищаться":
            DEF=DEF*2
        case "Атаковать":
            ATK_battle=random.randint(ATK/2,ATK)
            Danger[1]-=ATK_battle
            print("Вы нанесли ",ATK_battle,"урона")

def Battle_mob():
    ATK_mob=random.randint(Danger[2]/2,Danger[2])
    if ATK_mob>DEF:
        HP-=ATK_mob
        print(Danger[0]," наносит вам ",ATK_mob," урона")
    else:
        print("Вы успешо увернулись от атаки")
    DEF=DEF_static

MAX_HP=100
HP=100
XP=1
LVL=1
ATK=5
DEF_static=3           #статы
DEF=DEF_static
stages=0
life=True
print("интерлюдия")
while life==True:
    print("Выбирите что вы хотите сделать \nИдти дальше \nПроверить экипировку и показатели\nСдаться")
    choise=input()
    match choise:
        case "Идти дальше":
            Event=Ivents()
            print(Event)
            match Event:
                case "Бой":
                    Danger=Enimies()
                    print("Вы наткнулись на ",Danger[0],", готовьтесь биться!")
                    initiative=random.randint(0,1)
                    while Danger[1]!=0 or HP!=0:
                        if initiative==0:
                            print("Ваш ход , выбирите действие , которое хотите совершить:\n\n\n ")
                            Battle()
                            print("Ход", Danger[0])
                            Battle_mob()
                        else: 
                            print(Danger[0] ,"ходит первым")
                            Battle_mob()
                            print("Ваш ход , выбирите действие , которое хотите совершить:\n\n\n ")
                            Battle()
                    if HP!=0:
                        stages+=1
                    else:
                        life=False
                case "Продовольственный ящик":
                    print("Вы нашли продовольствие и можете восстановить здоровье")
                    stages+=1
                    if HP==MAX_HP:
                        print("Ваше здоровье уже максимальное")
                    else:
                        heal=random.randint(0,MAX_HP/4)
                        HP+=heal
                        if HP>MAX_HP:
                            HP=MAX_HP
                        print("Восстановлено ",heal," очков здоровья. Текущий показатель: ",HP )
                case "Интересная находка":
                    print("И")
                    #В разработке
                    stages+=1
        case "Проверить экипировку":
            print("кортежи экипировки")
            print("статы атаки , защита ,хп")
        case "Сдаться":
            life=False
        case _:
            print("Вы ввели некорректое действие")
print("Вы умерли")        
print("\nНабранные вами очки: ",XP,"\nВаш уровень: ",LVL,"\nпройдено этапов: ",stages)