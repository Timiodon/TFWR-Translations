[<- Balkabakları](docs/unlocks/pumpkins.md) <right>[Dinozorlar ->](docs/unlocks/dinosaurs.md)
---
# Kaktüs
Diğer bitkiler gibi [kaktüsler](objects/cactus) de toprakta yetiştirilebilir ve her zamanki gibi hasat edilebilir.

Ancak farklı boyutlarda olurlar ve tuhaf bir düzen anlayışları vardır.

Tamamen büyümüş bir kaktüsü hasat ettiğinde tüm komşu kaktüsler sıralı düzendeyse, komşu kaktüslerin hepsi de özyinelemeli olarak hasat edilir.

Bir kaktüsün sıralı düzende sayılması için `North` ve `East` yönündeki tüm komşu kaktüslerin tamamen büyümüş ve boyutça ondan büyük ya da ona eşit, `South` ve `West` yönündeki tüm komşu kaktüslerin ise tamamen büyümüş ve boyutça ondan küçük ya da ona eşit olması gerekir.

Hasat yalnızca bitişik kaktüslerin hepsi tamamen büyümüş ve sıralı düzendeyse yayılır.
Yani büyümüş kaktüslerden oluşan kare biçimli bir alan boyuta göre sıralanmışsa ve bir kaktüsü hasat edersen, alanın tamamı hasat edilir.

Tamamen büyümüş bir kaktüs sıralı değilse kahverengi görünür. Sıralandığında yeniden yeşile döner.

Hasat edilen kaktüs sayısının karesi kadar kaktüs alırsın. Aynı anda `n` kaktüs hasat edersen `n**2` `Items.Cactus` alırsın.

Bir kaktüsün boyutu `measure()` ile ölçülebilir.
Boyut her zaman şu sayılardan biridir: `0,1,2,3,4,5,6,7,8,9`.

`measure(direction)` fonksiyonuna bir yön vererek dronun o yöndeki komşu karesini de ölçebilirsin.

`swap()` komutuyla bir kaktüsün herhangi bir yöndeki komşusuyla yerini değiştirebilirsin.
`swap(direction)`, dronun altındaki nesneyle dronun `direction` yönündeki bitişik karede bulunan nesnenin yerini değiştirir.

{{codeexample 
{
    "camera_position": {"x": -1.5, "y": 2.4, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "pumpkin", "n": 32}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 1,
    "exclude_unlocks": ["fertilizer", "watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
for _ in range(4):
    for _ in range(4):
        till()
        plant(Entities.Cactus)
        move(East)
    move(North)
for _ in range(4):
    for _ in range(4):
        for _ in range(4):
            x,y = get_pos_x(), get_pos_y()
            if x > 0 and measure(West) > measure():
                swap(West)
            if y > 0 and measure(South) > measure():
                swap(South)
            if x < 3 and measure(East) < measure():
                swap(East)
            if y < 3 and measure(North) < measure():
                swap(North)
            move(East)
        move(North)
move(East)
move(North)
move(North)
swap(West)
swap(South)
swap(East)
swap(North)
#CODE
swap(North)
swap(East)
swap(South)
swap(West)
harvest()
}}

## Sayı Örnekleri
Bu ızgaraların her birinde tüm kaktüsler sıralı düzendedir ve hasat tüm tarlaya yayılır:
`3 4 5    3 3 3    1 2 3    1 5 9
2 3 4    2 2 2    1 2 3    1 3 8
1 2 3    1 1 1    1 2 3    1 3 4`

Bu ızgarada yalnızca sol alttaki kaktüs sıralı düzendedir; bu da hasadın yayılması için yeterli değildir:
`1 5 3
4 9 7
3 3 2`

<spoiler=1. ipucunu göster>
Her satır zaten kendi içinde sıralıysa, her sütunu kendi içinde sıralamak satırların sırasını bozmaz.
</spoiler>
<spoiler=2. ipucunu göster>
Pek çok akıllıca tasarlanmış, iyi bilinen sıralama algoritması vardır. Bunları bilmiyorsan araştırıp hangilerinin bu probleme uyarlanabileceğini düşünebilirsin. Yalnızca komşu kaktüslerin yerini değiştirebildiğin için hepsinin burada işe yaramayacağını unutma.
</spoiler>
<spoiler=3. ipucunu göster>
"Kabarcık sıralaması" (bubble sort) belki de en basit sıralama algoritmasıdır. Fikir şu: Elemanların üzerinden tekrar tekrar geçip yanlış sırada olan bitişik elemanların yerini değiştirirsin; bu, yanlış sırada eleman kalmayana kadar sürer.

Kaktüslerle şöyle görünür:
{{codeexample 
{
    "camera_position": {"x": -4, "y": 1, "z": 6},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": false,
    "show_inventory": true,
    "show_output": false,
    "collapsing": false,
    "autoplay": true,
    "items": [{"item": "pumpkin", "n": 18}],
    "world_size": {"x": 9, "y": 1},
    "execution_speed": 2,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": 1,
    "exclude_unlocks": ["fertilizer", "watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
for _ in range(9):
    till()
    plant(Entities.Cactus)
    move(East)
sorted = False
while not sorted:
    sorted = True
    for _ in range(9):
        move(East)
        if get_pos_x() > 0 and measure(West) > measure():
            swap(West)
            sorted = False
harvest()
}}
Bu stratejiyi geliştirmenin elbette pek çok yolu var!
Tek bir satırı sıralamayı başardıktan sonra, 1. ipucunu kullanarak tüm tarlayı sıralayabilirsin.
</spoiler>

---

[İstatistikler](docs/stats.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [till()](functions/till)      [swap()](functions/swap)      [measure()](functions/measure)
