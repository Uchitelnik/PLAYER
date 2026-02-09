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
        self.level = 1
        self.pxp = 0
        self.range_xp = 100
        self.talant = 0
    def xp_gave(self , exp):
        self.pxp += exp
        print(f"Вы получили {exp} ,у вас теперь {self.pxp}")
        while self.pxp >= self.range_xp:
            self.talant += 1
            self.level_up()
            self.pxp -= 100
        print(f"Получено {self.talant} уровней.")
        print(f"У вас отсалось {self.pxp - self.range_xp} xp до нового уровня")

    def level_up(self):
        self.level += 1
        print("Вы повысили уровень.")
        print(f"Ваш уровень теперь {self.level}")
        print(f"У вас теперь {self.talant} очков таланта.")
    def player_up(self):
        if self.talant <= 0:
            print("У вас не хватает очков таланта")
            return False
        else:
            while self.talant > 0:
                print(f"У вас {self.talant} очков таланта.")
                print("Нажмите '1' чтобы прокачать силу.")
                print("Нажмите '2' чтобы прокачать скорость.")
                print("Нажмите '3' чтобы прокачать ум.")
                print("Нажмите '4' чтобы прокачать хп.")
                print("Нажмите '5' чтобы прокачать ловкость.")
                print("Нажмите '6' чтобы выйти.")
                choicen = int(input("Введите число. "))
                if choicen == 1:
                    self.strong += 5
                    self.talant -= 1
                    continue
                elif choicen == 2:
                    self.speed += 5
                    self.talant -= 1
                    continue
                elif choicen == 3:
                    self.brain += 5
                    self.talant -= 1
                    continue
                elif choicen == 4:
                    self.maxhealth += 5
                    self.talant -= 1
                    continue
                elif choicen == 5:
                    self.dex += 5
                    self.talant -= 1
                    continue
                elif choicen == 6:
                    break
                else:
                    print("Не верно.Введите число от 1 до 6.")
            return True

    def inv_show(self):
        if not self.inv:
            print("Ваш инвентарь пустой")
        else:
            for i, item in enumerate(self.inv, 0):
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
        if self.origen == "people":  # Сбалансированный
            self.health = 100
            self.dex = 50
            self.strong = 20
            self.speed = 60
            self.brain = 70
            self.maxhealth = 100

        elif self.origen == "vampire":  # Высокое здоровье, средний урон
            self.health = 150
            self.dex = 40
            self.strong = 25
            self.speed = 50
            self.brain = 60
            self.maxhealth = 150

        elif self.origen == "elf":  # Высокий урон, низкое здоровье
            self.health = 70
            self.dex = 80
            self.strong = 30
            self.speed = 70
            self.brain = 50
            self.maxhealth = 70

        elif self.origen == "robot":  # Танк
            self.health = 180
            self.dex = 20
            self.strong = 15
            self.speed = 30
            self.brain = 90
            self.maxhealth = 180

        elif self.origen == "firekill":  # Стек урона
            self.health = 60
            self.dex = 60
            self.strong = 35
            self.speed = 65
            self.brain = 40
            self.maxhealth = 60

    def visible_origen(self):
        print(f"health - {self.health} \n"
              f"dex - {self.dex} \n"
              f"strong - {self.strong} \n"
              f"speed - {self.speed} \n"
              f"brain - {self.brain} \n"
              f"pxp - {self.pxp} \n"
              f"level - {self.level} \n"
              )


