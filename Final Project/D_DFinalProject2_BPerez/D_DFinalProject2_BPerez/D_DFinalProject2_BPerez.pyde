#Research   
##https://www.instructables.com/id/Creating-a-DD-5e-Character-for-Beginners/

#Class
##(random choice): Race, Class, Origin
##(rolls): Strength, dexterity, constitution, intellegence, wisdom, charisma, armorclass, initiative, 


race = "Race: Dragonborn","Race: Dwarf","Race: Elf","Race: Gnome","Race: Half-Elf","Race: Half-Orc","Race: Halfling","Race: Human","Race: Tiefling"
def colorchange(self, newchoice):
    rchoice = changerace 
    
    

origin = ['Origin: Acolyte','Origin: Criminal','Origin: Folk Hero','Origin: Noble','Origin: Soldier']



classlist = ['Class: Barbarian','Class: Bard','Class: Cleric','Class: Druid','Class: Fighter','Class: Monk','Class: Paladin','Class: Ranger','Class: Rogue', 'Class: Sorcerer', 'Class: Warlock', 'Class: Wizard'] 
    



rchoice = int(random(len(race))) 
ochoice = int(random(len(origin)))
cchoice = int(random(len(classlist)))

newrchoice = int(random(len(race))) 
newochoice = int(random(len(origin)))
newcchoice = int(random(len(classlist)))


sr = random(3, 19)
dr = random(3, 19)
conr = random(3, 19)
ir = random(3, 19)
wr = random(3, 19)
cr = random(3, 19)
acr = random(3, 19)
inr = random(3, 19)

def Font1():
    Font1 = createFont("Old English Text MT", 26) 

def setup():
    size (850, 1100)

def draw():
    background(222,184,135);

    Font1 = createFont("Old English Text MT", 30) 
    textFont(Font1)
    fill(0); 
    text(race[rchoice], 30, 100)
    
    Font1 = createFont("Old English Text MT", 30) 
    textFont(Font1)
    fill(0);
    text(origin[ochoice], 315, 100)
    
    Font1 = createFont("Old English Text MT", 30) 
    textFont(Font1)
    fill(0);
    text(classlist[cchoice], 600, 100)

    Font1 = createFont("Old English Text MT", 26) 
    textFont(Font1)
    fill(0);
    text("Strength:", 30, 200)
    text((int(sr)), 135,200)

    Font1 = createFont("Old English Text MT", 26) 
    textFont(Font1)
    fill(0);
    text("Dexterity:", 30, 250)
    text((int(dr)), 140, 250)
    
    Font1 = createFont("Old English Text MT", 26) 
    textFont(Font1)
    fill(0);
    text("Constitution:", 30, 300)
    text((int(conr)), 170, 300)
    
    Font1 = createFont("Old English Text MT", 26) 
    textFont(Font1)
    fill(0);
    text("Intellegence:", 30, 350)
    text((int(ir)), 165, 350)
    
    Font1 = createFont("Old English Text MT", 26) 
    textFont(Font1)
    fill(0);
    text("Wisdom:", 30, 400)
    text((int(wr)), 125, 400)
    
    Font1 = createFont("Old English Text MT", 26) 
    textFont(Font1)
    fill(0);
    text("Charisma:", 30, 450)
    text((int(cr)), 140, 450)
    
    Font1 = createFont("Old English Text MT", 26) 
    textFont(Font1)
    fill(0);
    text("Armorclass:", 30, 500)
    text((int(acr)), 160, 500)
    
    Font1 = createFont("Old English Text MT", 26) 
    textFont(Font1)
    fill(0);
    text("Initiative:", 30, 550)
    text((int(inr)), 140, 550)
    
    if ((keyPressed) and (key == ' ')):
        
        Font1 = createFont("Old English Text MT", 30) 
        textFont(Font1)
        fill(0);
        newrchoice = int(random(len(race))) 
        text(race[newrchoice], 30, 100)
        
        Font1 = createFont("Old English Text MT", 30) 
        textFont(Font1)
        fill(0);
        newochoice = int(random(len(origin)))
        text(origin[newochoice], 315, 100)
        
        Font1 = createFont("Old English Text MT", 30) 
        textFont(Font1)
        fill(0);
        newcchoice = int(random(len(classlist)))
        text(classlist[newcchoice], 600, 100)
    
        Font1 = createFont("Old English Text MT", 26) 
        textFont(Font1)
        fill(0);
        text("Strength:", 30, 200)
        text((int(random(3,19))), 135, 200)
    
        Font1 = createFont("Old English Text MT", 26) 
        textFont(Font1)
        fill(0);
        text("Dexterity:", 30, 250)
        text((int(random(3,19))), 140, 250)
        
        Font1 = createFont("Old English Text MT", 26) 
        textFont(Font1)
        fill(0);
        text("Constitution:", 30, 300)
        text((int(random(3,19))), 170, 300)
        
        Font1 = createFont("Old English Text MT", 26) 
        textFont(Font1)
        fill(0);
        text("Intellegence:", 30, 350)
        text((int(random(3,19))), 165, 350)
        
        Font1 = createFont("Old English Text MT", 26) 
        textFont(Font1)
        fill(0);
        text("Wisdom:", 30, 400)
        text((int(random(3,19))), 125, 400)
        
        Font1 = createFont("Old English Text MT", 26) 
        textFont(Font1)
        fill(0);
        text("Charisma:", 30, 450)
        text((int(random(3,19))), 140, 450)
        
        Font1 = createFont("Old English Text MT", 26) 
        textFont(Font1)
        fill(0);
        text("Armorclass:", 30, 500)
        text((int(random(3,19))), 160, 500)
        
        Font1 = createFont("Old English Text MT", 26) 
        textFont(Font1)
        fill(0);
        text("Initiative:", 30, 550)
        text((int(random(3,19))), 140, 550)
