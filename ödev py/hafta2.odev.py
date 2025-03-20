# Ödev: Koşullu İfadeler (if-else)
# Konu: Karar yapıları (if-elif-else).
# Görev:
# •	Kullanıcının girdiği bir sayının tek mi çift mi olduğunu bulan bir Python programı yazın.
print("*"*30)
gir=int(input("lütfen hangi sayının tek veya çift oldugunu ögrenmek istiyorsanız giriniz  :"))
print("*"*30)
if  gir%2==0:
      print(f"sayınız çiftri iyi günler dileri. Sayınız: {gir}")
else:
      print(f"sayınız Tektir. Sayınz : {gir}")
print("*"*30)
# •	Kullanıcının notunu alarak aşağıdaki not sistemine göre harf notunu hesaplayın:
# 90-100 -> A
# 80-89  -> B
# 70-79  -> C
# 60-69  -> D
# 0-59   -> F

notu = int(input("lütfen ögrencinin notunu Giriniz: "))
print("*"*30)
if notu >=90:
    print("Harf notunuz -> A ")
elif notu>=80:
      print("Harf notunuz -> B ")
elif notu>=70:
       print("Harf notunuz -> C ")
elif notu>=60:
       print("Harf notunuz -> D ")
elif notu>=0:
 print("Harf notunuz -> F ")
else:
 print("Geçersiz giriş...")
 print("*"*30)
 # •	Kullanıcının yaşına göre hangi yaş grubunda olduğunu bulan bir program yazın:
# 0-12 yaş: Çocuk
# 13-19 yaş: Genç
# 20-59 yaş: Yetişkin
# 60 ve üzeri: Yaşlı
print("*"*30)
yas=int(input("Yasınızı girinzi "))
print("*"*30)
if   yas>=60:
     print("Yaşlı")
elif yas >=13 and yas<=19:
     print("Genç")
elif yas>=20 and yas<=59:
     print("Yetişkin")
elif yas>=0 and yas<=12:
     print("çocuk")
else:
     print("geçersiz giriş")