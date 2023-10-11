import random

def Equip(item,equipment_E):
    match item:
        case "монтировка","мачете","пистолет":
            print("Это оружие хорошо вам послужит")
            equipment_E["руки"]=item
            return equipment_E
        case "самодельный доспех","одежда из прочной ткани","кевларовый бронижилет":
            print("Эта одежда вам впору")
            equipment_E["тело"]=item
            return equipment_E
        case "кроссовки","рабочие ботинки","сапоги с кевларовыми пластинами":
            print("Эта обувь отлично сидит")
            equipment_E["ноги"]=item 
            return equipment_E

def Stat_equipment(equipment_S,ATK,DEF):
    match equipment_S.get("руки"):
        case "монтировка":
            ATK+=2
        case "мачете":
            ATK+=4
        case "пистолет":
            ATK+=6
    match equipment_S.get("тело"):
        case "одежда из прочной ткани":
            DEF+=1
        case "самодельный доспех":
            DEF+=3
        case "кевларовый бронижилет":
            DEF+=5
    match equipment_S.get("ноги"):
        case "кроссовки":
            DEF+=1
        case "рабочие ботинки":
            DEF+=2
        case "сапоги с кевларовыми пластинами":
            DEF+=3
    return[ATK,DEF]

def Check_stat(item):
    match item:
        case "монтировка":
            return "+2 к атаке"
        case "мачете":
            return"+4 к атаке"
        case "пистолет":
            return "+6 к атаке"
        case "одежда из прочной ткани":
            return "+1 к защите"
        case "самодельный доспех":
            return "+3 к защите"
        case "кевларовый бронижилет":
            return "+5 к защите"
        case "кроссовки":
            return "+1 к защите"
        case "рабочие ботинки":
            return "+2 к защите"
        case "сапоги с кевларовыми пластинами":
            return "+3 к защите"
    
    
def Loot():
    loot=("монтировка","мачете","пистолет","самодельный доспех","одежда из прочной ткани","кевларовый бронижилет","кроссовки","рабочие ботинки","сапоги с кевларовыми пластинами")
    return random.choice(loot)


def Ivents():
    random_ivent=("Бой" ,"Интересная находка" ,"Продовольственный ящик")                                                  
    return random.choice(random_ivent)
        

def Enimies():
    enimies=["Койот","Скорпион" ,"Перекати поле"]               
    HP_enimies={"Койот":15 ,"Скорпион":8 ,"Перекати поле":10}   
    ATK_enimies={"Койот":12 ,"Скорпион":10 ,"Перекати поле":1}
    enimie=random.choice(enimies)                                                                                                    
    return [enimie,HP_enimies.get(enimie),ATK_enimies.get(enimie)]


def Battle(HP,XP):
    if Danger[0]=="Перекати поле":
        print(f"Вы наткнулись на {Danger[0]}, готовьтесь биться!\n")
    else:
        print(f"Вы наткнулись на {Danger[0]}а, готовьтесь биться!\n")
    print(f"\t{Danger[0]}\n Здоровье:{Danger[1]}\tАтака:{Danger[2]}\n")
    initiative=random.randint(0,1)
    while Danger[1]>0 and HP>0:
        if initiative==0:
            print("Ваш ход , выберите действие , которое хотите совершить:\t\tОбратите внимание ввод ответов производится с заглавной буквы\nЗащищаться\nАтаковать\n ")
            Danger[1]=Battle_hero(DEF)
            if Danger[1]>0:
                print(f"Ходит {Danger[0]}\n")
                HP=Battle_mob(DEF,HP) 
        else: 
            print(f"Ходит {Danger[0]}\n")
            HP=Battle_mob(DEF,HP) 
            if HP>0:
                print("Ваш ход , выберите действие , которое хотите совершить:\t\tОбратите внимание ввод ответов производится с заглавной буквы\nЗащищаться\nАтаковать\n ")
                Danger[1]=Battle_hero(DEF)
    if HP>0:
        match Danger[0]:
            case "Койот":
                print(f"Вам удалось одолеть {Danger[0]}а!\n")
                XP+=3
            case "Скорпион":
                print(f"Вам удалось одолеть {Danger[0]}а!\n")
                XP+=2
            case "Перекати поле":
                print(f"Вам удалось одолеть {Danger[0]}!\n")
                XP+=1
    return [HP,XP]


def Battle_hero(DEF):
    stop=True
    while stop==True:
        move=input()
        match move:
            case "Защищаться":
                DEF_option=DEF*2
                stop=False
            case "Атаковать":
                ATK_battle=random.randint(ATK-4,ATK)
                Danger[1]-=ATK_battle
                if Danger[1]>0:
                    print(f"\nВы нанесли {ATK_battle} единиц урона\nЗдоровье противника:{Danger[1]}\n")
                else:
                    print(f"Вы нанесли {ATK_battle} единиц урона\n")
                stop=False
            case _:
                print("Введено некорректное значение , попробуйте еще раз\n")
    return Danger[1]


