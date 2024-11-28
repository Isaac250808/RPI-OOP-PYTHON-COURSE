class Character():

    # Create a character
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None
        self.trades = []

    def setName(self,newName):
        self.name = newName

    def getName(self):
        return self.name

    def describe(self):
        print( self.name + " is here!" )
        print( self.description )

    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        self.conversation = conversation

    def addTrade(self,item):
        self.trades.append(item)

    def getTrades(self):
        return self.trades

    # Talk to this character
    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    # Fight with this character
    def fight(self, combat_item):
        print(self.name + " doesn't want to fight with you")
        return True

    def barter(self):
        print("FOR SALE (Type the name of the item as you see):")
        length = 0
        for i in self.trades:
            length += 1
            print("["+str(length)+"]: "+i.getName()+" - "+str(i.getPrice())+" Tokens")
        print("( Type \"cancel\" if you change your mind )")
        item = input("> ")
        temp = []
        for i in range(len(self.trades)):
            temp.append(self.trades[i].getName())
        if item != "cancel" and item in temp:
            i = 0
            while item != temp[i]:
                i += 1
            print("Are you sure you want to buy",item,"for",self.trades[i].getPrice(),"Tokens? (Y/N)")
            YorN = input("> ").lower()
            if YorN == "y":
                return self.trades[i]
            else:
                return None
        else:
            return None

class Enemy(Character):
    def __init__(self,char_name,char_description):
        super().__init__(char_name, char_description)
        self.weakness = None

    def setWeakness(self,charWeakness):
        self.weakness = charWeakness

    def getWeakness(self):
        return self.weakness

    def fight(self, combat_item):
        if combat_item == self.weakness:
            print("You fend " + self.name + " off with the " + combat_item )
            return True
        else:
            print(self.name + " crushes you, puny adventurer")
            return False


