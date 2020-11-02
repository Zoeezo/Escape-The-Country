from GameEngine import Console, Player, TextColors
from random import randint, choice

console = None
player = None
difficulty = 'Makkelijk'

def init():
    global console, player

    console = Console()
    player = Player()
    titleScreen()

def deToekomst():
    console.write('Na een aantal jaar in Nederland te hebben gewoont ben je gewend aan hoe alles hier is.', emptyString=False)
    console.write('Je zit een in Cafe na te denken over de afgelopen jaren...')

    console.clearScreen(prompt=True)
    while True:
        userInput = console.ask(question='Waar zal ik aan terugdenken?', answers=['Avontuur', 'Geld', 'Klaar'], color=TextColors.GREEN)


        if(userInput == 'Avontuur'):
            console.write('Het was een avontuur om hier te komen zeg, ik moest zo veel lopen... Ik ben blij dat ik het heb gehaald. Ik vraag me af of ik het ook had gedaan als mijn oude huis nog heel was...')
        elif(userInput == 'Geld'):
            console.write('Het was een lastige reis met weinig geld, ik had na de reis maar ' + str(player.getMoney()) + ' euro over... Hier in Nederland was het soms ook moeilijk om de huur te betalen...')
        elif(userInput == 'exit'):
            console.clearScreen(prompt=False)
            titleScreen()
        else:
            console.write('Bedankt voor het spelen van Escape The Country! <3')
            console.clearScreen(prompt=True)
            titleScreen()

def inNederland2():
    console.write('Je wordt ineens lastiggevallen op straat...')

    console.write('\'Hey kut vluchteling!\'', color=TextColors.BLUE)
    console.write('\'Ga terug naar je eigen land!\'', color=TextColors.BLUE)

    userInput = console.ask(question='Wat moet ik hier nou weer aan doen?', answers=['Vechten', 'Negeren'], color=TextColors.GREEN)

    if(userInput == 'Vechten'):
        console.write('Je besluit met hem te gaan vechten...')

        console.write('\'Hoe toch op!\'', color=TextColors.GREEN)

        if(randint(0, 1) == 1):
            console.write('Je begint met vechten en je slaat hem hard op zijn kaak, hij valt bewusteloos neer...')
            console.write('\'Dat krijg je ervan!\'', color=TextColors.GREEN)
        else:
            console.write('Je begint met vechten en hij slaat je hard in je maag, je valt neer van de pijn..')
            console.write('\'Dat krijg je ervan, kut buitenlander!\'', color=TextColors.BLUE)
    elif(userInput == 'exit'):
        console.clearScreen(prompt=False)
        titleScreen()
    else:
        console.write('Je besluit hem te negeren...')
        console.write('\'Haha je durft niet eens te vechten, pussy!\'', color=TextColors.BLUE)

    return

def inNederland1():
    console.write('Je hebt geld nodig voor de huur...')

    userInput = console.ask(question='Hoe ga ik geld verdienen...', answers=['Baan zoeken', 'Criminaliteit'], color=TextColors.GREEN)

    if(userInput == 'Baantje'):
        console.write('Je vind een tijdelijk baantje en je verdient genoeg geld om de huur te betalen.')
        return
    elif(userInput == 'exit'):
        console.clearScreen(prompt=False)
        titleScreen()
    else:
        console.write('Je besluit de criminaliteit in te gaan..')

        if(randint(0, 10) == 5):
            console.write('\'Stop, politie!\'', color=TextColors.BLUE)
            console.write('je plan mislukt en je wordt aangehouden door de politie...', color=TextColors.RED)

            console.clearScreen(prompt=True)
            titleScreen()
        else:
            console.write('Je plan lukt en je verdient genoeg geld om de huur te betalen.')
        return

def inNederland():
    global difficulty

    days = None

    if(difficulty == 'Makkelijk'):
        days = 3
    elif(difficulty == 'Middelmatig'):
        days = 5
    else:
        days = 7

    console.write('Je bent eindelijk in Nederland aangekomen!')

    while(days > 0):
        console.write('Je moet nog ' + str(days) + ' dagen doorkomen...')

        events = [inNederland1, inNederland2]

        choice(events)()

        days -= 1

        console.clearScreen(prompt=True)

    deToekomst()

def reisEvent5():
    console.write('Je gaat door je enkel heen tijdens het lopen...')

    answers = ['Doorlopen', 'Rustig aan doen', 'Verband gebuiken']

    if(not player.hasItem('Verband')):
        answers.remove('Verband gebruiken')

    userInput = console.ask(question='Kut me enkel doet zoveel pijn... Wat moet ik doen?', answers=answers, color=TextColors.GREEN)

    if(userInput == 'Doorlopen'):
        console.write('Je besluit door te lopen...')

        if(randint(0, 1) == 1):
            console.write('Na een tijdje lopen doet je enkel doet teveel zeer, je kan de reis niet meer afmaken...', color=TextColors.RED)
            console.clearScreen(prompt=True)
            titleScreen()
        else:
            console.write('Je enkel doet na een tijdje teveel zeer en je moet uitrusten...')
            return 2
    elif(userInput == 'exit'):
        console.clearScreen(prompt=False)
        titleScreen()
    elif(userInput == 'Rustig aan doen'):
        console.write('Je besluit rustig aan te doen, je loopt maar 5 kilometer die dag...')
        return 5
    else:
        console.write('Je doet verband om je enkel heen en je kan weer veilig doorlopen...')
        player.removeItem('Verband')
        return 15

