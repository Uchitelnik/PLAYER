import random
import time
from enum import Enum
from logging import exception

shetovod = 0


class Rarity(Enum):
    common = "Обычный"
    rare = "Редкий"
    epic = "Эпический"
    legendary = "Легендарный"
    secret = "Секретный"


class Item:
    def __init__(self, name, rarity, item, value, price, description):
        self.name = name
        self.rarity = rarity
        self.item = item  # тип предмета
        self.value = value
        self.price = price
        self.description = description

    @staticmethod
    def generation_item(type="buff", player_level=10):
        try:
            value = 10
            price = 20
            item_random = random.randint(1, 100)
            if player_level >= 15 and item_random <= 5:
                rarity = Rarity.secret
                price_mult = 5
                value_mult = 5
            elif player_level >= 10 and item_random <= 10:
                rarity = Rarity.legendary
                price_mult = 4
                value_mult = 4
            elif player_level >= 5 and item_random <= 25:
                rarity = Rarity.epic
                price_mult = 3
                value_mult = 3
            elif player_level >= 3 and item_random <= 40:
                rarity = Rarity.rare
                price_mult = 2
                value_mult = 2
            elif player_level >= 1 and item_random <= 100:
                rarity = Rarity.common
                price_mult = 1
                value_mult = 1

            value = value * value_mult
            price = price * price_mult
            buff = ["Ловкости", "Силы"]
            random_buff = random.choice(buff)
            if type == "heal":
                name = "Зелье исцеления"
                description = f"Восстанавливает {value} здоровья"
            elif type == "buff":
                name = f"Зелье {random_buff}"
                description = f"Увелечивает {random_buff} на {value}"
            elif type == "weapon":
                name = f"{rarity} меч"
                description = f"Наносит {value} урона"
            else:
                name = f"{rarity} броня"
                description = f"Добавляет {value} хп"

            return Item(name, rarity, type, value, price, description)
        except Exception as e:
            print(f"Ошибка генерации предмета {e}")
            return Item("rur" , Rarity.common , "heal" , 10 , 20 , "Ошибка генерации предмета")

    @staticmethod
    def open_chest(player):
        chest_list1 = ["gold", "armor", "orugie"]
        chest_list = random.choice(chest_list1)
        if chest_list == "gold":
            randch = random.randint(10, 50)
            player.gold += randch
            print(f"Вам добавилось , {randch} золота , теперь ваш баланс {player.gold}!")
        elif chest_list == "armor":
            small_armor_list = ["shlem", "nagrudnik", "ponogi", "botinki"]
            randomchoice = random.choice(small_armor_list)
            print(f"Вы получили {randomchoice}")
            player.inv.append(Item.generation_item(player_level=player.level, type="armor"))

        elif chest_list == "orugie":
            print(f"Вы получили меч!")
            player.inv.append(Item.generation_item(player_level=player.level, type="weapon"))


