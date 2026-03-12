import random
import time
import sys


# --- TYPEWRITER EFFECT ---
def typewriter(text="", speed=0.03):
    for char in str(text):
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    sys.stdout.write("\n")

# Replace all print statements with typewriter
print = typewriter

def introduce(name):
    print(f"Hello {name}")
    print("Welcome to Castaway")


print()
name = input("What is your name? ")
introduce(name)
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
strings = 0
inventory = [wood, stone, metal, strings]  # This is the set inventory for game materials
inventory2 = []  # This is the additional inventory for tools and other str items


def check_inventory():
    print()
    answer = input("Would you like to check your inventory? ")
    if answer == "yes":
        print(f"Wood: {wood}")
        print(f"Metal: {metal}")
        print(f"Stone: {stone}")
        print(f"String: {strings}")
        for item in inventory2:
            print(item)
    else:
        print()
    print()

def recipe_book():
    print("~Recipe Book~")
    print("1. Fishing Rod (adds hunting event where you can get fish) ")
    print("* Requires 3 wood + 5 string")
    print()
    print("2. Pickaxe (when used, gives 5 stone and 15 metal immediately) ")
    print("* Requires 2 wood + 2 metal")
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
    global wood, strings

    if wood >= 3 and strings >= 5:
        print("...checking for necessary materials...")
        print("---Crafting Initiated---")
        print("you crafted a fishing rod!")
        inventory2.append("fishing rod")
        wood -= 3
        strings -= 5
    else:
        print("sorry, you do not have enough materials to craft this item")
        print()


def craft_pickaxe():
    print("Pickaxe: Requires 2 wood + 2 metal")
    global wood, metal

    if wood >= 2 and metal >= 2:
        print("...checking for necessary materials...")
        print("---Crafting Initiated---")
        print("you crafted a pickaxe!")
        inventory2.append("pickaxe")
        wood -= 2
        metal -= 3
    else:
        print("sorry, you do not have enough materials to craft this item")
        print()

def craft_sword():
    print("Sword: Requires 2 wood + 5 stone + 5 metal")
    global wood, stone, metal

    if wood >= 2 and stone >= 5 and metal >= 5:
        print("...checking for necessary materials...")
        print("---Crafting Initiated---")
        print("you crafted a sword!")
        inventory2.append("sword")
        wood -= 2
        stone -= 5
        metal -= 5
    else:
        print("sorry, you do not have enough materials to craft this item")
        print()

def craft_pot():
    print("Pot: Requires 20 metal")
    global metal

    if metal >= 20:
        print("...checking for necessary materials...")
        print("---Crafting Initiated---")
        print("you crafted a pot!")
        inventory2.append("pot")
        metal -= 20
    else:
        print("sorry, you do not have enough materials to craft this item")
        print()

def craft_shield():
    print("Shield: Requires 1 wood + 6 metal")
    global wood, metal

    if wood >= 1 and metal >= 6:
        print("...checking for necessary materials...")
        print("---Crafting Initiated---")
        print("you crafted a shield!")
        inventory2.append("shield")
        wood -= 1
        metal -= 6
    else:
        print("sorry, you do not have enough materials to craft this item")
        print()

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
    print("You find some cotton flowers that you stretch into usable string.")
    time.sleep(0.5)
    print("+ 2 string")
    global strings
    strings += 2


def gather5():
    print()
    print("You walk into a clear spider web and see a more thick webs hanging over the clearing.")
    time.sleep(0.5)
    print("+ 3 string")
    global strings
    strings += 3


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
print("You wake up and get up off of the bed that you made out of the coconut tree leaves, you take a quick dive in the ocean to wash your face. You come back up to the surface and see a white box floating towards you.")
print("You realize its a mail package. You pick it up and bring to the shade under the palm trees. You rip it open with your bare hands and find...")
print("Another box. But then you rip that one open and find...")
print("A hatchet!")
inventory2.append('hatchet')
check_inventory()
print("What shall you do with the hatchet?")
choice = input("1 - Build a base | 2 - Hunt: ")

