import random


class PLAYER:
    def __init__(self, name, origen):
        self.name = name
        self.origen = origen
        self.speed = 0 #на скорость удара
        self.brain = 0 #больее дешевые цены у торговца
        self.health = 0 #хп
        self.strong = 0 #сила удара
        self.inv = []
        self.gold = 50



    def inv_show(self , item):
        if not self.inv == True:
            print("Ваш инвентарь пустой")
        else:
            for i, item in enumerate(self.inv , 1):
                print(f"{i} Имя - {item["name"]} , Описание - {item["description"]}")



    def choice_origen(self, origen):
        self.origen = origen
        if self.origen == "people":
            self.health = 150 #max = 200
            self.dex = 200 #max = 200
            self.strong = 15 #max = 50
            self.speed = 180 #max = 200
            self.brain = 80 #max = 100

        if self.origen == "vampire":
            self.health = 200 #max = 200
            self.dex = 200 #max = 200
            self.strong = 20 #max = 50
            self.speed = 200 #max = 200
            self.brain = 100 #max = 100

        if self.origen == "elf":
            self.health = 50 #max = 200
            self.dex = 20 #max = 200
            self.strong = 50 #max = 50
            self.speed = 100 #max = 200
            self.brain = 30 #max = 100

        if self.origen == "robot":
            self.health = 200 #max = 200
            self.dex = 10 #max = 200
            self.strong = 10 #max = 50
            self.speed = 10 #max = 200
            self.brain = 100 #max = 100

        if self.origen == "firekill":
            self.health = 30 #max = 200
            self.dex = 30 #max = 200
            self.strong = 30 #max = 50
            self.speed = 30 #max = 200
            self.brain = 30 #max = 100

    def visible_origen(self):
        print(f"health - {self.health} \n"
              f"dex - {self.dex} \n"
              f"strong - {self.strong} \n"
              f"speed - {self.speed} \n"
              f"brain - {self.brain} \n")



class Enemy:
    def __init__(self, name , speed , brain , health , size , strong , dex , attack_speed):
        self.name = name
        self.speed = speed
        self.health = health
        self.size = size
        self.strong = strong
        self.dex = dex

def Die_Player (player):
    if player.health == 0:
        print("Вы проиграли эту смертоносную битву ")
        return True
def Die_Enemy(enemy):
    if enemy.health == 0:
        print("Вы выиграли эту смертоносную битву ")
        return True


def Attack(player , enemy):
    max_hp = player.health
    print(F"Вы встретили {enemy.name} , у него такое хп {enemy.health}")
    while player.health > 0 and enemy.health > 0:
        print(f"Нажмите 1 ,чтобы начать битву , нажмите 2 чтобы ее избежать ")
        choice1 = input("Введите дейстие :)  :(  " )
        if player.dex < player.enemy:
            player.health - 0
        if choice1 == "1":
            attack = input("Нажмите '1' ,чтобы ударить или '2' ,чтобы увернутся ")
            if attack == "1" :
                 player.health -= enemy.strong
                 enemy.health -= player.strong
                 die = Die_Player(enemy , player )
                 die1 = Die_Enemy
                 print(f"У вас отнялось {enemy.strong} и у вас осталось {player.health}")
                 if die:
                     return "Вы слили"
                 elif die1:
                     return "Вы выиграли"
            elif attack == "2":
                    if player.dex >= enemy.dex:
                        if max_hp <= player.health:
                            print("У вас максимум хп! =+=")
                            player.health = max_hp
                        elif max_hp > player.health:
                            if player.dex > 30:
                                chens1 = random.randint(1 , 20)
                                if chens1 == 1:
                                    player.health + 10
                                    print("+10 хп")
                            elif player.dex > 50:
                                chens2 = random.randint(1, 10)
                                if chens2 == 1:
                                    player.health + 10
                                    print("+10 хп")
                            elif player.dex > 100:
                                chens3 = random.randint(1, 5)
                                if chens3 == 1:
                                    player.health + 10
                                    print("+10 хп")
                            elif player.dex > 150:
                                chens4 = random.randint(1, 3)
                                if chens4 == 1:
                                    player.health + 10
                                    print("+10 хп")
                            elif player.dex == 200:
                                player.health + 10
                                print("+10 хп")
                            else:
                                player.health + 0
                    else:
                        print("У врага больше ловкости чем у вас!")



        elif choice1 == "2":
            if enemy.speed > player.speed:
                print("Вам не удалось сбежать xD")
                attack1 = input("Нажмите '1' ,чтобы ударить или '2' ,чтобы увернутся ")
                if attack1 == "1":
                    player.health -= enemy.strong
                    enemy.health -= player.strong
                elif attack1 == "2":
                    if player.dex >= enemy.dex:
                        if max_hp <= player.health:
                            print("У вас максимум хп! =+=")
                            player.health = max_hp
                        elif max_hp > player.health:
                            if player.dex > 30:
                                chens1 = random.randint(1, 20)
                                if chens1 == 1:
                                    player.health + 10
                                    print("+10 хп")
                            elif player.dex > 50:
                                chens2 = random.randint(1, 10)
                                if chens2 == 1:
                                    player.health + 10
                                    print("+10 хп")
                            elif player.dex > 100:
                                chens3 = random.randint(1, 5)
                                if chens3 == 1:
                                    player.health + 10
                                    print("+10 хп")
                            elif player.dex > 150:
                                chens4 = random.randint(1, 3)
                                if chens4 == 1:
                                    player.health + 10
                                    print("+10 хп")
                            elif player.dex == 200:
                                player.health + 10
                                print("+10 хп")
                            else:
                                player.health + 0
                    else:
                        print("У врага больше ловкости чем у вас!")
                else:
                    print("Вам удалось сбежать!")

        else:
            print("Ошибка , введите 1 или 2 ")



