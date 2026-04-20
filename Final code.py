import random
import time
import sys

# AI assisted
# --- TYPEWRITER EFFECT ---
def typewriter(text="", speed=0.03):
    for char in str(text):
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    sys.stdout.write("\n")


# Replace all print statements with typewriter
print = typewriter

# coded by partner 1
# procedure introduces the user to the game
def introduce(name):
    print(f"Hello {name}")
    print("Welcome to Castaway")


print()
name = input("What is your name? ")
introduce(name)
# coded by partner 2
print(
    "POV: you are sitting in an airplane and all of a sudden it starts shaking, violently. You look out the window and see the engine is on fire. The plane starts going down, fast. But before this let's go to a flashback.")
print(
    "You are a mailman who has to fly on planes to deliver mail. It's the end of the year and you can smell the bonus. But, your last plane's number is 444, the world's unluckiest number. Now your confronted with 2 choices:")
print("Deliver those packages, or no bonus. But obviously we take the bonus so we can larp margiela gats.")
print(
    "Now lets cut back, your seconds away from crashing into the water, you grip the seat and pray to your God. Everything goes black.")
print(
    "You wake up again and spew out the sand in your mouth, your lips are crusted dry and the sun blazed your skin. Looks like you've out for a while. ")
print(
    "You get up, dust the sand off of you, pick up your head, and you see: palm trees, seagulls, and only the ocean is behind you. You hear the water crashing down, and realize, you're on a deserted island")
print("Day 1 starts:")

# coded by partner 1
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

# This procedure checks the values of the item variables and prints them out for the user
# It also prints any collected tools from inventory2
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

# This procedure and the following craft procedures allow you to use the items in your inventory to create a tool for inventory2
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
    global wood, metal, stone

    if wood >= 2 and metal >= 2:
        print("...checking for necessary materials...")
        print("---Crafting Initiated---")
        print("you crafted a pickaxe!")
        inventory2.append("pickaxe")
        wood -= 2
        metal -= 3
        print("+ 5 stone")
        print("+ 15 metal")
        metal += 15
        stone += 5
    else:
        print("sorry, you do not have enough materials to craft this item")
        print()
    check_inventory()

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
    print("Pot: Requires 10 metal")
    global metal

    if metal >= 10:
        print("...checking for necessary materials...")
        print("---Crafting Initiated---")
        print("you crafted a pot!")
        inventory2.append("pot")
        metal -= 10
        print("+ 30 hp")
        print(f"HP: {hp}")
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

# This is the crafting procedure that calls the individual craft procedures above
def craft():
    print()
    answer3 = input("Would you like to check the crafting recipe book? ")
    if answer3 == "yes":
        print("~Recipe Book~")
        print("1. Fishing Rod")
        print("* Requires 3 wood + 5 string")
        print()
        print("2. Pickaxe (when used, gives 5 stone and 15 metal immediately) ")
        print("* Requires 2 wood + 2 metal")
        print()
        print("3. Sword")
        print("* Requires 2 wood + 5 stone + 5 metal")
        print()
        print("4. Pot (gives + 30 hp) ")
        print("* Requires 20 metal")
        print()
        print("5. Shield")
        print("Requires 1 wood + 6 metal")
        answer2 = input("What do you want to craft? (1-5 or name of item) ")
        if answer2 == "1" or answer2.lower() == "fishing rod":
            craft_fishing_rod()
        elif answer2 == "2" or answer2.lower() == "pickaxe":
            craft_pickaxe()
        elif answer2 == "3" or answer2.lower() == "sword":
            craft_sword()
        elif answer2 == "4" or answer2.lower() == "pot":
            craft_pot()
        elif answer2 == "5" or answer2.lower() == "shield":
            craft_shield()
        else:
            print("Invalid choice.")


time.sleep(2)
print("You wake up from a pleasant dream about fluffy clouds and unicorns")
print("...and then you're brought back to reality")
print()
print("You realize that you might be here for a while...hopefully not more than 30 days")
print()
print("You may pick one action before night:")

# adding explore events to a list that can be randomly chosen from
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

