# Ödev: Döngüler (for & while)
# Konu: For ve while döngüleri.
# Görev:
# •	1’den 100’e kadar olan sayıları ekrana yazdırın.
# •	1’den 100’e kadar sadece çift sayıları ekrana yazdıran bir program yazın.
# •	Kullanıcıdan bir sayı alıp, bu sayının faktöriyelini hesaplayan bir program yazın.
# Örnek: 5! = 5 * 4 * 3 * 2 * 1 = 120
# •	1’den 100’e kadar olan tüm asal sayıları bulan bir program yazın.

for i in  range(1,101):
      #print(i)

 for i in range(2,100,2):
      
    print(i)

gir=int(input("lütfen sayıyı giriniz"))
sonuc=1    
for i in range (1,gir+1 ):
      sonuc*=i
print(sonuc)
      