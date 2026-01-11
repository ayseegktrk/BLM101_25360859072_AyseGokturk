# -------------------------------------------------
# Sanal Mantik Devresi Simulatoru
# Bu program temel mantik kapilarini simule eder
# ve A AND (B OR C) ifadesinin dogruluk tablosunu olusturur
# -------------------------------------------------

# AND mantik kapisi fonksiyonu
# Iki giris alir, her ikisi de 1 ise 1 dondurur

#def işlem tanımlar AND bu işlemin adıdır.
#(a,b) bu işlemin yapılması için dışarıdan iki tane girdiye ihtiyaç olduğunu söyler.
#return hesaplanan sonucu geri gönderir.
# Aşağıda def yapısı her kapı türü için kullanılmıştır.
def AND(a, b):
    return a & b
#Bit düzeyinde 've' & operatörünü kullanarak sonucu hesaplar ve döndürür.

# OR mantik kapisi fonksiyonu
# Girislerden en az biri 1 ise 1 dondurur
def OR(a, b):
    return a | b
#Bit düzeyinde 'veya' | operatörünü kullanarak sonucu hesaplar ve döndürür

# NOT mantik kapisi fonksiyonu
# 1 girilirse 0, 0 girilirse 1 dondurur
def NOT(a):
    return 0 if a == 1 else 1 #ternary (kisa if else) kullanimi
#ternary operatörünü kullanarak a=1 ise 0,değilse 1 döndürür.

# XOR mantik kapisi fonksiyonu
# Girisler farkliysa 1, ayniysa 0 dondurur
def XOR(a, b):
    return a ^ b
#Bit düzeyinde 'özel veya' ^ operatörünü kullanarak sonucu hesaplar ve döndürür

# -------------------------------
# 1. ASAMA: Kullanicidan veri alma
# -------------------------------

print("Sanal Mantik Devresi Simulatoru") #bu fonksiyon programın başlığını ekrana yazdırır.
print("Kullanilabilir Kapilar: AND, OR, NOT, XOR")#bu fonksiyon kullanıcın seçebileceği kapıları gösterir.

# Kullanicidan mantik kapisi turu alinir
gate = input("Mantik kapisini giriniz: ").upper() 
# upper mantik kapisi giriş türünü büyük harfe cevirir 'and'->'AND'
## gate kullanıcın seçtiği mantık kapısı türünü bir değişkene atar.

# Eger secilen kapi NOT ise tek giris alinir
if gate == "NOT":
    a = int(input("Giris degerini giriniz (0 veya 1): "))
    print("Sonuc:", NOT(a))

# NOT disindaki kapilar icin iki giris alinir
else:
    a = int(input("1. Giris degerini giriniz (0 veya 1): "))
    b = int(input("2. Giris degerini giriniz (0 veya 1): "))

    if gate == "AND": #kullanıcıdan alınan AND eşitse
        print("Sonuc:", AND(a, b))
    elif gate == "OR":
        print("Sonuc:", OR(a, b))
    elif gate == "XOR":
        print("Sonuc:", XOR(a, b))
    else:
        print("Gecersiz kapi turu!") #hatali kapi girisi

# ---------------------------------------------------
# 2. ASAMA: A AND (B OR C) ifadesinin dogruluk tablosu
# ---------------------------------------------------

print("\nA AND (B OR C) Dogruluk Tablosu")#bu fonksiyon tablo başlığını yansıtır.
print("A B C | Sonuc")#sutun başlıklarını yazdırır.
print("-" * 15) #ayırmak için çizgi çeker.
#A,B,C icin tum 0-1 kombinasyonlari denenir

#A,B ve C değişkenlerinin her birinin 0-1 olma durumlarını denemek için iç içe döngüler başlatılır.

for A in [0, 1]:#A değişkeni için once 0,sonra 1 değerini alır.

    for B in [0, 1]:#Her bir A değeri için B değişkeni 0 ve 1 değerlerini alır.

        for C in [0, 1]:#Her bir B değeri için C değişkeni 0 ve 1 değerlerini alır.

            sonuc = AND(A, OR(B, C))
             # Önce tanımlanan AND ve OR fonksiyonları kullanılarak A AND (B OR C) islemi yapılır.
              
            print(f"{A} {B} {C} |   {sonuc}") # sonuc tablo şeklinde ekrana yazdirilir
