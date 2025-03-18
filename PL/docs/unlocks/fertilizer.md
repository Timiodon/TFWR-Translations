# Nawóz
W pewnym momencie czekanie, aż rośliny urosną, przestaje być wystarczająco efektywne. Podobnie jak w przypadku wody, automatycznie otrzymasz 1 nawóz co 10 sekund, plus dodatkowy za każdą aktualizację.

Nawóz może sprawić, że rośliny urosną natychmiast. `use_item(Items.Fertilizer)` zmniejsza pozostały czas wzrostu rośliny pod dronem o 2 sekundy.

Ma to jednak pewne skutki uboczne. Rośliny wyhodowane z użyciem nawozu będą zainfekowane.

Kiedy roślina jest zainfekowana, połowa jej plonów zamienia się w `Items.Weird_Substance` w momencie zbioru. Dziwną Substancję można również używać na roślinach, co ma efekt zmiany statusu infekcji rośliny i wszystkich sąsiadujących roślin.

Jeśli więc użyjesz `use_item(Items.Weird_Substance)` na zainfekowanej roślinie, wyleczy ją, ale jeśli użyjesz jej na zdrowej roślinie, zainfekuje ją.

Jeśli użyjesz jej na zainfekowanej roślinie, która ma zdrowych sąsiadów, wyleczy roślinę, ale zainfekuje sąsiadów i odwrotnie.