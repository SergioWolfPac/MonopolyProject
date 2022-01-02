# Note This class Serves Logic as well as Data Structures necessary for this project
# Attempting to implement classes and lists
# styling details to refrain from call confusions inside of main.py
#    All functions and classes here begin with UPPERCASE
import random
from tkinter import *
import tkinter as tk


def Lost(player):
    if player.money <= 0:
        print("Player " + str(player.name) + " loses")
        return 1
    else:
        return 0


# attempting multiple class definitions
# note syntax def is under class and further is under def
class Player:
    def __init__(self, playerNumber):
        self.name = "Player" + str(playerNumber)
        self.dieRoll = 0
        self.money = 1000
        self.owns = []  # note this stores a list of Property Objects!
        self.isTurn = False
        self.pos = 0

    def RollDice(self):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        # print("die roll: " + str(die1) + " " + str(die2)) #debugging
        self.dieRoll = die1 + die2
        self.pos = self.pos + self.dieRoll
        if self.pos >= 40:
            self.pos = self.pos - 40
            self.money = self.money + 200  # when you pass go

    def EndTurn(self):
        self.isTurn = False


def createButtons(root):
    buttons = []  # list of all property buttons including the little button colors
    for x in range(62):
        buttons.append(tk.Button(root))
    return buttons


class Property:
    def __init__(self, name, cost, pos, isRailroad, isUtility):
        self.pos = pos
        self.name = name
        self.cost = cost
        self.pay = 0
        self.canBuy = True
        self.isRailroad = isRailroad
        self.isUtility = isUtility
        self.button = Button(text=name, state='disabled')

        # if pos % 10 == 0:
        #    self.button

        if not isRailroad or not isUtility:
            self.homes = 0
            self.mansions = 0

        self.fine = 0  # calculated separately including homes or mansions or railroad owned


def setNoBuy(dic):
    mylist = [0, 2, 4, 7, 10, 17, 20, 22, 30, 33, 36, 38]
    for x in mylist:
        dic[x].canBuy = False


def setPrices(dic):
    for y in dic:
        if dic[y].canBuy:
            dic[y].cost = (y * 10) + 10

    dic[5].isRailroad = True
    dic[10].isRailroad = True
    dic[15].isRailroad = True
    dic[20].isRailroad = True

    # setting utilities
    dic[12].isUtility = True
    dic[28].isUtility = True

    for x in dic:
        if dic[x].isRailroad:
            dic[x].cost = 200
        if dic[x].isUtility:
            dic[x].cost = 150


# list is in order
chicagolist = ["Go! Collect $200", "Chicago" + '\n' + "Theatre", "Community" + '\n' + "Chest 1",
               "Art" + '\n' + "Institute", "Income" + '\n' + "Tax 1", "Green" + '\n' + "Line",
               "Lincoln" + '\n' + "Park" + '\n' + "Zoo", "Chance 1", "Grant" + '\n' + "Park",
               "Magnificent" + '\n' + "Mile", "Just Visiting", "Shedd" + '\n' + "Aquarium", "ComEd", "Pequads",
               "Lou" + '\n' + "Malnatis", "Blue" + '\n' + "Line", "Giordanos", "Community" + '\n' + "Chest 2",
               "Portillos", "Drake" + '\n' + "Hotel", "Free Parking", "The Bean", "Chance 2",
               "Water" + '\n' + "Tower", "Wrigley" + '\n' + "Field", "Red" + '\n' + "Line", "Navy" + '\n' + "Pier",
               "Sears" + '\n' + "Tower", "Water" + '\n' + "Works", "Hancock" + '\n' + "Tower", "Go To Jail",
               "Field" + '\n' + "Museum", "Buckingham" + '\n' + "Fountain", "Community" + '\n' + "Chest 3",
               "Sox" + '\n' + "Stadium", "Brown" + '\n' + "Line", "Chance 3", "Chicago" + '\n' + "River",
               "Luxury Tax", "Millennium" + '\n' + "Park"]

