[<- Bambu](docs/unlocks/bamboo.md)
---
# Piramitler

Yeraltında artık enerji elde edebileceğin kadim, piramit biçimli yapılar var!

Piramitler kum bloklarından (`Grounds.Sand`) yapılır. Piramidin hemen altında kireçtaşından (`Grounds.Limestone`) bir temel katmanı bulunur. Piramitler eski ve aşınmış olduklarından onları yalnızca kısmen yıkılmış hâlde bulursun. Temel katmanı her zaman yerindedir ama kumun içinde delikler olur. Bir piramidi kazıp ortaya çıkardığında şöyle görünür:

{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 8},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "hay", "n": 100}, {"item": "block", "n": 100}],
    "world_size": {"x": 6, "y": 6},
    "execution_speed": 32,
    "digging_speed": 16,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 7,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "dynamite", "quartz"]
}
#SETUP
jump(Unlocks.Pyramid)
move(North)
#CODE
while get_ground_type() != Grounds.Limestone:
    dig()
do_a_flip()
z = get_pos_z()
for i in range(6):
    for j in range(6):
        while (get_ground_type() != Grounds.Limestone
                and get_ground_type() != Grounds.Sand
                and get_pos_z() > z):
            dig()
        move(North)
    move(East)
}}

Piramidin üstündeki bloklar her zaman topraktır. Bir piramidi yukarıdaki koddan daha verimli şekilde kazıp ortaya çıkarmak istersen bu bilgiden yararlanabilirsin.

Gördüğün gibi kumda doldurulması gereken birkaç delik var. Bu delikleri doldurup piramidi eski hâline getirdiğinde piramit kendini yok eder ve ödül olarak güç kazanırsın.

Bir piramidi `place(Grounds.Sand)` komutuyla blok yerleştirerek onarabilirsin. Kum, düzgün desteklenmediğinde hemen göçen özel bir bloktur. Yerleştirdiğin her kum bloğu ya doğrudan kireçtaşının üzerine ya da 3x3'lük bir kum bloğu alanının üzerine konmalıdır. Bunu göstermek için aşağıda elle yapılmış küçük bir piramit var. Elbette kendi inşa ettiğin bir piramit sana hiç güç kazandırmaz:

{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 8},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "hay", "n": 100}, {"item": "block", "n": 100}],
    "world_size": {"x": 3, "y": 3},
    "execution_speed": 4,
    "digging_speed": 4,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 9,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "coal", "quartz"]
}
#CODE
for i in range(3):
    for j in range(3):
        place(Grounds.Limestone)
        move(North)
    move(East)
    
for i in range(3):
    for j in range(3):
        place(Grounds.Sand)
        move(North)
    move(East)
    
move(North)
move(East)
place(Grounds.Sand)
}}

Doğru şekilde onarılmış bir piramit, kenar uzunluğu tek sayı olan (örneğin 5x5) kare biçimli bir kireçtaşı temelden oluşur. Bunun üstünde aynı boyutta (5x5) bir kum bloğu katmanı, onun üstünde de giderek küçülen katmanlar bulunur: önce 3x3, sonra 1x1.

Bir piramit tamamlandığında ufalanıp yok olur ve ortasında büyük bir ayçiçeği belirir. Onu hasat ederek güç kazanabilirsin. Tamamladığın piramit ne kadar büyükse o kadar çok güç kazanırsın.

---

[İstatistikler](docs/stats.md)      [Yeraltı Duyuları](docs/unlocks/underground_senses.md)

[move()](functions/move)      [dig()](functions/dig)      [use_item()](functions/use_item)      [place()](functions/place)
