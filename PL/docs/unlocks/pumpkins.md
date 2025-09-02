# Dynie
[Dynie](objects/pumpkin) rosną jak marchewki na zaoranej glebie. Sadzenie ich kosztuje marchewki.

Gdy wszystkie dynie na kwadracie są w pełni wyrośnięte, zrosną się, tworząc gigantyczną dynię. Niestety, dynie mają 20% szansy na obumarcie, gdy są w pełni wyrośnięte, więc będziesz musiał ponownie zasadzić martwe, jeśli chcesz, aby się połączyły. 

Gdy dynia obumrze, pozostawia po sobie martwą dynię, która nic nie da po zebraniu. Posadzenie nowej rośliny na jej miejscu automatycznie usuwa martwą dynię, więc nie trzeba jej zbierać. `can_harvest()` zawsze zwraca `False` na martwych dyniach.

Plon gigantycznej dyni zależy od jej rozmiaru.

Dynia 1x1 daje `1*1*1 = 1` dynię.
Dynia 2x2 daje `2*2*2 = 8` dyń zamiast `4`.
Dynia 3x3 daje `3*3*3 = 27` dyń zamiast `9`.
Dynia 4x4 daje `4*4*4 = 64` dynie zamiast `16`.
Dynia 5x5 daje `5*5*5 = 125` dyń zamiast `25`.
Dynia `n`x`n` daje `n*n*6` dyń dla `n >= 6`.

Dobrym pomysłem jest uzyskanie co najmniej dyni o rozmiarze 6x6, aby uzyskać pełny mnożnik. 

Oznacza to, że nawet jeśli posadzisz dynię na każdym polu w kwadracie, jedna z dyń może obumrzeć i uniemożliwić wzrost mega dyni.