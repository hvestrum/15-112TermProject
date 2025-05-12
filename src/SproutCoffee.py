# class to help determine which buttons are clicked on
# class to help determine which drink customization options are available
from screenHelpers import makeOrderHelpers, additionalButtons
from screenHelpers import DrinkOrder, endingHelper
from gameHelpers import DrawScreen
from classHands import detectHand

import google.generativeai as genai

from cmu_graphics import *
genai.configure(api_key="")

def onAppStart(app):
    # for screen and button sizing
    app.width = 900
    app.rectWidth = 150
    app.rectHeight = 50
    app.height = 600
    # sound used from https://youtu.be/iPzmBKQVcjo?si=VbXt3iWHhox-qjNh,
    app.sound = Sound('sound.mp3')
    app.sound.play(restart = True)
    app.stepsPerSecond = 5


    # used ai.google.dev: 
    # https://ai.google.dev/gemini-api/docs/quickstart?lang=python
    app.model = genai.GenerativeModel("gemini-2.0-flash-lite")

    #class for the order
    app.label = DrinkOrder(app)
    resetApp(app)

    # for screen modes
    app.screenMode = 'startScreen'

def resetApp(app):
    app.new = app.label.getOrder()

    # customer's displayed order
    response1 = app.model.generate_content(f"Take {app.new} and"
        f"give the barista your order in 1-2 sentences, max 100 characters.")
    app.geminiResponse = response1.candidates[0].content.parts[0].text
    print(app.geminiResponse)

    # dictionary of order information
    # dictionary built throughout process

    # dictionary built on customer screen
    app.customerOrder = {'milk':None, 'syrup':None, 'temp': None, 'size': None}

    #FOR TP PUT INTO ORDERTYPE CLASS in makingOrders.py
    # from chatGPT
    app.customerOrder['syrup'] = app.new.split(" with ")[1].split(" syrup")[0]

    # not from chatGPT
    app.customerOrder['size'] = app.new.split("order a ")[1].split(" drink")[0]
    app.customerOrder['temp'] = app.new.split("that is ")[1].split(" with")[0]
    app.customerOrder['milk'] = app.new.split(" with ")[-1].split(" milk!")[0]

    app.orderList={'milk':None,'syrup':None,'temp':None,'size':None}

    #ending for making drinks
    app.goodEnding = False
    app.kosbieGone = False
    app.badEnding = False
    app.customerResponse = None
    app.gameOver = False
    app.goodEndingTransition = False

    app.flagMilk = False
    app.flagSyrup = False
    app.detector = detectHand()
    app.detector.startThreadDetection()

def redrawAll(app):
    #color
    cream,tan=rgb(247, 231, 206),rgb(210, 180, 140)

    if app.screenMode == 'startScreen': DrawScreen.drawStartscreen()

    elif app.screenMode == 'howTo': DrawScreen.drawHowTo()

    elif app.screenMode == 'cafe': DrawScreen.drawCafe()
    
    elif app.screenMode == 'cupScreen': DrawScreen.drawCup()

    elif app.screenMode == 'milkScreen': DrawScreen.drawMilk()
   
    elif app.screenMode == 'syrupScreen': DrawScreen.drawSyrup()
    
    elif app.screenMode == 'finishScreen':
        if app.goodEnding: DrawScreen.goodEnding()
        elif app.badEnding: DrawScreen.badEnding()
        elif app.kosbieGone: DrawScreen.kosbieGone()
       
    if app.gameOver: DrawScreen.gameOver()

    # tokens on milkScreen, syrupScreen, and cupScreen!
    if(app.screenMode=='milkScreen'or app.screenMode=='syrupScreen'or
        app.screenMode == 'cupScreen'):
        #order question
        #end game button
        if not app.gameOver:
            drawRect(50, 10, 800, 60,fill = cream,border = tan, borderWidth = 5)
            drawLabel(f'{app.geminiResponse}',450,40,fill='saddleBrown',
                  size=20,align='center')
            #order table
            drawRect(700, 100, 150, 125, fill = cream,border=tan,borderWidth=5)
            drawLabel('order in progress:',775,120,fill='saddleBrown',
                      size= 15,bold=True)
            cx, cy = 775, 145
            for key in app.orderList:
                if app.orderList[key] != None:
                    drawLabel(app.orderList[key], cx, cy, align='center', 
                            fill='saddleBrown', size=15)
                    cy += 15
            drawRect(0, 0, 100, 25, fill=cream, border=tan, borderWidth = 3)
            drawLabel('End Game', 50, 13, bold=True, fill='red')

            DrawScreen.drawButtons()

