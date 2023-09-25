import random

def setup():
    global circx
    global circy
    global circx2
    global circy2
    global circx3
    global circy3
    global circx4
    global circy4
    global r
    global g
    global b
    global rr
    global rg
    global rb
    circx = width / 2
    circy = height / 2
    circx2 = width / 2
    circy2 = height / 2
    circx3 = width / 2
    circy3 = height / 2
    circx4 = width / 2
    circy4 = height / 2
    
    r = 0
    g = 255
    b = 0
    
    rr = 0
    rg = 0
    rb = 0
    

    
    size(500,500)
    
x = 0

def draw():
    global circx
    global circy
    global circx2
    global circy2
    global circx3
    global circy3
    global circx4
    global circy4
    global r
    global g
    global b
    global rr
    global rg
    global rb
    
    fill(r,g,b)
    r = r + 1
    g = g - 1
    b = b + 1
    
    rr = random.randint(0,255)
    rg = random.randint(0,255)
    rb = random.randint(0,255)
    stroke(rr,rg,rb)
    
    rect(0, mouseX, mouseY, 50)
    
    
    circle(circx, circy, 100)
    circle(circx2, circy2,100)
    circle(circx3, circy3,100)
    circle(circx4, circy4,100)

    circx = circx + 1
    circy = circy + 1
    
    circx2 = circx2 - 1
    circy2 = circy2 - 1
    
    circx3 = circx3 + 1
    circy3 = circy3 - 1
    
    circx4 = circx4 - 1
    circy4 = circy4 + 1

    
    
