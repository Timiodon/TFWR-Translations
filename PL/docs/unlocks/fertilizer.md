# Nawóz
W pewnym momencie, czekanie aż rośliny urosną, przestaje być wystarczająco wydajne.
Podobnie jak woda, automatycznie otrzymasz 1 nawóz co 10 sekund, plus dodatkowy za każde ulepszenie.

Nawóz może sprawić, że rośliny będą rosły natychmiast. `use_item(Items.Fertilizer)` skraca pozostały czas wzrostu rośliny pod dronem o 2 sekundy.

Ma to pewne efekty uboczne.
Rośliny wyhodowane z nawozem będą zainfekowane.

Gdy roślina jest zainfekowana, połowa jej plonu zamienia się w `Items.Weird_Substance` podczas zbioru.
Dziwną substancję można również używać na roślinach, co ma efekt przełączania statusu infekcji rośliny i wszystkich sąsiednich roślin.

Więc jeśli wywołasz `use_item(Items.Weird_Substance)` na zainfekowanej roślinie, wyleczy ją, ale jeśli użyjesz jej na zdrowej roślinie, zainfekuje ją.

Jeśli użyjesz jej na zainfekowanej roślinie, która ma zdrowych sąsiadów, wyleczy ona roślinę, ale zainfekuje sąsiadów i na odwrót.