# initializing variables as classes
orderHelper = makeOrderHelpers()        
buttonHelper = additionalButtons()     
def onMousePress(app, mouseX, mouseY):
    if app.screenMode=='startScreen':
        buttonHelper.startScreenNav(mouseX,mouseY)
        resetApp(app)

    elif app.screenMode == 'cafe':
        if 310<=mouseX<=620 and 560<=mouseY<=600: app.screenMode='cupScreen'
    
    # check endgame button or kitchen navigation buttons
    elif (app.screenMode =='cupScreen' or app.screenMode == 'milkScreen' or 
          app.screenMode == 'syrupScreen'):
        #check endgame button
        buttonHelper.clickEndGameButton(mouseX, mouseY)
        #click milk, syrup, or cup button
        buttonHelper.kitchenNavigationButton(mouseX, mouseY)

    if app.screenMode=='cupScreen':orderHelper.clickOptionCupSize(mouseX,mouseY)

    if app.screenMode == 'milkScreen':
        #click to choose milk
        orderHelper.clickOptionsMilk(mouseX, mouseY)
        #choose iced or hot
        orderHelper.clickOptionsTemp(mouseX, mouseY)

    # checks which bottles are clicked on
    if app.screenMode=='syrupScreen':orderHelper.clickOptionSyrup(mouseX,mouseY)
        
    #how to screen
    if app.screenMode == 'howTo':
        if 650<=mouseX<=800 and 435<=mouseY<=485: app.screenMode='startScreen'

    if app.screenMode == 'finishScreen':  
        endingHelper.getFinishScreen(mouseX, mouseY)

    if app.screenMode == 'finishScreen':
        if app.badEnding:
            response = app.model.generate_content("Respond in 1-2 sentences " \
            "expressively to a barista who made your drink order wrong. " \
            "You're very angry. Don't include options in your response. " \
            "Maximum 100 characters.")

        elif app.goodEnding:
            response = app.model.generate_content("Respond in 1-2 sentences " \
            "expressively to a barista who made your drink order correctly. " \
            "You're very very happy. Don't include options in your response. " \
            "Maximum 100 characters.")

        # referenced chatGPT for text extraction help
        app.customerResponse = response.candidates[0].content.parts[0].text

    if app.badEnding: endingHelper.getBadEnding(mouseX, mouseY)
        
    if app.goodEnding: endingHelper.getGoodEnding(mouseX, mouseY)

    if app.kosbieGone: endingHelper.getKosbieGone(mouseX, mouseY)

    if app.gameOver: endingHelper.getGameOver(mouseX, mouseY)

    if app.goodEndingTransition: resetApp(app)

# def onStep(app):
    #these were commented out due to difficulties to implement
    #opencv with two different mains and thus only one was able
    #to be kept in without the use of threading
    # if app.flagMilk == False:
    #     detectHand.main1()
    # if app.flagSyrup:
        # print('app.flagSyrup is True')
        # app.flagSyrup = True

        # print('app.flagSyrup is False')
        # detectHand.main2()
    # if app.main1:
    #     if detectHand.main1() == True:
    #         print('hi')
    #         app.milk = True
    #         app.main1 = False
    # if app.main2:
    #     if detectHand.main2():
    #         ####
    #         app.main2 = False
    #     app.milk = False

def onAppStop(app):
    app.detector.stopThreadDetection()


runApp()
