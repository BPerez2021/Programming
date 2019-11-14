
  #Changes 
  
class car(object):
    def __init__(self, c, xpos, ypos, xspeed):
        self.c = c
        self.xpos = xpos
        self.ypos = ypos
        self.xspeed = xspeed

    def display(self):
        stroke(0)
        fill(self.c)
        rectMode(CENTER)
        rect(self.xpos, self.ypos, 75, 50);
#3-1.1  I enlarged the size of the cars-->Unicycles as well as changed the shape
    def colorchange(self, newcolor):
        self.c = newcolor
        
        
    def drive(self):
        self.xpos = self.xpos + self.xspeed;
        if self.xpos > width:
            self.xpos = 0
        if self.xpos < 0:
            self.xpos = width

class Unicycle(object):
#3.3 Car--> Unicycle: I lost three wheels
    def __init__(self, c, xpos, ypos, xspeed):
        self.c = c
        self.xpos = xpos
        self.ypos = ypos
        self.xspeed = xspeed

    def display(self):
        stroke(0)
        fill(self.c)
        rectMode(CENTER)
        rect(self.xpos, self.ypos, 30,20);
    def colorchange(self, newcolor):
        self.c = newcolor
        

    def drive(self):
        self.ypos = self.ypos + self.xspeed;
        if self.xpos > width:
            self.xpos = 0
        if self.xpos < 0:
            self.xpos = width
  #I changed the direction of the Unicycle, so now they are "crossing" the street          

class Wheel(object):
    def __init__(self, c, xpos, ypos, xspeed):
        self.c = c
        self.xpos = xpos
        self.ypos = ypos
        self.xspeed = xspeed
        
    def updatelocation(self, xpos, ypos):
        self.xpos=xpos
        self.ypos=ypos

    def display(self):
        stroke(0)
        fill(self.c)
        ellipseMode(CENTER)
        ellipse(self.xpos, self.ypos, 10,10);
        
myWheel1 = Wheel(color(0, 0, 0), 0, 0, 1)
def mousePressed():
     myWheel1.updatelocation(mouseX, mouseY)    
     
        
        
mycar1 = car(color(255, 0, 0), 0, 450, 3)
mycar2 = car(color(0, 55, 255), 500, 100, -3)
mycar3 = car(color(0, 255, 255), 300, 10, -.5)
mycar4= car(color(0, 25, 100), 370, 300, 3)
mycar5 = car(color(50, 0, 255), 250, 250, .5)

myUnicycle1 = Unicycle(color(225, 225, 0), 300, 200, .57)
myUnicycle2= Unicycle(color(150, 100,0), 100, 30, .25)
myUnicycle3= Unicycle(color(150, 50,0), 400,400, 1)
myUnicycle4= Unicycle(color(50, 100,0), 500, 75,-.57)



def setup():

    size(500,500)


def draw(): 

  background(255)

  mycar1.drive()
  mycar1.display()

  mycar2.drive()
  mycar2.display()
  
  mycar3.drive()
  mycar3.display()

  mycar4.drive()
  mycar4.display()
  
  mycar5.drive()
  mycar5.display()
  
  myUnicycle1.drive()
  myUnicycle1.display()
  
  myUnicycle2.drive()
  myUnicycle2.display()
  
  myUnicycle3.drive()
  myUnicycle3.display()
  
  myUnicycle4.drive()
  myUnicycle4.display()  
  
  myWheel1.display()
  
  
  if ((keyPressed) and (key == ' ')):
      mycar1.colorchange(color(random(255), random (255), random (255)))
      mycar3.colorchange(color(random(255), random (255), random (255)))
      mycar5.colorchange(color(random(255), random (255), random (255)))
      myUnicycle2.colorchange(color(random(255), random (255), random (255)))
      myUnicycle4.colorchange(color(random(255), random (255), random (255)))
  if ((keyPressed) and (key == 'b')):
      mycar2.colorchange(color(0, 0, 0))
      mycar4.colorchange(color(0, 0, 0))
      myUnicycle1.colorchange(color(0, 0, 0))
      myUnicycle3.colorchange(color(0, 0, 0))
      
  if ((keyPressed) and (key == 'z')):
      mycar2.colorchange(color(random(255), random (255), random (255)))
      mycar4.colorchange(color(random(255), random (255), random (255)))
      myUnicycle1.colorchange(color(random(255), random (255), random (255)))
      myUnicycle3.colorchange(color(random(255), random (255), random (255)))
      
      
