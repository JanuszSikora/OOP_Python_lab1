from time import sleep

class Figura_Geometryczna:

    def __init__(self,nazwa,wspolrz_x,wspolrz_y):
        self.nazwa=nazwa
        self.wspolrz_x=wspolrz_x
        self.wspolrz_y=wspolrz_y    

    def __str__(self):
        return str(self.nazwa)+' o współrzędnych x,y: '+str(self.wspolrz_x)+','+str(self.wspolrz_y)

                
    
#main
#Konkretyzacja obiektu
figura=Figura_Geometryczna(str(input('Podaj nazwę figury geom.: ')),float(input('Podaj współrzędną "x" położenia figury geom.: ')),float(input('Podaj współrzędną "y" położenia figury geom.: ')))

#wyświetlenie obiektu
print(figura)

sleep(2)

