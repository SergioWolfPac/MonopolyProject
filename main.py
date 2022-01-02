from tkinter import *
import tkinter as tk
# from PIL import Image, ImageTk
import random
from logic import *  # imports all from logic

root = Tk()
root.title("Monopoly")
root.geometry("500x300")
# root.iconbitmap("logo1.ico") #download a gaming picture or something with .ico extension and keep it in the same folder and try it
root.configure(background='grey')


def gamescreen():
    player1 = Player(1)  # player 1 color is coral red
    player2 = Player(2)  # player 2 color is light purple
    player1.isTurn = True

    # button functions
    def endturn():
        P1_cash_balance['text'] = player1.money
        P2_cash_balance['text'] = player2.money
        if Lost(player1):
            print("Player 1 Ran out of  Money!")
            quit(1)
        if Lost(player2):
            print("Player 2 Ran out of Money!")
            quit(2)
        if player1.isTurn:
            player1.isTurn = False
            player2.isTurn = True
            player_turn['text'] = player2.name
            P2_rolldice_btn['state'] = 'active'
        else:
            player2.isTurn = False
            player1.isTurn = True
            player_turn['text'] = player1.name
            rolldice_btn['state'] = 'active'

    def diceRolled1():
        if player1.isTurn:
            buttons[player1.pos].configure(bg='SystemButtonFace')  # resets to default color
            player1.RollDice()
            print(player1.dieRoll)
            rolldice_btn['state'] = 'disabled'
            P1_position_n['text'] = propertydic[player1.pos].name
            buttons[player1.pos].configure(bg='coral1')  # test code
        else:
            print("Already Rolled " + player1.name)

    def diceRolled2():
        if player2.isTurn:
            buttons[player2.pos].configure(bg='SystemButtonFace')  # resets to default color
            player2.RollDice()
            print(player2.dieRoll)
            P2_rolldice_btn['state'] = 'disabled'
            P2_position_n['text'] = propertydic[player2.pos].name
            buttons[player2.pos].configure(bg='MediumPurple1')  # test code
        else:
            print("Already Rolled " + player2.name)

    # need checks here for right input!
    def player1owns():
        if propertydic[player1.pos].canBuy:
            player1.money = player1.money - propertydic[player1.pos].cost
            player1.owns.append(propertydic[player1.pos])
            P1_properties_n.insert('end', player1.owns[len(player1.owns) - 1].name)
            print("player 1 owns " + player1.owns[len(player1.owns) - 1].name + " now")
            P1_cash_balance['text'] = player1.money
        else:
            print("Cannot Buy This Property " + propertydic[player1.pos].name)

    def player2owns():
        if propertydic[player2.pos].canBuy:
            player2.money = player2.money - propertydic[player2.pos].cost
            player2.owns.append(propertydic[player2.pos])
            P2_properties_n.insert('end', player2.owns[len(player2.owns) - 1].name)
            print("player 2 owns " + player2.owns[len(player2.owns) - 1].name + " now")
            P2_cash_balance['text'] = player2.money
        else:
            print("Cannot Buy This Property " + propertydic[player2.pos].name)

    root.title("Monopoly")
    root.geometry("1500x720")
    root.configure(background='skyblue')

    entry_label.destroy()
    P1_label.destroy()
    P2_label.destroy()
    P1nameentered.destroy()
    P2nameentered.destroy()
    startbtn.destroy()
    entry_label.destroy()
    opt.destroy()

    if (city_selection.get().lower() == 'chicago'):
        # Note: propertydic is a dictionary using <i,Class Object: Property> where i is the i'th index of chicagoList
        #   using propertydic and searching by key[i] finds that {key,value} pair where the value is of class Property
        #                 therefore, that key[i] returns the object and all of it's members
        #                a range based for loop creates every instance of every property in a single line
        propertydic = {i: Property(name=name, pos=i, cost=0, isRailroad=0, isUtility=0) for i, name in
                       enumerate(chicagolist)}
        # print(propertydic[12].name) # prints comed
        setNoBuy(propertydic)
        setPrices(propertydic)


    elif (city_selection.get().lower() == 'new york'):
        propertydic = {i: Property(name=name, pos=i, cost=0, isRailroad=0, isUtility=0) for i, name in
                       enumerate(newyorklist)}
        setNoBuy(propertydic)
        setPrices(propertydic)

    else:
        propertydic = {i: Property(name=name, pos=i, cost=0, isRailroad=0, isUtility=0) for i, name in
                       enumerate(defaultlist)}
        setNoBuy(propertydic)
        setPrices(propertydic)

    buttons = createButtons(root)
    initializeButtons(propertydic, buttons)

    if (P1_name.get() == ""):
        P1_tag = Label(root, text="Player 1", font='20', height=1, width=8, bg='skyblue', state='disabled',
                       disabledforeground="darkblue")
        P1_tag.grid(row=1, column=15, padx=160)
    else:
        P1_tag = Label(root, text=P1_name.get(), font='20', height=1, width=8, bg='skyblue', state='disabled',
                       disabledforeground="darkblue")
        player1.name = P1_name.get()  # properly sets player name
        P1_tag.grid(row=1, column=15, padx=160)

    if (P2_name.get() == ""):
        P2_tag = Label(root, text="Player 2", font='20', height=1, width=8, bg='skyblue', state='disabled',
                       disabledforeground="darkblue")
        P2_tag.grid(row=1, column=20, padx=60)
    else:
        P2_tag = Label(root, text=P2_name.get(), font='20', height=1, width=8, bg='skyblue', state='disabled',
                       disabledforeground="darkblue")
        player2.name = P2_name.get()  # properly sets player name
        P2_tag.grid(row=1, column=20, padx=60)

        player_turn = Button(root, text=player1.name, height=2, width=8, bg='black', state='disabled',
                             disabledforeground="white")
        player_turn.grid(row=6, column=6)

    rolldice_btn = Button(root, text="P1 diceroll", height=2, width=8, command=diceRolled1)
    rolldice_btn.grid(row=6, column=4)

    P2_rolldice_btn = Button(root, text="P2 diceroll", height=2, width=8, command=diceRolled2)
    P2_rolldice_btn.grid(row=6, column=8)

    endturn_btn = Button(root, text="endturn", height=2, width=8, command=endturn)
    endturn_btn.grid(row=7, column=6, pady=5)

    P1_housebuy = Button(root, text="P1 buy" + '\n' + "house", height=2, width=8)
    P1_housebuy.grid(row=9, column=3)

    P2_housebuy = Button(root, text="P2 buy" + '\n' + "house", height=2, width=8)
    P2_housebuy.grid(row=9, column=5)

    P1_housesell = Button(root, text="P1 sell" + '\n' + "house", height=2, width=8)
    P1_housesell.grid(row=10, column=3)

    P2_housesell = Button(root, text="P2 sell" + '\n' + "house", height=2, width=8)
    P2_housesell.grid(row=10, column=5)

    P1_propertybuy = Button(root, text="P1 buy" + '\n' + "property", height=2, width=8, command=player1owns)
    P1_propertybuy.grid(row=9, column=7)

    P2_propertybuy = Button(root, text="P2 buy" + '\n' + "property", height=2, width=8, command=player2owns)
    P2_propertybuy.grid(row=9, column=9)

    P1_propertysell = Button(root, text="P1 sell" + '\n' + "property", height=2, width=8)
    P1_propertysell.grid(row=10, column=7)

    P2_propertysell = Button(root, text="P2 sell" + '\n' + "property", height=2, width=8)
    P2_propertysell.grid(row=10, column=9)

    main_label = Label(root, text="WELCOME TO MONOPOLY-WORLD", font='20', bg='skyblue', state='disabled',
                       disabledforeground="red")
    main_label.grid(row=2, column=3, columnspan=6, rowspan=4, pady=20)
    P1_position = tk.Label(root, text="Board Position:", font='20', height=1, width=11, bg='skyblue', state='disabled',
                           disabledforeground="brown")
    P1_position.grid(row=2, column=15, padx=160)
    P2_position = tk.Label(root, text="Board Position:", font='20', height=1, width=11, bg='skyblue', state='disabled',
                           disabledforeground="brown")
    P2_position.grid(row=2, column=20, padx=60)
    P1_cash = tk.Label(root, text="Cash Balance:", font='20', height=1, width=11, bg='skyblue', state='disabled',
                       disabledforeground="green")
    P1_cash.grid(row=4, column=15, padx=160)
    P2_cash = tk.Label(root, text="Cash Balance:", font='20', height=1, width=11, bg='skyblue', state='disabled',
                       disabledforeground="green")
    P2_cash.grid(row=4, column=20, padx=60)
    P1_properties = tk.Label(root, text="Properties:", font='20', height=1, width=11, bg='skyblue', state='disabled',
                             disabledforeground="purple")
    P1_properties.grid(row=6, column=15, padx=160)
    P2_properties = tk.Label(root, text="Properties:", font='20', height=1, width=11, bg='skyblue', state='disabled',
                             disabledforeground="purple")
    P2_properties.grid(row=6, column=20, padx=60)
    P1_properties_n = tk.Listbox(root, height=24, width=45)
    P1_properties_n.grid(row=7, column=15, rowspan=100)
    P2_properties_n = tk.Listbox(root, height=24, width=45)
    P2_properties_n.grid(row=7, column=20, rowspan=100)
    P1_cash_balance = tk.Label(root, text=player1.money, height=1, width=11, bg='skyblue', state='disabled',
                               disabledforeground="darkgreen")
    P1_cash_balance.grid(row=5, column=15, padx=160)
    P2_cash_balance = tk.Label(root, text=player2.money, height=1, width=11, bg='skyblue', state='disabled',
                               disabledforeground="darkgreen")
    P2_cash_balance.grid(row=5, column=20, padx=60)
    P1_position_n = tk.Label(root, text=propertydic[player1.dieRoll].name, height=3, width=14, bg='skyblue',
                             state='disabled', disabledforeground="brown")
    P1_position_n.grid(row=3, column=15, padx=160)
    P2_position_n = tk.Label(root, text=propertydic[player2.dieRoll].name, height=3, width=14, bg='skyblue',
                             state='disabled', disabledforeground="brown")
    P2_position_n.grid(row=3, column=20, padx=60)


