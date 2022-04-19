class Doviz:
    kur={'EURO':3.76,
         'USD':4.54,
         'CHF':3.87
         }
    def __init__(self,kur,miktar):
        self.kur=kur
        self.miktar=miktar
 
    def __add__(self, other):
        s=self.miktar*Doviz.kur[self.kur]
        o=other.miktar*Doviz.kur[other.kur]
        return  s+o
 
    def __str__(self):
        return ("%s %s"%(self.miktar,self.kur))
 
def main():
    print("Kur Hesaplama\n")
    dolar=Doviz("USD",2.5)
    euro=Doviz("EURO",3)
    toplam=dolar+euro
    print(dolar,"+" , euro,"=",toplam ,"TL ")
 
    print("\n\n**********************\n")
 
    chf = Doviz("CHF", 50)
    euro = Doviz("EURO", 35)
    toplam2 = chf + euro
    print(chf, "+", euro, "=", toplam2, "TL ")
 
main()