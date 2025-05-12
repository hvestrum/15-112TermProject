from cmu_graphics import * 

def onAppStart(app):
    app.width = 900
    app.height = 600
    app.takingOrder = True
    app.kitchen = False

def redrawAll(app):
    if app.takingOrder:
    #background image for the taking orders
        drawImage('customerScreenNoCoffee.jpeg', 0, 0, width = app.width, 
                height = app.height)
        cream = rgb(247, 231, 206)
        tan = rgb(210, 180, 140)
        #textbox for order
        drawRect(100, 100, 700, 60, fill = cream, border = tan, borderWidth = 5)
        #button to click kitchen
        drawRect(310, 560, 270, 40, fill = 'lightblue', border = tan)
        drawLabel('K I T C H E N', 350, 570, fill = 'saddleBrown', size = 30, 
                align = 'top-left', bold = True)
    
def onMousePress(app, mouseX, mouseY):
    if 310 <= mouseX <= 620 and 560 <= mouseY <= 600:
        app.kitchen = True
        app.takingOrder = False
        


#random

runApp()