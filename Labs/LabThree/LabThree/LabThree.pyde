
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
#when adding the Unicycle class the sizes of the objects became smaller and uniform even though my desired result was to have the unicyle be smaller
    def colorchange(self, newcolor):
        self.c = newcolor
        

    def drive(self):
        self.xpos = self.xpos + self.xspeed;
        if self.xpos > width:
            self.xpos = 0
        if self.xpos < 0:
            self.xpos = width

class Wheel(object):
#3.4 the lost wheels
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
     
 #yet another code that refuses to work with me, this one won't produce the ellipse and when I do click there is no error that pops up...so what's wrong
 #I did play with the color and the size of the ellipse (Wheels) to see if that changes anything  
 #I forgot to put it in display....day of forgetfulness
        
        
mycar1 = car(color(255, 0, 0), 0, 450, 3)
mycar2 = car(color(0, 55, 255), 500, 100, -3)
 #3-1.2 I made blue car go backwards, but once it "drives" off the screen it doesnt return
mycar3 = car(color(0, 255, 255), 300, 10, -.5)
mycar4= car(color(0, 25, 100), 370, 300, 3)
mycar5 = car(color(50, 0, 255), 250, 250, .5)

myUnicycle1 = Unicycle(color(225, 225, 0), 300, 200, .57)
myUnicycle2= Unicycle(color(150, 100,0), 100, 30, .25)
myUnicycle3= Unicycle(color(150, 50,0), 400,400, 1)
myUnicycle4= Unicycle(color(50, 100,0), 500, 75,-.57)

#^It doesnt want to join the other 2: Tried changing the various variables in order to make it join the screen...didnt work. even made the size of the screen larger


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
  
  #I had forgotten to add "MyUnicycle"
  
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
      
#I know to use what I learned in 3-2 with the space key to apply specific changes, but dont know how to have the instructions on the screen
      
#asked peer for help theirs worked with this code, but I am having trouble, "AttributeError:'car' object has no attribute 'setcolor'"
#istnt the set color defined under the "define drive" collection where "mycar1" and friends are all given their colors, locations, and speed??
#HEY LOOK I FIGURED IT OUT...had forgotten to define the change color in the classes
