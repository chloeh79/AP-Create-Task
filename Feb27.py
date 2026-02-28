import pygame
import random

print("Castaway")
#Here is where Anthony's background will be placed

i = 0
hp = 100
heal = 0
damage = 0
food = false
water = false
shelter = false
inventory = []

print("Day 1")
print("You wake up from a pleasant dream about fluffy clouds and unicorns")
print("...and then you're brought back to reality")
print("You realize that you'll have to find food, shelter, and water if you want to survive")

print("Every 5 days you must have all 3 needs, otherwise you lose")

print("You may choose 3 actions before night")
action = int(input("1 - Explore | 2 - Hunt | 3 - Gather Materials"))
if action == 1:
    random.choice(explore_functions)()


def explore1():
    print("a waterfall! + 5 hp")
    global heal
    heal = 5
    global hp
    hp += heal

def explore2():
    print("a cave! But it was occupied by bears. - 10 hp")
    global damage
    damage = 10
    global hp
    hp -= damage

explore_functions = [explore1, explore2]