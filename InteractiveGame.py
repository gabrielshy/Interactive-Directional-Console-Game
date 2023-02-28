"""
Interactive Game by Francis Gabriel Anos
- Be able to look in 4 directions
- Be able to interact with objects

Error notes:
Fridge wont work properly
"""

from os import ftruncate
import random
import time
from datetime import datetime
from types import TracebackType

now = datetime.now()
current_time = now.strftime("%H:%M:%S")


class Light:
    def __init__(self, on_off="On"):
        self.on = "On"
        self.off = "Off"
        self.on_off = on_off

    def turnOn(self):
        self.on_off = self.on

    def turnOff(self):
        self.on_off = self.off

    def lightStatus(self):
        return self.on_off


class Door:
    def __init__(self, open_close):
        self.open = "Open"
        self.close = "Closed"
        self.open_close = open_close

    def openDoor(self):
        self.open_close = self.open

    def closeDoor(self):
        self.open_close = self.close

    def doorStatus(self):
        return self.open_close


class Curtains:
    def __init__(self, open_close):
        self.open = "Open"
        self.close = "Closed"
        self.open_close = open_close

    def openCurtain(self):
        self.open_close = self.open

    def closeCurtain(self):
        self.open_close = self.close

    def curtainStatus(self):
        return self.open_close


class Bed:
    def __init__(self):
        super().__init__()
        self.sleep = "Asleep"
        self.awake = "Awake"
        self.sleep_awake = ''

    def sleeping(self):
        self.sleep_awake = "Asleep"

    def awake(self):
        self.sleep_awake = "Awake"


class Item:
    def __init__(self, item_name=''):
        self.item_name = item_name
        self.take = True
        self.discard = False
        self.in_inventory = True

    def takeItem(self):
        self.in_inventory = self.take
        inventory.append(self.item_name)

    def discardItem(self, item_name):
        self.in_inventory = self.discard
        inventory.remove(self.item_name)

    def itemStatus(self):
        return self.in_inventory


class Appliance:
    def __init__(self, on_off="On"):
        self.on = "On"
        self.off = "Off"
        self.on_off = on_off

    def turnOn(self):
        self.on_off = self.on

    def turnOff(self):
        self.on_off = self.off

    def applianceStatus(self):
        return self.on_off


name = input("Enter Name: ")
print(f"Welcome {name}, this is an interactive game\n"
      f"that allows you to look in four directions\n"
      f"and interact with objects.")

start = str(input("Start? y/n "))

inventory = []

# Areas that you can interact with
l1switch = Light(on_off="On")
d1door = Door(open_close="Closed")
d2door = Door(open_close="Closed")
d2closet = Door(open_close="Closed")
c1curtain = Curtains(open_close="Closed")
m1microwave = Appliance(on_off="Off")
b1bed = Bed()

# items
teddy_bear = Item("Teddy Bear")
fridgeContents = ["apples", "jar", "bear"]



def directions(direction, c):
    def changeDir(look, direction):

        if direction == "North":
            if look == "Left":
                mainWest(c)
            elif look == "Right":
                mainEast(c)
        if direction == "West":
            if look == "Left":
                mainSouth(c)
            elif look == "Right":
                mainNorth(c)
        if direction == "South":
            if look == "Left":
                mainEast(c)
            elif look == "Right":
                mainWest(c)
        if direction == "East":
            if look == "Left":
                mainNorth(c)
            if look == "Right":
                mainSouth(c)

    lookDecision = int(input("Look Left (1) or Right (2)? "))
    if lookDecision == 1:
        look = "Left"
        changeDir(look, direction)
    elif lookDecision == 2:
        look = "Right"
        changeDir(look, direction)
    else:
        wrong_input(direction, c)


def wrong_input(function, c):
    if c < 5:
        print(f"------------\n"
              f"Incorrect input. Strike {c}. He approaches.")
        function(c)
    elif c < 6:
        print(f"------------\n"
              f"I'm warning you {name}, select a correct input.\n"
              f"I'm warning you {name}, select a correct input.\n"
              f"I'm warning you {name}, select a correct input.\n"
              f"I'm warning you {name}, select a correct input.\n"
              f"I'm warning you {name}, select a correct input.\n")
        function(c)
    else:
        print("You are eviscerated from the face of the earth. Game over.")
        exit()
    return c


