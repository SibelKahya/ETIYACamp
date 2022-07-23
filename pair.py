
# pair.py dosya oluşturulalım, kullanıcıdan 2 adet input alalım 
# 1. input vize notu %40
# 2. input final notu %60
# geçme notunun 50'den büyük olma durumunu console'a yazdırıcaksın
vize =input()
vize=int(vize)
final=input()
final=int(final)

sonuc= (vize*0.4) +(final*0.6)

print(sonuc>50)