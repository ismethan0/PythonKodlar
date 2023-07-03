#Girilen ikilik sayıyı onluk sayıya dönüştürünüz?
def ikliktenonluk(sayi,):
    sayi=0
    a=1
    ikilik=input("ikilik sayıyı giriniz: ")
    for i in ikilik:
        sayi+=2**(len(ikilik)-a)*(int(i))
        a+=1
    return sayi
    

