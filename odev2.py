 # program sonunda girdiği notları kaçıncı not olduğu bilgisiyle beraber yazdır. 
# kişi direkt ortalama not girmek yerine vize ve final girecek, siz oradan 
# o dersin ortalamasını hesaplayıp geçip kalma durumuna göre işlem yapacaksınız # vize %40 , final %60

girilecekNotSayisi=int(input("Kaç adet ders gireceksiniz ?=>"))
gecilenDersSayisi=0
sayi=0
sayi2=0

girilenVizeNotlari=[]
girilenFinalNotlari=[]
ortalamaListesi=[]

for note in range(girilecekNotSayisi):
    girilenVizeNotlari.append(float(input(f"{note+1}. dersin vize notunu giriniz:")))
    girilenFinalNotlari.append(float(input(f"{note+1}. dersin Final notunu giriniz:")))
    sayi+=1

    sonuc=float(girilenVizeNotlari[sayi-1]*0.4+girilenFinalNotlari[sayi-1]*0.6)
    ortalamaListesi.append(sonuc) 
    

for average in ortalamaListesi:
    sayi2+=1
    
    if sonuc>=50:
        print(f"{sayi2}. dersi => {average}  notu ile GEÇTİNİZ !")
    else:
        print(f"{sayi2}. dersten ={average}  notu ile KALDINIZ !") 

  


