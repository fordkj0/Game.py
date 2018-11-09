from sys import exit
from random import randint
from textwrap import dedent

inventory = {'weapon': 'none',
    'monster': 0}


#Instead of a while loop I will just have my classes call out other class or
#what about a for loop going through a list of functions.
#I think the while loop gives me more options.
class Play(object):
    #We are expecting a class object. to use th object in the code
    #we must initialize it
    def __init__(self, play_Map):
        self.play_Map = play_Map

    def start(self):

        #Set variable current_scene to the opening scene object.
        current_scene = self.play_Map.opening()

        last_scene = self.play_Map.next('gold')


        while current_scene != last_scene:
            if inventory['monster'] < 4:
                #print('Top of the while loop')
                next_name = current_scene.base()
                #print("After the next name param")
                current_scene = self.play_Map.next(next_name)
            else:
                print(dedent("""
                    You have stalled for too long. A monster sneaks
                    up behind you and eats you"""))
                exit(1)
        last_scene.base()


#the purpose of class weapon is to select a weapon for the inventory
class Weapons(object):

    def base(self):
        print(dedent("""
            Three weapons lie in the chest before you. A sword, a spear,
            and a shield. Choose wisely"""))
        choice = input('>>  ')
        if choice == 'sword':
            inventory['weapon'] = 'sword'
            return 'doors'
        elif choice == 'spear':
            inventory['weapon'] = 'spear'
            return 'doors'
        elif choice == 'shield':
            inventory['weapon'] = 'shield'
            return 'doors'
        else:
            print('That was an incorrect option, the monsters get close')
            inventory['monster'] = inventory['monster'] + 1
            return 'weapon'



#Opening scene where the player awakens from unconciousness
class Awaken(object):
    def base(self):
        print(dedent("""
        You awaken from unconciousness. Before that you see a chest
        with weapons and a set of three doors.
        Do you check the 'weapons' or go to the 'doors'"""
        ))
        choice = input('> ')

        if choice == 'doors':
            print('You head straight to the doors')
            return 'doors'
        elif choice == 'weapons':
            print("It is wise not to proceed unarmed")
            return 'weapon'
        else:
            print("You must make a proper choice")
            inventory['monster'] = inventory['monster'] + 1
            return 'awaken'



#The awakening player must choose doors or Weapons
class Doors(object):
    def base(self):
        print(dedent("""
        The three doors leading out of the room each have a placard with a drawing on it.
        The door on the 'left' placard depicts a picture of Batman.
        The door on the 'middle' placard depicts a picture of Superman.
        The door on the 'right' placard has an eldritch horror on it
        Which do you choose?"""))
        dchoice = input('> ')
        if dchoice == 'left':
            print('Batman seeks to punsish evil')
            return 'left'
        elif dchoice == 'middle':
            print('Superman seeks to defend against evil')
            return 'middle'
        elif dchoice == 'right':
            print('Eldritch horrors are not to be messed with')
            return 'right'
        else:
            print("You must make a proper choice")
            return 'doors'


class Left_room(object):
    def base(self):
        print(dedent("""
            You enter the room and see a man with a glowing green sword.
            Without warning he swings it at your head"""))

        #By seing if weapon is not equal to shield it means you chose spear or sword.
        if inventory['weapon'] != 'shield':
            print(dedent("""You are Batman! Kryptonite doesn't work on you
                You quickly dodge the sword and stab the assailent in the heart
                You are able to proceed to the gold room"""))
            return 'gold'
        elif inventory['weapon'] == 'shield':
            print(dedent("""
                You are superman and weak to krytonite.
                Lex luthor cuts your head off"""))
            exit(1)
        else:
            print("I should never see this else statement")


class Right_room(object):
    def base(self):
        print(dedent("""
            Cthulu looks at you from a space from beyond the rooms.
            There is little you can do, 'flee' or 'proceed'"""))
        rchoice = input('> ')
        if rchoice == 'flee':
            print(dedent("""
                You succesfully flee the room, but
                you feel an eerie chill as if something is sneaking up behind you
                """))
            inventory['monster'] = inventory['monster'] + 1
            return 'doors'
        elif rchoice == 'proceed':
            print("You gouge out your eyes and start singing showtunes")
            exit(1)
        else:
            print("Your fear has made you unable to think straight, try again")
            inventory['monster'] = inventory['monster'] + 1
            return 'right'



class Center_room(object):
    def base(self):
        print("Out of nowhere a bear lunges at a picture of a damsel in distress")

        if inventory['weapon'] == 'shield':
            print(dedent("""
                Just like Superman you defend the citizen in distress.
                As the bear hits your shield it vanishes and a door
                is revealed at the end of the room"""))
            return 'gold'
        elif inventory['weapon'] == 'sword' or inventory['weapon'] != 'spear':
            print(dedent("""
                    You attack the bear, but your weapon passes straight
                    through the illusion. The bear touches the damnsel
                    on the wall, and spikes shoot up from the floor
                    impaling you."""))
            exit(1)
        else:
            print("the bear kills you dead")
            exit(1)



class Death(object):
    pass

class Gold_room(object):
    def base(self):
        print("All the gold is yours good job!")
        exit(1)

class Map(object):
    scenes = {
    'doors': Doors(),
    'weapon': Weapons(),
    'awaken': Awaken(),
    'gold': Gold_room(),
    'left': Left_room(),
    'right': Right_room(),
    'middle': Center_room(),

    }
    def __init__(self, start):
        self.start = start
        #print("start > ", start)
        #print("get(self.start)", Map.scenes.get(self.start))

    def opening(self):
        return Map.scenes.get(self.start)

    def next(self, scene_name):
        #I think val is unnecessary.
        #val = Map.scenes.get(scene_name)
        #return val
        return Map.scenes.get(scene_name)
init = Map('awaken')
Play(init).start()
print(inventory)
