# BLM101_25360859072_AyseGokturk
# BLM101-Dönem Projesi

## Öğrenci Bilgileri
. *Ad Soyad:*Ayşe GÖKTÜRK
. *Öğrenci No:*25360859072
. *Bölüm:*Bilgisayar Mühendisliği

## Proje Konusu
*Sanal Mantık Devresi Simülatörü*

## Proje Açıklaması 
Bu proje,temel dijital mantık kapılarını (AND,OR,NOT,XOR) simüle eden ve kullanıcıdan alınan girişlere 
göre hem anlık sonuç üreten hem de karmaşık ifadeler için doğruluk tablosu oluşturan bir Python uygulamasıdır.

## Kullanılan Konular
.Bilgisayar Mimarisi Temelleri:CPU ve ALU çalışma prensipleri
.Dijital Mantık Kapıları
.Doğruluk Tabloları 
.Veri Manipülasonu

## Programın Çalışma Mantığı 
Bu yazılım,dijital elektroniğin temelini oluşturan mantık kapılarını yazımsal olarak modellemektedir.
1.Fonksiyonel Yapı:Her mantık kapısı(AND,OR,NOT,XOR) bit düzeyinde işlem yapan özel Python fonksiyonları (def) ile tanımlanmıştır.
2.Kullanıcı Etkileşimi:Program,kullanıcıdan bir kapı türü seçmesini ister.Girilen metin .upper() metodu ile büyük harfe çevrilerek
hata payı azaltılır.
3.Hata Yönetimi:Eğer kullanıcı tanımlı olmayan bir kapı ismi girerse,else bloğu çalışarak "Gecersiz Kapi turu!" uyarısı verir.
4.Doğruluk Tablosu:Projenin ikinci aşamasında A AND (B OR C) ifadesi için iç içe 3 adet for döngüsü kullanılarak 8 farklı 
olasılığın tamamı hesaplanır ve ekrana tablo formatında basılır.

## Çalıştırma Talimatları
.Gereksinimler:Programın çalışması için bilgisayarınızda Python 3.x kurulu olmalıdır.
.Kütüphaneler:Herhangi bir dış kütüphane kurulumu gerekmemektedir.
(Sadece Python'ın yerleşik özellikleri kullanılmıştır.)
.Çalıştırma:Terminale python mantik_devreleri.py yazarak veya VS Code üzerinden "Run" butonuna basarak simülasyonu başlatabilirsiniz.

## Kod Açıklaması(Markdown)

Kodun Amacı:
Bu yazılım,bilgisayar mimarisinin temelini oluşturan Aritmetik Mantık Birimi(ALU) prensiplerini Python dili ile simüle eder.
Kullanıcıdan alınan verileri dijital mantık kapıları üzerinden işleyerek sonuç üretir.

Kullanılan Kütüphaneler ve Araçlar
.Standart Python Kütüphanesi:
Proje harici bir paket yüklemesi gerektirmeden standart Python 3.x ortamında çalışmaktadır.
.Yerleşik Fonksiyonlar:
İnput(),Print(),.upper()
.Bit düzeyinde İşleçler(Bitwise Operators)
Mantık kapılarının matematiksel modellemesi için Python'in yerleşik & , | ,^ işleçleri kullanılmıştır.
.F-String Biçimlendirme

Algoritmanın Genel Mantığı
Bu program, kullanıcıdan alınan seçimlere göre mantıksal veri manipülasyonu yapan ve otomatik bir doğruluk tablosu (truth table) üreten bir akışa sahiptir. 
Algoritmanın işleyişi şu temel adımlardan oluşur:
​Kullanıcıdan input() fonksiyonu ile hangi mantık kapısını simüle etmek istediği bilgisi alınır.
​Girilen metin .upper() metodu kullanılarak büyük harfe çevrilir; böylece algoritma "and", "And" veya "AND" girişlerinin tamamını aynı şekilde işleyerek kullanıcı hatalarını minimize eder.
​Seçilen kapının türüne göre (Örn: NOT ise tek giriş, AND ise çift giriş) program farklı if-elif-else bloklarına yönlendirilir.
​Geçersiz bir kapı ismi girildiğinde algoritma "Gecersiz kapi turu!" uyarısı vererek güvenli bir çıkış sağlar.
​Fonksiyonel Hesaplama (Bitwise Operations): * Mantıksal hesaplamalar, kodun başında tanımlanan modüler fonksiyonlar (def) aracılığıyla yapılır.
​Algoritma, Python’un yerleşik bit düzeyindeki işleçlerini (&, |, ^) kullanarak donanım seviyesinde doğrulukla sonuç üretir.
​A AND (B OR C) gibi karmaşık bir ifadeyi analiz etmek için iç içe geçmiş (nested) 3 adet for döngüsü kullanılır.
​Bu döngüler, 3 farklı değişkenin alabileceği tüm olasılıkları (000'dan 111'e kadar toplam 8 durum) otomatik olarak üretir.
​Her bir kombinasyonun sonucu, önceden tanımlanan fonksiyonlar (AND, OR) hiyerarşik bir sırada çağrılarak hesaplanır.
​Sonuçlar, f-string formatlama yapısı kullanılarak düzenli bir tablo görünümünde terminale yazdırılır.

## YouTube Video Linki
[
]



