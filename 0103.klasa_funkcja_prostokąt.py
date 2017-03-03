
class Prostokat:
    total=0
    @staticmethod
    def licznik():
        return Prostokat.total

    def __init__(self,bok1,bok2):
        self.bok1=bok1
        self.bok2=bok2
        Prostokat.total+=1
           
    def powierzchnia(self):
        self.pow_nia=self.bok1*self.bok2
        return self.pow_nia


def pokaz(Pro_kat):
    print('Pole trójkąta o bokach',P_katy[i].bok1,',',P_katy[i].bok2,'wynosi',P_katy[i].powierzchnia())

#main
P_katy=[]
#dodanie kolejnego obiektu zostaje automatycznie uwzględnione przez funkcję
#'pokaz' i metodę 'licznik'
P_katy.append(Prostokat(2,3))
P_katy.append(Prostokat(4,10))
P_katy.append(Prostokat(5,3.5))
P_katy.append(Prostokat(5,3))
P_katy.append(Prostokat(4,2))


#    print('Pole trójkąta o bokach',P_katy[i].bok1,',',P_katy[i].bok2,'wynosi',P_katy[i].powierzchnia())

for i in range(P_katy[2].total):#dostęp do atrybutu klasy poprzez obiekt
    pokaz(P_katy[i])

print('Razem obiektów:',Prostokat.licznik())#dostęp do atr. klasy poprzez metodę statyczną



