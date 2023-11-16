import random
import json
import csv
import os

def Input():
    value=input()
    value=value.strip()
    value=value.capitalize()
    return value


def Saves(XP,HP,equipment,Name):   
    data=[XP,HP,equipment["руки"],equipment["тело"],equipment["ноги"],Name]
    while(True):
        print("\nЧто вы хотите сделать с сохранением?\nСохранить\nЗагрузить\nУдалить\n")
        save=Input()
        match save:
            case "Сохранить":
                Save(data)
                print("\nСохранение успешно создано!\n")
                break
            case "Загрузить":
                return Load(data)
            case "Удалить":
                Delete()
                break
            case _:print("\nВведено некорректное значение")


def Save(data):
    if os.path.exists('save.json'):
        os.remove('save.json')
    with open('save.json', 'w',encoding='utf-8') as file:
        json.dump(data , file , indent=4,ensure_ascii=False)
        file.close() 


def Load(data):
    if os.path.exists('save.json'):
        with open('save.json','r',encoding='utf-8') as file:
            upload_data=json.load(file)
            file.close()
        print("\nСохранение успешно загружено!\n")
        return upload_data
    else:
        print("\nУ вас нет сохранения , которое можно загрузить\n")
        return(data)


def Delete():
    try:
        os.remove('save.json')
        print("\nСохранение успешно удалено!\n")
    except FileNotFoundError:
        print("\nУ вас нет сохранения, которое можно удалить\n")


def Tab_Lead(data_top):
    fieldnames = ['Очки','Имя','Уровень','Этапы']
    k=1
    if os.path.exists('results.csv'):
        with open('results.csv','r', newline='') as file:
            reader=csv.DictReader(file,fieldnames=fieldnames,delimiter=';')
            next(reader)
            for row in reader:
                data_top.append(row)  
        os.remove('results.csv')    
    with open('results.csv','w', newline='') as file:
        writer = csv.DictWriter(file,fieldnames=fieldnames,delimiter=';')
        writer.writeheader()  
        for row in data_top:
            writer.writerow(row)


def Loot():
    loot=("монтировка","мачете","пистолет","самодельный доспех","одежда из прочной ткани","кевларовый бронижилет","кроссовки","рабочие ботинки","сапоги с кевларовыми пластинами")
    return random.choice(loot)


def Events():
    random_ivent=("Бой" ,"Интересная находка" ,"Продовольственный ящик")                                                  
    return random.choice(random_ivent)


def Leveling(XP):
    match XP:
        case 1|2|3:return [1,5,3,100]
        case 4|5|6:return [2,7,4,108]
        case 7|8|9:return [3,8,9,120]
        case 10|11|12:return [4,10,10,128]
        case 13|_:return [5,12,12,140]


def Leveling_grades(old_XP,XP,LVL):
            if old_XP<1+(LVL-1)*3 and XP>=1+(LVL-1)*3 and LVL!=1 or old_XP>13:
                print(f"Поздравляю , вы достигли {LVL} уровня!\nХарактеристики были повышены\n")

def Look(equipment_L):
    print(f"\nУровень: {LVL}\nЗдоровье: {HP}/{MAX_HP}\nАтака: {ATK}\nЗащита: {DEF}\n")
    equip=[equipment_L.get("руки"),equipment_L.get("тело"),equipment_L.get("ноги")]
    print(f"В руках {equip[0]}\nНа теле {equip[1]}\nНа ногах {equip[2]}\n")

def Enimies():
    enimies=["Койот","Скорпион" ,"Перекати поле"]               
    HP_enimies={"Койот":5 ,"Скорпион":4 ,"Перекати поле":3}   
    ATK_enimies={"Койот":8 ,"Скорпион":5 ,"Перекати поле":4}
    enimie=random.choice(enimies)                                                                                                    
    return [enimie,HP_enimies.get(enimie)*LVL,ATK_enimies.get(enimie)*LVL]


