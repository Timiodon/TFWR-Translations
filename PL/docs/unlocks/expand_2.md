# Rozwijanie 2
Twoja farma znowu się powiększyła! Teraz kafelki nie są już w ładnym rzędzie, więc musisz znaleźć sposób na poruszanie się po kwadratowej siatce.

Z pętlą `while` nie jest to możliwe, dopóki nie odblokujesz zmysłów i operatorów.
Czas wprowadzić pętlę `for`.

Możesz przeczytać wszystko o pętli `for` na stronie [Pętla For](docs/scripting/for.md), ale na razie będziesz jej potrzebować tylko do powtarzania kodu określoną liczbę razy.

`#zrób n przewrotów
for i in range(5):
	do_a_flip()`

`range(n)` tworzy zakres liczb od `0` do `n-1`, który ma `n` elementów. Pętla `for` uruchamia ciało pętli raz dla każdego elementu w sekwencji. W tym przykładzie `do_a_flip()` zostanie wywołane `5` razy.

Funkcja `get_world_size()` jest teraz również dostępna. Zwraca ona długość boku twojej farmy. W ten sposób możesz napisać kod, który nie zepsuje się przy kolejnym ulepszeniu farmy.

`for i in range(get_world_size()):
	harvest()
	move(North)`

Ten przykład zbiera jedną kolumnę farmy dla dowolnego rozmiaru farmy.

Jeśli utknąłeś próbując znaleźć sposób, jak przemieszczać drona po farmie, zobacz poniższą podpowiedź.
<spoiler=pokaż wskazówkę> Istnieje oczywiście kilka sposobów na poruszanie się po farmie.
Szukamy sposobu na systematyczne przemierzanie farmy, który nie zepsuje się, gdy farma znowu się powiększy.
Systematyczny sposób dotarcia do każdego miejsca na farmie to powtarzanie następujących 2 kroków w nieskończoność:

1. Poruszaj się `North`, aż wrócisz na początek.
2. Poruszaj się `East`.

`for i in range(get_world_size()):` może być pomocne do przekształcenia tego pomysłu w kod.
</spoiler>
<spoiler=pokaż możliwe rozwiązanie> Podstawowe przemieszczanie może wyglądać tak:

`for i in range(get_world_size()):
	for j in range(get_world_size()):
		#zrób przewrót na każdym kafelku
		do_a_flip()
		move(North)
	move(East)`
</spoiler>