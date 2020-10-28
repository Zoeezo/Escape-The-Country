from time import sleep
from Exceptions import HpZeroError, moneyZeroError, itemNonExistantError
import os

class TextColors():
    '''Class that contains default colours.
    
    Attributes:
        WHITE (str): String that contains the ANSI escape sequence for white text.
        RED (str): String that contains the ANSI escape sequence for red text.
        BLUE (str): String that contains the ANSI escape sequence for blue text.
        GREEN (str): String that contains the ANSI escape sequence for green text.
        YELLOW (str): String that contains the ANSI escape sequence for yellow text.
        ENDLINE (str): String that contains the ANSI escape sequence that has to be at the end of the string.
        '''

    WHITE = '\033[37m'
    RED = '\033[31m'
    BLUE = '\033[34m'
    GREEN = '\033[32m'
    YELLOW = '\033[36m'

    ENDLINE = '\033[0m'

    @staticmethod
    def isValidColor(color):
        '''Static function to check if a color is a valid color the engine can use.
        
        Parameters:
            color (str): String that contains the ANSI escape sequence for color.
            
        Returns:
            bool: Boolean that returns True if color contains a valid color.'''

        if(color == TextColors.WHITE or color == TextColors.RED or color == TextColors.BLUE or color == TextColors.GREEN or color == TextColors.YELLOW):
            return True
        else:
            return False

class Console():
    '''Class that contains all the functions for the console.
    
    Arguments:
        defaultTextColor (str): the ANSI escape sequence that should be used as a default color.

    Attributes:
        defaultTextColor (str): This is where we store the ANSI escape sequence.
    '''

    def __init__(self, defaultTextColor = TextColors.WHITE):
        if(TextColors.isValidColor(defaultTextColor)):
            self.DefaultTextColor = defaultTextColor
        else:
            self.DefaultTextColor = TextColors.WHITE
        
        self.clearScreen(prompt=False)

    def write(self, text, color = None, emptyString = True):
        '''Function that writes text to the console with a type effect.
        
        Arguments:
            text (str): String that you wants to write to the console.
            color (str): ANSI escape sequence for the textcolor.
            emptyString (bool): Boolen to see if'''
        if(not TextColors.isValidColor(color)):
            color = self.DefaultTextColor

        string = ""
        length = len(text)
        index = 0

        for i in text:
            string += i

            # If it's the last char in the string
            if (length - 1 == index):
                print(color + string + TextColors.ENDLINE)

                if(emptyString):
                    print()
            else:
                print(color + string + TextColors.ENDLINE, end="\r", flush=True)
                index += 1
                sleep(0.1)

    def ask(self, question, answers = [], textColor = None):
        alphabet = ['A', 'B', 'C', 'D', 'E', 'F']
        openQuestion = False

        if(len(answers) == 0):
            openQuestion = True

        if(not TextColors.isValidColor(textColor) or textColor == None):
            textColor = self.DefaultTextColor

        self.write(question, color=textColor)

        if(not openQuestion):
            i = 0

            for answer in answers:
                if (i + 1 == len(answers)):
                    self.write(alphabet[i].upper() + ' - ' + str(answer), color=textColor, emptyString=True)
                else:    
                    self.write(alphabet[i].upper() + ' - ' + str(answer), color=textColor, emptyString=False)
                    i += 1

        while True:
            userInput = input(textColor + 'Input: ').lower()
            print(TextColors.ENDLINE)

            if(not openQuestion):
                x = 0
                while(x < len(answers)):    
                    if(userInput == alphabet[x].lower() or userInput == str(answers[x]).lower()):
                        return answers[x]
                    x += 1

                self.write('Dat is geen geldige input, probeer het opnieuw!', color=TextColors.RED)
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

    def addMoney(self, money):
        self.money += money

    def removeMoney(self, money):
        newMoney = self.money - money
        if(newMoney < 0):
            raise moneyZeroError()
        else:
            self.money -= money

    def getMoney(self):
        return self.money

    def hasItem(self, item):
        if item in self.inventory:
            return True
        else:
            return False

    def addItem(self, item, count = 1):
        x = 0
        while(x < count):
            self.inventory.append(item)
            x += 1
    
    def addItems(self, items):
        for item in items:
            self.inventory.append(item)

    def removeItem(self, item, count = 1):
        x = 0
        while(x < count):
            try:
                self.inventory.pop(item)
            except:
                raise itemNonExistantError()
            x += 1

    def removeItems(self, items):
        for item in items:
            try:
                self.inventory.pop(item)
            except:
                raise itemNonExistantError()