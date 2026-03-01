import random
import time

print("Welcome to Castaway")
print()
#Here is where Anthony's background will be placed

name = input("What is your name?")
print("Hello, " + name)
time.sleep(1)
i = 0
hp = 100
print()
print(f"HP: {hp}")
print()
heal = 0
damage = 0
food = False
water = False
shelter = False
inventory = []

print("Day 1")
print("________")
time.sleep(2)
print("You wake up from a pleasant dream about fluffy clouds and unicorns")
time.sleep(1)
print("...and then you're brought back to reality")
print()
time.sleep(2)
print("You realize that you'll have to find food, shelter, and water if you want to survive. Every 5 days you must meet 3 needs, otherwise you lose")
print()
time.sleep(3)
print("You may choose 3 actions before night:")
time.sleep(1)

def explore1():
    print()
    print("You found a waterfall! + 5 hp")
    global heal
    heal = 5
    global hp
    hp += heal
    print(f"HP: {hp}")
def explore2():
    print()
    print("You found a cave! But it was occupied by bears. - 10 hp")
    global damage
    damage = 10
    global hp
    hp -= damage
    print(f"HP: {hp}")

explore_functions = [explore1, explore2]

def hunt1():
    print()
    print("You find a small bird tweeting in its nest.")
    time.sleep(0.5)
    print("You creep up to it but it flies away. There are, however, eggs in the nest that you can collect.")
    print("+ 5 hp")
    global heal
    heal = 5
    global hp
    hp += heal
    print(f"HP: {hp}")
def hunt2():
    print()
    print("You creep up on a big fat rabbit and pounce on it. Looks like its meat for dinner today.")
    print("+ 15 hp")
    global heal
    heal = 15
    global hp
    hp += heal
    print(f"HP: {hp}")
def hunt3():
    print()
    print("You find a plump pigeon sitting on a tree branch.")
    time.sleep(0.5)
    print("You try to climb the tree but fall and twist your ankle.")
    time.sleep(0.5)
    print("- 10 hp")
    global damage
    damage = 10
    global hp
    hp -= damage
    print(f"HP: {hp}")
def hunt4():
    print()
    print("You stumble upon what looks like a squirrel but is black and white striped.")
    time.sleep(0.5)
    print("You attack ti but quickly realize that it's actually a skunk.")
    time.sleep(0.5)
    print("- 20 hp")
    global damage
    damage = 20
    global hp
    hp -= damage
    print(f"HP: {hp}")

hunt_functions = [hunt1, hunt2, hunt3, hunt4]

action = int(input("1 - Explore | 2 - Hunt | 3 - Gather Materials"))
time.sleep(1)
if action == 1:
    print("...")
    time.sleep(2)
    random.choice(explore_functions)()
if action == 2:
    print("...")
    time.sleep(2)
    random.choice(hunt_functions)()
if action == 3:
    print("...")
    time.sleep(2)
    random.choice(gather_functions)()

