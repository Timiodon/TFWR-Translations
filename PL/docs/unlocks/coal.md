[<- Górnictwo](docs/unlocks/mining.md) <right>[Żelazo ->](docs/unlocks/iron.md)
<right>[Skok ->](docs/unlocks/jump.md)
---
# Węgiel
Pod ziemią czekają różne rudy, które możesz odnaleźć i wydobyć. Gdy przekopiesz się przez powierzchnię do `Grounds.Dirt`, pierwszą znalezioną rudą będzie węgiel.

Wydobywanie węgla nie wymaga niczego specjalnego: wykonaj `dig()`, gdy dron jest bezpośrednio nad blokiem `Grounds.Coal`. Użyj `get_ground_type()`, by sprawdzić podłoże pod dronem, i `get_ground_type(direction)`, by sprawdzić cztery sąsiednie bloki.

Poniższy program to dobry punkt wyjścia do poszukiwania węgla. Kopie w dół w poszukiwaniu pokładu.
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
    "items": [],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 4,
    "digging_speed": 2,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 2,
    "exclude_unlocks": ["watering", "fertilizer"]
}
#SETUP
move(North)
move(East)
move(East)
#CODE
# Kop, aż pojawi się blok węgla
while get_ground_type() != Grounds.Coal:
    dig()

# Wydobądź węgiel
dig()
}}

## Uwaga o zawałach
Węgiel dostajesz wyłącznie z bezpośrednio wykopanych bloków, a nie z tych, które zawalą się wokół drona. Uwzględnij to w strategii, aby wydobyć jak najwięcej węgla i jak najmniej stracić w zawałach.

## Budowa żył
Żyły tworzą poziome warstwy o grubości 1 bloku, na które trzeba trafić podczas kopania ziemi. Większość bloków węgla w warstwie styka się bezpośrednio, ale niektóre łączą się tylko po skosie.

Złoża węgla rosną proporcjonalnie do farmy, więc dalej ulepszaj [Rozszerzenie](unlocks/expand), aby wydobywać więcej węgla.

## Strategia
<spoiler=pokaż wskazówkę>
Prosta strategia, zwłaszcza na małych farmach, to wykopanie wszystkich bloków na głębokości znalezionego węgla. Aby zwiększyć wydajność, zapamiętuj pozycje węgla za pomocą `get_ground_type(direction)` i unikaj tracenia czasu na ruch nad ziemią. Uważaj na połączenia ukośne, które przeoczysz, poruszając się tylko po blokach węgla.
</spoiler>

---

[Statystyki](docs/stats.md)      [Górnictwo](docs/unlocks/mining.md)      [Podziemne zmysły](docs/unlocks/underground_senses.md)

[move()](functions/move)      [get_ground_type()](functions/get_ground_type)      [dig()](functions/dig)