def reisEvent4():
    console.write('Je loopt door een rustig gebied heen,', emptyString=False)
    console.write('ineens duikt er iemand op uit de schaduw en wordt je overvallen...')
    console.write('\'Geef me al je geld nu!\'', color=TextColors.BLUE)
    console.write('\'W-w-wat?\'', color=TextColors.GREEN)
    console.write('\'JE HOORT ME TOCH?! GEEF ME AL JE GELD NU!!!\'', color=TextColors.BLUE)

    userInput = console.ask(question='Zal ik meewerken?', answers=['Ja', 'Nee'], color=TextColors.GREEN)

    if(userInput == 'Ja'):
        console.write('Je besluit mee te werken, je verliest al je geld...')
        player.setMoney(0)

        return 10
    elif(userInput == 'exit'):
        console.clearScreen(prompt=False)
        titleScreen()
    else:
        console.write('Je besluit niet mee te werken...')

        if(randint(0, 1) == 1):
            console.write('\'Nee je krijgt me geld niet! Je durft me toch niet neer te schieten!\'', color=TextColors.GREEN)
            console.write('\'Ik pak je nog eens een keer, pas maar op!!!\'', color=TextColors.BLUE)

            console.write('De overvaller rent weg...')
            return 10
        else:
            console.write('\'Nee je krijgt me geld niet! Je durft me toch niet neer te schieten!\'', color=TextColors.GREEN)
            console.write('\'Hou je bek!!!\'', color=TextColors.BLUE)

            console.write('Na het boos maken van de overvaller schiet hij je dood...', color=TextColors.RED)
            console.clearScreen(prompt=True)
            titleScreen()

def reisEvent3():
    console.write('Je loopt door een bos heen en het wordt donker...')

    answers = ['Ja', 'Nee']
    if(not player.hasItem('Zaklantaarn')):
        answers.remove('Ja')

    userInput = console.ask(question='Zal ik doorlopen?', answers=answers, color=TextColors.GREEN)

    if(userInput == 'Ja'):
        console.write('Je besluit door te lopen door de nacht heen...', emptyString=False)
        console.write('Je loopt een extra 10 kilometer, maar je zaklantaarn gaat stuk en je gooit hem weg...')

        player.removeItem('Zaklantaarn')
        return 10
    elif(userInput == 'exit'):
        console.clearScreen(prompt=False)
        titleScreen()
    else:
        console.write('Je besluit niet door te lopen, en je wacht tot het weer licht wordt...')
        return 0

def reisEvent2():
    console.write('Je komt bij een drukke weg aan...')

    userInput = console.ask(question='Zal ik anders gaan hitchhiken?', answers=['Ja', 'Nee'], color=TextColors.GREEN)

    if(userInput == 'Ja'):
        console.write('Je besluit om te gaan hitchhiken...')

        if(randint(0, 1) == 1):
            console.write('Na een tijdje stopt er een auto voor je en stap je in...')

            userInput = console.ask(question='\'Hallo! Ik ben Wout... Welke kant moet je op?\'', answers=['Noord', 'Oost', 'Zuid', 'West'], color=TextColors.BLUE)
            console.write('\'Ik moet naar het ' + userInput + 'en toe!\'', color=TextColors.GREEN)

            distance = randint(20, 50)
            console.write('\'Ik kan je ' + str(distance) + ' kilometer die kant op brengen!', color=TextColors.BLUE)

            console.write('Je rijdt mee met de aardige persoon voor ' + str(distance) + ' kilometer...')
            return distance
        else:
            console.write('Na uren je duim omhoog houden ben je het zat en geef je op...', emptyString=False)
    elif(userInput == 'exit'):
        console.clearScreen(prompt=False)
        titleScreen()

    console.write('Je loopt door en komt 10 kilometer verder...')
    return 10

