import random
import time


class PLAYER:
    def __init__(self, name, origen):
        self.name = name
        self.origen = origen
        self.speed = 0  # на скорость удара
        self.brain = 0  # больее дешевые цены у торговца
        self.health = 0  # хп
        self.strong = 0  # сила удара
        self.inv = []
        self.gold = 50
        self.maxhealth = 0
        self.buff_strong = 0
        self.buff_dex = 0
        self.level = 4

    def inv_show(self):
        if not self.inv == True:
            print("Ваш инвентарь пустой")
        else:
            for i, item in enumerate(self.inv, 1):
                print(f"{i} Имя - {item["name"]} , Описание - {item["description"]}")

    def use_item(self, numinv):
        item = self.inv[numinv]
        if item["type"] == "heal":
            if self.health == self.maxhealth:
                print("У вас максимум хп и вы потратили зелье!")
            elif self.maxhealth - self.health <= item["value"]:
                self.health = self.maxhealth
            else:
                self.health += item["value"]

        elif item["type"] == "buff":
            if item in self.inv:
                if "сил" in item["description"]:
                    self.strong = self.strong + item["value"]
                    self.buff_strong = 3
                    print(f"Вы выпили зелье силы , ваша сила теперь {self.strong}.Длится {self.buff_strong} битвы. ")
                elif "ловк" in item["description"]:
                    self.buff_dex = 5
                    self.dex += item["value"]
                    print(f"Вы выпили зелье ловкости , ваша ловкость теперь {self.dex}.{self.buff_strong} ")

    # с количеством битв

    def choice_origen(self, origen):
        self.origen = origen
        if self.origen == "people":
            self.health = 150  # max = 200
            self.dex = 200  # max = 200
            self.strong = 15  # max = 50
            self.speed = 180  # max = 200
            self.brain = 80  # max = 100
            self.maxhealth = 150

        if self.origen == "vampire":
            self.health = 200  # max = 200
            self.dex = 200  # max = 200
            self.strong = 20  # max = 50
            self.speed = 200  # max = 200
            self.brain = 100  # max = 100
            self.maxhealth = 200

        if self.origen == "elf":
            self.health = 50  # max = 200
            self.dex = 20  # max = 200
            self.strong = 50  # max = 50
            self.speed = 100  # max = 200
            self.brain = 30  # max = 100
            self.maxhealth = 50

        if self.origen == "robot":
            self.health = 200  # max = 200
            self.dex = 10  # max = 200
            self.strong = 10  # max = 50
            self.speed = 10  # max = 200
            self.brain = 100  # max = 100
            self.maxhealth = 200

        if self.origen == "firekill":
            self.health = 30  # max = 200
            self.dex = 30  # max = 200
            self.strong = 50  # max = 50
            self.speed = 30  # max = 200
            self.brain = 30  # max = 100
            self.maxhealth = 30

    def visible_origen(self):
        print(f"health - {self.health} \n"
              f"dex - {self.dex} \n"
              f"strong - {self.strong} \n"
              f"speed - {self.speed} \n"
              f"brain - {self.brain} \n")


class Enemy:
    def __init__(self, name, speed, health, strong, dex, level):
        self.name = name
        self.speed = speed
        self.health = health
        self.strong = strong
        self.dex = dex
        self.level = level

    def poisk_enemy(player_level):
        enemy = [Enemy("Skeleton", 50, 100, 10, 10, 1),
                 Enemy("Zombie", 100, 70, 15, 30, 2),
                 Enemy("Small Zombie", 200, 50, 15, 70, 3),
                 Enemy("Goblin", 30, 200, 35, 5, 4),
                 Enemy("Killer", 200, 50, 40, 100, 5),
                 Enemy("Fire Elemental", 80, 180, 45, 25, 6),
                 Enemy("Ice Mage", 60, 120, 30, 40, 7),
                 Enemy("Earth Golem", 20, 350, 55, 5, 8),
                 Enemy("Storm Rider", 150, 140, 50, 80, 9),
                 Enemy("Dark Knight", 70, 280, 65, 35, 10),
                 Enemy("Vampire Lord", 130, 320, 70, 60, 11),
                 Enemy("Hydra", 40, 450, 75, 20, 12),
                 Enemy("Mind Flayer", 90, 200, 55, 90, 13),
                 Enemy("Dragon Whelp", 110, 380, 85, 50, 14),
                 Enemy("Chaos Lord", 100, 500, 95, 70, 15)]
        enemy2 = []
        level_enemy = max(1, player_level + random.randint(-3, 3))
        for enemy1 in enemy:
            if level_enemy == enemy1.level:
                enemy2.append(enemy1)
        return random.choice(enemy2)


def Die_Player(player):
    if player.health == 0:
        print("Вы проиграли эту смертоносную битву ")
        return True


