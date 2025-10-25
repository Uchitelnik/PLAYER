class PLAYER:
    def __init__(self, name, origen):
        self.name = name
        self.origen = origen
        self.speed = 0
        self.brain = 0
        self.health = 0
        self.size = 0 #если будут стрелять , большой размер трудней увернутся
        self.strong = 0
        self.dex = 0
        self.atack_speed = 0
        self.thorns = 0
        self.armor = 0


    def choice_origen(self, origen):
        self.origen = origen
        if self.origen == "people":
            self.health = 150 #max = 200
            self.dex = 200 #max = 200
            self.strong = 15 #max = 50
            self.speed = 180 #max = 200
            self.atack_speed = 30 #max = 50
            self.brain = 80 #max = 100
            self.size = 170 #max = 170
            self.armor = 150 #max 200
            self.thorns = 0 #max 10

        if self.origen == "vampire":
            self.health = 200 #max = 200
            self.dex = 200 #max = 200
            self.strong = 20 #max = 50
            self.speed = 200 #max = 200
            self.atack_speed = 5 #max = 50
            self.brain = 100 #max = 100
            self.size = 160 #max = 170
            self.armor = 0 #max 200
            self.thorns = 10 #max 10

        if self.origen == "elf":
            self.health = 50 #max = 200
            self.dex = 20 #max = 200
            self.strong = 50 #max = 50
            self.speed = 100 #max = 200
            self.atack_speed = 30 #max = 50
            self.brain = 30 #max = 100
            self.size = 10 #max = 170
            self.armor = 120 #max 200
            self.thorns = 0 #max 10

        if self.origen == "robot":
            self.health = 200 #max = 200
            self.dex = 10 #max = 200
            self.strong = 10 #max = 50
            self.speed = 10 #max = 200
            self.atack_speed = 5 #max = 50
            self.brain = 100 #max = 100
            self.size = 170 #max = 170
            self.armor = 200 #max 200
            self.thorns = 0 #max 10

        if self.origen == "firekill":
            self.health = 30 #max = 200
            self.dex = 30 #max = 200
            self.strong = 30 #max = 50
            self.speed = 30 #max = 200
            self.atack_speed = 30 #max = 50
            self.brain = 30 #max = 100
            self.size = 30 #max = 170
            self.armor = 30 #max 200
            self.thorns = 30 #max 10

    def visible_origen(self):
        print(f"health - {self.health} \n"
              f" dex - {self.dex} \n"
              f" strong - {self.strong} \n"
              f" speed - {self.speed} \n"
              f" atack_speed - {self.atack_speed} \n"
              f" brain - {self.brain} \n"
              f" size = {self.size} \n"
              f" armor = {self.armor} \n"
              f" {self.thorns}")



class Enemy:
    def __init__(self, name , speed , brain , health , size , strong , dex , attack_speed):
        self.name = name
        self.speed = speed
        self.brain = brain
        self.health = health
        self.size = size
        self.strong = strong
        self.dex = dex
        self.attack_speed = attack_speed


def Attack(player , enemy):
    print(F"Вы встретили {enemy.name} , у него такое хп {enemy.health}")
     while player.health > 0 and enemy.health > 0:
         print(f"Нажмите 1 ,чтобы начать битву , нажмите 2 чтобы ее избежать ")
         choice1 = input("Введите дейстие :)  :(  ")