def Battle_mob(DEF_option,HP):
    ATK_mob=random.randint(Danger[2]-5,Danger[2])
    if ATK_mob>DEF_option:
        HP-=ATK_mob
        print(f"{Danger[0]} наносит вам {ATK_mob} урона\nОставшееся здоровье:{HP}\n")
    else:
        print("Вы успешно заблокировали атаку\n")
    return HP


def Leveling(XP):
    match XP:
        case 1,2,3:
            return [1,5,3,100]
        case 4:
            print("Поздравляю , вы достигли 2 уровня!\nХарактеристики были повышены\n")
            return [2,7,4,108]
        case 5,6:
            return [2,7,4,108]
        case 7:
            print("Поздравляю , вы достигли 3 уровня!\nХарактеристики были повышены\n")
            return [3,8,9,120]
        case 8,9:
            return [3,8,9,120]
        case 10:
            print("Поздравляю , вы достигли 4 уровня!\nХарактеристики были повышены\n")
            return [4,10,10,128]
        case 11,12:
            return [4,10,10,128]
        case 13:
            print("Поздравляю , вы достигли 5 уровня!\nХарактеристики были повышены\n")
            return [5,12,12,140]
        case _:
            return [5,12,12,140]

XP=1
Stats=Leveling(XP)
HP=100
LVL=Stats[0]
ATK=Stats[1]
DEF=Stats[2]
MAX_HP=Stats[3]
DEF_option=0
stages=0
life=True
equipment={"руки":"ничего","тело":"лохмотья","ноги":"ничего"}
print("Вы ничего не помните, кроме загадочнй фигуры в маске Анубиса , которая телепортирует вас в пустыню.Вы остаетесь один на раскалённых песчаных дюнах, выживая в суровых условиях и ища путь домой.\n")
while life==True:
    print("Выберите что вы хотите сделать: \nИдти\nОсмотреть себя(экипировка и харакстеристики)\nСдаться\n")
    choice=input()
    match choice:
        case "Идти":
            print(".....")
            Event=Ivents()
            match Event:
                case "Бой":             
                    Danger=Enimies()
                    Results=Battle(HP,XP)
                    HP=Results[0]
                    if HP<=0:
                        life=False
                    else:
                        XP=Results[1]
                        Stats=Leveling(XP)
                        LVL=Stats[0]
                        ATK=Stats[1]
                        DEF=Stats[2]
                        MAX_HP=Stats[3]
                        Stats=Stat_equipment(equipment,ATK,DEF)
                        ATK=Stats[0]
                        DEF=Stats[1]
                        stages+=1
                case "Продовольственный ящик":
                    print("Вы нашли продовольствие и можете восстановить здоровье\n")
                    if HP==MAX_HP:
                        print("Ваше здоровье уже на максимуме\n")
                    else:
                        heal=random.randint(0,MAX_HP/4)
                        max_heal=MAX_HP-HP
                        HP+=heal
                        if HP>MAX_HP:
                            heal=max_heal
                            HP=MAX_HP
                        print(f"Восстановлено {heal} очков здоровья. Текущий показатель: {HP}\n" )
                    stages+=1
                case "Интересная находка":
                    print("Кажется в песках ближайшего бархана что-то блестит...")
                    item=Loot()
                    if item==equipment["ноги"] or item==equipment["руки"] or item==equipment["тело"]:
                        print("Эх,похоже это всего лишь мусор")
                    else:
                        print(f"Ого , да это же {item} ,хотите взять? Это даст вам {Check_stat(item)}\t\t\t\t\tОбратите внимание ввод ответов производится с заглавной буквы")
                        stop1=True
                        while stop1==True:
                            grab=input()
                            match grab:
                                case "Да":
                                    equipment=Equip(item,equipment)
                                    New_stats=Stat_equipment(equipment,ATK,DEF)
                                    ATK=New_stats[0]
                                    DEF=New_stats[1]      
                                case "Нет":
                                    print("Вы отбросили вещицу от себя и продолжили свой путь")
                                case _:
                                    print("Введено некорректоное значение")
                    stages+=1
        case "Осмотреть себя":
            print(f"\nУровень: {LVL}\nЗдоровье: {HP}/{MAX_HP}\nАтака: {ATK}\nЗащита: {DEF}\n")
            equip=[equipment.get("руки"),equipment.get("тело"),equipment.get("ноги")]
            print(f"В руках {equip[0]}\nНа теле {equip[1]}\nНа ногах {equip[2]}\n")
        case "Сдаться":
            print(" ")
            life=False
        case _:
            print("Вы ввели некорректое действие\n")  
score=XP*10     
print(F"Вы умерли\nНабранные вами очки: {score}\nВаш уровень: {LVL}\nПройдено этапов: {stages}\n")
print("Вас встречает до боли знакомая фигура , это Анубис.\nОн раскатисто произносит:Ты прошел испытание и удостоен моей аудиенции смертный. Теперь посмотрим , дотоин ли ты пребывания в Аменти")