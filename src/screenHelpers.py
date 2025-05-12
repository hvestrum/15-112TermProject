from cmu_graphics import *
import random
from classHands import detectHand

class DrinkOrder:
    def __init__(self, app):
        self.milk = {'oat':1.00, 'soy': 1.00, 'whole':0}
        self.syrup = {'chocolate': 1.00, 'vanilla':1.00, 'almond':1.50,
                      'hazelnut':1.50, 'raspberry':1.50}
        self.heat = {'hot':0, 'iced':0}
        self.size = {'small': 4.50, 'medium': 5.25, 'large': 5.75}
    
    def getPrice(self, app):
        total = 0
        if app.orderList['milk'] != None:
            total += self.milk[app.orderList['milk']]
        if app.orderList['syrup'] != None:
            total += self.syrup[app.orderList['syrup']]
        if app.orderList['temp'] != None:
            total += self.heat[app.orderList['temp']]
        if app.orderList['size'] != None:
            total += self.size[app.orderList['size']]
        return f"Your total is ${total}."
    
    def getOrder(self):
        milk = random.choice(list(self.milk.keys()))
        syrup = random.choice(list(self.syrup.keys()))
        heat = random.choice(list(self.heat.keys()))
        size = random.choice(list(self.size.keys()))
        return(f"I would like to order a {size} drink with {syrup} syrup "
                f"that is {heat} with {milk} milk!")
    
class makeOrderHelpers:
    def clickOptionsMilk(self, x, y):
        if 150 <= x <= 190 and 200 <= y <= 350:
            if app.orderList['milk'] == None and app.flagMilk:
                app.orderList['milk'] = 'oat'
        elif 200 <= x <= 243 and 200 <= y <= 350:
            if app.orderList['milk'] == None and app.flagMilk:
                app.orderList['milk'] = 'soy'
        elif 255 <= x <= 290 and 200 <= y <= 350:
            if app.orderList['milk'] == None and app.flagMilk:
                app.orderList['milk'] = 'whole'

    def clickOptionSyrup(self, x, y):
        if 450 <= x <= 485 and 320 <= y <= 470:
            if app.orderList['syrup'] == None and app.flagSyrup:
                app.orderList['syrup'] = 'hazelnut'
        #vanilla
        elif 490 <= x <= 525 and 320 <= y <= 470:
            if app.orderList['syrup'] == None and app.flagSyrup:
                app.orderList['syrup'] = 'vanilla'
        #almond
        elif 530 <= x <= 570 and 320 <= y <= 470:
            if app.orderList['syrup'] == None and app.flagSyrup:
                app.orderList['syrup'] = 'almond'
        #chocolate
        elif 580 <= x <= 615 and 320 <= y <= 470:
            if app.orderList['syrup'] == None and app.flagSyrup:
                app.orderList['syrup'] = 'chocolate'
        #raspberry
        elif 620 <= x <= 665 and 320 <= y <= 470:
            if app.orderList['syrup'] == None and app.flagSyrup:
                app.orderList['syrup'] = 'raspberry'

    def clickOptionsTemp(self, x, y):
        #choose iced or hot
        if 120 <= x <= 190 and 400 <= y <= 430:
            if app.orderList['temp'] == None:
                app.orderList['temp'] = 'iced'
        elif 210 <= x <= 280 and 400 <= y <= 430:
            if app.orderList['temp'] == None:
                app.orderList['temp'] = 'hot'

    def clickOptionCupSize(self, x, y):
        if 200 <= x <= 275 and 500 <= y <= 550:
            if app.orderList['size'] == None:
                app.orderList['size'] = 'small'
        elif 280 <= x <= 350 and 495 <= y <= 550:
            if app.orderList['size'] == None:
                app.orderList['size'] = 'medium'
        elif 360 <= x <= 440 and 400 <= y <= 550:
            if app.orderList['size'] == None:
                app.orderList['size'] = 'large'

class additionalButtons:
    
    @staticmethod
    def clickEndGameButton(x, y):
        if 0 <= x <= 100 and 0 <= y <= 50:
            app.gameOver = True
        if app.gameOver:
            if 390 <= x <= 490 and 350 <= y <= 400:
                app.gameOver = False
                app.screenMode = 'startScreen'

    @staticmethod
    def kitchenNavigationButton(x, y):
        if 50 <= x <= 231 and 570 <= y <= 600:
            app.screenMode = 'cupScreen'
        #click the syrup bar to bring to syrup
        if 256 <= x <= 437 and 570 <= y <= 600:
            app.screenMode = 'syrupScreen'
        if 462 <= x <= 643 and 570 <= y <= 600:
            app.screenMode = 'milkScreen'
        if 668 <= x <= 849 and 570 <= y <= 600:
            app.screenMode = 'finishScreen'

    @staticmethod
    def startScreenNav(x, y):
        if 375 <= x <= 525 and 200 <= y <= 250:
            app.screenMode = 'cafe'
        if 375 <= x <= 525 and 350 <= y <= 400:
            app.screenMode = 'howTo'

class endingHelper:
    def getBadEnding(x, y):
        if 650 <= x <= 750 and 215 <= y <= 265:
            app.kosbieGone = True
            app.badEnding = False

    def getGoodEnding(x, y):
        if 650 <= x <= 750 and 215 <= y <= 265:
            app.goodEndingTransition = True
            app.screenMode = 'cafe'
            app.goodEnding = False
    
    def getKosbieGone(x, y):
        if 650 <= x <= 750 and 215 <= y <= 265:
            app.gameOver = True
            app.kosbieGone = False

    def getGameOver(x, y):
        if 390 <= x <= 490 and 350 <= y <= 400:
            app.screenMode = 'startScreen'
            app.badEnding = False
            app.goodEnding = False
            app.kosbieGone = False
            app.gameOver = False

    def getFinishScreen(x, y):
        print('orderList', app.orderList)
        if app.orderList == app.customerOrder:
            app.badEnding = False
            app.goodEnding = True
        else: 
            app.goodEnding = False
            app.badEnding = True
