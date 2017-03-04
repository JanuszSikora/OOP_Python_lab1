from time import sleep
import pickle,shelve

class Planety:

    dlugosc_listy=0
    @staticmethod
    def total():
        return Planety.dlugosc_listy

    def __init__(self,nazwa,odleglosc_Slonce,rzeczywista):
        self.nazwa=nazwa
        self.odleglosc_Slonce=odleglosc_Slonce
        self.rzeczywista=rzeczywista
        self.odleglosc_Slonce_kkm=self.odleglosc_Slonce*149597.8707
        Planety.dlugosc_listy+=1

    def __str__(self):
        return 'Planeta '+str(self.nazwa)+'\nznajdująca się w odległości '+str(round(self.odleglosc_Slonce_kkm,2))+' tys. km od Słońca\njest '+str(self.rzeczywista)

    def pokaz(self,wybor_rzeczyw):
        if self.rzeczywista==wybor_rzeczyw or wybor_rzeczyw==None or self.rzeczywista==None:
            if self.rzeczywista==None:
                self.rzeczywista='False/True'
            print('Planeta ',self.nazwa,'\nw odległości ',round(self.odleglosc_Slonce_kkm,1),' tys. km od Słońca\njest ',self.rzeczywista)
                
    
#main

#odczyt obiektów z pliku
dlugosc_listy_planet=open('Planet_plik_dlug.dat','rb')
dlugosc_listy_planet=pickle.load(dlugosc_listy_planet)

lista_planet=[]
plik_planety=open('Planet_plik.dat','rb')
for i in range(dlugosc_listy_planet):
    lista_planet.append(pickle.load(plik_planety))


#wyświetlenie obiektu
for i in range(len(lista_planet)):
    lista_planet[i].pokaz(None)#wybór parametru generuje podlisty
#wg wartości self.rzeczywista lub całość listy dla wartości 'None'

sleep(2)