class PLAYER:
    def __init__(self, name, origen):
        self.name = name
        self.origen = origen
        self.speed = 0  # на скорость удара
        self.brain = 0  # больее дешевые цены у торговца
        self.health = 0  # хп
        self.strong = 0  # сила удара
        self.inv = []
        self.dex = 0
        self.gold = 10000
        self.maxhealth = 0
        self.buff_strong = 0
        self.buff_dex = 0
        self.level = 1
        self.pxp = 0
        self.range_xp = 100
        self.talant = 0

    def xp_gave(self, exp):
        try:
            self.pxp += exp
            print(f"Вы получили {exp} ,у вас теперь {self.pxp}")
            while self.pxp >= self.range_xp:
                self.talant += 1
                self.level_up()
                self.pxp -= 100
            print(f"Получено {self.talant} уровней.")
            print(f"У вас отсалось {self.pxp - self.range_xp} xp до нового уровня")
        except ValueError as e:
            print(f"Ошибка {e}")

    def level_up(self):
        self.level += 1
        print("Вы повысили уровень.")
        print(f"Ваш уровень теперь {self.level}")
        print(f"У вас теперь {self.talant} очков таланта.")

    def player_up(self):
        try:
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
                    try:
                        choicen = int(input("Введите число. "))
                    except ValueError:
                        print("Ошибка введите число")
                        continue
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
        except Exception as e:
            print(f"Неожиданная ошибка при прокачке {e}")
            return False

    def inv_show(self):
        try:
            if not self.inv:
                print("Ваш инвентарь пустой")
            else:
                for i, item in enumerate(self.inv):
                    print(f"{i}. \nИмя: {item.name}")
                    print(f" Редкость: {item.rarity}")
                    print(f" Описание: {item.description}")
                    print(f" Цена: {item.price}")
                    print()
        except AttributeError as e:
            print(f"Ошибка прдмет в инвенторе имеет непраивльный формат {e}")
        except Exception as e:
            print(f"Ошибка при показе инвенторя {e}")

    def use_item(self, numinv):
        try:
            self.inv_show()
            item = self.inv[numinv]
            if item.item == "heal":
                if self.health == self.maxhealth:
                    print("У вас максимум хп и вы потратили зелье!")
                elif self.maxhealth - self.health <= item.value:
                    self.health = self.maxhealth
                else:
                    self.health += item.value
                self.inv.remove(item)

            elif item.item == "buff":
                if item in self.inv:
                    if "Сил" in item.description:
                        self.strong = self.strong + item.value
                        self.buff_strong = 3
                        print(f"Вы выпили зелье силы , ваша сила теперь {self.strong}.Длится {self.buff_strong} битвы. ")
                    elif "Ловк" in item.description:
                        self.buff_dex = 5
                        self.dex += item.value
                        print(f"Вы выпили зелье ловкости , ваша ловкость теперь {self.dex}.{self.buff_strong} ")
                    self.inv.remove(item)
            elif item.item == "weapon":
                self.strong += item.value
                print(f"У вас меч {item.rarity} , и добавилось {item.value} , силы")
                self.inv.remove(item)
            elif item.item == "armor":
                self.health += item.value
                print(f"У вас {item.rarity} броня , и дает вам +{item.value}хп")
                self.inv.remove(item)
        except IndexError as e:
            print(f"Ошибка {e}")
        except Exception as e:
            print(f"Неожиданная ошибка {e}")
        except AttributeError as e:
            print(f"Ошибка в формате {e}")

    def choice_origen(self, origen):
        try:
            self.origen = origen
            if self.origen == "people":  # Сбалансированный
                self.health = 100
                self.dex = 50
                self.strong = 20
                self.speed = 60
                self.brain = 70

                self.maxhealth = 100

            elif self.origen == "vampire":  # Высокое здоровье, средний урон
                self.health = 125
                self.dex = 40
                self.strong = 25
                self.speed = 50
                self.brain = 60
                self.maxhealth = 125

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
        except ValueError as e:
            print(f"Ошибка {e}")
        except Exception as e:
            print(f"Неожиданная ошибка {e}")

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

    @staticmethod
    def poisk_enemy(player_level):
        try:
            enemy = [
                Enemy("Скелет", 35, 50, 15, 25, 1, 150),
                Enemy("Зомби", 20, 80, 20, 10, 2, 250),
                Enemy("Гоблин", 60, 45, 18, 50, 3, 350),
                Enemy("Волк", 80, 40, 25, 70, 4, 450),
                Enemy("Орк", 45, 100, 35, 30, 5, 600),
                Enemy("Огненный элементаль", 70, 90, 40, 45, 6, 750),
                Enemy("Ледяной маг", 50, 80, 35, 60, 7, 850),
                Enemy("Земляной голем", 30, 180, 45, 20, 8, 1000),
                Enemy("Всадник бури", 90, 85, 38, 85, 9, 1100),
                Enemy("Темный рыцарь", 60, 140, 55, 50, 10, 1300),
                Enemy("Вампир-лорд", 85, 130, 50, 80, 11, 1500),
                Enemy("Гидра", 40, 250, 60, 35, 12, 1800),
                Enemy("Пожиратель разума", 75, 250, 55, 90, 13, 2500),
                Enemy("Дракон", 95, 350, 80, 70, 14, 3500),
                Enemy("Повелитель хаоса", 300, 400, 105, 140, 15, 4000)
            ]
            enemy2 = []
            level_enemy = max(1, player_level + random.randint(-3, 3))
            for enemy1 in enemy:
                if level_enemy == enemy1.level:
                    enemy2.append(enemy1)
            return random.choice(enemy2)
        except NameError as e:
            print(f"Ошибка {e}")


