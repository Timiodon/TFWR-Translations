[<- Grzyby](docs/unlocks/mushroom.md) <right>[Wiertło wybuchowe ->](docs/unlocks/explosive_drill.md)
---
# Dynamit

Rewolucyjny materiał wybuchowy pozostawiony przez poprzednie wyprawy górnicze. Na (nie)szczęście twoje wiertło idealnie nadaje się do detonowania dynamitu i wysadzania wszystkich bloków wokół.

Aby bezpiecznie wydobywać dynamit, musisz znaleźć podwójną warstwę `Grounds.Dynamite` i `Grounds.Soot`. Znajdujący się wyżej dynamit nieco się zestarzał i do części jego bloków można bezpiecznie się dokopać. Niektóre ładunki są jednak nadal aktywne i eksplodują po dokopaniu się do nich.

{{codeexample 
{
    "camera_position": {"x": -3, "y": -3, "z": 12},
    "show_image": true,
    "image_size": {"x": 900, "y": 500},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": false,
    "autoplay": true,
    "items": [{"item": "hay", "n": 100}],
    "world_size": {"x": 5, "y": 5},
    "execution_speed": 8,
    "digging_speed": 8,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 4,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "coal", "quartz", "petrified_pumpkins"]
}
#SETUP
jump(Unlocks.Dynamite)
#CODE
while get_ground_type() != Grounds.Soot:
    dig()
dig()
dig()
}}

Czy potrafisz znaleźć i wykopać wszystkie niewypały, pozostawiając tylko aktywne bloki? Każdy aktywny blok otoczony wyłącznie innymi aktywnymi blokami lub blokami sadzy da ci dodatkowy dynamit, gdy warstwa dynamitu zniknie.

Na szczęście pomogą ci bloki sadzy poniżej: potrafią wykryć liczbę sąsiednich bloków dynamitu zawierających aktywne ładunki. Nie wskażą dokładnie, które bloki są aktywne, a tylko ich łączną liczbę, więc musisz połączyć odczyty z kilku bloków sadzy i samodzielnie znaleźć rozwiązanie.

Wywołanie `measure()` na bloku sadzy zwraca liczbę min na ośmiu sąsiednich polach w warstwie dynamitu powyżej. Wynik może wynosić od `0` (brak aktywnych min) do `8` (każdy sąsiad zawiera aktywną minę).

Pierwszy wykopany blok w warstwie dynamitu jest zawsze niewypałem. Każdy wydobyty blok daje trochę dynamitu. Gdy warstwa zostanie zniszczona — przez wykopanie wszystkich niewypałów lub przypadkowe dokopanie się do aktywnego dynamitu — otrzymasz także ilość dynamitu równą kwadratowi liczby całkowicie odsłoniętych aktywnych bloków.

Jeśli dokopiesz się do aktywnego dynamitu, oba pokłady eksplodują. Możesz to sprawdzić za pomocą `get_ground_type()` po dokopaniu się do `Grounds.Dynamite`. Jeśli podłoże nie jest typu `Grounds.Soot`, zagadka zakończyła się niepowodzeniem. Jeśli natomiast wykopiesz ostatni nieaktywny blok dynamitu, wszystkie bloki dynamitu znikną, a ty otrzymasz maksymalny plon za tę zagadkę. Warstwa sadzy pozostanie, ale `measure()` zwróci `None`, co oznacza, że zagadka została pomyślnie rozwiązana.

`# Dokop się do bloku dynamitu i sprawdź stan zagadki
def dig_dynamite():
    dig()
    if get_ground_type() != Grounds.Soot:
        # Dokopano się do aktywnego dynamitu, zagadka nieudana
        return False
    elif measure() == None:
        # Wykopano ostatni niewypał, zagadka rozwiązana
        return True
    else:
        # Pomiar zwrócił liczbę, zagadka nadal trwa
        return None
`

Liczba aktywnych min w warstwie dynamitu, a tym samym trudność ich odnalezienia, rośnie wraz z głębokością.

Zebranego dynamitu można użyć za pomocą `use_item(Items.Dynamite)`; eksploduje bezpośrednio pod dronem.

Ulepszaj dynamit, aby zwiększyć plon z wykopywania bloków dynamitu i całkowitego odsłaniania aktywnych bloków. Ulepszenie zwiększa też energię eksplozji o 30%.

---

[Statystyki](docs/stats.md)      [Podziemne zmysły](docs/unlocks/underground_senses.md)      [Słowniki](docs/scripting/dicts.md)      [Zbiory](docs/scripting/sets.md)

[move()](functions/move)      [dig()](functions/dig)      [measure()](functions/measure)      [use_item()](functions/use_item)
