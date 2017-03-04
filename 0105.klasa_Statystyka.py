class Statystyka:
    
    def __init__(self,lista,dlugosc):
        self.lista=lista
        self.dlugosc=dlugosc
                        
    def __str__(self):
        return str(self.lista)

    def suma(self):
        print('''metoda wymaga podania indeksów listy
'start ' i 'koniec'; indeksy nie mogą
być większe niż dlugość listy, mniejsze
od zera,a 'start' nie może być większy
niż "koniec"''')
        self.koniec=self.dlugosc
        self.start=0
        while 0>self.start or self.start>(self.dlugosc-1) or 0>self.koniec or self.koniec>(self.dlugosc-1) or self.start>self.koniec:
            self.start=int(input('Podaj indeks "start":'))
            self.koniec=int(input('Podaj indeks "koniec":'))
        self.sumaa=0
        for i in range(self.start,self.koniec+1):
            self.sumaa+=self.lista[i]
        return self.sumaa

    def srednia(self):
        print('''Do wyliczenia średniej trzeba wprowadzić indeksy
jeszcze raz, ponieważ ta metoda korzysta z metody "suma"''')
        self.sredniaa=self.suma()/(self.koniec-self.start+1)
        return self.sredniaa

    def sortuj(self):
        self.posortowana=sorted(self.lista) 
        return self.posortowana

    def mediana(self):
        self.sortuj()
        if self.dlugosc%2==0:
            self.medianaa=(self.posortowana[self.dlugosc//2-1]+self.posortowana[self.dlugosc//2])/2
        else:
            self.medianaa=(self.posortowana[self.dlugosc//2])
        return self.medianaa

    def minimum(self):
        self.sortuj()
        self.minimuma=self.posortowana[0]
        return self.minimuma

    def maximum(self):
        self.sortuj()
        self.maximuma=self.posortowana[self.dlugosc-1]
        return self.maximuma


    
#main
#wpisanie z ręki listy liczb do wykonania działań statystycznych
ciag=[3,2,5,1,12,10,8,2,4]
dlugosc=len(ciag)
lista1=Statystyka(ciag,dlugosc)

print('Dla listy',lista1.lista)
print('lub po posortowaniu',lista1.sortuj())

print('suma podanego wycinka listy wynosi',lista1.suma())#wywołanie metody sumującej z klasy
print('średnia arytmetyczna podanego wycinka listy wynosi',lista1.srednia())#wywołanie metody średniej arytmetycznej z klasy
print('mediana całej listy wynosi',lista1.mediana())#wywołanie metody mediany z klasy
print('najmniejsza wartość całej listy to',lista1.minimum())#wywołanie metody wartości minimalnej z klasy
print('największa wartość całej listy to',lista1.maximum())#wywołanie metody wartości maksymalnej z klasy




