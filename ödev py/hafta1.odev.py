# Ödev: Değişkenler ve Veri Tipleri
# Konu: Değişkenler, veri tipleri (int, float, string, boolean), kullanıcıdan veri alma.
# Görev:
# •	Kullanıcıdan adını, yaşını ve doğum yılını alarak ekrana aşağıdaki gibi yazdıran bir Python programı yazın:
# Merhaba Ali! 25 yaşındasın ve 1998 yılında doğmuşsun.
# Kullanıcıdan iki sayı alarak bu sayıların toplamını, farkını, çarpımını ve bölümünü ekrana yazdırın.
ad=input("lütfen adınızı giriniz: ")
yas=input("lütfen yasınızı giriniz : ")
dogum=input("lütfen dogum yılılnızı giriniz: ")
print(f"Merhaba  {ad}! {yas} yaşındasın ve {dogum} yılında doğmuşsun .")

sayi1=int(input(" lütfen işlem için kullanılacak ilk sayıyı giriniz: "))

sayi2=int(input(" lütfen işlem için kullanılacak ikinici sayıyı giriniz: "))
top=sayi1+sayi2
fark=sayi1-sayi2
carp=sayi1*sayi2
bol=sayi1//sayi2
print(f"sayınızın toplamı:  {top}\n  sayınızın farkı:{fark}\n sayınızın çarpımmı:{carp}\n sayınızın bölümü {bol}")