print(1==1) #eşittir : dönüş tipi boolean dir
print(1!=1) #eşit değildir : false değer döndürecek
print(1>1) #sağa yazılan değerin sola büyükür
print(1>=1)
print(1<=1)
print("1">"1")
print("12">"1") # true döner
# print("12">1) #hata fırlatır değersel bir işlem yapıyor
print("12">"11.4")

print("*"*30)

#and 
vade=24
maxVade=35
kredi=1000
print(vade>12 and kredi<100000)


print("*"*30)
#or  herhangi bir koşul sağlansa bile true döner 
print(vade>12 or kredi<100000)
print(vade<30 and maxVade==36 or kredi<10000)

print((vade>30 or maxVade==36) and kredi>10000)