class Enemy:
    def __init__(self, name, speed, health, strong, dex, level, exp):
        self.name = name
        self.speed = speed
        self.health = health
        self.strong = strong
        self.dex = dex
        self.level = level
        self.exp = exp

    def poisk_enemy(player_level):
        enemy = [
            Enemy("Скелет", 30, 40, 10, 20, 1 , 100),
            Enemy("Зомби", 20, 60, 15, 10, 2 , 200),
            Enemy("Гоблин", 50, 35, 12, 40, 3 , 300),
            Enemy("Волк", 70, 30, 18, 60, 4 , 400),
            Enemy("Орк", 40, 80, 25, 25, 5 , 500),
            Enemy("Огненный элементаль", 60, 70, 30, 35, 6 , 600),
            Enemy("Ледяной маг", 45, 60, 22, 45, 7 , 700),
            Enemy("Земляной голем", 25, 120, 35, 15, 8 , 800),
            Enemy("Всадник бури", 80, 65, 28, 70, 9 , 900),
            Enemy("Темный рыцарь", 55, 100, 40, 40, 10, 1000),
            Enemy("Вампир", 75, 90, 35, 65, 11 , 1100),
            Enemy("Гидра", 35, 150, 45, 30, 12 , 1200),
            Enemy("Пожиратель разума", 65, 80, 32, 75, 13 , 1300),
            Enemy("Дракончик", 85, 110, 50, 55, 14 , 1400),
            Enemy("Повелитель хаоса", 90, 200, 60, 60, 15 , 1500)
        ]
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
    if enemy.health <= 0:
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
                print(f"Вы нанесли урон врагу '-{player.strong}' у него теперь '{enemy.health}' ")
                print(f"Вам нанесли урон '-{enemy.strong}' и у вас теперь '{player.health}'")
                die = Die_Player(player)
                die1 = Die_Enemy(enemy, player)
                if die:
                    return "Вы слили"
                elif die1:
                    player.xp_gave(enemy.exp)
                    return "Вы выиграли"
            elif attack == "2":
                if player.dex >= enemy.dex:
                    if player.maxhealth <= player.health:
                        print("У вас максимум хп! =+=")
                        player.health = player.maxhealth
                    elif player.maxhealth > player.health:
                        if player.dex > 30:
                            chens1 = random.randint(1, 20)
                            if chens1 == 1:
                                player.health += 5
                                print("+5 хп")
                        if player.dex > 50:
                            chens2 = random.randint(1, 10)
                            if chens2 == 1:
                                player.health += 5
                                print("+5 хп")
                        if player.dex > 100:
                            chens3 = random.randint(1, 5)
                            if chens3 == 1:
                                player.health += 5
                                print("+5 хп")
                        if player.dex > 150:
                            chens4 = random.randint(1, 3)
                            if chens4 == 1:
                                player.health += 5
                                print("+5 хп")
                        if player.dex == 200:
                            player.health += 7
                            print("+7 хп")
                        else:
                            player.health += 0
                else:
                    print("У врага больше ловкости чем у вас!")
                    player.health -= enemy.strong
                    print(f"Вам нанесли урон '-{enemy.strong}' и у вас теперь '{player.health}'")


        elif choice1 == "2":
            if enemy.speed > player.speed:
                print("Вам не удалось сбежать xD")
                attack = input("Нажмите '1' ,чтобы ударить или '2' ,чтобы увернутся ")
                if attack == "1":
                    player.health -= enemy.strong
                    enemy.health -= player.strong
                    print(f"Вы нанесли урон врагу '-{player.strong}' у него теперь '{enemy.health}' ")
                    print(f"Вам нанесли урон '-{enemy.strong}' и у вас теперь '{player.health}'")
                    die = Die_Player(player)
                    die1 = Die_Enemy(enemy, player)
                    if die:
                        return "Вы слили"
                    elif die1:
                        player.xp_gave(enemy.exp)
                        return "Вы выиграли"
                elif attack == "2":
                    if player.dex >= enemy.dex:
                        if player.maxhealth <= player.health:
                            print("У вас максимум хп! =+=")
                            player.health = player.maxhealth
                        elif player.maxhealth > player.health:
                            if player.dex > 30:
                                chens1 = random.randint(1, 20)
                                if chens1 == 1:
                                    player.health += 5
                                    print("+5 хп")
                            if player.dex > 50:
                                chens2 = random.randint(1, 10)
                                if chens2 == 1:
                                    player.health += 5
                                    print("+5 хп")
                            if player.dex > 100:
                                chens3 = random.randint(1, 5)
                                if chens3 == 1:
                                    player.health += 5
                                    print("+5 хп")
                            if player.dex > 150:
                                chens4 = random.randint(1, 3)
                                if chens4 == 1:
                                    player.health += 5
                                    print("+5 хп")
                            if player.dex == 200:
                                player.health += 7
                                print("+7 хп")
                            else:
                                player.health += 0
                    else:
                        print("У врага больше ловкости чем у вас!")
                        player.health -= enemy.strong
                        print(f"Вам нанесли урон '-{enemy.strong}' и у вас теперь '{player.health}'")
            else:
                print("Вам удалось сбежать!")
                return


        else:
            print("Ошибка , введите 1 или 2 ")
            continue


def poisk(player):
    poisk_list = ["empty", "enemy", "chest", "village", "hilling"]
    event = random.choice(poisk_list)
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
        print("Нажмите '4' , чтобы 'улучшить характеристики' .")
        print("Нажмите '5' , чтобы 'выйти из игры!' .")
        var1 = int(input("Введите число "))
        if var1 == 1:
            poisk(player)
        elif var1 == 2:
            player.inv_show()
            if player.inv:
                var2 = input("Хотите использовать? _Yes or No_      ")
                if var2 == "Yes":
                    var3 = int(input("Введите номер предмета "))
                    player.use_item(var3)
                else:
                    continue
        elif var1 == 3:
            player.visible_origen()
        elif var1 == 4:
            player.player_up()
        elif var1 == 5:
            print("Вы закончили игру :(")
            break
    if player.health <= 0:
        print(f"Вы исследовали {cretrik} районов. И умерли")

    # while vill == True and player.health > 0:


Brodilka()

# при прохождение игры нужно убить 3 босса , может появляться только после 20 исследования и будет прибавляться с каждым исследованием (1,2,3 ... 100)
