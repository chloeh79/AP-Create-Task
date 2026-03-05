import random
import time
import sys


# --- TYPEWRITER EFFECT ---
def typewriter(text="", speed=0.00):
    for char in str(text):
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    sys.stdout.write("\n")


# Replace all print statements with typewriter
print = typewriter

print("Welcome to Castaway")
print()
print(
    "POV: you are sitting in an airplane and all of a sudden it starts shaking, violently. You look out the window and see the engine is on fire. The plane starts going down, fast. But before this lets go to a flashback.")
print(
    "You are a mailman who has to fly on planes to deliver mail. It's the end of the year and you can smell the bonus. But, your last plane's number is 444, the world's unluckiest number. Now your confronted with 2 choices:")
print("Deliver those packages, or no bonus. But obviously we take the bonus so we can larp margiela gats.")
print(
    "Now lets cut back, your seconds away from crashing into the water, you grip the seat and pray to your God. Everything goes black.")
print(
    "You wake up again and spew out the sand in your mouth, your lips are crusted dry and the sun blazed your skin. Looks like you've out for a while. ")
print(
    "You get up, dust the sand off of you, pick up your head, and you see: palm trees, seagulls, and only the ocean is behind you. You here the water crashing down, and realize, you're on a deserted island")
print("Day 1 starts:")

time.sleep(1)
i = 0
hp = 100
print()
print(f"HP: {hp}")
print()
food = False
water = False
shelter = False
wood = 0
stone = 0
metal = 0
cloth = 0
string = 0
inventory = [wood, stone, metal, cloth, string]  # This is the set inventory for game materials
inventory2 = []  # This is the additional inventory for tools and other str items


def check_inventory():
    print()
    answer = input("Would you like to check your inventory? ")
    if answer == "yes":
        print(f"Wood: {wood}")
        print(f"Metal: {metal}")
        print(f"Cloth: {cloth}")
        print(f"Stone: {stone}")
        print(f"String: {string}")
        for item in inventory2:
            print(item)


def recipe_book():
    print("~Recipe Book~")
    print("1. Fishing Rod (adds hunting event where you can get fish) ")
    print("* Requires 3 wood + 5 string")
    print()
    print("2. Pickaxe (when used, gives 5 stone and 15 metal immediately) ")
    print("* Requires 2 wood + 3 stone")
    print()
    print("3. Sword (adds hunting event where you can kill animals for food) ")
    print("* Requires 2 wood + 5 stone + 5 metal")
    print()
    print("4. Pot (gives + 30 hp) ")
    print("* Requires 20 metal")
    print()
    print("5. Shield (you might need this later) ")
    print("Requires 1 wood + 6 metal")

def craft_fishing_rod():
    print("Fishing Rod: Requires 3 wood + 5 string")

def craft_pickaxe():
    print("Pickaxe: Requires 2 wood + 3 stone")

def craft_sword():
    print("Sword: Requires 2 wood + 5 stone + 5 metal")

def craft_pot():
    print("Pot: Requires 20 metal")
    
def craft_shield():
    print("Shield: Requires 1 wood + 6 metal")

def craft():
    print()
    answer2 = input("Would you like to check the crafting recipe book?")
    if answer2 == "yes":
        recipe_book()
    else:
        print()
    answer2 = input("What would you like to craft?")
    if answer2 == "1" or "fishing rod":
        craft_fishing_rod()
    elif answer2 == "2" or "pickaxe":
        craft_pickaxe()
    elif answer2 == "3" or "sword":
        craft_sword()
    elif answer2 == "4" or "pot":
        craft_pot()
    elif answer2 == "5" or "shield":
        craft_shield()


time.sleep(2)
print("You wake up from a pleasant dream about fluffy clouds and unicorns")
print("...and then you're brought back to reality")
print()
print("You realize that you might be here for a while...hopefully not more than 30 days")
print()
print("You may pick one action before night:")


def explore1():
    print()
    print("You found a waterfall! + 5 hp")
    global hp
    hp += 5
    print(f"HP: {hp}")


def explore2():
    print()
    print("You found a cave! But it was occupied by bears. - 10 hp")
    global hp
    hp -= 10
    print(f"HP: {hp}")


explore_functions = [explore1, explore2]


def hunt1():
    print()
    print("You find a small bird tweeting in its nest.")
    time.sleep(0.5)
    print("You creep up to it but it flies away. There are, however, eggs in the nest that you can collect.")
    print("+ 5 hp")
    global hp
    hp += 5
    print(f"HP: {hp}")


def hunt2():
    print()
    print("You creep up on a big fat rabbit and pounce on it. Looks like its meat for dinner today.")
    print("+ 15 hp")
    global hp
    hp += 15
    print(f"HP: {hp}")


def hunt3():
    print()
    print("You find a plump pigeon sitting on a tree branch.")
    time.sleep(0.5)
    print("You try to climb the tree but fall and twist your ankle.")
    time.sleep(0.5)
    print("- 10 hp")
    global hp
    hp -= 10
    print(f"HP: {hp}")


def hunt4():
    print()
    print("You stumble upon what looks like a squirrel but is black and white striped.")
    time.sleep(0.5)
    print("You attack ti but quickly realize that it's actually a skunk.")
    time.sleep(0.5)
    print("- 20 hp")
    global hp
    hp -= 20
    print(f"HP: {hp}")


hunt_functions = [hunt1, hunt2, hunt3, hunt4]


def gather1():
    print()
    print("You pick up sticks that fell from a sturdy tree.")
    time.sleep(0.5)
    print("+ 3 wood")
    global wood
    wood += 3


def gather2():
    print()
    print("You found some scraps of metal leftover from the airplane crash.")
    time.sleep(0.5)
    print("+ 2 metal")
    global metal
    metal += 2


def gather3():
    print()
    print("You collect some nice rocks that look easy to shape.")
    time.sleep(0.5)
    print("+ 3 stone")
    global stone
    stone += 3


def gather4():
    print()
    print("You find some cotton flowers that you stretch into usable cloth.")
    time.sleep(0.5)
    print("+ 2 cloth")
    global cloth
    cloth += 2


def gather5():
    print()
    print("You walk into a clear spider web and see a more thick webs hanging over the clearing.")
    time.sleep(0.5)
    print("+ 3 string")
    global string
    string += 3


gather_functions = [gather1, gather2, gather3, gather4]

action = int(input("1 - Explore | 2 - Hunt | 3 - Gather Materials "))
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
    check_inventory()

print()
print("- night -")
time.sleep(0.5)
print("It's hard to fall asleep on the ground without a shelter, but you manage.")
time.sleep(2)

print("Day 2")
print(
    "You wake up and get up off of the bed that you made out of the coconut tree leaves, you take a quick dive in the ocean to wash your face. You come back up to the surface and see a white box floating towards you.")
print(
    "You realize its a mail package. You pick it up and bring to the shade under the palm trees. You rip it open with your bare hands and find...")
print("Another box. But then you rip that one open and find...")
print("A hatchet!")
inventory2.append('hatchet')
check_inventory()

print("What will you do with the hatchet?")
choice = input("1 - Build a base | 2 - Hunt: ")
if choice == "1":
    print()
    print("You use the hatchet to chop down trees and start building a small shelter.")
    print("By nightfall, you have a basic wooden base to protect you from... them.")
    print("+ 20 wood")
    wood += 20
    check_inventory()
elif choice == "2":
    print()
    print("You grip the hatchet tightly and head into the deep forest, the heart of the island.")
    print("With your new tool, hunting just became a lot easier.")
    print("+ 20 hp")
    hp += 20
    print(f"HP: {hp}")
else:
    print("Invalid choice")