def random_start():
    x = random.randrange(0, 7)
    lines = ["It's chilly", "Something is staring.",
             "I think there's something in the room.", "My skin itches.",
             "My head hurts.", "Are those eyes?", "I'm hungry.", "Meh."]
    start_line = lines[x]
    return start_line


def mainNorth(c):
    def lightSwitch(c):
        try:
            done = False
            while not done:
                print(f"------------\n"
                      f"{name} walks towards the Light Switch.\n"
                      f"It emits a strange energy.\n"
                      f"1. Flip it\n"
                      f"2. Leave\n")
                l1 = int(input("What do you do? "))
                if l1 == 1:
                    if l1switch.lightStatus() == "Off":
                        l1switch.turnOn()
                        print("------------\n"
                              "The light is now on!")
                        done = True
                        mainNorth(c)
                    elif l1switch.lightStatus() == "On":
                        l1switch.turnOff()
                        print("------------\n"
                              "The light is now off. It is dark.\n"
                              "You walk back.")
                        done = True
                        mainNorth(c)
                elif l1 == 2:
                    print("You walk back.")
                    done = True
                    mainNorth(c)
                else:
                    c += 1
                    wrong_input(lightSwitch, c)
        except:
            c += 1
            wrong_input(lightSwitch, c)

    def openedDoor(c):
        try:
            print(f"------------\n"
                  f"{name} walks towards the Door.\n"
                  f"It's giving an ominous chill. It is already opened.\n"
                  f"1. Enter\n"
                  f"2. Close it\n"
                  f"3. Leave\n")
            d1 = int(input("What do you do? "))
            if d1 == 1:
                for i in range(3):
                    time.sleep(2)
                    print(".  .  .")
                print("You died.")
                exit()
            elif d1 == 2:
                d1door.closeDoor()
                print("You closed the door.")
                mainNorth(c)
            elif d1 == 3:
                print("You walk back.")
                mainNorth(c)
            else:
                c += 1
                wrong_input(openedDoor, c)
        except:
            c += 1
            wrong_input(openedDoor, c)

    def closedDoor(c):
        try:
            print(f"------------\n"
                  f"{name} walks towards the Door.\n"
                  f"It's giving an ominous chill.\n"
                  f"1. Open it\n"
                  f"2. Leave\n")
            d1 = int(input("What do you do? "))
            if d1 == 1:
                d1door.openDoor()
                print("------------\n"
                      "The door is open")
                d1_enter = input("Enter? (y,n)").lower()
                if d1_enter == 'y':
                    print("You died.")
                    exit()
                elif d1_enter == 'n':
                    d1_close = input("Close door? (y,n) ").lower()
                    if d1_close == 'y':
                        d1door.closeDoor()
                        print("You closed the door.")
                        mainNorth(c)
                    elif d1_close == 'n':
                        print("You walk back.")
                        mainNorth(c)
                    else:
                        c += 1
                        wrong_input(closedDoor, c)
                else:
                    c += 1
                    wrong_input(closedDoor, c)
            elif d1 == 2:
                mainNorth(c)
            else:
                c += 1
                wrong_input(closedDoor, c)
        except:
            c += 1
            wrong_input(closedDoor, c)
        return c

    def chooseNorth(c):
        direction = "North"
        try:
            decide = int(input(f"What would you like to do {name}?\n"
                               f"{random_start()}\n"
                               f"Enter a number (4 to look somewhere else): "))
            if decide < 4:
                if decide == 1:
                    lightSwitch(c)
                elif decide == 2:
                    if d1door.doorStatus() == "Closed":
                        closedDoor(c)
                    elif d1door.doorStatus() == "Open":
                        openedDoor(c)
                elif decide == 3:
                    print(f"------------\n"
                          f"{name} walks towards the Curtains.\n"
                          f"There's a faint glow.\n"
                          f"1. Open it\n"
                          f"2. Leave\n")
                    c1 = int(input("What do you do? "))
                    if c1 == 1:
                        print("You opened the curtains.\n"
                              ".  .  .")
                        print("1. Close\n"
                              "2. Leave")
                        c1_2 = int(input("What now? "))
                        if c1_2 == 1:
                            c1curtain.closeCurtain()
                            print("The curtain is closed.")
                            mainNorth(c)
                        elif c1_2 == 2:
                            print("You leave\n"
                                  ".  .  .")
                            mainNorth(c)
                    elif c1 == 2:
                        print("You walk back.")
                        mainNorth(c)
                    else:
                        c += 1
                        wrong_input(chooseNorth, c)
            elif decide == 4:
                directions(direction, c)
            else:
                c += 1
                wrong_input(chooseNorth, c)
        except:
            c += 1
            wrong_input(chooseNorth, c)
        return c

    direction = "North"
    if l1switch.lightStatus() == "Off":
        light_stat = "Unknown (Dark) (Obviously off)"
        door_stat = "Unknown (Dark)"
        curtain_stat = "Unknown (Dark)"
    else:
        light_stat = l1switch.lightStatus()
        door_stat = d1door.doorStatus()
        curtain_stat = c1curtain.curtainStatus()
    print("_______________")
    print(f"-----------  Direction: North\n"
          f"-----^-----  Objects in view: 1. Light Switch ({light_stat})\n"
          f"-----|-----                   2. Door ({door_stat})\n"
          f"-----|-----                   3. Curtains ({curtain_stat})\n"
          f"-----------  Inventory: {inventory}\n")
    chooseNorth(c)
    return direction


