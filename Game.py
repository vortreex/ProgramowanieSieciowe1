Kolko = 'o'
Krzyzyk = 'x'
LiniaPozioma = '-- --- --'
LiniaPionowa = ' | '
VictoryX = 'xxx'
VictoryO = 'ooo'


class game(object):
    def __init__(self):
        self.wyborPolaFailCounter = 0
        self.wyborPolaCounter = 0
        self.victoryFlagX = False
        self.victoryFlagO = False
        self.victoryFlagTie = False
        self.Pola = []

        for i in range(1, 10):
            self.Pola.append(str(i))

    def wyswietlPlansze(self):
        print("\033[H\033[J")
        print(self.Pola[0] + LiniaPionowa + self.Pola[1] + LiniaPionowa + self.Pola[2])
        print(LiniaPozioma)
        print(self.Pola[3] + LiniaPionowa + self.Pola[4] + LiniaPionowa + self.Pola[5])
        print(LiniaPozioma)
        print(self.Pola[6] + LiniaPionowa + self.Pola[7] + LiniaPionowa + self.Pola[8])

    def wybierzPole(self, rola):
        self.ustawPole(rola)
        self.wyswietlPlansze()
        self.victoryConditionCheck()

    def ustawPole(self, rola):
        Pole = int(input('Wybierz pole: ')) - 1
        if Pole > 8 or Pole < 0:
            print('Wybierz pole od 1 do 9')
            self.wybierzPole(rola)
        elif self.Pola[Pole] == Krzyzyk or self.Pola[Pole] == Kolko:
            print('To pole zostalo wybrane')
            self.wybierzPole(rola)
        else:
            if rola == 'k':
                self.Pola[Pole] = Krzyzyk
            elif rola == 's':
                self.Pola[Pole] = Kolko
            self.wyborPolaCounter += 1

    def victoryConditionCheck(self):
        for i in range(0, 3):
            if (self.Pola[0 + 3 * i] + self.Pola[1 + 3 * i] + self.Pola[2 + 3 * i] == VictoryX or
            	self.Pola[0 + i] + self.Pola[3 + i] + self.Pola[6 + i] == VictoryX or
                self.Pola[0] + self.Pola[4] + self.Pola[8] == VictoryX or
                self.Pola[2] + self.Pola[4] + self.Pola[6] == VictoryX):
                self.victoryFlagX = True
            elif (self.Pola[0 + 3 * i] + self.Pola[1 + 3 * i] + self.Pola[2 + 3 * i] == VictoryO or
            	self.Pola[0 + i] + self.Pola[3 + i] + self.Pola[6 + i] == VictoryO or
            	self.Pola[0] + self.Pola[4] + self.Pola[8] == VictoryO or
            	self.Pola[2] + self.Pola[4] + self.Pola[6] == VictoryO):
                self.victoryFlagO = True

        if self.victoryFlagX:
            print('Krzyzyk wygral!')
        elif self.victoryFlagO:
            print('Kolko wygralo!')
        elif self.victoryFlagO == False and self.victoryFlagX == False and self.wyborPolaCounter == 9:
            print('Remis!')
            self.victoryFlagTie = True

    @staticmethod
    def start():
        return game()
