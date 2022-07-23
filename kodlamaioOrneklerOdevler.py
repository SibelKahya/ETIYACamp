#kodlama io calismalar
dolarDun=7.65
dolarBugun=7.75
if dolarDun>dolarBugun:
    print("Azalış oku")
elif dolarBugun>dolarDun:
    print("Artış oku")

print("Bitti")       

#if dolarDun<dolarBugun:
 #   print("Artış oku")
#if dolarDun==dolarBugun:
 #   print("Eşittir oku")   
print("*** Kodlama.io şart blokları ödev 1")
sayi1=80
sayi2=79

if sayi1>sayi2:
   print(f"büyük sayi : {sayi1}")
else:
    print(f"büyük sayi : {sayi2}")

print("*** Kodlama.io şart blokları ödev 2") 
s1=29
s2=69
s3=78

if  s1>s2 and s1>s3:
    print(f"Büyük sayi :{s1}")
elif s2>s1 and s2>s3:
    print(f"Büyük sayi :{s2}")
else:
    print(f"Büyük Sayi :{s3}")

print("*** Kodlama.io dizi yapıları ") 
krediler=["Hızlı Kredi","Maaşını Akbanktan lanalara Özel","Mutlu Emekli İhtyaç Kredisi"]
print(krediler)
print(krediler[0])
print(krediler[1])
print(krediler[2])
print(len(krediler))

krediler[0]="Çabuk Kredi"
print(krediler)

#print(krediler[5]) #sınırların dışında yazılan index için program hata verir
print("*** Kodlama.io dizi yapıları Bölüm Ödevi 1 ") 

ogrenciler=["Eymen","Sibel","Özge","Songül","Esra","Deniz","Hatice","Azra"]
print(ogrenciler)
ogrenciler[0]="Mustafa"
print(ogrenciler)
print(ogrenciler[5])
print(len(ogrenciler))

print("*** Kodlama.io Döngüler ")
krediler2=["Hızlı Kredi","Maaşını Akbanktan Alanlara Özel","Mutlu Emekli İhtyaç Kredisi"]

for kredi in krediler:
    print("<Options>"+kredi+"<Options>")

#for i in range(10): #0 dan 9 a kadar yazar 10 dahil değil 
 #   print(i)
for i in range (5,45): # 5 ten 44 e kadar yazar
    print(i)    

for a in range(5,46,6):# 5 ten itibaren 45 e kadar 6 şar gider
    print(a)    

for b in range(0,11,2): # 0 dan 10 a kadar olan çift sayıları yazar
    print(b)

print("*** Kodlama.io Fonksiyonlar ") 

def kredileriListele():
    krediler3=["Hızlı Kredi","Maaşını Akbanktan Alanlara Özel","Mutlu Emekli İhtyaç Kredisi"]
    for kredi in krediler3:
          print(kredi)
          
kredileriListele();          