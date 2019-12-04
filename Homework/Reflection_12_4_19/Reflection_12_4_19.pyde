#Research   
##https://www.instructables.com/id/Creating-a-DD-5e-Character-for-Beginners/

#Class
##(random choice): Race, Class, Origin
##(rolls): Strength, dexterity, constitution, intellegence, wisdom, charisma, armorclass, initiative, 

race = "Race: Dragonborn","Race: Dwarf","Race: Elf","Race: Gnome","Race: Half-Elf","Race: Half-Orc","Race: Halfling","Race: Human","Race: Tiefling"
rchoice = int(random(len(race)))  

origin = ['Origin: Acolyte','Origin: Criminal','Origin: Folk Hero','Origin: Noble','Origin: Soldier']
ochoice = int(random(len(origin)))


classlist = ['Class: Barbarian','Class: Bard','Class: Cleric','Class: Druid','Class: Fighter','Class: Monk','Class: Paladin','Class: Ranger','Class: Rogue', 'Class: Sorcerer', 'Class: Warlock', 'Class: Wizard'] 
cchoice = int(random(len(classlist)))    


def Font1():
    Font1 = createFont("Old English Text MT", 26) 

def setup():
    size (850, 1100)

def draw():
    background(222,184,135);
      
    Font1 = createFont("Old English Text MT", 26) 
    textFont(Font1)
    fill(0);
    text(race[rchoice], 30, 100)
    
    Font1 = createFont("Old English Text MT", 26) 
    textFont(Font1)
    fill(0);
    text(origin[ochoice], 330, 100)
    
    Font1 = createFont("Old English Text MT", 26) 
    textFont(Font1)
    fill(0);
    text(classlist[cchoice], 630, 100)

    
    #random (3-19)
  
