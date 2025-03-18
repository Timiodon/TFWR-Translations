# Podlewanie
Rośliny rosną szybciej, gdy są podlewane. Ziemia ma poziom wody od `0` do `1`.  
Funkcja `get_water()` zwraca poziom wody w ziemi, nad którą się znajduje.  

Prędkość wzrostu rośliny rośnie liniowo od prędkości 1x przy poziomie wody 0 do prędkości 5x przy poziomie wody 1.  

Ziemia wysycha z czasem: Średnio traci 1% obecnego poziomu wody na sekundę, ale występuje pewna losowa zmienność tego procesu. Utrzymanie wysokiego poziomu wody zużywa znacznie więcej wody niż utrzymanie niskiego poziomu wody.  

Możesz używać zbiorników na wodę, aby podlewać swoje rośliny. Jeden zbiornik na wodę jest automatycznie dodawany do twojego ekwipunku co 10 sekund.  
Zaktualizowanie `Unlocks.Watering` da ci dodatkowy zbiornik na wodę co 10 sekund.  

Zbiornik mieści `0.25` wody.  

Użyj `use_item(Items.Water)` nad dowolnym kawałkiem ziemi, aby ją podlać.