def mainWest(c):
    def closedDoor(c):
        print(f"------------\n"
              f"{name} walks towards the Door.\n"
              f"It seems slightly ajar.\n"
              f"1. Open it\n"
              f"2. Leave\n")
        try:
            d2 = int(input("What do you do? "))
            if d2 == 1:
                d2door.openDoor()
                print("------------\n"
                      "The door is open")
                d2_enter = input("Enter? (y,n)").lower()
                if d2_enter == 'y':
                    print("------------\n"
                          "You enter.")
                    for i in range(3):
                        time.sleep(2)
                        print(".  .  .")
                    print("The room you enter feels similar.")
                    mainEast(c)
                elif d2_enter == 'n':
                    d2_close = input("Close door? (y,n) ").lower()
                    if d2_close == 'y':
                        d2door.closeDoor()
                        print("You closed the door.")
                        mainWest(c)
                    elif d2_close == 'n':
                        print("You walk back.")
                        mainWest(c)
                    else:
                        c += 1
                        wrong_input(closedDoor, c)
                else:
                    c += 1
                    wrong_input(closedDoor, c)
            elif d2 == 2:
                print("You leave.")
                mainWest(c)
            else:
                c += 1
                wrong_input(closedDoor, c)
        except:
            c += 1
            wrong_input(closedDoor, c)

    def openedDoor(c):
        print(f"------------\n"
              f"{name} walks towards the Door.\n"
              f"It's open.\n"
              f"1. Enter\n"
              f"2. Close it\n"
              f"3. Leave\n")
        try:
            d2 = int(input("What do you do? "))
            if d2 == 1:
                print("------------\n"
                      "You enter.")
                for i in range(3):
                    time.sleep(2)
                    print(".  .  .")
                print("The room you enter feels similar.")
                mainEast(c)
            elif d2 == 2:
                d2door.closeDoor()
                print("------------\n"
                      "The door is closed")
                d2_leave = input("Leave? (y,n)").lower()
                if d2_leave == 'y':
                    print("------------\n"
                          "You leave.")
                    mainWest(c)
                elif d2_leave == 'n':
                    d2_close = input("Open door? (y,n) ").lower()
                    if d2 == 'y':
                        openedDoor(c)
                    elif d2_close == 'n':
                        print("You walk back.")
                        mainWest(c)
                    else:
                        wrong_input(openedDoor, c)
            elif d2 == 3:
                print("You leave.")
                mainWest(c)
            else:
                c += 1
                wrong_input(openedDoor, c)
        except:
            c += 1
            wrong_input(openedDoor, c)

    def openedCloset(c):
        print(f"------------\n"
              f"{name} walks towards the Closet\n"
              f"It is dark and empty inside.\n"
              f"1. Enter\n"
              f"3. Close 'et'\n"
              f"2. Leave\n")
        c1 = int(input("What do you do? "))
        if c1 == 2:
            print("You closed the Closet.\n")
            print("1. Open\n"
                  "2. Leave")
            c1_2 = int(input("What now? "))
            if c1_2 == 1:
                d2closet.openDoor()
                print("The closet is open.")
                openedDoor(c)
            elif c1_2 == 2:
                print("You leave\n"
                      ".  .  .")
                mainWest(c)
            else:
                c += 1
                wrong_input(openedDoor, c)
        elif c1 == 2:
            print("You walk back.")
            mainWest(c)
        else:
            wrong_input(openedDoor, c)
        return c

    def closedCloset(c):
        print(f"------------\n"
              f"{name} walks towards the Closet\n"
              f"You can hear scratching.\n"
              f"1. Open it\n"
              f"2. Leave\n")
        c1 = int(input("What do you do? "))
        if c1 == 1:
            print("You opened the Closet.\n")
            for i in range(3):
                time.sleep(2)
                print(".  .  .")
            print("It is dark and empty.\n"
                  "1. Close\n"
                  "2. Leave")
            c1_2 = int(input("What now? "))
            if c1_2 == 1:
                d2closet.closeDoor()
                print("The closet is closed.")
                mainNorth(c)
            elif c1_2 == 2:
                print("You leave\n"
                      ".  .  .")
                mainWest(c)
        elif c1 == 2:
            print("You walk back.")
            mainWest(c)
        else:
            if c < 5:
                print("------------")
                print("Incorrect input. Don't do it again. He approaches.")
                c += 1
                chooseWest(c)
            elif c < 6:
                print("------------")
                print(f"I'm warning you {name}, select a correct input.\n"
                      f"I'm warning you {name}, select a correct input.\n"
                      f"I'm warning you {name}, select a correct input.\n"
                      f"I'm warning you {name}, select a correct input.\n"
                      f"I'm warning you {name}, select a correct input.")
                c += 1
                chooseWest(c)
            else:
                print("You are eviscerated from the face of the earth. Game over.")
                exit()
        return c

    def sleepWorld(c):
        def wrong_inputSleep(d):
            if d < 3:
                print("------------")
                print("Incorrect input.")
                sleepWorld(d)
            elif d < 5:
                print("------------")
                print(f"Incorrect output. Almost there.")
                sleepWorld(d)
            else:
                print("You are freed from sleep.")
                chooseWest(d)

        s = 0
        print("------------\n"
              "You wake up, however things don't seem right.\n"
              "It is dark.\n"
              "1. Get up\n"
              "2. Stay in bed\n")
        try:
            sleep1 = int(input("What do you do? "))
            if sleep1 == 1:
                print("------------\n"
                      "You wake up, however things don't seem right.\n"
                      "It is dark.\n"
                      "1. Get up\n"
                      "2. Stay in bed\n"
                      "3. Stay in bed\n")
                sleep2 = int(input("What do you do? "))
                if sleep2 == 1:
                    print("------------\n"
                          "You wake up, however things don't seem right.\n"
                          "It is dark.\n"
                          "1. Get up\n"
                          "2. Stay in bed\n"
                          "3. Stay in bed\n"
                          "4. Stay in bed\n"
                          "5. Stay in bed\n"
                          "6. Stay in bed\n")
                    sleep3 = int(input("What do you do? "))
                    if sleep3 == 1:
                        print("You seem to get up")
                        for i in range(3):
                            time.sleep(2)
                            print(".  .  .")
                        print("You never wake up again.")
                        exit()
                    elif 2 <= sleep3 <= 6:
                        print("You fall asleep again.")
                        for i in range(3):
                            time.sleep(2)
                            print(".  .  .")
                        chooseWest(c)
                    else:
                        s += 1
                        wrong_inputSleep(s)
                elif 2 <= sleep2 <= 3:
                    print("You fall asleep again.")
                    for i in range(3):
                        time.sleep(2)
                        print(".  .  .")
                    chooseWest(c)
                else:
                    s += 1
                    wrong_inputSleep(s)
            elif sleep1 == 2:
                print("You fall asleep again.")
                for i in range(3):
                    time.sleep(2)
                    print(".  .  .")
                chooseWest(c)
            else:
                s += 1
                wrong_inputSleep(s)
        except:
            s += 1
            wrong_inputSleep(s)

    def chooseWest(c):
        direction = "West"
        try:
            decide = int(input(f"What would you like to do {name}?\n"
                               f"{random_start()}\n"
                               f"Enter a number (4 to look somewhere else):"))
            if decide < 4:
                if decide == 1:
                    done = False
                    while not done:
                        c = 0
                        print(f"------------\n"
                              f"{name} walks towards the Bed.\n"
                              f"Seems cozy.\n"
                              f"1. Sleep\n"
                              f"2. Leave\n")
                        b1 = int(input("What do you do? "))
                        if b1 == 1:
                            print("You enter the bed.\n"
                                  "You fall asleep . . .\n"
                                  "")
                            for i in range(3):
                                time.sleep(2)
                                print(".  .  .")
                            sleepWorld(c)
                        elif b1 == 2:
                            print("You walk back.")
                            done = True
                            chooseWest(c)
                        else:
                            if c < 5:
                                print("------------")
                                print("Incorrect input. Don't do it again. He approaches.")
                                c += 1
                                chooseWest(c)
                            elif c < 6:
                                print("------------")
                                print(f"I'm warning you {name}, select a correct input.\n"
                                      f"I'm warning you {name}, select a correct input.\n"
                                      f"I'm warning you {name}, select a correct input.\n"
                                      f"I'm warning you {name}, select a correct input.\n"
                                      f"I'm warning you {name}, select a correct input.")
                                c += 1
                                chooseWest(c)
                            else:
                                print("You are eviscerated from the face of the earth. Game over.")
                                exit()
                elif decide == 2:
                    if d2door.doorStatus() == "Closed":
                        closedDoor(c)
                    elif d2door.doorStatus() == "Open":
                        openedDoor(c)
                elif decide == 3:
                    if d2closet.doorStatus() == "Closed":
                        closedCloset(c)
                    elif d2closet.doorStatus() == "Open":
                        openedCloset(c)
            elif decide == 4:
                directions(direction, c)
            else:
                wrong_input(chooseWest, c)
        except:
            wrong_input(chooseWest, c)

    direction = "West"
    if l1switch.lightStatus() == "Off":
        bed_stat = "Unknown (Dark) (Might be neat)"
        door_stat = "Unknown (Dark)"
        closet_stat = "Unknown (Dark)"
    else:
        bed_stat = "Neat"
        door_stat = d2door.doorStatus()
        closet_stat = d2closet.doorStatus()
    print("_______________")
    print("------------  Direction: West\n"
          f"-----------  Objects in view: 1. Bed ({bed_stat})\n"
          f"---<===----                   2. Door ({door_stat})\n"
          f"-----------                   3. Closet ({closet_stat})\n"
          f"------------  Inventory: {inventory}                 \n")
    chooseWest(c)
    return direction


