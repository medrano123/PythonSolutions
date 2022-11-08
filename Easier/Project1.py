#  File: Project1.py
#  Description: The project below demonstrates my understanding of object-oriented techniques and how to use them by creating a small two floor map of an advanture game. By creating various objects to represent 
#  specific rooms in the house along with a method to show the attributes of said room, and a functioning way of moving throughout the house I am demonstrating my knowledge of classes and objects.
#  Student's Name: Giovanni Medrano 


class Room:
#  Creates the cpnstructor that allows the object to itialize the parameters 
    def __init__(self,name,north,east,south,west,up,down):
        self.name = name
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.up = up
        self.down = down
        
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
        print()
        
  #Creates the rooms by taking in the information from the floorplan.
def createRoom(roomData):
        newRoom = Room(roomData[0],roomData[1],roomData[2],roomData[3],roomData[4],roomData[5],roomData[6])
        return newRoom
    
  #Tells the user what room the character is currently in.    
def look():
    print('You are currently in the ' + current.name + '.')

  #Gathhers the proper room object according to the name of the room/     
def getRoom(name):
        for room in floorPlan:
            if room.name == name:
                return room
        return None
    
  #Takes in the direction parameter and prints out the room the character is moved to (if it can move in that direction, if it can't then it prints nothing).                  
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
            

##########################################################################
###     All code below this is given to you.  DO NOT EDIT IT unless    ###
###     you need to adjust the indentation to match the indentation    ###
###     of the rest of your code.                                      ###
##########################################################################
        
def loadMap():

    global floorPlan    # make the variable "floorPlan" a global variable
    
    room1 = ["Living Room","Dining Room",None,None,None,"Upper Hall",None]
    room2 = ["Dining Room",None,None,"Living Room","Kitchen",None,None]
    room3 = ["Kitchen",None,"Dining Room",None,None,None,None]
    room4 = ["Upper Hall","Bathroom","Small Bedroom","Master Bedroom",None,None,"Living Room"]
    room5 = ["Bathroom",None,None,"Upper Hall",None,None,None]
    room6 = ["Small Bedroom",None,None,None,"Upper Hall",None,None]
    room7 = ["Master Bedroom","Upper Hall",None,None,None,None,None]

    floorPlan = [createRoom(room1),createRoom(room2),createRoom(room3),createRoom(room4),createRoom(room5),createRoom(room6),createRoom(room7)]

def main():

    global current      # make the variable "current" a global variable
    
    loadMap()
    
    displayAllRooms()

    # TEST CODE:  walk around the house
    
    current = floorPlan[0]      # start in the living room
    look()                      # Living Room
    
    current = move("south")     # can't move this direction
    current = move("west")      # can't move this direction
    current = move("north")     # Dining Room
    current = move("south")     # Living Room
    current = move("up")        # Upper Hall
    look()                      # Upper Hall
    current = move("east")      # Small Bedroom
    current = move("east")      # can't move this direction
    current = move("west")      # Upper Hall
    current = move("south")     # Master Bedroom
    current = move("north")     # Upper Hall
    current = move("north")     # Bathroom
    current = move("south")     # Upper Hall
    look()                      # Upper Hall
    current = move("west")      # can't move this direction
    look()                      # still in the Upper Hall
    current = move("down")      # Living Room
    current = move("north")     # Dining Room
    current = move("west")      # Kitchen
    current = move("north")     # can't move this direction

main()
