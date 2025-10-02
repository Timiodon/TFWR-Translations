# Dinozaury
Dinozaury to starożytne, majestatyczne stworzenia, które można hodować dla starożytnych kości.

Niestety dinozaury wyginęły dawno temu, więc najlepsze, co możemy teraz zrobić, to przebrać się za jednego.
W tym celu otrzymałeś nowy kapelusz dinozaura.

Kapelusz można założyć za pomocą
`change_hat(Hats.Dinosaur_Hat)`

Niestety nie wygląda on tak jak na reklamie...

Jeśli założysz kapelusz dinozaura i masz wystarczająco dużo dyń, [jabłko](objects/apple) zostanie automatycznie zakupione i umieszczone pod dronem.
Gdy dron znajdzie się nad jabłkiem i ponownie się poruszy, zje jabłko i jego ogon urośnie o jeden. Jeśli cię na to stać, nowe jabłko zostanie zakupione i umieszczone w losowej lokalizacji.
Jabłko nie może się pojawić, jeśli coś innego jest posadzone tam, gdzie chce być.

Ogon dinozaura będzie ciągnięty za dronem, wypełniając poprzednie pola, nad którymi poruszał się dron. Jeśli dron spróbuje wejść na ogon, `move()` nie powiedzie się i zwróci `False`. 
Ostatni segment ogona usunie się z drogi podczas ruchu, więc możesz na niego wejść. Jednakże, jeśli wąż wypełni całą farmę, nie będziesz mógł się już poruszyć. Możesz więc sprawdzić, czy wąż jest w pełni wyrośnięty, sprawdzając, czy nie możesz się już poruszyć.

Użycie `measure()` na jabłku zwróci pozycję następnego jabłka jako krotkę.

`next_x, next_y = measure()`

Gdy kapelusz zostanie ponownie zdjęty przez założenie innego kapelusza, ogon zostanie zebrany.
Otrzymasz kości równe długości ogona do kwadratu. Więc za ogon o długości `n` otrzymasz `n**2` `Items.Bone`. 
Na przykład:
długość 1 => 1 kość
długość 2 => 4 kości
długość 3 => 9 kości
długość 4 => 16 kości
długość 16 => 256 kości
długość 100 => 10000 kości

Kapelusz dinozaura jest bardzo ciężki, więc jeśli go założysz, wykonanie `move()` zajmie 400 ticków zamiast 200. Jednak za każdym razem, gdy podniesiesz jabłko, liczba ticków używanych przez `move()` jest zmniejszana o 3% (zaokrąglone w dół), ponieważ dłuższy ogon może pomóc w poruszaniu się.

Poniższa pętla wyświetla liczbę ticków używanych przez `move()` po dowolnej liczbie jabłek:

`ticks = 400
for i in range(100):
    print("ticki po ", i, " jabłkach: ", ticks)
    ticks -= ticks * 0.03 // 1`

Masz tylko jeden kapelusz dinozaura, więc tylko jeden dron może go nosić.

<spoiler=pokaż podpowiedź 1>Jeśli będziesz poruszać się po tej samej ścieżce, która obejmuje całe pole, możesz łatwo uzyskać węża, który za każdym razem obejmuje całe pole. Nie jest to bardzo wydajne, ale działa.
Pełne przemierzenie bardzo dużej farmy może zająć dużo czasu i być może nie potrzebujesz aż tylu kości. Możesz użyć `set_world_size()`, aby zmienić rozmiar farmy na coś bardziej wygodnego.</spoiler>