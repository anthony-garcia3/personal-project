import inquirer
import simpleaudio as sa
import threading
import random
import cmd,sys,textwrap
from colorama import Fore 
import commands

# Functions 



def play_audio():
    while True:
        wave_obj = sa.WaveObject.from_wave_file("Strange-House.wav")
        play_obj = wave_obj.play()
        play_obj.wait_done()

def inventory_option(arg):
    if len(INVENTORY) == 0:
        print("You're as broke as broke can be.")
        return
    item_count = {}
    for item in INVENTORY:
        if item in item_count.keys():
            item_count[item] += 1
        else:
            item_count[item] = 1

    print("Inventory: ")
    for item in set(INVENTORY):
        if item_count[item] > 1:
            print("  %s(%s)" % (item, item_count[item]))
        else:
            print(" ", item)
    print("\n")

inv = inventory_option


def show_options():

    while True:
        options = [
            inquirer.List(
                "action",
                message=Fore.CYAN + "What will you do?",
                choices=["Attack", "Check Inventory", "Run"])]
        choice = inquirer.prompt(options,theme=commands.PrettyTheme())
        if choice["action"] == "Attack":
            if random.random() <= FATALITY:
                print(victory_message)
                break
            else:
              print("You lack hatred. You will never survive being so pathetic.")
              continue
        elif choice["action"]== "Check Inventory":
            inventory_option(INVENTORY)
            continue
        elif choice["action"] == "Run":
            if random.random() <= COWARD:
                print("You escaped succesfully!")
                break
            else:
                print("You fool, you fail to even run properly.")
                continue

def displayLocation(loc):
    print(Fore.LIGHTYELLOW_EX + loc)
    print("=" * len(loc))
    print(DESC)

            

# Game ------------------------------------------------------------------------       


audio_thread = threading.Thread(target=play_audio)
audio_thread.start()

INVENTORY = []
HEALTH = 100
KARMA = 50
DURABILITY = 0
FATALITY = 0
COWARD = 0.40
SCREEN = 80
LOCATION = "Wendys"
NORTH = "north"
SOUTH = "south"
EAST = "east"
WEST = "west"
answers = {}
victory_message = None
DESC = f"{Fore.LIGHTYELLOW_EX}#1 fast food chain in america. This is not a paid sponsor.\n"


print("\nYou're a Wendy's employee that fell asleep during his shift.\n" + 
  "\nWhen you wake up the tv is showing that there has been a massive outbreak.\n" +
  "\nA zombie apocalypse took place while you slacked off.\n" + 
  "\nYou look to your left and there are three dead bodies in a table.\n" + 
  "\nA cop, a street fighter and a weeb with a katana.\n")

displayLocation(LOCATION)
Room_1_1 = [
    inquirer.List(
        "weapon",message=Fore.CYAN 
        +"Choose your weapon",choices=["Gun","Katana","Brass Knuckles"] )]
answers["Room_1_1"] = inquirer.prompt(Room_1_1, theme=commands.PrettyTheme())
weapon = answers["Room_1_1"]["weapon"]
if weapon == "Gun":
    DURABILITY = 10
    FATALITY = 1
elif weapon == "Katana":
    DURABILITY = 13
    FATALITY = 0.75
elif weapon == "Brass Knuckles":
    DURABILITY = 100
    FATALITY = 0.50

print("As you take your weapon the pathetic weeb starts waking up." 
      " You discover two things.\n" + "1. He became a zombie that killed the other guys" 
      " on the table.\n" + "2. He was as hungry dead as he was alive.\n" +
      f"{Fore.RED}!!! Zombie Weeb Steve sweeps for the kill !!!")

victory_message = "Zombie Weeb Steve dies(actually dies this time)"
"; never to binge watch anime and be a degenerate again."

print(answers["Room_1_1"]["weapon"])

show_options()








