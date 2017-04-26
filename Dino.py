class Dino(object):
    def __init__(self):
        self.health = 5
        self.power = 1

    def alive(self):
        return self.health > 0

    def attack(self, enemy):
        if not self.alive():
            return
        print "%s attacks %s" % (self.name, enemy.name)
        enemy.receive_damage(self.power)
        # time.sleep(1.5)

    def receive_damage(self, damage):
        self.health -= damage
        print "%s received %d damage." % (self.name, damage)
        if self.health <= 0:
            print "%s is dead." % self.name

    def print_status(self):
        print "%s has %d health and %d power." % (self.name, self.health, self.power)

class Veloc(Dino):
    def __init__(self):
        self.name = "Velociraptor"
        self.health = 10
        self.power = 3
        self.max_health = self.health

class Coel(Dino):
    def __init__(self):
        self.name = "Coelophysis Bauri"
        self.health = 20
        self.power = 6
        self.max_health = self.health

class Spino(Dino):
    def __init__(self):
        self.name = "Spinosaurus"
        self.health = 30
        self.power = 12
        self.max_health = self.health

class Tyran(Dino):
    def __init__(self):
        self.name = "Tyrannosaurus Rex"
        self.health = 40
        self.power = 15
        self.max_health = self.health