if choice == "1":
    print()
    print("You use the hatchet to chop down trees and start building a small shelter.")
    print("By nightfall, you have a basic wooden base.")
    print("+ 20 wood")
    wood += 20

elif choice == "2":
    print()
    print("You grip the hatchet tightly and head into the deep forest, the heart of the island.")
    print("With your new tool, hunting just became a lot easier.")
    print("+ 20 hp")
    hp += 20
    print(f"HP: {hp}")
else:
    print("Invalid choice.")

print("After working all day you set 6 big stones in a cirlce, find some twigs, some dry leaves, and try to start a fire. It doesn't work. ")
print("You try again, but no flames appear.")
print("You need something to help you. You remember the package that gave you your most useful tool, the hatchet.")
print("Let's try to find some more packages.Where do you want to look first?")
choice = input("1 - Behind the huge stone rocks | 2 - In the plane carcass: ")
if choice == "1":
    print()
    print("You climb the rocks and find...")
    print("Nothing?")
    print("Let's try choice 2.")
    print()
    print("You walk towards the remains of the plane, it is destroyed with only the back half still in tact. You go inside, and find your current holy grail.")
    print("There are 3 packages scattered on the airplane floor, in almost perfect condition. You pick all of them up and run back to the base.")
    print("You decide that for each day that passes, you open a new package. You choose the one that you think is most likely to help you with the fire and... ")
    print("You did it! You found a lighter!")
    print("You scramble back to your fire and after a few clicks, it starts to burn. You blow on it hard and the flame starts to spread.")
    print("Congratulations, you now have a fire.")
elif choice == "2":
    print()
    print("You walk towards the remains of the plane, it is destroyed with only the back half still in tact. You go inside, and find your current holy grail.")
    print("There are 3 packages scattered on the airplane floor, in almost perfect condition. You pick all of them up and run back to the base.")
    print("You decide that for each day that passes, you open a new package. You choose the on that you think is most likely to help you with the fire and... ")
    print("You did it! You found a lighter!")
    print("You scramble back to your fire and after a few clicks, it starts to burn. You blow on it hard and the flame starts to spread.")
    print("Congratulations, you now have a fire.")
print("With this new accomplishment you now go to bed satisfied.")
print()

print("Day 3")
print()
print("You wake up and feel some invisible force telling you to get to work.")
print("Maybe it's warning you of something to come.")

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

print("It's still early in the morning and you've already done something good.")
print("You definitely feel like you can do a couple more things before nighttime.")
print()
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

print("While working, you see a treasure chest at the bottom of a lake")
print()
choice1 = input("Do you want to try to retrieve the chest?")
if choice1 == "yes":
    print("You dive into the lake headfirst, feeling the cold water shock your body.")
    print("You get your hands on the chest and feel the heavy weight of it, despite being in the water.")
    print("It's a struggle to pull the chest out of the sand and you feel your lungs burning for air.")
    print("- 25 hp")
    print("...")
    print("You pull the chest free!")
    print("You drag it onto the beach to reap your rewards")
    print()
    print("+ 5 wood")
    print("+ 10 metal")
    print("+ 2 string")
    print("+ dagger")
    print()
    inventory2.append("dagger")
    check_inventory()
    print(f"HP: {hp}")
else:
    print()
    print("You decide not to risk it.")
    
print()
print("You walk back home and decide to open another package from the plane crash.")
print("You crack open a nice looking package to see...a volleyball and some markers.")
print("It's obvious what you should do, so you take a marker and draw a smiley face on the volleyball.")
volleyball = input("What would you like to name your new volleyball friend? ")
print(f"You decide to name it {volleyball}.")
print()
print(f"Tired from the long day, you and {volleyball} go to sleep, prepared to survive together for the days to come.")