# lists below are not in order initialization will not work correctly
newyorklist = ["Go! Collect $200", "Staten" + '\n' + "Island", "Community" + '\n' + "Chest 1",
               "Joe's Pizza", "Income" + '\n' + "Tax 1", "6 Train",
               "Rockefeller" + '\n' + "Plaza", "Chance 1", "Radio City" + '\n' + "Music Hall",
               "Metro" + '\n' + "Museum" + '\n' + "Of Art", "Just Visiting", "Chrysler" + '\n' + "Building",
               "Con Edison", "New York" + '\n' + "Times", "Statue" + '\n' + "Of" + '\n' + "Liberty",
               "B Train", "Central" + '\n' + "Park", "Community" + '\n' + "Chest 2", "Broadway" + '\n' + "District",
               "Wall" + '\n' + "Street", "Free Parking", "9/11" + '\n' + "Memorial", "Chance 2", "High" + '\n' + "Line",
               "Times" + '\n' + "Square", "C Train", "Brooklyn" + '\n' + "Bridge", "Fifth" + '\n' + "Avenue",
               "NYC" + '\n' + "Water DEP", "Grand" + '\n' + "Central" + '\n' + "Terminal", "Go To Jail",
               "The" + '\n' + "Frick" + '\n' + "Collection", "New York" + '\n' + "Public" + '\n' + "Library",
               "Community" + '\n' + "Chest 3", "St Patrick's" + '\n' + "Cathedral", "M Train", "Chance 3",
               "Empire" + '\n' + "State" + '\n' + "Building", "Luxury Tax", "One World" + '\n' + "Trade Center"]

defaultlist = ["Go! Collect $200", "Old Kent" + '\n' + "Road", "Community" + '\n' + "Chest 1",
               "Whitechapel" + '\n' + "Road", "Income" + '\n' + "Tax 1", "King's Cross" + '\n' + "Station",
               "The Angel" + '\n' + "Islington", "Chance 1", "Euston" + '\n' + "Road", "Pentonville" + '\n' + "Road",
               "Just Visiting", "Pall Mall", "London City" + '\n' + "Electrical", "Whitehall", "Northumberland" + '\n'
               + "Avenue", "Marylebone" + '\n' + "Station", "Bow Street", "Community" + '\n' + "Chest 2", "Great" +
               '\n' + "Marlborough" + '\n' + "Street", "Vine Street", "Free Parking", "Strand", "Chance 2",
               "Fleet" + '\n' + "Street", "Trafalgar" + '\n' + "Square",
               "Fenchurch" + '\n' + "Street" + '\n' + "Station", "Leicester" + '\n' + "Square", "Coventry" + '\n' +
               "Street", "London" + '\n' + "Utility", "Piccadilly", "Go To Jail", "Regent" + '\n' + "Street",
               "Oxford" + '\n' + "Street", "Community" + '\n' + "Chest 3", "Bond" + '\n' + "Street",
               "Liverpool" + '\n' + "Street" + '\n' + "Station", "Chance 3", "Park Lane", "Luxury Tax", "Mayfair"]


# propertydictionary = {name: Property(name=name, cost=0, isRailroad=0, isUtility=0) for name in propertylist}
# print(propertydictionary["The Bean"].name)  # note the name of the property is the key


