[<- Żelazo](docs/unlocks/iron.md)
---
# Poszukiwanie żelaza
Być może zauważyłeś, że żyły żelaza czasem trudno znaleźć. Można kopać na oślep i liczyć na szczęście, ale istnieje lepszy sposób: żelazo jest magnetyczne, więc możemy wykrywać je na odległość.

Właśnie do tego służy polecenie `prospect_iron()`. Funkcja `prospect_iron()` zwraca kierunek (`North`, `East`, `South` lub `West`), w którym dron musi się poruszyć, aby zrobić krok w stronę najbliższej rudy żelaza.

Wykonanie polecenia kosztuje 1 węgiel.

`prospect_iron()` zwraca `None`, jeśli dron znajduje się już bezpośrednio nad najbliższą rudą żelaza, nie masz wystarczająco dużo węgla albo w zasięgu nie ma żelaza.

Poniższy kod przesuwa drona o jeden krok bliżej następnej rudy żelaza:

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
    "items": [{"item": "coal", "n": 100}],
    "world_size": {"x": 5, "y": 5},
    "execution_speed": 1,
    "digging_speed": 10,
    "action_ticks": 200,
    "operation_ticks": 50,
    "seed": 8,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "quartz"]
}
#SETUP
jump(Unlocks.Iron)
#CODE
# Upewnij się, że poszukiwanie zwraca kierunek
if prospect_iron() != None:
    move(prospect_iron()) # Zbliż się do żyły żelaza
}}

Warto zoptymalizować ten kod za pomocą zmiennej, ponieważ obecnie wywołuje `prospect_iron()` dwukrotnie, co kosztuje 2 sztuki węgla.

## Obliczanie odległości
Najbliższa ruda żelaza jest wyznaczana na podstawie liczby kroków, które musi wykonać dron. Jeśli ruda znajduje się 2 bloki na wschód i 3 bloki na północ od drona, odległość wynosi 5, ponieważ dotarcie tam wymaga pięciu kroków.

Kopanie również liczy się jako krok. Jeśli dodatkowo żelazo jest zakopane 7 bloków pod ziemią, odległość wynosi 12, ponieważ dron musi zrobić pięć kroków, aby znaleźć się nad rudą, a następnie wykopać siedem bloków, aby do niej dotrzeć.

---

[Żelazo](docs/unlocks/iron.md)      [Podziemne zmysły](docs/unlocks/underground_senses.md)

[move()](functions/move)      [dig()](functions/dig)      [prospect_iron()](functions/prospect_iron)
