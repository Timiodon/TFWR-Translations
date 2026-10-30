[<- Pirinç](docs/unlocks/rice.md)
---
# Taşlaşmış Balkabakları

Görünüşe göre yeraltında da balkabağı bulabiliyorsun. Katılaşıp taşlaşmışlar ama yine de işimizi görecek kadar iyiler.

Taşlaşmış balkabakları yeraltında 3x3x3 ya da 5x5x5 boyutunda bloklar halinde bulunur. Onları bulmanın kesin bir yolu yok, dronunun birine denk gelmesini ummaktan başka çaren yok; ama taş ve demir katmanının altındaki sert toprakta, aşağı yukarı kuvarsın çıktığı yükseklikte bulunurlar (kuvarsın kilidini açtıysan).

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
    "items": [{"item": "hay", "n": 100}],
    "exclude_unlocks": ["mushrooms", "watering", "fertilizer", "pyramid", "dynamite"],
    "world_size": {"x": 6, "y": 6},
    "execution_speed": 8,
    "digging_speed": 16,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 3
}
#SETUP
jump(Unlocks.Petrified_Pumpkins)
move(East)
move(North)
move(North)
move(North)
#CODE
while get_ground_type() != Grounds.Petrified_Pumpkin:
    dig()
z = get_pos_z()
for i in range(get_world_size()):
    for j in range(get_world_size()):
        while get_pos_z() > z:
            dig()
        move(North)
    move(East)
}}

---

[İstatistikler](docs/stats.md)      [Madencilik](docs/unlocks/mining.md)      [Yeraltı Duyuları](docs/unlocks/underground_senses.md)

[move()](functions/move)      [dig()](functions/dig)      [get_ground_type()](functions/get_ground_type)