# buttons are as follows [0]-[39] are normal board places. 40+ are the small labels for color on top of properties
def initializeButtons(propertydic, buttons):
    buttons[0].configure(text=propertydic[0].name, height=7, width=14, state='disabled', disabledforeground="black")
    buttons[1].configure(text=propertydic[1].name, height=5, width=8, state='disabled', disabledforeground="black")
    buttons[2].configure(text=propertydic[2].name, height=7, width=8, state='disabled', disabledforeground="black")
    buttons[3].configure(text=propertydic[3].name, height=5, width=8, state='disabled', disabledforeground="black")
    buttons[4].configure(text=propertydic[4].name, height=7, width=8, state='disabled', disabledforeground="black")
    buttons[5].configure(text=propertydic[5].name, height=7, width=8, state='disabled', disabledforeground="black")
    buttons[6].configure(text=propertydic[6].name, height=5, width=8, state='disabled', disabledforeground="black")
    buttons[7].configure(text=propertydic[7].name, height=7, width=8, state='disabled', disabledforeground="black")
    buttons[8].configure(text=propertydic[8].name, height=5, width=8, state='disabled', disabledforeground="black")
    buttons[9].configure(text=propertydic[9].name, height=5, width=8, state='disabled', disabledforeground="black")
    buttons[10].configure(text=propertydic[10].name, height=7, width=12, state='disabled', disabledforeground="black")
    buttons[11].configure(text=propertydic[11].name, height=3, width=8, state='disabled', disabledforeground="black")
    buttons[12].configure(text=propertydic[12].name, height=3, width=12, state='disabled', disabledforeground="black")
    buttons[13].configure(text=propertydic[13].name, height=3, width=8, state='disabled', disabledforeground="black")
    buttons[14].configure(text=propertydic[14].name, height=3, width=8, state='disabled', disabledforeground="black")
    buttons[15].configure(text=propertydic[15].name, height=3, width=12, state='disabled', disabledforeground="black")
    buttons[16].configure(text=propertydic[16].name, height=3, width=8, state='disabled', disabledforeground="black")
    buttons[17].configure(text=propertydic[17].name, height=3, width=12, state='disabled', disabledforeground="black")
    buttons[18].configure(text=propertydic[18].name, height=3, width=8, state='disabled', disabledforeground="black")
    buttons[19].configure(text=propertydic[19].name, height=3, width=8, state='disabled', disabledforeground="black")
    buttons[20].configure(text=propertydic[20].name, height=6, width=12, state='disabled', disabledforeground="black")
    buttons[21].configure(text=propertydic[21].name, height=4, width=8, state='disabled', disabledforeground="black")
    buttons[22].configure(text=propertydic[22].name, height=6, width=8, state='disabled', disabledforeground="black")
    buttons[23].configure(text=propertydic[23].name, height=4, width=8, state='disabled', disabledforeground="black")
    buttons[24].configure(text=propertydic[24].name, height=4, width=8, state='disabled', disabledforeground="black")
    buttons[25].configure(text=propertydic[25].name, height=6, width=8, state='disabled', disabledforeground="black")
    buttons[26].configure(text=propertydic[26].name, height=4, width=8, state='disabled', disabledforeground="black")
    buttons[27].configure(text=propertydic[27].name, height=4, width=8, state='disabled', disabledforeground="black")
    buttons[28].configure(text=propertydic[28].name, height=6, width=8, state='disabled', disabledforeground="black")
    buttons[29].configure(text=propertydic[29].name, height=4, width=8, state='disabled', disabledforeground="black")
    buttons[30].configure(text=propertydic[30].name, height=6, width=14, state='disabled', disabledforeground="black")
    buttons[31].configure(text=propertydic[31].name, height=3, width=10, state='disabled', disabledforeground="black")
    buttons[32].configure(text=propertydic[32].name, height=3, width=10, state='disabled', disabledforeground="black")
    buttons[33].configure(text=propertydic[33].name, height=3, width=14, state='disabled', disabledforeground="black")
    buttons[34].configure(text=propertydic[34].name, height=3, width=10, state='disabled', disabledforeground="black")
    buttons[35].configure(text=propertydic[35].name, height=3, width=14, state='disabled', disabledforeground="black")
    buttons[36].configure(text=propertydic[36].name, height=3, width=14, state='disabled', disabledforeground="black")
    buttons[37].configure(text=propertydic[37].name, height=3, width=10, state='disabled', disabledforeground="black")
    buttons[38].configure(text=propertydic[38].name, height=3, width=14, state='disabled', disabledforeground="black")
    buttons[39].configure(text=propertydic[39].name, height=3, width=10, state='disabled', disabledforeground="black")

    # end normal properties begin small color boxes on top of them
    buttons[40].configure(text="", height=1, width=8, bg='red', state='disabled', disabledforeground="red")
    buttons[41].configure(text="", height=1, width=8, bg='red', state='disabled', disabledforeground="red")
    buttons[42].configure(text=" ", height=1, width=8, bg='red', state='disabled', disabledforeground="red")
    buttons[43].configure(text=" ", height=1, width=8, bg='yellow', state='disabled', disabledforeground="yellow")
    buttons[44].configure(text=" ", height=1, width=8, bg='yellow', state='disabled', disabledforeground="yellow")
    buttons[45].configure(text=" ", height=1, width=8, bg='yellow', state='disabled', disabledforeground="yellow")
    buttons[46].configure(text=" ", height=3, width=2, bg='orange', state='disabled', disabledforeground="orange")
    buttons[47].configure(text="", height=3, width=2, bg='orange', state='disabled', disabledforeground="orange")
    buttons[48].configure(text=" ", height=3, width=2, bg='orange', state='disabled', disabledforeground="orange")
    buttons[49].configure(text=" ", height=3, width=2, bg='pink', state='disabled', disabledforeground="pink")
    buttons[50].configure(text=" ", height=3, width=2, bg='pink', state='disabled', disabledforeground="pink")
    buttons[51].configure(text=" ", height=3, width=2, bg='pink', state='disabled', disabledforeground="pink")
    buttons[52].configure(text=" ", height=3, width=2, bg='green', state='disabled', disabledforeground="green")
    buttons[53].configure(text=" ", height=3, width=2, bg='green', state='disabled', disabledforeground="green")
    buttons[54].configure(text=" ", height=3, width=2, bg='green', state='disabled', disabledforeground="green")
    buttons[55].configure(text=" ", height=3, width=2, bg='darkblue', state='disabled', disabledforeground="darkblue")
    buttons[56].configure(text="", height=3, width=2, bg='darkblue', state='disabled', disabledforeground="darkblue")
    buttons[57].configure(text=" ", height=1, width=8, bg='lightblue', state='disabled', disabledforeground="lightblue")
    buttons[58].configure(text=" ", height=1, width=8, bg='lightblue', state='disabled', disabledforeground="lightblue")
    buttons[59].configure(text=" ", height=1, width=8, bg='lightblue', state='disabled', disabledforeground="lightblue")
    buttons[60].configure(text=" ", height=1, width=8, bg='brown', state='disabled', disabledforeground="brown")
    buttons[61].configure(text=" ", height=1, width=8, bg='brown', state='disabled', disabledforeground="brown")

    # begin putting buttons on the grid (out of order)
    buttons[21].grid(row=1, column=2)
    buttons[22].grid(row=1, column=3, rowspan=2)
    buttons[23].grid(row=1, column=4)
    buttons[24].grid(row=1, column=5)
    buttons[25].grid(row=1, column=6, rowspan=2)
    buttons[26].grid(row=1, column=7)
    buttons[27].grid(row=1, column=8)
    buttons[28].grid(row=1, column=9, rowspan=2)
    buttons[29].grid(row=1, column=10)
    buttons[30].grid(row=1, column=11, columnspan=2, rowspan=2)
    buttons[20].grid(row=1, column=0, columnspan=2, rowspan=2)
    buttons[19].grid(row=3, column=0)
    buttons[18].grid(row=4, column=0)
    buttons[17].grid(row=5, column=0, columnspan=2)
    buttons[16].grid(row=6, column=0)
    buttons[15].grid(row=7, column=0, columnspan=2)
    buttons[14].grid(row=8, column=0)
    buttons[13].grid(row=9, column=0)
    buttons[12].grid(row=10, column=0, columnspan=2)
    buttons[11].grid(row=11, column=0)
    buttons[10].grid(row=12, column=0, columnspan=2, rowspan=2)
    buttons[31].grid(row=3, column=12)
    buttons[32].grid(row=4, column=12)
    buttons[33].grid(row=5, column=11, columnspan=2)
    buttons[34].grid(row=6, column=12)
    buttons[35].grid(row=7, column=11, columnspan=2)
    buttons[36].grid(row=8, column=11, columnspan=2)
    buttons[37].grid(row=9, column=12)
    buttons[38].grid(row=10, column=11, columnspan=2)
    buttons[39].grid(row=11, column=12)
    buttons[9].grid(row=13, column=2)
    buttons[8].grid(row=13, column=3)
    buttons[7].grid(row=12, column=4, rowspan=2)
    buttons[6].grid(row=13, column=5)
    buttons[5].grid(row=12, column=6, rowspan=2)
    buttons[4].grid(row=12, column=7, rowspan=2)
    buttons[3].grid(row=13, column=8)
    buttons[2].grid(row=12, column=9, rowspan=2)
    buttons[1].grid(row=13, column=10)
    buttons[0].grid(row=12, column=11, columnspan=2, rowspan=2)

    # non property small color block property buttons
    buttons[40].grid(row=2, column=2)
    buttons[41].grid(row=2, column=4)
    buttons[42].grid(row=2, column=5)
    buttons[43].grid(row=2, column=7)
    buttons[44].grid(row=2, column=8)
    buttons[45].grid(row=2, column=10)
    buttons[46].grid(row=3, column=1)
    buttons[47].grid(row=4, column=1)
    buttons[48].grid(row=6, column=1)
    buttons[49].grid(row=8, column=1)
    buttons[50].grid(row=9, column=1)
    buttons[51].grid(row=11, column=1)
    buttons[52].grid(row=3, column=11)
    buttons[53].grid(row=4, column=11)
    buttons[54].grid(row=6, column=11)
    buttons[55].grid(row=9, column=11)
    buttons[56].grid(row=11, column=11)
    buttons[57].grid(row=12, column=2)
    buttons[59].grid(row=12, column=5)
    buttons[58].grid(row=12, column=3)
    buttons[60].grid(row=12, column=8)
    buttons[61].grid(row=12, column=10)
