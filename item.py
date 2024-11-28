class Item:
    def __init__(self,quantity,itemName):
        self.name = itemName
        self.description = None
        self.damage = None
        self.price = None
        self.ability = None
        self.quantity = quantity
        self.healing = None
        self.durability = None

    def setDescription(self,itemDescription):
        self.description = itemDescription

    def setDamage(self,itemDamage):
        self.damage = itemDamage

    def setPrice(self,itemPrice):
        self.price = itemPrice

    def setAbility(self,itemAbility):
        self.ability = itemAbility

    def setQuantity(self,numb):
        self.quantity = numb

    def setHealing(self,amount):
        self.healing = amount

    def setDurability(self, amount):
        self.durability = amount

    def getName(self):
        return self.name

    def getDescription(self):
        return self.description

    def getDamage(self):
        return self.damage

    def getPrice(self):
        return self.price

    def getAbility(self):
        return self.ability

    def getQuantity(self):
        return self.quantity

    def getHealing(self):
        return self.healing
