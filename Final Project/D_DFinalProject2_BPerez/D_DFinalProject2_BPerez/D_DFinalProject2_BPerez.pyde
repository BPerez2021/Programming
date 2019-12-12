#Research   
##https://www.instructables.com/id/Creating-a-DD-5e-Character-for-Beginners/

#Class
##(random choice): Race, Class, Origin
##(rolls): Strength, dexterity, constitution, intellegence, wisdom, charisma, armorclass, initiative, 


race = "Race: Dragonborn","Race: Dwarf","Race: Elf","Race: Gnome","Race: Half-Elf","Race: Half-Orc","Race: Halfling","Race: Human","Race: Tiefling"
crace = 0     
    

origin = ['Origin: Acolyte','Origin: Criminal','Origin: Folk Hero','Origin: Noble','Origin: Soldier']
corigin= 0


classlist = ['Class: Barbarian','Class: Bard','Class: Cleric','Class: Druid','Class: Fighter','Class: Monk','Class: Paladin','Class: Ranger','Class: Rogue', 'Class: Sorcerer', 'Class: Warlock', 'Class: Wizard'] 
cclasslist=0



vstren = 0
vdex = 0
vcon = 0
vint = 0
vwis = 0
vcha = 0
varmc = 0
vinit = 0
#sr = 0 
#dr = 0
#conr = 0
#ir = 0
#wr = 0
#cr = 0
#acr = 0
#inr = 0
sr = (int(random(3, 19)))
dr = (int(random(3, 19)))
conr = (int(random(3, 19)))
ir = (int(random(3, 19)))
wr = (int(random(3, 19)))
cr = (int(random(3, 19)))
acr = (int(random(3, 19)))
inr = (int(random(3, 19)))


def keyPressed():
    global crace
    global corigin
    global cclasslist
    global rchoice
    global ochoice
    global cchoice
    global sr
    global dr
    global conr
    global ir
    global wr
    global cr
    global acr
    global inr
    crace = int(random(len(race))) 
    corigin = int(random(len(origin)))
    cclasslist = int(random(len(classlist)))
    rchoice = int(random(len(race))) 
    ochoice = int(random(len(origin)))
    cchoice = int(random(len(classlist)))
    sr = (int(random(3, 19)))
    dr = (int(random(3, 19)))
    conr = (int(random(3, 19)))
    ir = (int(random(3, 19)))
    wr = (int(random(3, 19)))
    cr = (int(random(3, 19)))
    acr = (int(random(3, 19)))
    inr = (int(random(3, 19)))


def Font1():
    Font1 = createFont("Old English Text MT", 26) 

def setup():
    size (850, 1100)

def draw():
    background(222,184,135); 
    Font1 = createFont("Old English Text MT", 30) 
    textFont(Font1)
    fill(0);
    text(race[crace], 30, 100)
    
    Font1 = createFont("Old English Text MT", 30) 
    textFont(Font1)
    fill(0);
    text(origin[corigin], 315, 100)
    
    Font1 = createFont("Old English Text MT", 30) 
    textFont(Font1)
    fill(0);
    text(classlist[cclasslist], 600, 100)
    
    Font1 = createFont("Old English Text MT", 26) 
    textFont(Font1)
    fill(0);
    text("Strength:", 30, 200)
    #text((int(random(3,19))), 135, 200)
    text((sr), 135, 200)
    
    Font1 = createFont("Old English Text MT", 26) 
    textFont(Font1)
    fill(0);
    text("Dexterity:", 30, 250)
    #text((int(random(3,19))), 140, 250)
    text((dr), 140, 250)
        
    Font1 = createFont("Old English Text MT", 26) 
    textFont(Font1)
    fill(0);
    text("Constitution:", 30, 300)
    #text((int(random(3,19))), 170, 300)
    text((conr), 170, 300)
        
    Font1 = createFont("Old English Text MT", 26) 
    textFont(Font1)
    fill(0);
    text("Intelligence:", 30, 350)
    #text((int(random(3,19))), 165, 350)
    text((ir), 165, 350)

    Font1 = createFont("Old English Text MT", 26) 
    textFont(Font1)
    fill(0);
    text("Wisdom:", 30, 400)
    #text((int(random(3,19))), 125, 400)
    text((wr), 125, 400)
        
    Font1 = createFont("Old English Text MT", 26) 
    textFont(Font1)
    fill(0);
    text("Charisma:", 30, 450)
    #text((int(random(3,19))), 140, 450)
    text((cr), 140, 450)
        
    Font1 = createFont("Old English Text MT", 26) 
    textFont(Font1)
    fill(0);
    text("Armorclass:", 30, 500)
    #text((int(random(3,19))), 160, 500)
    text((acr), 160, 500)
        
    Font1 = createFont("Old English Text MT", 26) 
    textFont(Font1)
    fill(0);
    text("Initiative:", 30, 550)
    #text((int(random(3,19))), 140, 550)
    text((inr), 140, 550)
    
    #note
