[<- Żelazo](docs/unlocks/iron.md)
---
# Mapa skarbu
Legendy mówią o nieuchwytnym skarbie ukrytym przez dawno zmarłego, zapominalskiego pirata — albo jakoś tak. A co, jeśli zapisał drogę do skarbu na mapie, a potem ją zgubił? Może upuścił mapę, gdy odcięła mu drogę rzeka lawy, i zachowała się ona pod warstwą bazaltu.

Pomiar bloków bazaltu może coś ujawnić!

<spoiler=powiedz mi więcej>
Wypatruj warstwy `Grounds.Basalt`. Spróbuj zmierzyć bazalt i sprawdź, co ci powie. Wskazówka może zaprowadzić cię do mapy skarbu, a zmierzenie mapy z pewnością zwróci drogę do samego skarbu — tylko czy uda ci się rozszyfrować jej instrukcje?
</spoiler>

<spoiler=po prostu powiedz jak>
Dobrze, sprawa wygląda tak: znajdź warstwę `Grounds.Basalt` i blok `Grounds.Treasure_Map` znajdujący się bezpośrednio pod nią. Możesz użyć `measure()` na bazalcie, aby uzyskać pozycję `(x, y)` leżącego niżej bloku mapy.

Wywołaj `measure()` na bloku mapy, aby otrzymać drogę do skarbu jako ciąg liter oznaczających kierunki. N, E, S i W oznaczają odpowiednio `North`, `East`, `South` i `West`, natomiast D oznacza „Down” lub „Dig”. Litery te opisują drogę złożoną z bloków `Grounds.Treasure_Path`, która prowadzi do skarbu.

{{codeexample 
{
    "camera_position": {"x": -1.5, "y": 0, "z": 6},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "digging_speed": 10,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 3,
    "exclude_unlocks": ["watering", "fertilizer", "dynamite", "iron"]
}

#SETUP
jump(Unlocks.Treasure_Map)
#CODE
# Znajdź warstwę bazaltu
while get_ground_type() != Grounds.Basalt:
    dig()

# Pomiar bazaltu zwraca pozycję mapy skarbów
map_pos = measure()

while get_pos_x() < map_pos[0]:
    move(East)
while get_pos_y() < map_pos[1]:
    move(North)

while get_ground_type() != Grounds.Treasure_Map:
    dig()

# Znaleziono mapę, zmierz ją, aby poznać ścieżkę
do_a_flip()
instructions = measure()
print("instrukcje: ", instructions)

# Wykop mapę, aby rozpocząć poszukiwanie skarbu
dig()
}}

Możesz użyć pętli `for` na łańcuchu, aby przetworzyć go litera po literze:
{{codeexample 
{
    "camera_position": {"x": -1.5, "y": 0, "z": 6},
    "show_image": false,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "digging_speed": 10,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 3,
    "exclude_unlocks": ["watering", "fertilizer", "dynamite", "iron"]
}
#SETUP
jump(Unlocks.Treasure_Map)
while get_ground_type() != Grounds.Basalt:
    dig()

map_pos = measure()

while get_pos_x() < map_pos[0]:
    move(East)
while get_pos_y() < map_pos[1]:
    move(North)

while get_ground_type() != Grounds.Treasure_Map:
    dig()
#CODE
# Instrukcje mapy są zwracane jako jeden łańcuch
instructions = measure()
# Użyj for-in, aby przetworzyć łańcuch litera po literze
for letter in instructions:
    print(letter)
}}

Dron przez cały czas musi pozostawać na blokach `Grounds.Treasure_Path`. Jeśli przemieści się na inne podłoże, droga zniknie, a skarb zostanie utracony.

## Cel
Na końcu drogi znajduje się blok `Grounds.Treasure_Goal`. Jeśli dron nie zboczył z drogi, pojawi się na nim `Entities.Underground_Treasure`. Dron może użyć `harvest()` na skrzyni, aby zebrać złoto.

## Nagroda
Ilość złota jest proporcjonalna do długości drogi do skarbu. Ulepszanie odblokowania Mapy skarbu zwiększa jej głębokość, a ulepszanie Rozszerzenia daje jej więcej miejsca na ruch w poziomie. Oba ulepszenia wydłużają drogę do skarbu i zwiększają ilość znalezionego złota.

## Wiele dronów
Dron, który wykopie blok mapy skarbów, musi znaleźć skarb bez opuszczania bloków ścieżki.
</spoiler>

---

[Statystyki](docs/stats.md)      [Pętla for](docs/scripting/for.md)      [Krotki](docs/scripting/tuples.md)      [Podziemne zmysły](docs/unlocks/underground_senses.md)

[harvest()](functions/harvest)      [move()](functions/move)      [dig()](functions/dig)      [measure()](functions/measure)
