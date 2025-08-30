# Dinozaury
Dinozaury to starożytne, majestatyczne stworzenia, które można hodować dla starożytnych kości.

Niestety, dinozaury wyginęły dawno temu, więc najlepsze, co możemy teraz zrobić, to przebrać się za jednego z nich.
W tym celu otrzymałeś nowy kapelusz dinozaura.

Kapelusz można założyć za pomocą
`change_hat(Hats.Dinosaur_Hat)`

Niestety nie wygląda on tak dobrze, jak w reklamie...

Jeśli założysz kapelusz dinozaura i będziesz mieć wystarczająco dużo dyń, [jabłko](objects/apple) zostanie automatycznie kupione i umieszczone pod dronem.
Gdy dron znajdzie się nad jabłkiem i ponownie się poruszy, zje jabłko, a jego ogon urośnie o jeden. Jeśli cię na to stać, nowe jabłko zostanie kupione i umieszczone w losowej lokalizacji.
Jabłko nie może się pojawić, jeśli w jego miejscu jest już coś posadzone.

Ogon dinozaura będzie ciągnął się za dronem, wypełniając pola, nad którymi dron się przemieszczał. Jeśli dron spróbuje wejść na ogon, `move()` nie powiedzie się i zwróci `False`. 
Ostatni segment ogona usunie się z drogi podczas ruchu, więc możesz na niego wejść. Jednakże, jeśli wąż wypełni całą farmę, nie będziesz mógł się już poruszać. Możesz więc sprawdzić, czy wąż jest w pełni rozwinięty, sprawdzając, czy nie możesz się już poruszać.

Użycie `measure()` na jabłku zwróci pozycję następnego jabłka jako krotkę (tuple).

`next_x, next_y = measure()`

Gdy kapelusz zostanie zdjęty poprzez założenie innego kapelusza, ogon zostanie zebrany.
Otrzymasz kości w liczbie równej kwadratowi długości ogona. Więc za ogon o długości `n` otrzymasz `n**2` `Items.Bone`. 
Na przykład:
długość 1 => 1 kość
długość 2 => 4 kości
długość 3 => 9 kości
długość 4 => 16 kości
długość 16 => 256 kości
długość 100 => 10000 kości

Kapelusz Dinozaura jest bardzo ciężki, więc jeśli go założysz, `move()` będzie zajmować 400 ticks zamiast 200. Jednak za każdym razem, gdy podniesiesz jabłko, liczba ticków używanych przez `move()` zmniejsza się o 3% (zaokrąglone w dół), ponieważ dłuższy ogon pomaga w poruszaniu się.

Poniższa pętla drukuje liczbę ticków używanych przez `move()` po zebraniu dowolnej liczby jabłek:

`ticks = 400
for i in range(100):
    print("ticks after ", i, " apples: ", ticks)
    ticks -= ticks * 0.03 // 1`

Masz tylko jeden kapelusz dinozaura, więc tylko jeden dron może go nosić.

<spoiler=show hint 1>Jeśli będziesz poruszać się po tej samej ścieżce, która pokrywa całe pole, możesz łatwo uzyskać węża, który za każdym razem pokryje całe pole. Nie jest to bardzo wydajne, ale działa.
Pełne przemierzenie bardzo dużej farmy może zająć dużo czasu, a być może nie potrzebujesz aż tylu kości. Możesz śmiało użyć `set_farm_size()`, aby zmienić rozmiar farmy na bardziej dogodny.</spoiler>