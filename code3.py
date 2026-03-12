print("Day 2")
print(
    "You wake up and get up off of the bed that you made out of the coconut tree leaves, you take a quick dive in the ocean to wash your face. You come back up to the surface and see a white box floating towards you.")
print(
    "You realize its a mail package. You pick it up and bring to the shade under the palm trees. You rip it open with your bare hands and find...")
print("Another box. But then you rip that one open and find...")
print("A hatchet!")
inventory2.append('hatchet')
check_inventory()
print("What sha'll you do with the hatchet?")
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
