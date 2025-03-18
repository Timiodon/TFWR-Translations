# İmport
Tüm kodunu tek bir dosyada toplamak hızlı bir şekilde yönetilemez hale gelir.
`import` ifadeleri, başka bir dosyadaki fonksiyonları ve global değişkenleri içeri aktarmanı sağlar.

`import filename`

Bu, en basit import ifadesi şeklidir. Bu ifade, `filename` adlı dosyada tanımlanmış her şeye erişmeni sağlar. Oyundaki her pencere bir dosyadır ve dosya adı, pencerenin üst kısmında görüntülenen isimdir.

İşte iki dosyayla bir örnek:
helper adlı dosya:
`x = 0

def say_hello():
    print("hello from helper")`

Başka bir dosya:
`import helper
helper.say_hello()
helper.x += 1`

Burada `import helper`, `helper` adlı dosyayı çalıştırır ve tüm global değişkenlerine erişim sağlar.
Bu şekilde, import edilen modülün içindeki değişkenlere ve fonksiyonlara `.` operatörü ile erişebilirsin.
Bu örnekte, `helper.say_hello()` ifadesi helper'daki `say_hello()` fonksiyonunu çağırır ve son satırda global `x` değişkenini artırır.

Ayrıca, import ifadesinin çalıştırıldığı mevcut scope'a, import edilen modülden global değişkenleri taşımak için `from` söz dizimini kullanabilirsin.

`from helper import *`
helper'den tüm global değişkenleri import eder.

veya

`from helper import say_hello`
helper'den sadece belirtilen global değişkenleri import eder.

Bu da helper dosyasını import eder, ancak `helper` adlı bir değişken yerine, `helper` içindeki global değişkenleri local scope'a doğrudan atar.

`from helper import say_hello
say_hello()`

Bu tür import genellikle önerilmez çünkü iki dosya birbirini import ediyorsa iyi çalışmaz ve isim çakışmaları nedeniyle import eden dosyadaki değişkenleri yanlışlıkla geçersiz kılabilirsin.

# Gerçekten nasıl çalışıyor

## TLDR
İmport işlemleri epey sezgisel olmayabilir, ancak çoğu problem `import file` söz dizimine bağlı kalarak ve global tanımlar haricindeki her şeyi 
`if __name__ == "__main__":`
bloğuna sararak önlenebilir.

## Import Yan Etkileri
Bir dosya ilk defa import edildiğinde, tüm dosyayı çalıştırır ve sonrasında tanımlanan tüm değişkenlere erişim sağlar.
Aynı dosya tekrar import edilirse, sadece ilk seferdeki önbelleğe alınmış modülü geri döndürür.

Bu, import ifadelerinin yan etkilerine yol açabileceği anlamına gelir. Eğer bir dosya `harvest()` fonksiyonunu çağırıyorsa, import sırasında gerçekten hasat yapacaktır. Ancak aynı dosya tekrar import edildiğinde tekrar hasat yapmayacaktır çünkü dosya yalnızca bir kez çalıştırılır.

Böyle yan etkilerden kaçınmanın bir yolu `__name__` değişkenini kullanmaktır. Bu, bir dosya doğrudan çalıştırıldığında otomatik olarak `"__main__"` olarak ayarlanır ve `import` yoluyla çalıştırıldığında dosyanın adına ayarlanır.
Dosya import edildiğinde çalışmasını istemediğin kodu `if __name__ == "__main__":` bloğunun içine koymak iyi bir uygulama olarak kabul edilir.

Python'da yaygın bir dosya yapısı, bir dosya çalıştırıldığında çalışması gereken kodu bir `main()` fonksiyonuna koymaktır. Bu şekilde, local değişkenler (x)`main()` içinde tanımlanan) ile import edilebilen global değişkenler (x)`main()` dışında tanımlanan) arasında net bir ayrım olur.

`a_global_variable = "global"

def main():
    a_local_variable = "local"
    # bir şeyler yap

if __name__ == "__main__":
    main()`

## Import Döngüleri
Eğer `a` dosyası `b` dosyasını ve `b` dosyası `a` dosyasını import ediyorsa ne olur?

`a` dosyası:
`import b
x = 0`

`b` dosyası:
`import a
def f():
    print(a.x)`

Bu gayet iyi çalışacaktır. Diyelim ki iki dosya da henüz yüklenmemiş ve birisi `import a` ifadesini çalıştırdı.

-`a`, `import b` satırına kadar çalışır.
-`b`, `import a` satırına kadar çalışır.
-Modül `a` zaten var, ancak henüz `x` içermiyor çünkü sadece `import b` satırına kadar ulaştı.
-`b`, yarıya kadar yüklenmiş olan `a` modülüne bir referansı `a` adlı bir değişkende depolar.
-`b`, `def` ifadesini çalıştırır ve fonksiyon `f()`'yi depolar.
-`a`, çalışmaya devam eder ve `x`'i başlatır.

Birisi `b.f()` çağırdığında, doğru bir şekilde `0` yazdıracaktır çünkü `b`'nin referans aldığı `a` modülü artık tamamen yüklüdür.

Şimdi aynı kodu `from` söz dizimiyle yapmayı düşün.

`a` dosyası:
`from b import *
x = 0`

`b` dosyası:
`from a import *
def f():
    print(x)`

-`a`, `from b import *` satırına kadar çalışır.
-`b`, `from a import *` satırına kadar çalışır.
-Modül `a` zaten var, ancak henüz tamamen çalıştırılmadı.
-`b`, `a` dosyasındaki her şeyi kendi global scope'una açar. Bu noktada, `a`, `x = 0` satırına ulaşmadığı için hiçbir şey içermediğinden hiçbir şey import edilmez.
-`b`, `def` ifadesini çalıştırır ve fonksiyon `f()`'yi depolar.
-`a`, çalışmaya devam eder ve `x`'i başlatır.

Şimdi biri `b.f()` çağırırsa, mevcut scope'da `x` olmadığını belirten bir hata alır. Bunun nedeni, bu sefer `b`'nin hala yükleniyor olan `a`'ya bir referansa sahip olmaması ve importtan sonra eklenen tanımları görmemesidir.