
ortalamaNot=65

if ortalamaNot<50:
    print("Kaldınız")
    print("tebrikler ..")
elif ortalamaNot>=50 and ortalamaNot<=70:
    print("Normal geçtiniz")

else:
    print("başarıyla geçtiniz")

print("her halükarda çalıştırmak istediğim kod ")    


#kullanıcıdan sayı gir tek mi çift mi 
sayi=input("Sayi giriniz:")
sayi=int(sayi)
if sayi%2==0:
    print("sayi çifttir")
elif sayi%2==1:
    print("sayi tektir")    