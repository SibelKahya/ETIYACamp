print("operatorler")
sayi=15
print(sayi +10)
print(sayi -10)
print(sayi *10)
print(sayi /10)

sayi=sayi+10
print(sayi)
print(sayi +10)
print(sayi -10)
print(sayi *10)
print(sayi /10)

print(sayi%5)  #mod operatörü

ondaliksayi=10.5
print(ondaliksayi+10)
print(ondaliksayi-10)
print(ondaliksayi-20)


sayi=100
print(sayi**3)  #üs alma
print(sayi//15) #tam bolme islemi

baslik ="Merhaba "
isim="engin Demiroğ"
print(baslik+ " Etiya")
print(baslik+" kodlama.io")

print("*"*30)
print("String format")
## string format
print("{}".format(baslik))
print("{} {}".format(baslik,isim))
print("{title} sayın {name}".format(baslik,isim))
print(f"{baslik} sayın {isim}")


print(baslik*10)
#  print(baslik/10) # hata verir

print(baslik.lower()) # tüm yazıları küçük harfe döüştürür
print(baslik.upper()) # tüm yazıları büyük harfe döüştürüür

print(len(baslik)) # metindeki kararkter sayısını verir

print("İnput kullanımı***")
#Kulllanıcıdan veri alma 

vade=input()
print(f"vadenin tipi iilk başta :{type(vade)}")
vade=int(vade)
vade=vade+10
print(f"vadenin tip dönüşümden sonra : {type(vade)}")

print(f"Girdiğiniz vade : {vade}")



# pair.py dosya oluşturulalım, kullanıcıdan 2 adet input alalım 
# 1. input vize notu %40
# 2. input final notu %60
# geçme notunun 50'den büyük olma durumunu console'a yazdırıcaksın

