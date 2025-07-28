# Podlewanie
Rośliny rosną szybciej, gdy są podlewane. Ziemia ma poziom wody w zakresie od `0` do `1`.
Funkcja `get_water()` zwraca poziom wody w ziemi, nad którą się znajduje.

Prędkość wzrostu rośliny skaluje się liniowo od prędkości 1x przy poziomie wody 0 do prędkości 5x przy poziomie wody 1.

Ziemia z czasem wysycha: Średnio traci 1% swojej obecnej wody na sekundę, ale występuje w tym pewna losowa zmienność. Utrzymanie wysokiego poziomu wody zużyje znacznie więcej wody niż utrzymanie niskiego poziomu.

Możesz używać wody na swoich roślinach. Jeden zbiornik wody jest automatycznie dodawany do twojego ekwipunku co 10 sekund.
Ulepszenie `Unlocks.Watering` da ci dodatkowy zbiornik wody co 10 sekund.

Zbiornik mieści `0.25` wody.

Wywołaj `use_item(Items.Water)` nad dowolnym podłożem, aby je podlać.