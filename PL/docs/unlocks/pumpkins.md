# Dynie
[Dynie](objects/pumpkin) rosną jak marchewki na zaoranej ziemi. Sadzenie ich kosztuje marchewki.

Gdy wszystkie dynie na kwadracie są w pełni wyrośnięte, zrosną się, tworząc gigantyczną dynię. Niestety, dynie mają 20% szans na obumarcie, gdy są w pełni wyrośnięte, więc będziesz musiał ponownie zasadzić te martwe, jeśli chcesz, aby się połączyły.

Gdy dynia umiera, pozostawia po sobie martwą dynię, z której nic nie wypadnie po zebraniu. Zasadzenie nowej rośliny na jej miejscu automatycznie usuwa martwą dynię, więc nie ma potrzeby jej zbierać. `can_harvest()` zawsze zwraca `False` na martwych dyniach.

Plon gigantycznej dyni zależy od jej rozmiaru.

Dyni 1x1 daje `1*1*1 = 1` dyni.
Dyni 2x2 daje `2*2*2 = 8` dyni zamiast `4`.
Dyni 3x3 daje `3*3*3 = 27` dyni zamiast `9`.
Dyni 4x4 daje `4*4*4 = 64` dyni zamiast `16`.
Dyni 5x5 daje `5*5*5 = 125` dyni zamiast `25`.
Dyni `n`x`n` daje `n*n*6` dyni dla `n >= 6`.

Dobrym pomysłem jest uzyskanie dyni o rozmiarze co najmniej 6x6, aby uzyskać pełny mnożnik.

Oznacza to, że nawet jeśli posadzisz dynię na każdym polu w kwadracie, jedna z dyni może umrzeć i uniemożliwić wzrost mega dyni.
