class PLAYER:
    def __init__(self, name, origen, clas):
        self.name = name
        self.origen = origen
        self.clas = clas
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
            self.armor = 0 #max 200
            self.thorns = 0 #max 10