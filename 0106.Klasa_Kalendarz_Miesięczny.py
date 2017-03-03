from time import sleep

class Kalendarz_Miesieczny:

    def __init__(self,rok,miesiac):
        self.rok=rok
        self.miesiac=miesiac

    def __str__(self):
        return str(self.rok)+' '+str(self.miesiac)

    #sprawdza, czy podany rok jest przestępny i zwraca True (jeżeli jest) lub False
    def CzyPrzestępny(self):
        if self.rok%4==0 and self.rok%100!=0 or self.rok%400==0:
            return True    
        else:
            return False

    #na podst. zadanej daty wylicza, jaki to dzień tygodnia - zwraca od 0(poniedziałek)
    #do 7 (niedziela)
    def Dzień_tygodnia(self):
        YY=(self.rok-1)%100
        C=(self.rok-1)-YY
        G=YY+YY//4
        dz_tyg_dla_1_stycz=(((((C//100)%4)*5)+G)%7)
        self.Dz_Tyg=self.DzieńWRoku()%7+dz_tyg_dla_1_stycz
        if self.Dz_Tyg>6:
            self.Dz_Tyg=self.Dz_Tyg-7
        if self.Dz_Tyg==0:
            self.Dz_Tyg=7
        return self.Dz_Tyg

    #sprawdza na podst. atrybutów obiektu,
    #którym dniem roku jest 1-szy dzień
    #miesiąca zadanego roku
    def DzieńWRoku(self):
        dzień_roku=30*(self.miesiac-1)
        for i in range(self.miesiac):
            if i==1 or i==3 or i==5 or i==7 or i==8 or i==10:
                dzień_roku+=1
            if i==2:
                dzień_roku-=2
        if self.CzyPrzestępny()==True and self.miesiac>2:
            dzień_roku+=1
        self.dzień_roku=dzień_roku+1
        return self.dzień_roku

    #Sprawdza, czy podany nr miesiąca jest prawidłowy
    #zwraca None, jeżeli błędna;
    #zwraca liczbę dni w miesiącu z uwzględnieniem
    #lat przestępnych
    def Ile_dni_w_mscu(self):
        if self.miesiac>0 and self.miesiac<13:
            if self.miesiac==1 or self.miesiac==3 or self.miesiac==5 or self.miesiac==7 or self.miesiac==8 or self.miesiac==10 or self.miesiac==12:
                return 31
            elif self.miesiac==4 or self.miesiac==6 or self.miesiac==9 or self.miesiac==11:
                return 30
            elif self.CzyPrzestępny()==True and self.miesiac==2:
                return 29
            elif self.CzyPrzestępny()==False and self.miesiac==2:
                return 28
            else:
                return None
        else:
            return None

    #wyświetla kalendarz
    def pokaz(self):
        if self.Ile_dni_w_mscu()==None:
            print('błędny numer miesiąca')
        else:    
            print('Pn\tWt\tŚr\tCzw\tPt\tSo\tNd')
            for i in range(self.Dzień_tygodnia()-1):
                print('\t',end='')
            j=self.Dzień_tygodnia()
            for i in range(1,self.Ile_dni_w_mscu()+1):
                print(i,'\t',end='')
                if j%7==0:
                    print('\n')    
                j+=1
            
    
#main
#Konkretyzacja obiektu
Kal_mies=Kalendarz_Miesieczny(2017,2)

print(Kal_mies)
Kal_mies.pokaz()

sleep(2)

