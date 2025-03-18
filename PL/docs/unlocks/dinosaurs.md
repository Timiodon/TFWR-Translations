# Dinozaury
Dinozaury to starożytne, majestatyczne stworzenia, które można uprawiać dla starożytnych kości.

Niestety, dinozaury wymarły już dawno temu, więc najlepiej, co możemy teraz zrobić, to przebrać się za jednego.
W tym celu otrzymałeś nowy kapelusz dinozaura.

Kapelusz można założyć używając
`change_hat(Hats.Dinosaur_Hat)`

Niestety nie wygląda on tak dobrze, jak w reklamie...

Jeśli założysz kapelusz dinozaura i masz wystarczająco dużo dyni, [apple](objects/apple) zostanie automatycznie zakupione i umieszczone pod dronem.
Kiedy dron znajdzie się nad jabłkiem i poruszy się ponownie, zje jabłko i jego ogon wydłuży się o jeden segment. Jeśli cię na to stać, nowe jabłko zostanie zakupione i umieszczone w losowym miejscu.
Jabłko nie może się pojawić, jeśli coś innego jest zasiane w miejscu, gdzie chce być.

Ogon dinozaura będzie ciągnięty za dronem, wypełniając poprzednie pola, po których dron się poruszył. Jeśli dron spróbuje przejść na ogon, `move()` nie powiedzie się i zwróci `False`.
Ostatni segment ogona odsunie się w trakcie ruchu, więc możesz się na niego przemieścić. Jednak jeśli wąż wypełni całe pole, nie będziesz mógł się już więcej poruszać. Możesz sprawdzić, czy wąż jest w pełni rozwinięty, sprawdzając, czy nie możesz się już poruszać.

Użycie `measure()` na jabłku zwróci pozycję następnego jabłka w postaci krotki.

`next_x, next_y = measure()`

Kiedy znowu zdejmiesz kapelusz, zakładając inny kapelusz, ogon zostanie zebrany.
Otrzymasz kości równe długości ogona do kwadratu. Tak więc dla ogona o długości `n` otrzymasz `n**2` `Items.Bone`.
Na przykład:
długość 1 => 1 kość
długość 2 => 4 kości
długość 3 => 9 kości
długość 4 => 16 kości
długość 16 => 256 kości
długość 100 => 10000 kości

Kapelusz Dinozaura jest bardzo ciężki, więc jeśli go założysz, spowoduje, że `move()` będzie trwało 800 ticków zamiast 200. Jednak za każdym razem, gdy podniesiesz jabłko, liczba ticków używanych przez `move()` zmniejszy się o 3% (zaokrąglone w dół), ponieważ dłuższy ogon może ci pomóc w ruchu.

Poniższa pętla wypisuje liczbę ticków używanych przez `move()` po dowolnej liczbie jabłek:

`ticks = 800
for i in range(100):
    print("ticks after ", i, " apples: ", ticks)
    ticks -= ticks * 0.03 // 1`

<spoiler=pokaż wskazówkę 1>Jeśli będziesz poruszać się wzdłuż tej samej ścieżki, która obejmuje całe pole, możesz łatwo uzyskać węża pokrywającego całe pole za każdym razem, ponieważ pokryjesz każdą wolną przestrzeń, zanim wrócisz do miejsca, gdzie jest twój ogon. To nie jest bardzo efektywne, ale działa.
Pola o nieparzystych rozmiarach mogą być trudniejsze. Jeśli masz `Unlocks.Debug2` odblokowane, możesz zmienić rozmiar pola na coś bardziej wygodnego.</spoiler>