def Die_Enemy(enemy, player):
    if enemy.health == 0:
        print("Вы выиграли эту смертоносную битву ")
        if player.buff_dex > 0:
            player.buff_dex -= 1
        elif player.buff_strong > 0:
            player.buff_strong -= 1
        return True


def Attack(player, enemy):
    print(F"Вы встретили {enemy.name} , у него такое хп {enemy.health}")
    print(f"Нажмите 1 ,чтобы начать битву , нажмите 2 чтобы ее избежать ")
    choice1 = input("Введите дейстие :)  :(  ")
    while player.health > 0 and enemy.health > 0:
        if choice1 == "1":
            attack = input("Нажмите '1' ,чтобы ударить или '2' ,чтобы увернутся ")
            if attack == "1":
                player.health -= enemy.strong
                enemy.health -= player.strong
                die = Die_Player(player)
                die1 = Die_Enemy(enemy, player)
                print(f"У вас отнялось {enemy.strong} и у вас осталось {player.health}")
                if die:
                    return "Вы слили"
                elif die1:
                    return "Вы выиграли"
            elif attack == "2":
                if player.dex >= enemy.dex:
                    player.health += enemy.strong
                    if player.maxhealth <= player.health:
                        print("У вас максимум хп! =+=")
                        player.health = player.maxhealth
                    elif player.maxhealth > player.health:
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

        elif choice1 == "2":
            if enemy.speed > player.speed:
                print("Вам не удалось сбежать xD")
                attack1 = input("Нажмите '1' ,чтобы ударить или '2' ,чтобы увернутся ")
                if attack1 == "1":
                    player.health -= enemy.strong
                    enemy.health -= player.strong
                elif attack1 == "2":
                    if player.dex >= enemy.dex:
                        if player.maxhealth >= player.health:
                            print("У вас максимум хп! =+=")
                            player.health = player.maxhealth
                        elif player.maxhealth > player.health:
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


def poisk(player):
    poisk_list = ["empty", "enemy", "chest", "village", "hilling"]
    event = random.choice(poisk_list)

    event = "enemy"
    print("Исследование Территорие...")
    time.sleep(2)
    if event == "empty":
        print("Вы ничего не нашли , попробуйте еще раз.")
    elif event == "enemy":
        randen = Enemy.poisk_enemy(player.level)
        Attack(player, randen)
    elif event == "chest":
        randch = random.randint(10, 50)
        player.gold += randch
        print(f"Вам добавилось , {randch} золота , теперь ваш баланс {player.gold}!")
    elif event == "village":
        print("Вы встретили торговца! 'Не отходя от кассы!' ")
        village1 = Villager()
        while True:
            village1.Visual()
            village2 = int(input("Введите число от 0 до 4 , какой предмет хотите купить!     '6' чтобы выйти "))
            if village2 == 6:
                break
            village1.Buy(player, village2)
    elif event == "hilling":
        print("Вы встретили , лечебное озеро!")
        hill1 = random.randint(10, 30)
        player.health = min(player.maxhealth, player.health + hill1)
        print(f"У вас добавилось {hill1} хп , и теперь у вас {player.health} хп")


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
            {"name": "Защитный амулет", "price": 60, "type": "amulet", "value": 15,
             "description": "+15 к максимальному здоровью"},
        ]

    def Visual(self):
        print(f"Список : Вы вашли в лавку торговца!")
        for i, item in enumerate(self.items, 0):
            print(f"{i} Имя - {item["name"]} , Цена - {item["price"]} , Описание - {item["description"]}")

    def Buy(self, player, i):
        if 0 < i <= len(self.items) - 1:
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
    player = PLAYER(nick, "")
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

    cretrik = 0
    while player.health >= 0:
        cretrik += 1
        print("Нажмите '1' , чтобы 'исследовать территорию' .")
        print("Нажмите '2' , чтобы 'посмотреть инвентарь' .")
        print("Нажмите '3' , чтобы 'посмотреть характеристики' .")
        print("Нажмите '4' , чтобы 'выйти из игры!' .")
        var1 = int(input("Введите число "))
        if var1 == 1:
            poisk(player)
        elif var1 == 2:
            player.inv_show()
            if player.inv == True:
                var2 = input("Хотите использовать? (Yes or No")
                if var2 == "Yes":
                    var3 = int(input("Введите номер предмета "))
                    player.use_item(var3)
        elif var1 == 3:
            player.visible_origen()
        elif var1 == 4:
            print("Вы закончили игру :(")
            break
    if player.health <= 0:
        print(f"Вы исследовали {cretrik} районов. И умерли")

    # while vill == True and player.health > 0:


Brodilka()

# при прохождение игры нужно убить 3 босса , может появляться только после 20 исследования и будет прибавляться с каждым исследованием (1,2,3 ... 100)
