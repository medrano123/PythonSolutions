#  File: Project2.py
#  Description: The project below demonstrates my understanding of object-oriented techniques and how to use them by creating a small two floor map of an advanture game. By creating various objects to represent 
#  specific rooms in the house along with a method to show the attributes of said room, and a functioning way of moving throughout the house I am demonstrating my knowledge of classes and objects.
#  Part two of the project demonstrates my understanding of extracting data from files and applying it to the map of the house, along with implementing functions to gather items from specific rooms and manipulating the lists they are in.
#  Finally the project has me incorporating a user interface in which the user commands where the player in the game is going, and how they take/drop items in different rooms.
#  Student's Name: Giovanni Medrano 

class Room:
#  Creates the cpnstructor that allows the object to itialize the parameters 
    def __init__(self,name,north,east,south,west,up,down,contents):
        self.name = name
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.up = up
        self.down = down
        self.contents = contents
        
#  Displays the location of which the character is currently in.
    def displayRoom(self):
        print('Room name:  {}'.format(self.name))
        if (self.north != None):
            print('   Room to the north:  {}'.format(self.north))
        if (self.east != None):        
            print('   Room to the east:   {}'.format(self.east))
        if (self.south != None):
            print('   Room to the south:  {}'.format(self.south))
        if (self.west != None):
            print('   Room to the west:   {}'.format(self.west))
        if (self.up != None):
            print('   Room above:         {}'.format(self.up))
        if (self.down != None):
            print('   Room below:         {}'.format(self.down))
        if (self.contents != None):
            print('   Room contents:      {}'.format(self.contents))
        else:
            print('   Room contents:      []')
        print()
        
#  Creates the rooms by taking in the information from the floorplan.
def createRoom(roomData):
        contents = []
        len(roomData)
        numContents = len(roomData) - 7
        if numContents != 0:
            contents = roomData[7:]            
        newRoom = Room(roomData[0],roomData[1],roomData[2],roomData[3],roomData[4],roomData[5],roomData[6],contents)
        return newRoom
    
#  Tells the user what room the character is currently in.    
def look():
    print('You are currently in the ' + current.name + '.')
    print("Contents of the room:")
    if len(current.contents) >= 1:
        for i in range(len(
            current.contents)):
            print("   " + current.contents[i])
    else:
        print("   None")
        
#  Picks up the desired item and puts it into the inventory.
def pickup(item):
    
    if item in current.contents:
        inventory.append(item)       
        current.contents.remove(item)
        print("You now have the " + item + ".")
    else:
        print("That item is not in this room.")
        

#  Drops the item by removing it from the inventory, and adding it to the rooms contents.
def drop(item):

    if item in inventory:
        inventory.remove(item)
        current.contents.append(item)
        print("You have dropped the " + item)
    else:
        print("You don't have that item")
        
def listInventory():

    if inventory == []:
        print("You are currently carrying:" + "\n" + "   nothing.")
    else:
        print('You are currently carrying:')
        for i in range(len(inventory)):
            print("   " + inventory[i])

#  Gathhers the proper room object according to the name of the room.
def getRoom(name):
        for room in floorPlan:
            if room.name == name:
                return room
        return None
    
#  Takes in the direction parameter and prints out the room the character is moved to (if it can move in that direction, if it can't then it prints nothing).                  
def move(direction):
        #THE PERSON CANNOT MOVE.
        if (direction == 'north'):
            if current.north == None:
                print("You can't move in that direction.")
                return current
            else:
                print("You are now in the " + current.north + ".") 
                return getRoom(current.north)
            
        if (direction == 'east'):
            if current.east == None:
                print("You can't move in that direction.")
                return current
            else:
                print("You are now in the " + current.east + ".") 
                return getRoom(current.east)
            
        if (direction == 'south'):
            if current.south == None:
                print("You can't move in that direction.")
                return current
            else:
                print("You are now in the " + current.south + ".") 
                return getRoom(current.south)
            
        if (direction == 'west'):
            if current.west == None:
                print("You can't move in that direction.")
                return current
            else:
                print("You are now in the " + current.west + ".") 
                return getRoom(current.west)
            
        if (direction == 'up'):
            if current.up == None:
                print("You can't move in that direction.")
                return current
            else:
                print("You are now in the " + current.up + ".") 
                return getRoom(current.up)
            
        if (direction == 'down'):
            if current.down == None:
                print("You can't move in that direction.")
                return current
            else:
                print("You are now in the " + current.down + ".") 
                return getRoom(current.down)

#  Prints out the characteristics of every room; meaning which directions it can move and what rooms are there.

def displayAllRooms():
        for room in floorPlan:
            room.displayRoom()
            
def loadMap():

    global floorPlan    # make the variable "floorPlan" a global variable


    myFile = open("projectData.txt", "r")
    line = myFile.readline()
    rooms = []
    for i in range(1,8):
        theLine = line.split(",")
        for j in range(len(theLine)):
            if theLine[j].find('"') != -1:
                theLine[j] = theLine[j].replace('"', "")
            if theLine[j].find("\n") != -1:
                theLine[j] = theLine[j].replace("\n", "")
            if theLine[j].find("None") != -1:
                theLine[j] = None
        rooms.append(theLine)
        line = myFile.readline()        
    #print(rooms)    
    room1 = rooms[0]
    room2 = rooms[1]
    room3 = rooms[2]
    room4 = rooms[3]
    room5 = rooms[4]
    room6 = rooms[5]
    room7 = rooms[6]
    floorPlan = [createRoom(room1),createRoom(room2),createRoom(room3),createRoom(room4),createRoom(room5),createRoom(room6),createRoom(room7)]

def main():
    global inventory
    inventory = []

    global current      # make the variable "current" a global variable
    
    loadMap()
    
    displayAllRooms()

    # TEST CODE:  walk around the house
    current = floorPlan[0]      # start in the living room
    go = True
    look()
    print()
    command = input("Enter a command: ")
    while True:
        if (command == "help"):
            print()
            print("look:        display the name of the current room and its contents")
            print("north:       move north")
            print("east:        move east")
            print("south:       move south")
            print("west:        move west")
            print("up:          move up")
            print("down:        move down")
            print("inventory:   list what items you're currently carrying")
            print("get <item>:  pick up an item currently in the room")
            print("drop <item>: drop an item you're currently carrying")
            print("help:        print this list")
            print("exit:        quit the game")
            print()
            command = input("Enter a command: ")

        elif (command == "north"):
            current = move("north")
            print()
            command = input("Enter a command: ")
        elif (command == "east"):
            current = move("east")
            print()
            command = input("Enter a command: ")
        elif (command == "south"):
            current = move("south")
            print()
            command = input("Enter a command: ")
        elif (command == "west"):
            current = move("west")
            print()
            command = input("Enter a command: ")
        elif (command == "up"):
            current = move("up")
            print()
            command = input("Enter a command: ")
        elif (command == "down"):
            current = move("down")
            print()
            command = input("Enter a command: ")
        elif (command == "look"):
            look()
            print()
            command = input("Enter a command: ")
            
        elif (command == "inventory"):            
            listInventory()
            print()
            command = input("Enter a command: ")            
        elif ("get" in command):
            command = command.replace("get ","")
            pickup(command)
            print()
            command = input("Enter a command: ")          
        elif ("drop" in command):
            command = command.replace("drop ","")
            drop(command)
            print()
            command = input("Enter a command: ")            
        elif (command == "exit"):
            print("Quitting game.")
            break

main()
