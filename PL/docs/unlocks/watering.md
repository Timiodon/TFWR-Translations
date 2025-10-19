# Podlewanie
Rośliny rosną szybciej, gdy są podlewane. Ziemia ma poziom wody w zakresie od `0` do `1`.
Funkcja `get_water()` zwraca poziom wody podłoża, nad którym się znajduje.

Prędkość wzrostu rośliny skaluje się liniowo od 1x prędkości przy poziomie wody 0 do 5x prędkości przy poziomie wody 1.

Ziemia z czasem wysycha: Średnio traci 1% swojej obecnej wody na sekundę, ale jest w tym pewna losowa zmienność. Utrzymywanie wysokiego poziomu wody zużyje znacznie więcej wody niż utrzymywanie niskiego poziomu.

Możesz używać wody na swoich roślinach. Jeden zbiornik wody jest automatycznie dodawany do twojego ekwipunku co 10 sekund.
Ulepszenie `Unlocks.Watering` podwoi ilość wody, którą otrzymujesz co 10 sekund.

Jeden zbiornik mieści `0.25` wody.

Wywołaj `use_item(Items.Water)` nad dowolnym podłożem, aby je podlać.
