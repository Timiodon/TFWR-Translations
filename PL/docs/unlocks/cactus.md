# Kaktus
Podobnie jak inne rośliny, [kaktusy](objects/cactus) można uprawiać na glebie i zbierać jak zwykle.

Jednak występują w różnych rozmiarach i mają dziwne poczucie porządku.

Jeśli zbierzesz w pełni wyrośniętego kaktusa, a wszystkie sąsiednie kaktusy są posortowane, zostaną one również zebrane rekurencyjnie.

Kaktus jest uważany za posortowany, jeśli wszystkie sąsiednie kaktusy na `North` i `East` są w pełni wyrośnięte i mają większy lub równy rozmiar, a wszystkie sąsiednie kaktusy na `South` i `West` są w pełni wyrośnięte i mają mniejszy lub równy rozmiar.

Zbiór rozprzestrzeni się tylko wtedy, gdy wszystkie sąsiednie kaktusy będą w pełni wyrośnięte i posortowane.
Oznacza to, że jeśli kwadrat wyrośniętych kaktusów jest posortowany według rozmiaru i zbierzesz jednego kaktusa, zbierze on cały kwadrat.

W pełni wyrośnięty kaktus będzie brązowy, jeśli nie jest posortowany. Po posortowaniu ponownie stanie się zielony.

Otrzymasz kaktusy w liczbie równej kwadratowi liczby zebranych kaktusów. Więc jeśli zbierzesz `n` kaktusów jednocześnie, otrzymasz `n**2` `Items.Cactus`.

Rozmiar kaktusa można zmierzyć za pomocą `measure()`.
Jest to zawsze jedna z tych liczb: `0,1,2,3,4,5,6,7,8,9`.

Możesz również przekazać kierunek do `measure(direction)`, aby zmierzyć sąsiednie pole w tym kierunku od drona.

Możesz zamienić kaktusa z jego sąsiadem w dowolnym kierunku za pomocą polecenia `swap()`.
`swap(direction)` zamienia obiekt pod dronem z obiektem o jedno pole w `direction` od drona.

## Przykłady
W każdej z tych siatek wszystkie kaktusy są posortowane, a zbiór rozprzestrzeni się na całe pole:
`3 4 5    3 3 3    1 2 3    1 5 9
2 3 4    2 2 2    1 2 3    1 3 8
1 2 3    1 1 1    1 2 3    1 3 4`

W tej siatce tylko lewy dolny kaktus jest posortowany, co nie wystarcza do rozprzestrzenienia się:
`1 5 3
4 9 7
3 3 2`

<spoiler=pokaż wskazówkę 1>
Jeśli wiersze są już posortowane, sortowanie kolumn nie zepsuje porządku w wierszach.
</spoiler>
<spoiler=pokaż wskazówkę 2>
Jeśli nie znasz algorytmów sortowania, możesz poszukać ich w Internecie i zastanowić się, które można by zaadaptować do tego problemu. Pamiętaj, że nie wszystkie działają, ponieważ możesz zamieniać tylko sąsiednie kaktusy.
</spoiler>