def reisEvent1():
    console.write('Je komt een winkeltje tegen, je kijkt naar je geld en je ziet dat je nog ' + str(player.getMoney()) + ' euro bij je hebt...')

    userInput = console.ask(question='Zal ik naar binnen gaan?', answers=['Ja', 'Nee'], color=TextColors.GREEN)

    if(userInput == 'Ja'):
        console.write('Je gaat naar binnen en je gaat naar de winkelier toe...')

        while True:
            userInput = console.ask(question='\'Hallo! Waar kan ik u mee helpen?\'', answers=['Kopen', 'Laat maar'], color=TextColors.BLUE)

            if(userInput == 'Kopen'):
                console.write('\'Ik zou graag wat willen kopen.\'', color=TextColors.GREEN)
                console.write('\'Ik heb in de aanbieding: Verband voor 20 euro en een zaklantaarn voor 50 euro.\'', color=TextColors.BLUE)

                userInput = console.ask(question='Wat zal ik kopen?', answers = ['Verband', 'Zaklantaarn', 'Niks'])

                if(userInput == 'Verband'):
                    try:
                        player.removeMoney(20)
                        player.addItem('Verband')
                    except:
                        console.write('Daar heb ik niet genoeg geld voor...', color=TextColors.GREEN)

                elif(userInput == 'exit'):
                    console.clearScreen(prompt=False)
                    titleScreen()

                elif(userInput == 'Zaklantaarn'):
                    try:
                        player.removeMoney(50)
                        player.addItem('Zaklantaarn')
                    except:
                        console.write('Daar heb ik niet genoeg geld voor...', color=TextColors.GREEN)
                else:
                    break

            else:
                console.write('\'Laat maar...\'', color=TextColors.GREEN)
                console.write('\'Oke, fijne dag!.\'', color=TextColors.BLUE)


        console.write('Je loopt na het winkelen nog 5 kilometer...')
        return 5

    elif(userInput == 'exit'):
        console.clearScreen(prompt=False)
        titleScreen()

    else:
        console.write('Je besluit niet naar binnen te gaan en loopt 10 kilometer...')
        return 10

def deReis():
    global difficulty

    distance = None

    if(difficulty == 'Makkelijk'):
        distance = 100
    elif(difficulty == 'Middelmatig'):
        distance = 200
    else:
        distance = 300

    while(distance > 0):
        console.write('Je moet nog ' + str(distance) + ' kilometers lopen...')

        events = [reisEvent1, reisEvent2, reisEvent3, reisEvent4, reisEvent5]

        returnedValue = choice(events)()

        distance -= returnedValue

        console.clearScreen(prompt=True)

    inNederland()

def startStory():
    console.write('\'Hey! Je bent eindelijk wakker! Er zijn bommen ontploft hier,', color=TextColors.BLUE, emptyString=False)
    console.write('het is een wonder dat je nog leeft!\'', color=TextColors.BLUE)
    userInput = console.ask(question='\'Gaat het goed met je?\'', answers=['Ja', 'Nee'], color=TextColors.BLUE)

    if(userInput == 'exit'):
        console.clearScreen(prompt=False)
        titleScreen()


    console.write('Wow wat is er met mijn huis gebeurd?.. Het is helemaal ingestort... Wat moet ik nu?', color=TextColors.GREEN, emptyString=False)
    userInput = console.ask(question='Zal ik zoeken naar spullen?', answers=['Ja', 'Nee'], color=TextColors.GREEN)

    if(userInput == 'Ja'):
        console.write('Je besluit te gaan zoeken in de ruine van je huis...')
        player.addMoney(randint(10, 100))

        items = ['Verband', 'Zaklantaarn']

        player.addItem(choice(items))
    elif(userInput == 'exit'):
        console.clearScreen(prompt=False)
        titleScreen()
    else:
        console.write('Je besluit niet te zoeken in de ruine van je huis...')

    console.clearScreen(prompt=True)
    deReis()

def settings():
    global difficulty
    console.write('//Settings//')
    userInput = console.ask(question='Moeilijkheidsgraad:', answers=['Makkelijk', 'Middelmatig', 'Moeilijk'], addExit=False)

    difficulty = userInput

    console.clearScreen()
    menuScreen()

def menuScreen():
    userInput = console.ask(question='//Menu//', answers=['Instellingen', 'Begin', 'Exit'], addExit=False)
    console.clearScreen(prompt=False)

    if(userInput == 'Instellingen'):
        settings()
    elif(userInput == 'Exit'):
        exit(1)
    else:
        console.clearScreen(prompt=False)
        startStory()

def titleScreen():

    console.printText(' _______   ________  ________  ________  ________  _______', emptyString=False)
    console.printText('|\  ___ \ |\   ____\|\   ____\|\   __  \|\   __  \|\  ___ \\', emptyString=False)
    console.printText('\ \   __/|\ \  \___|\ \  \___|\ \  \|\  \ \  \|\  \ \   __/|', emptyString=False)
    console.printText(' \ \  \_|/_\ \_____  \ \  \    \ \   __  \ \   ____\ \  \_|/__', emptyString=False)
    console.printText('  \ \  \_|\ \|____|\  \ \  \____\ \  \ \  \ \  \___|\ \  \_|\ \\', emptyString=False)
    console.printText('   \ \_______\____\_\  \ \_______\ \__\ \__\ \__\    \ \_______\\', emptyString=False)
    console.printText('    \|_______|\_________\|_______|\|__|\|__|\|__|     \|_______|', emptyString=False)
    console.printText('             \|_________|')

    console.clearScreen(prompt=True, promptText='  Druk op enter om te beginnen!')
    menuScreen()

if __name__ == "__main__":
    init()
