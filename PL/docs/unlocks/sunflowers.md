# Słoneczniki
[Słoneczniki](objects/sunflower) zbierają energię słoneczną. Możesz zbierać tę energię. 

Sadzenie ich działa dokładnie tak samo, jak sadzenie marchewek czy dyń. 

Zbieranie dojrzałego słonecznika daje energię.
Jeśli na farmie jest co najmniej 10 słoneczników i zbierzesz ten z największą liczbą płatków, otrzymasz `8` razy więcej energii!
Jeśli zbierzesz słonecznik, podczas gdy na farmie jest inny z większą liczbą płatków, następny zebrany słonecznik również da ci tylko normalną ilość energii (bez bonusu 8x).

`measure()` zwraca liczbę płatków słonecznika pod dronem.
Słoneczniki mają co najmniej `7` i co najwyżej `15` płatków.
Można je mierzyć, zanim w pełni dojrzeją.

Kilka słoneczników może mieć taką samą liczbę płatków, więc może być też kilka słoneczników z największą liczbą płatków. W takim przypadku nie ma znaczenia, który z nich zbierzesz.

Dopóki masz energię, dron będzie jej używał, aby działać dwa razy szybciej. 
Zużywa 1 jednostkę energii co 30 akcji (takich jak ruchy, zbiory, sadzenie...)
Wykonywanie innych instrukcji kodu również może zużywać energię, ale znacznie mniej niż akcje drona.

Ogólnie rzecz biorąc, wszystko, co jest przyspieszane przez ulepszenia prędkości, jest również przyspieszane przez energię.
Wszystko, co jest przyspieszane przez energię, zużywa ją proporcjonalnie do czasu potrzebnego na wykonanie, ignorując ulepszenia prędkości.
