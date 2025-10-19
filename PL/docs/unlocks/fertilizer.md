# Nawóz
W pewnym momencie, czekanie na wzrost roślin po prostu przestaje być wystarczająco wydajne. 
Podobnie jak woda, będziesz automatycznie otrzymywać 1 nawóz co 10 sekund, a ilość ta podwaja się z każdym ulepszeniem.

Nawóz może sprawić, że rośliny będą rosły natychmiast. `use_item(Items.Fertilizer)` skraca pozostały czas wzrostu rośliny pod dronem o 2 sekundy.

Ma to pewne skutki uboczne.
Rośliny uprawiane z nawozem zostaną zainfekowane.

Gdy roślina jest zainfekowana, połowa jej plonu zamienia się w `Items.Weird_Substance` podczas zbioru.
Dziwna Substancja może być również używana na roślinach, co ma efekt przełączania statusu infekcji rośliny i wszystkich sąsiednich roślin.

Więc jeśli wywołasz `use_item(Items.Weird_Substance)` na zainfekowanej roślinie, uleczy ją, ale jeśli użyjesz jej na zdrowej roślinie, zainfekuje ją.

Jeśli użyjesz jej na zainfekowanej roślinie, która ma zdrowych sąsiadów, uleczy roślinę, ale zainfekuje sąsiadów i na odwrót.