# Ekspansja 2
Twoja farma znów się powiększyła! Teraz pola nie są już w ładnym rzędzie, więc musisz znaleźć sposób na przemierzanie kwadratowej siatki.

Z pętlą `while` nie jest to możliwe, dopóki nie odblokujesz zmysłów i operatorów.
Nadszedł czas na wprowadzenie pętli `for`.

Możesz przeczytać wszystko o pętli `for` na stronie [Pętla For](docs/scripting/for.md), ale na razie będziesz jej potrzebować tylko do powtarzania kodu stałą liczbę razy.

`#wykonaj n obrotów
for i in range(5):
	do_a_flip()`

`range(n)` tworzy zakres liczb od `0` do `n-1`, który ma `n` elementów. Pętla `for` wykonuje swoje ciało raz dla każdego elementu w sekwencji. W tym przykładzie `do_a_flip()` zostanie wywołane `5` razy.

Dostępna jest teraz również funkcja `get_world_size()`. Zwraca ona długość boku twojej farmy. W ten sposób możesz pisać kod, który nie zepsuje się przy następnym ulepszeniu ekspansji.

`for i in range(get_world_size()):
	harvest()
	move(North)`

Ten przykład zbiera plony z jednej kolumny farmy dla dowolnego rozmiaru farmy.

Jeśli utknąłeś, próbując wymyślić, jak poruszać dronem po farmie, zobacz podpowiedź poniżej.
<spoiler=pokaż podpowiedź>Oczywiście, istnieje kilka sposobów poruszania się po farmie.
Szukamy sposobu na systematyczne jej przemierzanie, który nie zepsuje się, gdy farma znów urośnie.
Systematycznym sposobem dotarcia do każdego miejsca na farmie byłoby powtarzanie następujących 2 kroków w nieskończoność:

1. Poruszaj się na `North`, aż się zawinie.
2. Porusz się na `East`

`for i in range(get_world_size()):` może być pomocne w przekształceniu tego pomysłu w kod.
</spoiler>
<spoiler=pokaż możliwe rozwiązanie> Podstawowe przemierzanie mogłoby wyglądać tak:

`for i in range(get_world_size()):
	for j in range(get_world_size()):
		#wykonaj obrót na każdym polu
		do_a_flip()
		move(North)
	move(East)`
</spoiler>