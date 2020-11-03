from Exceptions import moneyZeroError, itemNonExistantError
from ctypes import wintypes
from time import sleep
import subprocess
import keyboard
import ctypes
import msvcrt
import sys
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

        kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)
        user32 = ctypes.WinDLL('user32', use_last_error=True)

        SW_MAXIMIZE = 3

        kernel32.GetConsoleWindow.restype = wintypes.HWND
        kernel32.GetLargestConsoleWindowSize.restype = wintypes._COORD
        kernel32.GetLargestConsoleWindowSize.argtypes = (wintypes.HANDLE,)
        user32.ShowWindow.argtypes = (wintypes.HWND, ctypes.c_int)

        fd = os.open('CONOUT$', os.O_RDWR)

        try:
            hCon = msvcrt.get_osfhandle(fd)
            max_size = kernel32.GetLargestConsoleWindowSize(hCon)
            if max_size.X == 0 and max_size.Y == 0:
                raise ctypes.WinError(ctypes.get_last_error())

        finally:
            os.close(fd)

        cols = max_size.X
        hWnd = kernel32.GetConsoleWindow()

        if cols and hWnd:
            lines = max_size.Y
            subprocess.check_call('mode.com con cols={} lines={}'.format(
                                    cols, lines))
            user32.ShowWindow(hWnd, SW_MAXIMIZE)

        self.width = cols
        self.height = lines

    def write(self, text, color = None, emptyString = True):
        '''Function that writes text to the console with a type effect.

        Arguments:
            text (str): String that you wants to write to the console.
            color (str): ANSI escape sequence for the textcolor.
            emptyString (bool): Boolen to see if'''
        if(not TextColors.isValidColor(color)):
            color = self.DefaultTextColor

        margin = int((int(len(text.center(self.width))) - int(len(text))) / 2)

        string = ' ' * int(margin)
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
                sleep(0.05)

    def printText(self, text, color=None, emptyString = True):
        if(not TextColors.isValidColor(color)):
            color = self.DefaultTextColor

        margin = int((int(len(text.center(self.width))) - int(len(text))) / 2)

        string = (' ' * int(margin) + color + text + TextColors.ENDLINE)

        print(string)

        if(emptyString):
            print()

    def ask(self, question, answers, color= None, addExit=True):

        if(not TextColors.isValidColor(color) or color == None):
            color = self.DefaultTextColor

        self.write(question, color=color)

        if(addExit):
            answers.append('exit')

        selected = 0

        def showOptions(answers, selected, clear=False):
            if (clear):
                for i in range(len(answers)):
                    sys.stdout.write("\033[F")

            for i in range(len(answers)):

                margin = int((int(len(answers[i].center(self.width))) - int(len(answers[i]))) / 2)

                print(color + '{3} {1}{0}{2}'.format(answers[i], ">" if selected == i else " ", "<" if selected == i else " ", ' ' * margin) + TextColors.ENDLINE)

        def up(selected, answers):
            if (selected == 0):
                selected = len(answers) - 1
            else:
                selected -= 1

            return selected

        def down(selected, answers):
            if (selected == len(answers) - 1):
                selected = 0
            else:
                selected += 1

            return selected

        showOptions(answers, selected)

        while True:
            if(keyboard.is_pressed('down')):
                selected = down(selected, answers)
                showOptions(answers, selected, clear=True)
            elif(keyboard.is_pressed('up')):
                selected = up(selected, answers)
                showOptions(answers, selected, clear=True)
            elif(keyboard.is_pressed('enter')):
                break

            sleep(0.15)

        print()
        return answers[selected]

    def clearScreen(self, prompt=True, promptText='Druk op Enter om door te gaan!'):
        if(prompt):
            self.write(promptText)
            while True:
                if(keyboard.is_pressed('enter')):
                    break

        if os.name == 'nt': # Windows
            _ = os.system('cls')
        else: # Mac/Linux
            _ = os.system('clear')

    def getScreenWidth(self):
        return self.width

    def getScreenHeight(self):
        return self.height


class Player():
    def __init__(self, hp = 100, money = 10.0, inventory = []):
        self.inventory = inventory
        self.hp = hp
        self.money = money

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

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
                self.inventory.remove(item)
            except:
                raise itemNonExistantError()
            x += 1

    def removeItems(self, items):
        for item in items:
            try:
                self.inventory.remove(item)
            except:
                raise itemNonExistantError()