def Die_Player(player):
    try:
        if player.health == 0:
            print("Вы проиграли эту смертоносную битву ")
            return True
    except ValueError as e:
        print(e)


def Die_Enemy(enemy, player):
    try:
        global shetovod
        if enemy.health <= 0:
            print("Вы выиграли эту смертоносную битву ")
            if player.buff_dex > 0:
                player.buff_dex -= 1
            elif player.buff_strong > 0:
                player.buff_strong -= 1
            if enemy.name in ["Повелитель хаоса", "Дракон", "Пожиратель разума"]:
                shetovod += 1
            return True
    except NameError as e:
        print(e)


def Attack(player, enemy):
    global shetovod
    print(F"Вы встретили {enemy.name} , у него такое хп {enemy.health}")
    print(f"Нажмите 1 ,чтобы начать битву , нажмите 2 чтобы ее избежать ")
    try:
        choice1 = input("Введите дейстие :)  :(  ")
    except ValueError:
        print("Вы можете вводить только числа")
    while player.health > 0 and enemy.health > 0:
        if choice1 == "1":
            try:
                attack = input("Нажмите '1' ,чтобы ударить или '2' ,чтобы увернутся ")
            except ValueError:
                print("Вы можете вводить только числа")
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
                try:
                    attack = input("Нажмите '1' ,чтобы ударить или '2' ,чтобы увернутся ")
                except ValueError:
                    print("Вы можете вводить только числа")
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
    poisk_list = "enemy" #["empty", "enemy", "chest", "village", "hilling"]
    event = random.choice(poisk_list)
    print("Исследование Территорие...")
    time.sleep(2)
    if event == "empty":
        print("Вы ничего не нашли , попробуйте еще раз.")
    elif event == "enemy":
        randen = Enemy.poisk_enemy(player_level = player.level)
        Attack(player, randen)
    elif event == "chest":
        Item.open_chest(player)
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
        if player.health >= player.maxhealth:
            player.health = player.maxhealth
        print(f"У вас добавилось {hill1} хп , и теперь у вас {player.health} хп")


class Villager:
    def __init__(self):
        self.items = [
            Item.generation_item("buff"),
            Item.generation_item("heal"),
            Item.generation_item("heal"),
            Item.generation_item("buff"),
            Item.generation_item("buff")
        ]

    def Visual(self):
        print(f"Список : Вы вашли в лавку торговца!")
        for i, item in enumerate(self.items, 0):
            print(f"{i} Имя - {item.name} , Цена - {item.price} , Описание - {item.description}")

    def Buy(self, player, i):
        if 0 <= i <= len(self.items) - 1:
            item = self.items[i]
            if player.brain >= 50:
                item.price = item.price / 1.5
                if player.brain >= 75:
                    item.price = item.price / 1.5
                    if player.gold >= item.price:
                        player.gold -= item.price
                        player.inv.append(item)
                        print(
                            f"Вы успешно купили предмет {item.name}, поздравляю с покупкой! У вас осталось {player.gold} золото!")
                    else:
                        print("У вас не хватает денег!")
                else:
                    if player.gold >= item.price:
                        player.gold -= item.price
                        player.inv.append(item)
                        print(
                            f"Вы успешно купили предмет {item.name}, поздравляю с покупкой! У вас осталось {player.gold} золото!")
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
    while player.health >= 0 or shetovod < 3:
        cretrik += 1
        print("Нажмите '1' , чтобы 'исследовать территорию' .")
        print("Нажмите '2' , чтобы 'посмотреть инвентарь' .")
        print("Нажмите '3' , чтобы 'посмотреть характеристики' .")
        print("Нажмите '4' , чтобы 'улучшить характеристики' .")
        print("Нажмите '5' , чтобы 'выйти из игры!' .")
        try:
            var1 = int(input("Введите число "))
        except ValueError:
            print("Вы можете вводить только числа")
            continue
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
    elif shetovod == 3:
        print(f"Вы выиграли игру! Вы прошли {cretrik} районов! И смогли выиграть! Поздравляю!")

    # while vill == True and player.health > 0:
Brodilka()
# при прохождение игры нужно убить 3 босса , может появляться только после 20 исследования и будет прибавляться с каждым исследованием (1,2,3 ... 100)