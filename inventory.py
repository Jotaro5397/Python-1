playerinventory = ("sword", "bow", "key","tentacle sweeper", "broom")

playerinput = input("As you wander around the dungeon you step on a trap, the floor breaks,\n\ncrack!!!!\n\n you come to face with a huge tentacle beast hungry ready\nto attack... \n\n what will you do? : ")

playerinput = playerinput.lower()
if playerinput == "tentacle sweeper" and playerinput in playerinventory :
    print("\n\nwith one swoop of the tentacle sweeper,\n the beast has been defeated")
else:
    print("\n\n that weapon was not effective!\n\n the beast subdues you and it tentacles enter your body")
    print("\n\n YOU HAVE BEEN VIOLATED")
