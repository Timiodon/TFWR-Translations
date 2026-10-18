[<- Fonksiyonlar](docs/scripting/functions.md)
---
# Import
Tüm kodunu tek bir dosyaya koymak kısa sürede içinden çıkılmaz bir hâl alır. 
`import` ifadeleri, başka bir dosyadan fonksiyonları ve global değişkenleri içe aktarmanı sağlar.
Tek bir ekran görüntüsünde nasıl çalıştığı:
![|x400](ImportsInOnePicture)

Burada `import module2`, `module2` adlı dosyayı çalıştırır ve sana onun tüm global değişkenlerine erişim verir.
Ardından içe aktarılan modüldeki değişkenlere ve fonksiyonlara `.` operatörüyle erişebilirsin.
Yani bu örnekte `module2.print_x()`, `module2` içindeki `print_x()` fonksiyonunu çağırır.

### Daha Fazlasını Okumana Gerek Yok

`from` söz dizimini kullanarak, içe aktarılan modüldeki global değişkenleri import ifadesinin çalıştırıldığı mevcut kapsama da taşıyabilirsin.

`from module2 import print_x
print_x()`
`module2` içinden yalnızca belirtilen global değişkenleri içe aktarır.

ya da

`from module2 import *
print_x()`
`module2` içindeki tüm global değişkenleri içe aktarır.

Bu da `module2` dosyasını içe aktarır, ancak ona `module2` adlı bir değişken üzerinden erişmek yerine, `module2` içindeki global değişkenleri açıp doğrudan yerel kapsama atar.

Bu içe aktarma biçimi genellikle önerilmez; çünkü iki dosya birbirini içe aktardığında iyi çalışmaz ve ad çakışmaları yüzünden içe aktaran dosyadaki değişkenlerin üzerine yanlışlıkla yazabilirsin. Ne yaptığından emin değilsen `from` söz diziminden uzak durmak daha güvenlidir.

# Gerçekte nasıl çalışır

## Özetle
İçe aktarmalar oldukça kafa karıştırıcı olabilir, ancak sorunların çoğu `from file import` yerine `import file` söz dizimine bağlı kalarak ve global tanım olmayan her şeyi şunun içine alarak önlenebilir:
`if __name__ == "__main__":`

## İçe Aktarmanın Yan Etkileri
Bir dosyayı ilk kez içe aktardığında, oyun dosyanın tamamını çalıştırır ve ardından bu çalışma sırasında tanımlanan tüm değişkenlere erişim verir.
Aynı dosyayı tekrar içe aktarırsan, ilk içe aktarmada önbelleğe alınmış modül döndürülür.

Bu, import ifadelerinin yan etkileri olabileceği anlamına gelir. `harvest()` çağıran bir dosyayı içe aktarırsan, içe aktarma sırasında gerçekten hasat yapılır. Ama onu tekrar içe aktardığında yeniden hasat yapılmaz, çünkü dosya yalnızca bir kez çalıştırılır.

Bu tür yan etkilerden `__name__` değişkenini kullanarak kaçınmanın bir yolu var. Bu değişken, bir dosya doğrudan çalıştırıldığında otomatik olarak `"__main__"` değerini, `import` ile çalıştırıldığında ise dosyanın adını alır.
Dosya içe aktarıldığında çalışmasını istemediğin tüm kodu bir `if __name__ == "__main__":` bloğunun içine koymak iyi bir alışkanlık olarak kabul edilir.

Python'da yaygın bir dosya yapısı, dosya çalıştırıldığında yürütülmesi gereken kodu bir `main()` fonksiyonunun içine koymaktır. Böylece yerel değişkenler (`main()` içinde tanımlananlar) ile içe aktarılabilen global değişkenler (`main()` dışında tanımlananlar) arasında net bir ayrım olur.

`a_global_variable = "global"

def main():
    a_local_variable = "local"
    # do things

if __name__ == "__main__":
    main()`

## İçe Aktarma Döngüleri
`a` dosyası `b` dosyasını, `b` dosyası da `a` dosyasını içe aktarırsa ne olur?

`a` dosyası:
`import b
x = 0`

`b` dosyası:
`import a
def f():
    print(a.x)`

Bu sorunsuz çalışır. Diyelim ki iki dosya da henüz yüklenmemiş ve başka biri `import a` çalıştırıyor.

- `a`, `import b` satırına kadar çalışır.
- `b`, `import a` satırına kadar çalışır.
- `a` modülü zaten vardır, ancak yalnızca `import b` satırına ulaştığı için `x` içermez.
- `b`, yarı yüklenmiş `a` modülüne bir referansı `a` adlı bir değişkende saklar.
- `b`, `def` ifadesini çalıştırır ve `f()` fonksiyonunu saklar.
- `a` çalışmaya devam eder ve `x` değişkenine ilk değerini verir.

Biri `b.f()` çağırdığında doğru şekilde `0` yazdırılır, çünkü `b`'nin referansını tuttuğu `a` modülü artık tamamen yüklenmiştir.

Şimdi aynı kodu `from` söz dizimiyle düşün.

`a` dosyası:
`from b import *
x = 0`

`b` dosyası:
`from a import *
def f():
    print(x)`

- `a`, `from b import *` satırına kadar çalışır.
- `b`, `from a import *` satırına kadar çalışır.
- `a` modülü zaten vardır, ancak henüz tamamen çalıştırılmamıştır.
- `b`, o anda `a` içinde ne varsa kendi global kapsamına açar. Bu noktada `a` henüz `x = 0` satırına ulaşmadığı için hiçbir şey içermez, dolayısıyla hiçbir şey içe aktarılmaz.
- `b`, `def` ifadesini çalıştırır ve `f()` fonksiyonunu saklar.
- `a` çalışmaya devam eder ve `x` değişkenine ilk değerini verir.

Şimdi biri `b.f()` çağırırsa, mevcut kapsamda `x` bulunmadığını söyleyen bir hata alır. Bunun nedeni, bu kez `b`'nin hâlâ yüklenmekte olan `a` modülüne bir referans tutmaması ve içe aktarmadan sonra eklenen tanımları görmemesidir.

---

[Fonksiyonlar](docs/scripting/functions.md)      [Ad Kapsamları](docs/scripting/scopes.md)