P1_label = tk.Label(root, text="Player 1 name", font='20', bg='gray', state='disabled', disabledforeground="skyblue")
P1_label.grid(row=5, column=3, padx=0, pady=10)
P1_name = tk.StringVar()

P1nameentered = tk.Entry(root, width=15, textvariable=P1_name)
P1nameentered.grid(row=6, column=3, padx=20, pady=10)

P2_label = tk.Label(root, text="Player 2 name", font='20', bg='gray', state='disabled', disabledforeground="skyblue")
P2_label.grid(row=5, column=6, padx=10, pady=10)
P2_name = tk.StringVar()

P2nameentered = tk.Entry(root, width=15, textvariable=P2_name)
P2nameentered.grid(row=6, column=6, padx=20, pady=10)

startbtn = Button(root, text="Start Game", command=gamescreen)
startbtn.grid(row=9, column=4, pady=5)

entry_label = tk.Label(root, text="Enter city", font='20', bg='gray', state='disabled', disabledforeground="skyblue")
entry_label.grid(row=7, column=4)

options = ["Choose location", "Chicago", "New York"]
city_selection = tk.StringVar(root)

opt = tk.OptionMenu(root, city_selection, *options)
city_selection.set(options[0])
opt.grid(row=8, column=4)

button_quit = Button(root, text="Quit", command=root.quit)
button_quit.grid(row=13, column=4, pady=10)
root.mainloop()
