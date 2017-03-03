from time import sleep

class Konwersja_jednostek:

    def konwersja():
        opcja=0
        while opcja<1 or opcja>4:
            opcja=int(input('''Podaj, co przeliczyć: 1-cale na cm, 2-cm na cale,
3-kg na lbs, 4-lbs na kg: '''))
        if opcja==1:
            we='in'
            wy='cm'
            przelicznik=2.54
        elif opcja==2:
            we='cm'
            wy='in'
            przelicznik=0.393700787
        elif opcja==3:
            we='kg'
            wy='lbs'
            przelicznik=2.20462262
        else:
            we='lbs'
            wy='kg'
            przelicznik=0.45359237
        print('Podaj liczbę ',we,' którą chcesz przeliczyć na ',wy)
        dana=float(input())
        wynik=przelicznik*dana
        return print(dana,' ',we,' = ',wynik,' ',wy)

    
#main
Konwersja_jednostek.konwersja()
sleep(2)

