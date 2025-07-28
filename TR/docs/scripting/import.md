# Import
Tüm kodunu tek bir dosyaya koymak hızla yönetilemez hale gelir. 
`import` ifadeleri, başka bir dosyadan fonksiyonları ve global değişkenleri içe aktarmana olanak tanır.

`import filename`

Bu, en basit import ifadesi şeklidir. Sana `filename` adlı dosyada tanımlanan her şeye erişim sağlar. Oyundaki her pencere bir dosyadır ve dosya adı pencerenin üstünde görüntülenen isimdir.

İşte iki dosyalık bir örnek:
helper adlı dosya:
`x = 0

def say_hello():
    print("helper'dan selam")`

Başka bir dosya:
`import helper
helper.say_hello()
helper.x += 1`

Burada `import helper`, `helper` adlı dosyayı çalıştırır ve tüm global'larına erişim sağlar.
Daha sonra, içe aktarılan modül içindeki değişkenlere ve fonksiyonlara `.` operatörünü kullanarak erişebilirsin.
Yani bu örnekte, `helper.say_hello()`, helper içindeki `say_hello()` fonksiyonunu çağırır ve son satır global değişken x'i artırır.

`from` sözdizimini kullanarak içe aktarılan modüldeki global'ları, import ifadesinin yürütüldüğü mevcut scope'a da taşıyabilirsin.

`from helper import *`
helper'dan tüm global'ları içe aktarır.

veya

`from helper import say_hello`
helper'dan yalnızca belirtilen global'ları içe aktarır.

Bu da helper dosyasını içe aktarır, ancak ona `helper` adlı bir değişken aracılığıyla erişmek yerine, `helper`'dan global'ları paketinden çıkarır ve onları doğrudan yerel scope'a atar.

`from helper import say_hello
say_hello()`

Bu import biçimi genellikle önerilmez çünkü iki dosya birbirini içe aktardığında iyi çalışmaz ve isim çakışmaları nedeniyle içe aktaran dosyada yanlışlıkla değişkenlerin üzerine yazabilirsin.

# Gerçekte nasıl çalışır

## ÖZET
Import'lar oldukça sezgi dışı olabilir, ancak çoğu sorun `from file import` yerine `import file` sözdizimine bağlı kalarak ve global bir tanım olmayan her şeyi şunun içine alarak önlenebilir:
`if __name__ == "__main__":`

## Import Yan Etkileri
Bir dosyayı ilk kez içe aktardığında, tüm dosyayı yürütür ve ardından yürütme sırasında tanımlanmış olan tüm değişkenlere erişim sağlar.
Aynı dosyayı tekrar içe aktarırsan, sadece ilk seferden önbelleğe alınmış modülü tekrar döndürür.

Bu, import ifadelerinin yan etkileri olabileceği anlamına gelir. Eğer `harvest()` çağıran bir dosyayı içe aktarırsan, import sırasında gerçekten hasat yapacaktır. Ancak tekrar içe aktardığında, dosya yalnızca bir kez çalıştığı için tekrar hasat yapmayacaktır.

Bu tür yan etkilerden kaçınmanın bir yolu `__name__` değişkenini kullanmaktır. Bu, bir dosya doğrudan çalıştırıldığında otomatik olarak `"__main__"` olarak ayarlanan ve bir dosya `import` aracılığıyla çalıştırıldığında dosyanın adına ayarlanan bir değişkendir.
Dosya içe aktarıldığında çalışmasını istemediğin herhangi bir kodu `if __name__ == "__main__":` bloğunun içine koymak iyi bir uygulama olarak kabul edilir.

Python'da yaygın bir dosya yapısı, dosya çalıştırıldığında yürütülmesi gereken kodu bir `main()` fonksiyonuna koymaktır. Bu şekilde, yerel değişkenler (`main()` içinde tanımlanan) ile içe aktarılabilen global değişkenler (`main()` dışında tanımlanan) arasında net bir ayrım yapmış olursun.

`a_global_variable = "global"

def main():
    a_local_variable = "local"
    # bir şeyler yap

if __name__ == "__main__":
    main()`

## Import Döngüleri
`a` dosyası `b` dosyasını ve `b` dosyası `a` dosyasını içe aktarırsa ne olur?

dosya `a`:
`import b
x = 0`

dosya `b`:
`import a
def f():
    print(a.x)`

Bu sorunsuz çalışacaktır. Diyelim ki iki dosyadan hiçbiri henüz yüklenmedi ve başka biri `import a` komutunu çalıştırıyor.

-`a` dosyası, `import b` satırına kadar çalışır.
-`b` dosyası, `import a` satırına kadar çalışır.
-`a` modülü zaten mevcut, ancak `import b` satırına henüz ulaştığı için `x`'i içermiyor.
-`b`, yarı yüklenmiş `a` modülüne bir referansı `a` adlı bir değişkende saklar.
-`b`, `def` ifadesini çalıştırır ve `f()` fonksiyonunu saklar.
-`a` çalışmaya devam eder ve `x`'i başlatır.

Birisi `b.f()`'yi çağırdığında, `b`'nin referans aldığı `a` modülü artık tam olarak yüklendiği için doğru bir şekilde `0` yazdırır.

Şimdi aynı kodu `from` sözdizimini kullanarak düşünelim.

dosya `a`:
`from b import *
x = 0`

dosya `b`:
`from a import *
def f():
    print(x)`

-`a` dosyası, `from b import *` satırına kadar çalışır.
-`b` dosyası, `from a import *` satırına kadar çalışır.
-`a` modülü zaten mevcut, ancak henüz tam olarak yürütülmedi.
-`b`, `a`'da o anda bulunan her şeyi kendi global scope'una açar. Bu noktada, `a` henüz `x = 0` satırına ulaşmadığı için hiçbir şey içermez, bu yüzden hiçbir şey içe aktarılmaz.
-`b`, `def` ifadesini çalıştırır ve `f()` fonksiyonunu saklar.
-`a` çalışmaya devam eder ve `x`'i başlatır.

Eğer biri şimdi `b.f()`'yi çağırırsa, mevcut scope'ta `x`'in mevcut olmadığına dair bir error alırlar. Bunun nedeni, bu sefer `b`'nin hala yüklenmekte olan `a`'ya bir referansı olmaması ve içe aktarmadan sonra eklenen tanımları görmemesidir.