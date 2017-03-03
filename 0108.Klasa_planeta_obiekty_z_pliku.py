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
#Konkretyzacja obiektów - tylko komentarz po zamarynowaniu obiektów w 'Planet_plik.dat'
#lista_planet=[]
#lista_planet.append(Planety('Wulkan',.03,False))
#lista_planet.append(Planety('Merkury',.038,True))
#lista_planet.append(Planety('Wenus',.72,True))
#lista_planet.append(Planety('Ziemia',1,True))
#lista_planet.append(Planety('Mars',1.52,True))
#lista_planet.append(Planety('Faeton',1.7,False))
#lista_planet.append(Planety('Jowisz',5.2,True))
#lista_planet.append(Planety('Saturn',9.53,True))
#lista_planet.append(Planety('Uran',19.19,True))
#lista_planet.append(Planety('Neptun',30.06,True))
#lista_planet.append(Planety('Pluton',39.48,'False/True'))


#zapis obiektów do pliku - operacja jednorazowa, potem "za-#-owane"
#plik_planety=open('Planet_plik.dat','wb')
#for i in range(Planety.total()):
 #   pickle.dump(lista_planet[i],plik_planety)
#plik_planety.close()

#dlugosc_listy_planet=open('Planet_plik_dlug.dat','wb')
#pickle.dump(Planety.total(),dlugosc_listy_planet)
#dlugosc_listy_planet.close()

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

