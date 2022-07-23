#for
# ogrenciler1=["fatih","Aykut","deniz"]
# for ogrenci in ogrenciler:
#     print(f"ogrenci adı:{ogrenci}")

#     if (ogrenci.lower()=="fatih".lower()):
#         print("okey")

# ogrenciler2=["fatih","Aykut","deniz"]

# for sayi in range(50,100): 
#     if(sayi%2==0):
#         print(sayi)    # buraya tekrar dön bak 

#while = olduğu süreece demek 
# sayac=0       
# while sayac<50:
#     print(sayac)
#     sayac+=1  



#ornek
#kullanıcı x kadar not ortalaamsı girmek istiyor
# girdiğinot ortalamalarında 50 den büyük ve eşit olanalar geçti
#conosle'da 50 dersten 25 ini geçtiiniz 
#girdiği tüm notları görmek istiyor

girilecekNotSayisi=int(input("girilecek not sayisi"))
gecilenDersSayisi=0
for note in range(girilecekNotSayisi):
    girilenNot=float(input(f"{note+1}.notu giriniz :"))
    if (girilenNot>=50):
        gecilenDersSayisi+=1
print(f"{girilecekNotSayisi} dersten {gecilenDersSayisi} kadar dersi geçtiniz")   



#ödev
# program sonunda girdiği notları kaçıncı not olduğu bilgisiyle beraber yazdır.
# kişi direkt ortalama not girmek yerine vize ve final girecek, siz oradan 
# o dersin ortalamasını hesaplayıp geçip kalma durumuna göre işlem yapacaksınız
# vize %40 , final %60