def Battle(HP,XP):
    if Danger[0]=="Перекати поле":
        print(f"Вы наткнулись на {Danger[0]}, готовьтесь биться!\n")
    else:
        print(f"Вы наткнулись на {Danger[0]}а, готовьтесь биться!\n")
    print(f"\t{Danger[0]}\nЗдоровье:{Danger[1]}\tАтака:{Danger[2]}\n")
    K=0
    DEF_option=0
    initiative=random.randint(0,1)
    while Danger[1]>0 and HP>0:
        if initiative==0:
            print("Ваш ход , выберите действие , которое хотите совершить:\nЗащищаться (снизить входящий урон на следующие 2 раунда)\nАтаковать\n ")
            Result_hero=Battle_hero(DEF,DEF_option,K)
            Danger[1]=Result_hero[0]
            DEF_option=Result_hero[1]
            K=Result_hero[2]
            if Danger[1]>0:
                print(f"Ходит {Danger[0]}\n")
                Result_mob=Battle_mob(DEF_option,HP,K)
                HP=Result_mob[0]
                K=Result_mob[1]
                if K==0:
                    DEF_option=0
        else: 
            print(f"Ходит {Danger[0]}\n")
            Result_mob=Battle_mob(DEF_option,HP,K)
            HP=Result_mob[0]
            K=Result_mob[1]
            if K==0:
                DEF_option=0               
            if HP>0:
                print("Ваш ход , выберите действие , которое хотите совершить: (снизить входящий урон на следующие 2 раунда)\nЗащищаться\nАтаковать\n ")
                Result_hero=Battle_hero(DEF,DEF_option,K)
                Danger[1]=Result_hero[0]
                DEF_option=Result_hero[1]
                K=Result_hero[2]
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


def Battle_hero(DEF,DEF_option,K):
    stop=True
    while stop==True:
        move=Input()
        match move:
            case "Защищаться":
                DEF_option=DEF
                K=2
                print(" ")
                stop=False
            case "Атаковать":
                ATK_battle=random.randint(ATK-4,ATK)
                remain=Danger[1]
                Danger[1]-=ATK_battle
                if Danger[1]>0:
                    print(f"\nВы нанесли урон в количестве {ATK_battle}\nЗдоровье противника: {Danger[1]}\n")
                else:
                    print(f"\nВы нанесли урон в количестве {remain}\n")
                stop=False
            case _:
                print("\nВведено некорректное значение , попробуйте еще раз\n")
    return [Danger[1],DEF_option,K]


def Battle_mob(DEF_option,HP,K):
    ATK_mob=random.randint(Danger[2]-3,Danger[2])
    DEF_random=random.randint(DEF_option-3,DEF_option)
    if DEF_option>0:
        K-=1
        if ATK_mob-DEF_random>0:
            HP-=(ATK_mob-DEF_random)
            print(f"{Danger[0]} наносит вам урон в количестве {ATK_mob-DEF_random}\t(Оставшиеся заряды защиты: {K})\nОставшееся здоровье: {HP}\n")
        else:
            HP=HP
            print(f"{Danger[0]} не наносит вам урон\t(Оставшиеся заряды защиты: {K})\nОставшееся здоровье: {HP}\n")
    else:
        HP-=ATK_mob
        print(f"{Danger[0]} наносит вам урон в количестве {ATK_mob}\nОставшееся здоровье: {HP}\n")
    return [HP,K]


def Healing(HP,MAX_HP):
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
        if heal>1:
            print(f"Восстановлено {heal} очков здоровья. Текущий показатель: {HP}\n" )
        else:
            print(f"Восстановлено {heal} очко здоровья. Текущий показатель: {HP}\n" )
    return [HP,MAX_HP]


def New_item(equipment_I,ATK,DEF):
    print("Кажется в песках ближайшего бархана что-то блестит...")
    item=Loot()
    if item==equipment_I["ноги"] or item==equipment_I["руки"] or item==equipment_I["тело"]:
        print("Эх,похоже это всего лишь мусор\n")
    else:
        print(f"Ого , да это же {item} ,хотите взять?\nПрибавка к характеристикам: {Check_stat(item)}")
        if equipment_I[Check_class(item)]=="ничего":
            print(f"Нынешняя экипировка: Отсутствует\nПрибавка к характеристикам: {Check_stat(equipment_I[Check_class(item)])}\n")
        else:
            print(f"Нынешняя экипировка: {equipment_I[Check_class(item)]}\nПрибавка к характеристикам: {Check_stat(equipment_I[Check_class(item)])}\n")
        stop1=True
        while stop1==True:
            grab=Input()
            match grab:
                case "Да":
                    New_stats=Stat_unequipment(ATK,DEF,equipment_I)
                    ATK=New_stats[0]
                    DEF=New_stats[1]
                    equipment_I=Equip(item,equipment_I)
                    stop1=False
                case "Нет":  
                    print("\nВы отбросили вещицу от себя и продолжили свой путь\n")
                    stop1=False
                case _:print("\nВведено некорректоное значение\n")
    return [equipment_I,ATK,DEF]