class Villager:
    def __init__(self):
        self.items = [
            {"name": "Малое зелье здоровья", "price": 20, "type": "heal", "value": 30,
             "description": "Восстанавливает 30 HP"},
            {"name": "Большое зелье здоровья", "price": 50, "type": "heal", "value": 70,
             "description": "Восстанавливает 70 HP"},
            {"name": "Эликсир силы", "price": 40, "type": "buff", "value": 5,
             "description": "+5 к силе на следующий бой"},
            {"name": "Зелье ловкости", "price": 35, "type": "buff", "value": 10,
             "description": "+10 к ловкости на следующий бой"},
            {"name": "Защитный амулет", "price": 60, "type": "buff", "value": 15,
             "description": "+15 к максимальному здоровью"},
        ]
    def Visual(self):
        print(f"Список : Вы вашли в лавку торговца!")
        for i, item in enumerate(self.items , 1):
            print(f"{i} Имя - {item["name"]} , Цена - {item["price"]} , Описание - {item["description"]}")

    def Buy(self , player , i):
        if 0 < i <= len(self.items):
            item = self.items[i]
            if player.brain >= 50:
                item["price"] / 1.5
                if player.brain >= 75:
                    item["price"] / 1.5
                    if player.gold >= item["price"]:
                        player.gold -= item["price"]
                        player.inv.append(item)
                        print(
                            f"Вы успешно купили предмет {item["name"]}, поздравляю с покупкой! У вас осталось {player.gold} золото!")
                    else:
                        print("У вас не хватает денег!")
                else:
                    if player.gold >= item["price"]:
                        player.gold -= item["price"]
                        player.inv.append(item)
                        print(
                            f"Вы успешно купили предмет {item["name"]}, поздравляю с покупкой! У вас осталось {player.gold} золото!")
                    else:
                        print("У вас не хватает денег!")


def Brodilka():
    print("Добро пожаловать в игру 'NIT'")
    nick = input("Введите ваш никнейм ")
    player = PLAYER(nick , "")
    print("Выберете персонажа!")
    print("Нажмите '1' для выбора персонажа 'people'")
    print("Нажмите '2' для выбора персонажа 'vampire'")
    print("Нажмите '3' для выбора персонажа 'elf'")
    print("Нажмите '4' для выбора персонажа 'robot'")
    print("Нажмите '5' для выбора персонажа 'firekill'")
    ch1 = int(input("Введите число для взятия персонажа "))
    if ch1 == 1:
        player.choice_origen("people")

    elif ch1 == 2:
        player.choice_origen("vampire")

    elif ch1 == 3:
        player.choice_origen("elf")

    elif ch1 == 4:
        player.choice_origen("robot")

    elif ch1 == 5:
        player.choice_origen("firekill")

    else:
        print("Вы ввели неправильное число , введите число от 1 до 5 включительно!")

    player.visible_origen()

    villager = Villager()
    vill = True

    #while vill == True and player.health > 0:

Brodilka()