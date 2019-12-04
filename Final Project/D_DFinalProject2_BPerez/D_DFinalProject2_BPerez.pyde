#Research
##https://processing.org/tutorials/text/   
##https://processing.org/tutorials/pixels/
##https://processing.org/tutorials/data/
##https://processing.org/tutorials/print/   
##https://www.instructables.com/id/Creating-a-DD-5e-Character-for-Beginners/

#Class
##(random choice): Race (Based on time determines pictures), Class, Origin, Status
##(rolls): Strength, dexterity, constitution, intellegence, wisdom, charisma, armorclass, initiative, 
##(random and roll): Weapon, Armor
list_of_Race = ['Dragonborn','Dwarf','Elf','Gnome','Half-Elf','Half-Orc','Halfling','Human','Tiefling']
list_of_Origin = ['Acolyte','Criminal','Folk Hero','Noble','Soldier']

def list_of_class(list):
    list_of_class = ['Class: Barbarian','Class: Bard','Class: Cleric','Class: Druid','Class:Fighter','Monk','Paladin','Ranger','Rogue', 'Sorcerer', 'Warlock', 'Wizard'] 


#class Race(object)
def Font1():
    Font1 = createFont("Old English Text MT", 26) 

def setup():
    size (1100, 850)

def draw():
    background(222,184,135);
    
    Font1 = createFont("Old English Text MT", 26) 
    textFont(Font1)
    fill(0)
    text("Race: Dragonborn", 30, 100)
    
    Font1 = createFont("Old English Text MT", 26) 
    textFont(Font1)
    fill(0)
    text(random(list_of_class), 330, 100)
