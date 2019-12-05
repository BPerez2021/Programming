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
list_of_Class = ['Barbarian','Bard','Cleric','Druid','Fighter','Monk','Paladin','Ranger','Rogue', 'Sorcerer', 'Warlock', 'Wizard'] 
list_of_Origin = ['Acolyte','Criminal','Folk Hero','Noble','Soldier']

#class Race(object)


def setup():
  size(200,200);
  f = createFont("Arial",26); 

def draw(): 
  background(222,184,135);
  textFont(f,26);
  fill(0);
  text("Race: Dragonborn",10,100);
  