def Equip(item,equipment_E):
    match item:
        case "монтировка":
            print("\nГордон гордится вами\n")
            equipment_E["руки"]=item
            return equipment_E
        case "мачете":
            print("\nЭто мачете все еще хорошо режет, несмотря на несколько видимых сколов\n")
            equipment_E["руки"]=item
            return equipment_E
        case "пистолет":
            print("\nЭтот пистолет в удивительно хорошем состонии ,для пролежавшего некоторое время в песке\n")
            equipment_E["руки"]=item
            return equipment_E
        case "самодельный доспех":
            print("\nДовольно странный доспех , сделанный из подручных средств , ну это лучше чем ничего\n")
            equipment_E["тело"]=item
            return equipment_E
        case "одежда из прочной ткани":
            print("\nОдежда из плотной матерчатой ткани , довольно удобная , но ее защитные свойства вызывают сомнения\n")
            equipment_E["тело"]=item
            return equipment_E
        case "кевларовый бронижилет":
            print("\nУдивительно , что такой технологичный бронижилет оказался посреди пустыне\n")
            equipment_E["тело"]=item
            return equipment_E
        case "кроссовки":
            print("\nУдобные кроссовки , по песку конечно не побегаешь , но хотя-бы ступни не болят\n")
            equipment_E["ноги"]=item 
            return equipment_E
        case "рабочие ботинки":
            print("\nСапоги сделанные на века , к тому же очень хорошо сидят\n")
            equipment_E["ноги"]=item 
            return equipment_E
        case "сапоги с кевларовыми пластинами":
            print("\nВау , что военное обмундирование делает посреди пустыни , а впрочем это не моё дело\n")
            equipment_E["ноги"]=item 
            return equipment_E


def Stat_unequipment(ATK,DEF,equipment_S):
    match equipment_S["руки"]:
        case "ничего"                           :ATK-=0
        case "монтировка"                       :ATK-=2
        case "мачете"                           :ATK-=4
        case "пистолет"                         :ATK-=6
    match equipment["тело"]:
        case "лохмотья"                         :DEF-=0
        case "одежда из прочной ткани"          :DEF-=1
        case "самодельный доспех"               :DEF-=3
        case "кевларовый бронижилет"            :DEF-=5
    match equipment["ноги"]:
        case "потрепанные сандалии"             :DEF-=0
        case "кроссовки"                        :DEF-=1
        case "рабочие ботинки"                  :DEF-=2
        case "сапоги с кевларовыми пластинами"  :DEF-=3
    return[ATK,DEF]


def Stat_equipment(ATK,DEF,equipment_S):
    match equipment_S["руки"]:
        case "ничего"                           :ATK+=0
        case "монтировка"                       :ATK+=2
        case "мачете"                           :ATK+=4
        case "пистолет"                         :ATK+=6
    match equipment["тело"]:
        case "лохмотья"                         :DEF+=0
        case "одежда из прочной ткани"          :DEF+=1
        case "самодельный доспех"               :DEF+=3
        case "кевларовый бронижилет"            :DEF+=5
    match equipment["ноги"]:
        case "потрепанные сандалии"             :DEF+=0
        case "кроссовки"                        :DEF+=1
        case "рабочие ботинки"                  :DEF+=2
        case "сапоги с кевларовыми пластинами"  :DEF+=3
    return[ATK,DEF]


def Check_stat(item):
    match item:
        case "ничего"                            :return "+0 к атаке"
        case "монтировка"                        :return "+2 к атаке"
        case "мачете"                            :return "+4 к атаке"
        case "пистолет"                          :return "+6 к атаке"
        case "лохмотья"                          :return "+0 к защите"
        case "одежда из прочной ткани"           :return "+1 к защите"
        case "самодельный доспех"                :return "+3 к защите"
        case "кевларовый бронижилет"             :return "+5 к защите"
        case "потрепанные сандалии"              :return "+0 к защите"
        case "кроссовки"                         :return "+1 к защите"
        case "рабочие ботинки"                   :return "+2 к защите"
        case "сапоги с кевларовыми пластинами"   :return "+3 к защите"


