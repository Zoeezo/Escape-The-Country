from time import sleep
from Exceptions import HpZeroError
import os

class TextColors():
    white = '\033[37m'
    red = '\033[31m'
    blue = '\033[34m'
    green = '\033[32m'
    yellow = '\033[36m'

    endLine = '\033[0m'

    def isValidColor(self, color):
        if(color == self.white or color == self.red or color == self.blue or color == self.green or color == self.yellow):
            return True
        else:
            return False

class Console():
    def __init__(self, defaultTextColor = TextColors.white):
        if(TextColors.isValidColor(TextColors, defaultTextColor)):
            self.DefaultTextColor = defaultTextColor
        else:
            self.DefaultTextColor = TextColors.white
        
        self.clearScreen(prompt=False)

    def write(self, text, color = None, emptyString = True):
        if(not TextColors.isValidColor(TextColors, color)):
            color = self.DefaultTextColor

        string = ""
        length = len(text)
        index = 0

        for i in text:
            string += i

            # If it's the last char in the string
            if (length - 1 == index):
                print(color + string + TextColors.endLine)

                if(emptyString):
                    print()
            else:
                print(color + string + TextColors.endLine, end="\r", flush=True)
                index += 1
                sleep(0.1)

    def ask(self, question, answers = None, openQuestion = False, textColor = None):
        alphabet = ['A', 'B', 'C', 'D', 'E', 'F']

        if(not TextColors.isValidColor(TextColors, textColor)):
            TextColor = self.DefaultTextColor

        self.write(question, color=textColor)

        if(not openQuestion):
            i = 0

            for answer in answers:
                if (i + 1 == len(answers)):
                    self.write(alphabet[i].upper() + ' - ' + answer, color=textColor, emptyString=True)
                else:    
                    self.write(alphabet[i].upper() + ' - ' + answer, color=textColor, emptyString=False)
                    i += 1

        while True:
            userInput = input(textColor + 'Input: ').lower()
            print(TextColors.endLine)

            if(not openQuestion):
                x = 0
                while(x < len(answers)):
                    if(userInput == alphabet[x].lower()):
                        return answers[x]
                    x += 1

                self.write('Dat is geen geldige input, probeer het opnieuw!', color=TextColors.red)
            else:
                return userInput

    def clearScreen(self, prompt=True):
        if(prompt):
            self.write('Druk op Enter om door te gaan!')
            input()

        if os.name == 'nt': # Windows
            _ = os.system('cls')
        else: # Mac/Linux
            _ = os.system('clear')

class Player():
    def __init__(self, hp = 100, money = 10.0, inventory = []):
        self.inventory = inventory
        self.hp = hp
        self.money = money

    def setName(self, name):
        self.name = name
    
    def getName(self):
        return self.name

    def setHP(self, hp):
        self.hp = hp

    def addHP(self, hp):
        self.hp += hp

    def removeHP(self, hp):
        newHP = self.hp - hp
        if(newHP <= 0 ):
            raise HpZeroError()
        else:
            self.hp = newHP

    def getHP(self):
        return self.hp

    def setMoney(self, money):
        self.money = money

        return self.money

    def addMoney(self, money):
        self.money += money

        return self.money

    def removeMoney(self, money):
        self.money -= money

        return self.money

    def getMoney(self):
        return self.money

    def hasItem(self, item):
        if item in self.inventory:
            return True
        else:
            return False

    def addItem(self, item):
        self.inventory.append(item)
    
    def addItems(self, items):
        for item in items:
            self.inventory.append(item)

    def removeItem(self, item, count = 1):
        x = 0
        while(x < count):
            self.inventory.pop(item)
            x += 1

    def removeItems(self, items):
        for item in items:
            self.inventory.pop(item)
    
