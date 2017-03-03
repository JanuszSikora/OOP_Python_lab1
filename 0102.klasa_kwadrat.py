
class Kwadrat:
    def __init__(self,bok):
        self.bok=bok

    def powierzchnia(self):
        self.pow_nia=self.bok**2
        return self.pow_nia
        
        
kw1=Kwadrat(3)
kw2=Kwadrat(4)
kw3=Kwadrat(5)

print(kw1.bok,kw1.powierzchnia())
print(kw2.bok,kw2.powierzchnia())
print(kw3.bok,kw3.powierzchnia())

