import random


class PLAYER:
    def __init__(self, name, origen):
        self.name = name
        self.origen = origen
        self.speed = 0 #на скорость удара
        self.brain = 0 #больше способностей и урона
        self.health = 0 #хп
        self.size = 0 #если будут стрелять , большой размер трудней увернутся
        self.strong = 0 #сила удара


    def choice_origen(self, origen):
        self.origen = origen
        if self.origen == "people":
            self.health = 150 #max = 200
            self.dex = 200 #max = 200
            self.strong = 15 #max = 50
            self.speed = 180 #max = 200
            self.brain = 80 #max = 100
            self.size = 170 #max = 170

        if self.origen == "vampire":
            self.health = 200 #max = 200
            self.dex = 200 #max = 200
            self.strong = 20 #max = 50
            self.speed = 200 #max = 200
            self.brain = 100 #max = 100
            self.size = 160 #max = 170

        if self.origen == "elf":
            self.health = 50 #max = 200
            self.dex = 20 #max = 200
            self.strong = 50 #max = 50
            self.speed = 100 #max = 200
            self.brain = 30 #max = 100
            self.size = 10 #max = 170

        if self.origen == "robot":
            self.health = 200 #max = 200
            self.dex = 10 #max = 200
            self.strong = 10 #max = 50
            self.speed = 10 #max = 200
            self.brain = 100 #max = 100
            self.size = 170 #max = 170

        if self.origen == "firekill":
            self.health = 30 #max = 200
            self.dex = 30 #max = 200
            self.strong = 30 #max = 50
            self.speed = 30 #max = 200
            self.brain = 30 #max = 100
            self.size = 30 #max = 170

    def visible_origen(self):
        print(f"health - {self.health} \n"
              f" dex - {self.dex} \n"
              f" strong - {self.strong} \n"
              f" speed - {self.speed} \n"
              f" brain - {self.brain} \n"
              f" size = {self.size} \n")



class Enemy:
    def __init__(self, name , speed , brain , health , size , strong , dex , attack_speed):
        self.name = name
        self.speed = speed
        self.brain = brain
        self.health = health
        self.size = size
        self.strong = strong
        self.dex = dex


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
            elif attack == "2":
                    if max_hp <= player.health:
                        print("У вас максимум хп! =+=")
                        player.health = max_hp
                    elif max_hp > player.health:
                        if player.dex > 30:
                            chens1 = random.randint(1 , 20)
                            if chens1 == 1:
                                player.health + 10
                        elif player.dex > 50:
                            chens2 = random.randint(1, 10)
                            if chens2 == 1:
                                player.health + 10
                        elif player.dex > 100:
                            chens3 = random.randint(1, 5)
                            if chens3 == 1:
                                player.health + 10
                        elif player.dex > 150:
                            chens4 = random.randint(1, 3)
                            if chens4 == 1:
                                player.health + 10
                        elif player.dex = 200:
                            chens5 = random.randint(1, 1)
                            if chens5 == 1:
                                player.health + 10              #надо сделать чтобы не с 30 ловкости допустим, а с 30 до 50 и так далее все!



        elif choice1 == "2":
            if enemy.speed > player.speed:
                print("Вам не удалось сбежать xD")
                attack = input("Нажмите '1' ,чтобы ударить или '2' ,чтобы увернутся ")
                if attack == "1":
                    player.health -= enemy,strong
                    enemy.health -= player.strong
                elif attack == "2":
                    player.health += 5
                    enemy.health -= 0
                else:
                    print("Вам удалось сбежать!")

        else:
            print("Ошибка , введите 1 или 2 ")



