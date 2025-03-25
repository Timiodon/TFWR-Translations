# Podlewanie
Rośliny rosną szybciej, gdy są podlewane. Podłoże ma poziom wody od `0` do `1`.  
Funkcja `get_water()` zwraca poziom wody w glebie, nad którą się znajduje.  

Prędkość wzrostu rośliny zwiększa się liniowo, od 1x przy poziomie wody 0 do 5x przy poziomie wody 1.  

Ziemia wysycha z czasem: Średnio traci 1% swojej obecnej ilości wody na sekundę, ale jest też trochę losowej zmienności. Utrzymywanie wysokiego poziomu wody zużywa znacznie więcej wody niż utrzymywanie niskiego poziomu.  

Możesz używać wody na swoich roślinach. Jedna zbiornik wody jest automatycznie dodawana do twojego inwentarza co 10 sekund.  
Ulepszenie `Unlocks.Watering` zapewni ci dodatkowy zbiornik wody co 10 sekund.  

Zbiornik mieści `0.25` wody.  

Wywołaj `use_item(Items.Water)` nad dowolnym podłożem, aby je podlać.