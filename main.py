from classes.game import Person, bcolors

magic = [{"name": "Fire", "cost": 10, "dmg": 60},
         {"name": "Thunder", "cost": 12, "dmg": 80},
         {"name": "Blizzard", "cost": 10, "dmg": 60}]

player = Person(460, 65, 60, 34, magic)

enemy = Person(1200, 65, 45, 25, magic)

running = True
print(bcolors.FAIL + bcolors.BOLD + "AN EMEMY ATTACKS!" + bcolors.ENDC)

while running:
    print ("========================")
    player.choose_action()
    choice = input("Choose actions:")
    index = int(choice) - 1
    print("You chose", index)

    running = False
