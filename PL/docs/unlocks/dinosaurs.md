# Dinozaury
Dinozaury to starożytne, majestatyczne stworzenia, które można hodować dla starożytnych kości.

Niestety dinozaury wyginęły dawno temu, więc najlepsze co możemy teraz zrobić, to przebrać się za jednego.
W tym celu otrzymałeś nowy kapelusz dinozaura.

Kapelusz można założyć za pomocą
`change_hat(Hats.Dinosaur_Hat)`

Niestety nie wygląda on tak jak na reklamie...

Jeśli założysz kapelusz dinozaura i będziesz miał wystarczająco dużo dyń, [jabłko](objects/apple) zostanie automatycznie zakupione i umieszczone pod dronem.
Gdy dron znajdzie się nad jabłkiem i ponownie się poruszy, zje jabłko, a jego ogon urośnie o jeden. Jeśli cię na to stać, nowe jabłko zostanie zakupione i umieszczone w losowej lokalizacji.
Jabłko nie może się pojawić, jeśli w miejscu, w którym chce się pojawić, jest już coś posadzone.

Ogon dinozaura będzie ciągnął się za dronem, wypełniając poprzednie pola, po których poruszał się dron. Jeśli dron spróbuje wejść na ogon, `move()` zakończy się niepowodzeniem i zwróci `False`.
Ostatni segment ogona usunie się z drogi podczas ruchu, więc możesz na niego wejść. Jednak jeśli wąż wypełni całą farmę, nie będziesz mógł się już poruszać. Możesz więc sprawdzić, czy wąż jest w pełni wyrośnięty, sprawdzając, czy nie możesz się już poruszać.

Użycie `measure()` na jabłku zwróci pozycję następnego jabłka jako krotkę.

`next_x, next_y = measure()`

Gdy kapelusz zostanie ponownie zdjęty przez założenie innego kapelusza, ogon zostanie zebrany.
Otrzymasz kości równe kwadratowi długości ogona. Czyli za ogon o długości `n` otrzymasz `n**2` `Items.Bone`.
Na przykład:
długość 1 => 1 kość
długość 2 => 4 kości
długość 3 => 9 kości
długość 4 => 16 kości
długość 16 => 256 kości
długość 100 => 10000 kości

Kapelusz Dinozaura jest bardzo ciężki, więc jeśli go założysz, `move()` będzie zajmować 800 ticks zamiast 200. Jednak za każdym razem, gdy podniesiesz jabłko, liczba ticks używanych przez `move()` jest zmniejszana o 3% (zaokrąglone w dół), ponieważ dłuższy ogon może pomóc ci się poruszać.

Poniższa pętla drukuje liczbę ticks używanych przez `move()` po dowolnej liczbie jabłek:

`ticks = 800
for i in range(100):
    print("ticks po ", i, " jabłkach: ", ticks)
    ticks -= ticks * 0.03 // 1`

<spoiler=pokaż wskazówkę 1>Jeśli będziesz poruszać się tą samą ścieżką, która pokrywa całe pole, możesz łatwo uzyskać węża, który za każdym razem pokrywa całe pole, ponieważ pokryjesz każde wolne miejsce, zanim wrócisz tam, gdzie jest twój ogon. Nie jest to bardzo wydajne, ale działa.
Nieparzyste rozmiary pól mogą być trudniejsze. Jeśli masz odblokowane `Unlocks.Debug2`, możesz zmienić rozmiar pola na coś wygodniejszego.</spoiler>