from graph import *

windowSize(600, 800)
canvasSize(600, 800)
penColor(10, 250, 255)
brushColor(10, 200, 255)
rectangle(0, 350, 600, 0)
penColor(10, 255, 0)
brushColor(10, 255, 0)
rectangle(0, 800, 600, 350)
penColor(255, 255, 0)
brushColor(255, 255, 0)
circle(550, 50, 80)


def tree(x, y, a):
    brushColor(200, 200, 150)
    penColor(200, 200, 150)
    rectangle(x + a * 22, y, x + a * 28, y - a * (90 - 65))
    brushColor(30, 125, 10)
    penColor(0, 255, 10)
    
    ELIPSCOUNT = 4
    LEFTBOTX = [10, 0, 10, 0]
    LEFTBOTY = [45, 55, 70, 35]
    RIGHTTOPX = [40, 50, 40, 50]
    RIGHTTOPY = [0, 25, 50, 75]
    for i in range(ELIPSCOUNT):
        rtx = x + a * RIGHTTOPX[i] 
        lbx = x + a * LEFTBOTX[i] 
        rty = y - a * (90 - RIGHTTOPY[i])
        lby = y - a * (90 - LEFTBOTY[i])
        changeCoords(circle(0, 0, 10), [(rtx, rty), (lbx, lby)])

    #changeCoords(circle(0, 0, 10), [(x + a * 40, y - a * (90 - 0)), (x + a * 10, y - a * (90 - 45))])
    #changeCoords(circle(0, 0, 10), [(x + a * 0, y - a * (90 - 55)), (x + a * 50, y - a * (90 - 25))])
    #changeCoords(circle(0, 0, 10), [(x + a * 10, y - a * (90 - 70)), (x + a * 40, y - a * (90 - 50))])
    brushColor(255, 50, 80)
    penColor(255, 30, 50)
    circle(x + a * 30, y - a * (90 - 10), 3 * a)
    circle(x + a * 30, y - a * (90 - 60), 3 * a)
    circle(x + a * 10, y - a * (90 - 45), 3 * a)
    circle(x + a * 40, y - a * (90 - 40), 3 * a)


tree(30, 400, 1.2)
tree(110, 420, 1.3)
tree(170, 400, 1.1)
tree(200, 450, 1.7)
tree(40, 500, 2)
tree(100, 600, 2.4)
tree(150, 680, 2.7)
tree(10, 750, 3.1)
tree(550, 130, -0.5)


def unicorn(x, y, a):
    penColor(255, 255, 255)
    brushColor(255, 255, 255)
    changeCoords(circle(0, 0, 10), [(x + a * 40, y - a * (105 - 85)), (x + a * 90, y - a * (105 - 60))])
    changeCoords(circle(0, 0, 10), [(x + a * 75, y - a * (105 - 52)), (x + a * 98, y - a * (105 - 42))])
    changeCoords(circle(0, 0, 10), [(x + a * 70, y - a * (105 - 50)), (x + a * 90, y - a * (105 - 35))])
    rectangle(x + a * 70, y - a * (105 - 70), x + a * 85, y - a * (105 - 45))
    rectangle(x + a * 45, y - a * (105 - 105), x + a * 50, y - a * (105 - 75))
    rectangle(x + a * 56, y - a * (105 - 100), x + a * 61, y - a * (105 - 75))
    rectangle(x + a * 68, y - a * (105 - 105), x + a * 73, y - a * (105 - 75))
    rectangle(x + a * 79, y - a * (105 - 100), x + a * 84, y - a * (105 - 75))
    penColor(230, 180, 210)
    brushColor(230, 180, 210)
    polygon([(x + a * 79, y - a * (105 - 35)), (x + a * 83, y - a * (105 - 36)), (x + a * 82, y - a * (105 - 15))])
    circle(x + a * 83, y - a * (105 - 42), a * 2.5)
    brushColor(0, 0, 0)
    circle(x + a * 84, y - a * (105 - 42), a * 0.8)
    penColor(180 + randint(0, 70), 180 + randint(0, 50), 180 + randint(0, 75))
    brushColor(180 + randint(0, 70), 180 + randint(0, 50), 180 + randint(0, 75))
    polygon([(x + a * 50, y - a * (105 - 55)),
             (x + a * 60, y - a * (105 - 50)),
             (x + a * 73, y - a * (105 - 35)),
             (x + a * 76, y - a * (105 - 37)),
             (x + a * 75, y - a * (105 - 36)),
             (x + a * 71, y - a * (105 - 42)),
             (x + a * 70, y - a * (105 - 50)),
             (x + a * 72, y - a * (105 - 62)),
             (x + a * 55, y - a * (105 - 65))])
    penColor(180 + randint(0, 70), 180 + randint(0, 50), 180 + randint(0, 75))
    brushColor(180 + randint(0, 70), 180 + randint(0, 50), 180 + randint(0, 75))
    polygon([(x + a * 40, y - a * (105 - 85)),
             (x + a * 42, y - a * (105 - 74)),
             (x + a * 42, y - a * (105 - 70)),
             (x + a * 37, y - a * (105 - 73)),
             (x + a * 29, y - a * (105 - 90)),
             (x + a * 23, y - a * (105 - 92)),
             (x + a * 26, y - a * (105 - 98)),
             (x + a * 37, y - a * (105 - 98)),
             (x + a * 39, y - a * (105 - 92))])

unicorn(250, 455, 1.4)
unicorn(430, 425, 1.2)
unicorn(270, 545, 2)
unicorn(220,755, 3)


run()