def Check_class(item):
    match item:
        case "монтировка"|"мачете"|"пистолет"                                          :return"руки"
        case "одежда из прочной ткани"|"самодельный доспех"|"кевларовый бронижилет"    :return"тело"
        case "кроссовки"|"рабочие ботинки"|"сапоги с кевларовыми пластинами"           :return"ноги"


print("Вы ничего не помните, кроме загадочной фигуры в маске Анубиса , которая телепортирует вас в пустыню\nВозможно вам удастся вспомнить свое имя?\n")
Name=Input()
print(f"\nИ так ,{Name}, Вы остаетесь один на раскалённых песчаных дюнах, выживая в суровых условиях и ища путь домой.\n")
XP =1
Stats=Leveling(XP)
HP=100
LVL=Stats[0]
ATK=Stats[1]
DEF=Stats[2]
MAX_HP=Stats[3]
stages=0
life=True
equipment={"руки":"ничего","тело":"лохмотья","ноги":"потрепанные сандалии"}

while life==True:
    print("Выберите что вы хотите сделать: \nИдти\nОсмотреть себя(экипировка и харакстеристики)\nСдаться\nСохранение\n")
    choice=Input()
    match choice:
        case "Идти":
            print(".....")
            Event=Events()
            match Event:
                case "Бой":             
                    Danger=Enimies()
                    Results=Battle(HP,XP)
                    HP=Results[0]
                    if HP<=0:
                        life=False
                    else:
                        old_XP=XP
                        XP=Results[1]
                        Stats=Leveling(XP)
                        LVL=Stats[0]
                        ATK=Stats[1]
                        DEF=Stats[2]
                        MAX_HP=Stats[3]
                        Leveling_grades(old_XP,XP,LVL)
                        Stats=Stat_equipment(ATK,DEF,equipment)
                        ATK=Stats[0]
                        DEF=Stats[1]
                        stages+=1
                case "Продовольственный ящик":
                    Heal=Healing(HP,MAX_HP)
                    HP=Heal[0]
                    MAX_HP=Heal[1]
                    stages+=1
                case "Интересная находка":
                    Old_stats=New_item(equipment,ATK,DEF)
                    equipment=Old_stats[0]
                    ATK=Old_stats[1]
                    DEF=Old_stats[2]
                    New_stats=Stat_equipment(ATK,DEF,equipment)
                    ATK=New_stats[0]
                    DEF=New_stats[1]   
                    stages+=1
        case "Осмотреть себя":
            Look(equipment)
        case "Сдаться":
            print(" ")
            life=False
        case "Сохранение":
            Saved_stats=Saves(XP,HP,equipment,Name)
            if Saved_stats is None:
                continue
            else:
                XP                  =Saved_stats[0]
                HP                  =Saved_stats[1]
                equipment["руки"]   =Saved_stats[2]
                equipment["тело"]   =Saved_stats[3]
                equipment["ноги"]   =Saved_stats[4]
                Name                =Saved_stats[5]
                Stats=Leveling(XP)
                LVL                 =Stats[0]
                ATK                 =Stats[1]
                DEF                 =Stats[2]
                MAX_HP              =Stats[3]
                Stats=Stat_equipment(ATK,DEF,equipment)
                ATK                 =Stats[0]
                DEF                 =Stats[1]
        case _:
            print("\nВы ввели некорректое действие\n")          
score=XP*10     
print(F"Вы умерли\nНабранные вами очки: {score}\nВаш уровень: {LVL}\nПройдено этапов: {stages}\n")
print("Вас встречает до боли знакомая фигура , это Анубис.\nОн раскатисто произносит:Теперь я понял твою сущность иты можешь быть удостоен моей аудиенции , смертный. Теперь посмотрим , дотоин ли ты пребывания в Аменти...\n")
data_top=[
    {'Очки': score,'Имя': Name ,'Уровень':LVL,'Этапы':stages}
]
Tab_Lead(data_top)