def mainEast(c):
    def closedFridge(c):
        def fridgeUpdate(c):
            def decideFridge(c):
                def decideFridge_1(c):
                    try:
                        f1_3 = input("Would you like to do anything else? y/n ")
                        if f1_3 == "y":
                            decideFridge(c)
                        elif f1_3 == "n":
                            print("You close the fridge and leave.")
                            mainEast(c)
                        else:
                            wrong_input(decideFridge_1, c)
                    except:
                        wrong_input(decideFridge_1, c)
                if apple_jar_bear:
                    print("------------\n"
                          "Weird lineup.\n"
                          "1. Eat an apple\n"
                          "2. Shake the jar\n"
                          "3. Take the teddy bear\n"
                          "4. Leave")
                    f1_2 = int(input("What would you like to do? "))
                    if f1_2 == 1:
                        for i in range(3):
                            time.sleep(2)
                            print(".  .  .")
                        time.sleep(2)
                        print("You feel sick")
                        fridgeContents.remove("apples")
                        decideFridge_1(c)
                    elif f1_2 == 2:
                        for i in range(3):
                            time.sleep(2)
                            print(".  .  .")
                        time.sleep(2)
                        print("An eye appears in the jar")
                        decideFridge_1(c)
                    elif f1_2 == 3:
                        print("Teddy Bear added to your inventory.")
                        teddy_bear.takeItem()
                        fridgeContents.remove('bear')
                        decideFridge_1(c)
                    elif f1_2 == 4:
                        print("You leave.")
                        mainEast(c)
                    else:
                        wrong_input(decideFridge, c)
                elif jar_bear:
                    print("------------\n"
                          "Weird lineup.\n"
                          "1. Shake the jar\n"
                          "2. Take the teddy bear\n"
                          "3. Leave")
                    f1_2 = int(input("What would you like to do? "))
                    if f1_2 == 1:
                        for i in range(3):
                            time.sleep(2)
                            print(".  .  .")
                        time.sleep(2)
                        print("An eye appears in the jar")
                        decideFridge_1(c)
                    elif f1_2 == 2:
                        print("Teddy Bear added to your inventory.")
                        teddy_bear.takeItem()
                        fridgeContents.remove('bear')
                        decideFridge_1(c)
                    elif f1_2 == 3:
                        print("You leave.")
                        mainEast(c)
                    else:
                        wrong_input(decideFridge, c)
                elif apple_jar:
                    print("------------\n"
                          "Weird lineup.\n"
                          "1. Eat an apple\n"
                          "2. Shake the jar\n"
                          "3. Leave")
                    f1_2 = int(input("What would you like to do? "))
                    if f1_2 == 1:
                        for i in range(3):
                            time.sleep(2)
                            print(".  .  .")
                        time.sleep(2)
                        print("You feel sick")
                        fridgeContents.remove("apples")
                        decideFridge_1(c)
                    elif f1_2 == 2:
                        for i in range(3):
                            time.sleep(2)
                            print(".  .  .")
                        time.sleep(2)
                        print("An eye appears in the jar")
                        decideFridge_1(c)
                    elif f1_2 == 3:
                        print("You leave.")
                        mainEast(c)
                    else:
                        wrong_input(decideFridge, c)
                elif jar:
                    print("------------\n"
                          "Just the jar now. Can't believe you ate the apples.\n"
                          "1. Shake the jar\n"
                          "2. Leave\n")
                    f1_2 = int(input("What would you like to do? "))
                    if f1_2 == 1:
                        for i in range(3):
                            time.sleep(2)
                            print(".  .  .")
                        time.sleep(2)
                        print("You feel sick")
                        fridgeContents.remove("apples")
                        decideFridge_1(c)
                    elif f1_2 == 1:
                        for i in range(3):
                            time.sleep(2)
                            print(".  .  .")
                        time.sleep(2)
                        print("An eye appears in the jar")
                        decideFridge_1(c)
                    elif f1_2 == 2:
                        print("You leave.")
                        mainEast(c)
                    else:
                        wrong_input(decideFridge, c)
            
            if fridgeContents[0] == "apples":
                if fridgeContents[1] == "jar":
                    if fridgeContents[2] == "bear":
                        apple_jar_bear = True
                        apple_jar = False
                    else:
                        apple_jar_bear = False
                        apple_jar = True
                    apple_jar = True
            elif fridgeContents[0] == "jar":
                apple_jar = False
                apple_jar_bear = False
                if fridgeContents[1] == "bear":
                    jar_bear = True
                    jar = False
                else:
                    jar_bear = False
                    jar = True
             

            if apple_jar_bear:
                print("You take a look.  .  .")
                time.sleep(3)
                print("Some rotten apples.  .  .")
                time.sleep(3)
                print("A jar filled with a dark redish fluid.  .  .")
                time.sleep(3)
                print("And a teddy bear.")
                time.sleep(2)
                decideFridge(c)
            if apple_jar:
                print("You take a look.  .  .")
                time.sleep(3)
                print("Some rotten apples.  .  .")
                time.sleep(3)
                print("And a jar filled with a dark redish fluid.")
                time.sleep(2)
                decideFridge(c)
            if jar_bear:
                print("You take a look.  .  .")
                time.sleep(3)
                print("A jar filled with a dark redish fluid.  .  .")
                time.sleep(3)
                print("And a teddy bear.")
                time.sleep(2)
                decideFridge(c)
            if jar:
                print("You take a look.  .  .")
                time.sleep(3)
                print("Just a jar filled with a dark redish fluid.")
                time.sleep(2)
                decideFridge(c)
            

        print(f"------------\n"
              f"{name} walks towards the Fridge.\n"
              f"Kind of reeks.\n"
              f"1. Open it\n"
              f"2. Leave\n")
        try:
            f1 = int(input("What do you do? "))
            if f1 == 1:
                d2door.openDoor()
                print("------------\n"
                      "The fridge is open")
                viewContent = str(input("View contents? (y,n) ").lower())
                if viewContent == 'y':
                    print(fridgeContents)
                    fridgeUpdate(c)
                elif viewContent == 'n':
                    print("You just want to stand there then.")
                    time.sleep(2)
                    print("Okay")
                    time.sleep(2)
                    print("You close the fridge and leave.")
                    mainEast(c)
                else:
                    c += 1
                    wrong_input(closedFridge, c)
            elif f1 == 2:
                print("You leave.")
                mainWest(c)
            else:
                c += 1
                wrong_input(closedFridge, c)
        except:
            c += 1
            wrong_input(closedFridge, c)

    def useMicrowave(c):
        print("------------\n"
              "You walk towards the Microwave\n"
              "1. Put something in it"
              "2. Leave")
        m1 = input("What do you do? ")
        if m1 == 1:
            if len(inventory) == 0:
                print("You have nothing to put in.")
            else:
                for i in inventory:
                    print(inventory.index(i) + 1, end=' ')
                    print(" ", i)
                m1_2 = input("What do you want to put in?")

    def chooseEast(c):
        try:
            decide = int(input(f"What would you like to do {name}?\n"
                               f"{random_start()}\n"
                               f"Enter a number (4 to look somewhere else): "))
            if decide < 4:
                if decide == 1:
                    closedFridge(c)
                elif decide == 2:
                    useMicrowave(c)

            elif decide == 4:
                directions(direction, c)
            else:
                wrong_input(chooseEast, c)
        except:
            wrong_input(chooseEast, c)

    direction = "East"
    if l1switch.lightStatus() == "Off":
        fridge_stat = "Unknown (Dark) (You can hear the buzzing)"
        microwave_stat = "Unknown (Dark)"
        clock_stat = "Unknown (Dark)"
    else:
        fridge_stat = "Running"
        microwave_stat = m1microwave.applianceStatus()
        clock_stat = current_time
    print("_______________\n")
    print("-----------  Direction: East\n"
          f"-----------  Objects in view: 1. Fridge ({fridge_stat})\n"
          f"---===>----                   2. Microwave ({microwave_stat})\n"
          f"-----------                   3. Clock (says {clock_stat})\n"
          f"-----------                   \n")
    chooseEast(c)
    return direction


def mainSouth(c):
    direction = "South"
    print("_______________")
    print("-----------  Direction: South\n"
          "-----|-----  Objects in view: 1. Void\n"
          "-----|-----                   2. Light Switch\n"
          "-----V-----                   3. Door\n"
          "-----------                   \n")
    decide = int(input(f"What would you like to do {name}?\n"
                       f"Enter a number (4 to look somewhere else):"))
    decision(decide)
    return direction, decide


def intro():
    c = 0
    time.sleep(3)
    print('"Where am I?"')
    time.sleep(3)
    print(f'{name} wakes up in the middle of a room\n'
          f'Groggily, they get up.')
    time.sleep(3)
    print("Starting.  .  .")
    for i in range(2):
        time.sleep(1)
        print(".  .  .")
    mainNorth(c)


if start == 'y':
    intro()
elif start == 'n':
    print("Exiting game.")
    exit()
else:
    exit_yn = input("Do you want to exit? y/n ")
    if exit_yn == "y":
        print("Goodbye")
        exit()
    elif exit_yn == "n":
        print("Starting game.  .  .")
        time.sleep(3)
        c = 0
        intro()
    else:
        print("Wrong input. Exiting game.")
        exit()
