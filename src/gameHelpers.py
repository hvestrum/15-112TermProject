from cmu_graphics import *
import random
cream = rgb(247, 231, 206)
tan = rgb(210, 180, 140)
moreRed = rgb(210, 105, 30)

class DrawScreen:
    @staticmethod
    def drawCafe():
        #background image for the taking orders
        # Used https://sora.com to generate image
        drawImage('customerScreenNoCoffee.jpeg', 0, 0, width = app.width, 
                height = app.height)
        #textbox for order
        drawRect(50, 100, 800, 60, fill = cream, border = tan, borderWidth = 5)
        #button to click kitchen
        drawRect(310, 560, 270, 40, fill = 'lightblue', border = tan)
        drawLabel('K I T C H E N', 350, 570, fill = 'saddleBrown', size = 30, 
                  align = 'top-left')
        drawLabel(f'{app.geminiResponse}', 450, 130, fill = 'saddleBrown', 
                  size = 20, align = 'center')

        
    @staticmethod
    def drawCup():
        # Used https://sora.com to generate image
        drawImage('sizeChoice.png', 0, 0, width = app.width, 
                height = app.height)
        drawRect(180, 400, 270, 40, fill = cream, border = moreRed, 
             borderWidth = 5)
        drawLabel("click on the customer's cup size", 315, 420, 
              fill = 'saddleBrown', size = 16, bold = True)
        
    
    @staticmethod
    def drawMilk():
        # Used https://sora.com to generate image
        drawImage('milkChoice.jpeg', 0, 0, width = app.width, 
                height = app.height)
        drawRect(120, 400, 70, 30, fill = 'lightCyan', border = tan,
                 borderWidth = 5, opacity = 90)
        drawLabel('ICED', 155, 415, fill = 'saddleBrown', size = 15,bold = True)
        drawRect(210, 400, 70, 30, fill = 'lightCoral', border = tan,
                 borderWidth = 5, opacity = 85)
        drawLabel('HOT', 245, 415, fill = 'saddleBrown', size = 15, bold = True)

        #added directions for milk and temperature
        drawRect(50, 150, 350, 40, fill = cream, border = moreRed, 
             borderWidth = 5)
        drawLabel("click on the customer's milk and tempature", 225, 170, 
              fill = 'saddleBrown', size = 16, bold = True)
        
        #draw instructions for opencv POUR (turn) second
        drawRect(380, 240, 500, 60, fill = cream, border = moreRed,
                  borderWidth = 5)
        drawLabel("to unlock the milk, show your right hand, palm facing the",
                  630, 260, fill = 'saddleBrown', size = 16, bold = True)
        drawLabel("camera and slowly rotate your hand 90 degrees to the left", 
                  630, 280, fill = 'saddleBrown', size = 16, bold = True)
    
    @staticmethod
    def drawHowTo():
        # Used https://sora.com to generate image
        drawImage('howToImage.png', 0,0, width=app.width, height=app.height)
        drawRect(650, 435, 150, 50, fill= rgb(71,85,55), 
                border='black', borderWidth=4,)
        drawLabel('B A C K', 725,460, bold=True, size=25, fill=rgb(206,166,104),
                font = 'sansSerif')
    
    @staticmethod
    def drawButtons():
        #buttons for each part
        #cup size
        drawRect(50, 570, 181, 30, fill = 'lightblue', border = tan)
        drawLabel('CUP SIZE', 140, 585, fill = 'saddleBrown', bold = True,
                size = 20)
        #syrup
        drawRect(256, 570, 181, 30, fill = 'lightblue', border = tan)
        drawLabel('SYRUP', 346, 585, fill = 'saddleBrown', bold = True,
                size = 20)
        #milk and temp
        drawRect(462, 570, 181, 30, fill = 'lightblue', border = tan)
        drawLabel('MILK+TEMP', 552, 585, fill = 'saddleBrown', bold = True,
                size = 20)
        #draw Finish Label
        drawRect(668, 570, 181, 30, fill = 'paleGreen', border = tan)
        drawLabel('FINISH', 758, 585, fill = 'saddleBrown', bold = True,
                size = 20)
        
    @staticmethod
    def drawStartscreen():
        #background screen
        drawImage('OpeningScreen.jpeg', 0, 0, 
            width=app.width, height=app.height)

        #start button
        drawRect(app.width//2-app.rectWidth//2, 
            app.height//2-app.rectHeight*2, app.rectWidth, app.rectHeight, 
            fill='lightBlue', border = tan, borderWidth = 5)
        drawLabel("PLAY", app.width//2,225,bold=True, size=20, 
                  fill = 'saddleBrown')

        #howTo button
        drawRect(app.width//2-app.rectWidth//2, app.height//2+app.rectHeight, 
            app.rectWidth, app.rectHeight, fill='lightBlue', border = tan,
            borderWidth = 5)
        drawLabel("HOW TO", app.width//2, 375, bold=True, size=20,
                  fill = 'saddleBrown')
    
    @staticmethod
    def drawSyrup():
        # Used https://sora.com to generate image
        drawImage('syrupScreenImage.png', 0, 0, width = app.width, 
                height = app.height)
        #title of order
        drawRect(100, 10, 700, 60, fill = cream, border = tan, borderWidth = 5)
        drawLabel(f'{app.geminiResponse}', 450, 40, fill = 'saddleBrown', 
                  size = 20)
        #added directions for syrup
        drawRect(420, 250, 270, 40, fill = cream, border = moreRed, 
             borderWidth = 5)
        drawLabel("click on the customer's syrup", 555, 270, 
              fill = 'saddleBrown', size = 16, bold = True)
        
        #draw Instructions for opencv STIR (fist) first
        drawRect(150, 100, 500, 60, fill = cream, border = moreRed,
                  borderWidth = 5)
        drawLabel("to unlock the syrup, show your right fist facing the",
                  400, 120, fill = 'saddleBrown', size = 16, bold = True)
        drawLabel("camera", 400, 140, 
                  fill = 'saddleBrown', size = 16, bold = True)
    
    @staticmethod
    def goodEnding():
        # Used https://sora.com to generate image
        drawImage('goodEnding.jpeg', 0, 0, width=app.width, 
                    height=app.height)
        drawRect(100, 145, 700, 60, fill = cream, 
                    border = tan, borderWidth = 5)
        drawLabel(f"{random.choice(['Kosbie','Mike'])}: {app.customerResponse}", 
                  450, 175, align='center', bold=True, 
                  size = 16,fill = 'saddleBrown')
        drawRect(650, 215, 100, 50, fill= cream, border=tan, borderWidth=5)
        drawLabel('NEXT', 700, 240, align='center', bold=True, size=20,
                    fill = 'saddleBrown')
        #draw total price
        drawRect(350, 450, 200, 100, fill=cream, border=tan, borderWidth=4)
        drawLabel(f'{app.label.getPrice(app)}', 450, 500, bold=True, 
                  size=16, fill='saddleBrown')
    
    @staticmethod
    def badEnding():
        # Used https://sora.com to generate image
        drawImage('customerScreenNoCoffee.jpeg', 0, 0, 
                width=app.width, height=app.height)
        drawRect(100, 145, 700, 60, fill = cream, border = tan, 
                    borderWidth = 5)
        drawLabel(f'Kosbie: {app.customerResponse}', 450, 175, 
                    align='center', bold=True, size = 16,fill = 'saddleBrown')
        drawRect(650, 215, 100, 50, fill= cream, border=tan, borderWidth=5)
        drawLabel('NEXT', 700, 240, align='center', bold=True, size=20,
                    fill = 'saddleBrown')
        #draw total price
        drawRect(350, 450, 200, 100, fill=cream, border=tan, borderWidth=4)
        drawLabel(f'{app.label.getPrice(app)}', 450, 500, bold=True, 
                  size=16, fill='saddleBrown')
    
    @staticmethod
    def kosbieGone():
        drawImage('kosbieGone.jpeg', 0, 0, width=app.width, 
                      height=app.height)
        drawRect(390, 350, 100, 50, fill=cream, border=tan, borderWidth=5)
        drawLabel('HOME', 440, 375, size=20, bold=True, fill='saddleBrown')
    
    @staticmethod
    def gameOver():
        # Used https://sora.com to generate image
        drawImage('gameOver_sproutCoffee.png', 0, 0, 
                width=app.width, height=app.height)
        drawRect(390, 350, 100, 50, fill=cream, border=tan, borderWidth=5)
        drawLabel('HOME', 440, 375, size=20, bold=True, fill='saddleBrown')