# adding hunt events to a list that can be randomly chosen from
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
    print("You attack it but quickly realize that it's actually a skunk.")
    time.sleep(0.5)
    print("- 20 hp")
    global hp
    hp -= 20
    print(f"HP: {hp}")


hunt_functions = [hunt1, hunt2, hunt3, hunt4]

# adding gather events to a list that can be randomly chosen from
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

def gather6():
    print()
    print("You grab some metal scraps from the leftover plane crash")
    time.sleep(0.5)
    print("+ 5 metal")
    global metal
    metal += 5

gather_functions = [gather1, gather2, gather3, gather4, gather5, gather6]

# procedure where user chooses an action which outputs a random event from the action lists
def user_action(num):
    for _ in range(num):
        print("\n--- Choose Action ---")
        try:
            action = int(input("1 - Explore | 2 - Hunt | 3 - Gather Materials: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        time.sleep(0.5)
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

user_action(1)
print()
print("- night -")
time.sleep(0.5)
print("It's hard to fall asleep on the ground without a shelter, but you manage.")
time.sleep(2)

# coded by partner 2
print("Day 2")
print(
    "You wake up and get up off of the bed that you made out of the coconut tree leaves, you take a quick dive in the ocean to wash your face. You come back up to the surface and see a white box floating towards you.")
print(
    "You realize its a mail package. You pick it up and bring to the shade under the palm trees. You rip it open with your bare hands and find...")
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

print(
    "After working all day you set 6 big stones in a circle, find some twigs, some dry leaves, and try to start a fire. It doesn't work. ")
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
    print(
        "You walk towards the remains of the plane, it is destroyed with only the back half still intact. You go inside, and find your current holy grail.")
    print(
        "There are 3 packages scattered on the airplane floor, in almost perfect condition. You pick all of them up and run back to the base.")
    print(
        "You decide that for each day that passes, you open a new package. You choose the one that you think is most likely to help you with the fire and... ")
    print("You did it! You found a lighter!")
    print(
        "You scramble back to your fire and after a few clicks, it starts to burn. You blow on it hard and the flame starts to spread.")
    print("Congratulations, you now have a fire.")
elif choice == "2":
    print()
    print(
        "You walk towards the remains of the plane, it is destroyed with only the back half still in tact. You go inside, and find your current holy grail.")
    print(
        "There are 3 packages scattered on the airplane floor, in almost perfect condition. You pick all of them up and run back to the base.")
    print(
        "You decide that for each day that passes, you open a new package. You choose the on that you think is most likely to help you with the fire and... ")
    print("You did it! You found a lighter!")
    print(
        "You scramble back to your fire and after a few clicks, it starts to burn. You blow on it hard and the flame starts to spread.")
    print("Congratulations, you now have a fire.")
print("With this new accomplishment you now go to bed satisfied.")
print()

# coded by partner 1
print("Day 3")
print()
print("You wake up and feel some invisible force telling you to get to work.")
print("Maybe it's warning you of something to come.")
print()
user_action(3)

print()

print("While working, you see a treasure chest at the bottom of a lake")
print()
choice1 = input("Do you want to try to retrieve the chest? ")
if choice1 == "yes":
    print("You dive into the lake headfirst, feeling the cold water shock your body.")
    print("You get your hands on the chest and feel the heavy weight of it, despite being in the water.")
    print("It's a struggle to pull the chest out of the sand and you feel your lungs burning for air.")
    print("- 25 hp")
    hp += 25
    print("...")
    print("You pull the chest free!")
    print("You drag it onto the beach to reap your rewards")
    print()
    print("+ 5 wood")
    print("+ 10 metal")
    print("+ 2 string")
    print("+ dagger")
    wood += 5
    metal += 10
    strings += 2
    print()
    inventory2.append("dagger")
    check_inventory()
    print(f"HP: {hp}")
else:
    print()
    print("You decide not to risk it.")


print()
print("You have been working all day and think that some tools might be helpful.")
craft()
print()
choice2 = input("Would you like to craft again? ")
if choice2 == "yes":
    craft()
else:
    print()

print()
print("You walk back home and decide to open another package from the plane crash.")
print("You crack open a nice looking package to see...a volleyball and some markers.")
print("It's obvious what you should do, so you take a marker and draw a smiley face on the volleyball.")
volleyball = input("What do you want to name your new volleyball friend? ")
print(f"You decide to name it {volleyball}.")
print()
print(f"Tired from the long day, you and {volleyball} go to sleep, prepared to survive together for the days to come.")

print()
print("In the middle of the night you hear a growl in the darkness...")
print("You wake up to see a bear right outside of your base, stalking you with hungry eyes.")
print(f"It seems to be hunting...{volleyball}?")
print("Not on your watch.")
print()
print(f"The bear launches itself towards you and {volleyball}")
print(f"Current Inventory: {inventory2}")
item_use = input("Which item would you like to use? ")
if item_use in inventory2:
    print()
    print(f"You pull out your {item_use} and step in front of {volleyball}")
    print("You fight with all your might against the bear and successfully make it back off.")
    print(f"The bear runs away, slightly wounded and you cheer and hug {volleyball}.")
    print()
    print("You fall back asleep peacefully.")
else:
    print()
    print(f"You step forward bravely in front of {volleyball}.")
    print("The bear charges towards you and you yell at it and make yourself bigger.")
    print("Your yelling throws the bear off but not before it scratches your leg.")
    print("- 20 hp")
    print("The bear runs away.")
    print(f"You curl up next to {volleyball} and go back to sleep")

# coded by partner 2
print("Day 4 begins.")
print(f"You wake up and see {volleyball} right by your side. You guys have a friendly little chat.")
print(f"You tell {volleyball} about what your life was like before you got trapped on this little Island. You remember the tasty food, the beautiful skyscrapers, you even start to miss your boss.")
print("Then it hits you. You need to go back home. Even if you didn't finish the job, the company would still reimburse you and you would get even more than the actual bonus.")
print("So you make a plan.")
print("1st: You gather all the wood, twigs, vines, and a rag that washed up on the shore.")
print("2nd: You use your hatchet to cut and shape the materials to your liking.")
print("3rd: You use the vines to tie everything together.")
print(f"4th: You make a comfy and safe spot for {volleyball}.")
print("5th: You gather everything you think your gonna need to make it back to your home.")
print("Finally: You attach the rag as your sail and push it into the water. You jump on and start to sail. 'It works! It really works!' You say to yourself.")
print("Everything seemed to be going fine until you see a black and fast moving storm up ahead. You are too far into the journey to turn back now.")
print(f"'WE MUST FIGHT IT!' You scream to {volleyball} as the lightning strikes and the waves crash.")
print("But when you turn back around, A huge wave crashes right onto your boat.")
print("Everything goes black...")
print("You wake up again, and see the sun, you pick yourself up and see that you are still on your little raft.")
print(f"You check to see where {volleyball} is but he is nowhere to be found. Until you see a faint white ball in the distance. You use your arms to paddle towards it as fast as you can, but its just plastic.")
print("You have now lost your only friend since the crash, the only thing keeping you going is the last package which luckily is still there.")
print("You here a splashing noise behind you and when you turn around you see a bunch of flying carp coming right at you.")
print("You lie down on your raft covering your head, and once they pass you look back from where they came and see a giant cruise.")
print("You scream for help, wave your hands, anything to get the cruise's attention and then you pass out from dehydration and malnourishment.")
print("You wake up in a hospital, with flowers and cards on the desk next to you. You also notice the last package is propped up against the wall.")
print(f"But sadly, {volleyball} is nowhere to be found.")
print("A few hours pass before the hospital admits you to leave, you take your package, and start to drive.")
print("For some reason you feel really dedicated to delivering this package, I mean, it has been your only hope on the island.")
print("You arrive to the home, ring the doorbell, and wait. A kind old man in a white beater and jorts walks out.")
print("He complains about the late delivery and the damaged packaging but you just leave without really caring. You feel a sense of fulfillment.")
print("You drive into the sunset as the old man opens his package back at his home. He takes out what seems to be a Satellite Messenger. This whole time, rescue could have been a lot easier.")
print("                                                                               ...The End...")
