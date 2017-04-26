class Hero(object):
    def __init__(self, name):
        self.name = name
        self.health = 40
        self.power = 15
        self.max_health = self.health

    def alive(self):
        return self.health > 0

    def attack(self, enemy):
        if not self.alive():
            return
        print "%s attacks %s" % (self.name, enemy.name)
        enemy.receive_damage(self.power)

    def receive_damage(self, damage):
        self.health -= damage
        print "%s received %d damage." % (self.name, damage)
        if self.health <= 0:
            print "%s is dead." % self.name

    def print_status(self):
        print "%s has %d health and %d power." % (self.name, self.health, self.power)

    def increase_health(self, amount):
        self.health += amount
        if self.health > self.max_health:
            self.health = self.max_health
        print "You have time to tend your wounds. Your health has increased to %d!" % (self.max_health)

    def flee(self):
        self.health = 0