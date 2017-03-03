
class Zliczanie:
    
    def __init__(self,liczba1,liczba2):
        print('''Utwórz obiekt poprzez podanie 2-ch liczb "liczba1"
i "liczba2";za pomocą metod "dodaj" i "odejmij" można wykonać
te działania, a za pomocą "wyświetl" zobaczyć ich wynik''')
        self.liczba1=liczba1
        self.liczba2=liczba2
        
    def dodaj(self):
        self.wynik=self.liczba1+self.liczba2
        return self.wynik

    def odejmij(self):
        self.wynik=self.liczba1-self.liczba2
        return self.wynik

    def wypisz(self):
        pisanie=print('Wynik działania to:',self.wynik)
        return pisanie

#main
zlicz=Zliczanie(5,2)
zlicz.dodaj()#wywołanie metody dodającej
zlicz.odejmij()#wywołanie metody odejmującej
zlicz.wypisz()#wypisuje wartość ostatniego wywołanego działania dla obiektu


