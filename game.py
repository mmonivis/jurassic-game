from Hero import Hero
from Dino import Dino
from Dino import Veloc
from Dino import Coel
from Dino import Spino
from Dino import Tyran

from random import randint

# JURRASIC PARK RPG GAME

print "Hello! Welcome to Jurassic Park! We're excited to have you."
print "I'll be your tour guide today. What is your name?"
hero_name = raw_input("> ")
hero = Hero(hero_name)

print "Excellent! It's great to meet you, %s. How many dinosaurs do you think you'll see today?" % (hero_name)
num_of_dinos = int(raw_input("> "))

print "Wait, what's going on?! The theme park has been sabotaged..."
print "The power has gone out... The electric fences are shut down... The dinosaurs have escaped!"
print "Take this AK-47. RUN FOR THE EXIT!"

dino_types = [Veloc(), Coel(), Spino(), Tyran()]

dinos = []
for i in range(0,num_of_dinos):
    rand = randint(0,len(dino_types)-1)
    dinos.append(dino_types[rand])

for dino in dinos:
    # Run game as long as BOTH characters have health
    dino.health = dino.max_health
    while dino.health > 0 and hero.alive():
        print "====================="
        print "Oh no! You've encountered a %s" % dino.name
        print "====================="
        hero.print_status()
        dino.print_status()
        print "---------------------"
        print "What do you want to do?"
        print "1. Fight %s" % (dino.name)
        print "2. Do nothing"
        print "3. Flee"
        print "4. Use first aid kit"
        print "> ",
        user_input = raw_input()
        if user_input == "1":
            dino.receive_damage(hero.power)
            dino.print_status()
            if dino.health <= 0:
                hero.increase_health(20)

        elif user_input == "2":
            pass

        elif user_input == "3":
            print "You somehow outran the %s" % dino.name
            hero.flee()
            break

        elif user_input == "4":
            hero.increase_health(10)

        else:
            print "Invalid input %s" % user_input

        if dino.health > 0:
            # Hero has attacked (or not) AND goblin is still alive
            hero.health -= dino.power
            print "The %s hits you for %d damage." % (dino.name, dino.power)
            if hero.health <= 0:
                print "You became a morsel of food for the %s. :(" % (dino.name)