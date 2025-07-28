# Rozszerzenie 2
Twoja farma znowu się rozszerzyła! Teraz pola nie są już w ładnym rzędzie, więc musisz znaleźć sposób na przemierzanie kwadratowej siatki.

Z pętlą `while` nie jest to możliwe, dopóki nie odblokujesz zmysłów i operatorów.
Nadszedł czas na wprowadzenie pętli `for`.

Możesz przeczytać wszystko o pętli `for` na stronie [Pętla For](docs/scripting/for.md), ale na razie będziesz jej potrzebować tylko do powtarzania kodu ustaloną liczbę razy.

`#zrób n fikołków
for i in range(5):
	do_a_flip()`

`range(n)` tworzy zakres liczb od `0` do `n-1`, który ma `n` elementów. Pętla `for` uruchamia swoje ciało raz dla każdego elementu w sekwencji. W tym przykładzie `do_a_flip()` zostanie wywołane `5` razy.

Dostępna jest teraz także funkcja `get_world_size()`. Zwraca ona długość boku twojej farmy. W ten sposób możesz pisać kod, który nie zepsuje się przy następnym ulepszeniu rozszerzenia.

`for i in range(get_world_size()):
	harvest()
	move(North)`

Ten przykład zbiera jedną kolumnę farmy dla dowolnego rozmiaru farmy.

Jeśli utknąłeś, próbując wymyślić, jak poruszać dronem po farmie, zobacz wskazówkę poniżej.
<spoiler=pokaż wskazówkę>Oczywiście, istnieje kilka sposobów poruszania się po farmie.
Szukamy sposobu na systematyczne przemierzanie jej w taki sposób, który nie zepsuje się, gdy farma znów się powiększy.
Systematycznym sposobem na dotarcie do każdego miejsca na farmie byłoby powtarzanie w nieskończoność następujących 2 kroków:

1.Poruszaj się na `North`, aż zawinie z powrotem.
2.Poruszaj się na `East`

`for i in range(get_world_size()):` może być pomocne w przekształceniu tego pomysłu w kod.
</spoiler>
<spoiler=pokaż możliwe rozwiązanie> Podstawowe przemierzanie może wyglądać tak:

`for i in range(get_world_size()):
	for j in range(get_world_size()):
		#zrób fikołka na każdym polu
		do_a_flip()
		move(North)
	move(East)`
</spoiler>