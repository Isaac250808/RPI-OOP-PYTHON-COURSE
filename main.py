from room import Room
from character import Enemy
from item import Item
from rpginfo import RPGInfo

game = RPGInfo("The Adventures")
game.welcome()
RPGInfo.author = "Isaac"

balance = 110
inventory = []

kitchen = Room("kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies")

dining_hall = Room("dining hall")
dining_hall.set_description("A large room with ornate golden decorations on each wall")

ballroom = Room("ballroom")
ballroom.set_description("A vast room with a shiny wooden floor; huge candlesticks guard the entrance")

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

torch = Item(1,"Torch")
torch.setDescription("Lights up the world, one area at a time")
torch.setPrice(10)
inventory.append(torch)

choco = Item(2,"Chocolate bar")
choco.setDescription("A smooth, sweet treat")
choco.setPrice(20)
choco.setDurability = 1
choco.setHealing = 15
inventory.append(choco)

cheese = Item(1,"Cheese")
cheese.setDescription("Don't let the rats near it!")
cheese.setPrice(15)
cheese.setDurability = 1
cheese.setHealing = 35
inventory.append(cheese)

ak47 = Item(1,"AK47")
ak47.setDescription("Good luck getting this through the airport")
ak47.setPrice(45)
ak47.setDamage(85)

watch = Item(1,"Watch")
watch.setDescription("Watch's the time?")
watch.setPrice(15)

dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("Give me brain plese")
dave.setWeakness("cheese")
dining_hall.setCharacter(dave)

gabe = Enemy("Gabe", "A sneaky trader")
gabe.set_conversation("Nice watch, it'd be a shame if someone were to steal it")
gabe.setWeakness("police")
gabe.addTrade(ak47)
gabe.addTrade(watch)
# print(gabe.getTrades())
ballroom.setCharacter(gabe)

current_room = kitchen
alive = True
while alive == True:
    print("\n")
    current_room.get_details()
    if current_room.getCharacter() != None:
        current_room.getCharacter().describe()
    if current_room.getItem() != None:
        ##########################################
    command = input("> ")
    if command in ["north","south","east","west"]:
        current_room = current_room.move(command)
    elif command == "talk":
        if current_room.getCharacter() != None:
            current_room.getCharacter().talk()
        else:
            print("No character to talk to")
    elif command == "fight":
        if current_room.getCharacter() != None:
            if current_room.getCharacter().fight(input("What do you want to fight "+current_room.getCharacter().getName()+" with? ")) == False:
                alive = False
        else:
            print("No character to fight")
    elif command == "trade":
        bought = current_room.getCharacter().barter()
        if bought != None:
            if balance >= bought.getPrice():
                print("-$"+str(bought.getPrice()),"-",bought.getName())
                balance -= bought.getPrice()
                temp = []
                for i in range(len(inventory)):
                    temp.append(inventory[i].getName())
                if bought.getName() in temp:
                    j = 0
                    while temp[j] != bought.getName():
                        j+=1
                    current = inventory[j].getQuantity()
                    inventory[j].setQuantity(current+1)
                else:
                    inventory.append(bought)
    elif command == "balance":
        print("Balance is",balance)
    elif command == "inventory":
        for i in inventory:
            print(f"Item: {i.getName()}    Quantity: {i.getQuantity()}    Description: {i.getDescription()}    Value: {i.getPrice()}")
    elif command in ["exit","end","close","quit"]:
        input("Press [ENTER] to quit")
        alive = False
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        RPGInfo.credits()
