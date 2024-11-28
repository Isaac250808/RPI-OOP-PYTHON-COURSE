from character import Enemy

dave = Enemy("Dave", "A smelly zombie")

dave.describe()
dave.set_conversation("Brain please")
dave.talk()

dave.setWeakness("cheese")
fightWith = input("What will you fight with? - ")
dave.fight(fightWith)
