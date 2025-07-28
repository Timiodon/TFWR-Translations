# Mega Farma
To niezwykle potężne odblokowanie znacznie zwiększa rozmiar farmy i daje dostęp do wielu dronów.

Aby ułatwić sprawę, zawsze otrzymujesz dokładnie 36 nowych pól na każdego nowego drona. Stosunek dronów do pól pozostaje stały.

## Wiele Dronów
Jak poprzednio, nadal zaczynasz z jednym dronem. Dodatkowe drony muszą najpierw zostać stworzone i znikną po zakończeniu programu.
Każdy dron uruchamia własną, oddzielną instancję programu. Drony mogą tworzyć nowe drony za pomocą
`new_drone_id = spawn_drone("nazwa_pliku")`

Tworzy to nowego drona w tej samej pozycji co dron, który uruchomił polecenie `spawn_drone("nazwa_pliku")`. Nowy dron rozpocznie wykonywanie programu z pliku o nazwie `nazwa_pliku`, więc zastąp `"nazwa_pliku"` nazwą pliku, który chcesz uruchomić.

Możesz o tym myśleć, jakbyś powiedział swojemu dronowi, aby poszedł do pliku o nazwie `nazwa_pliku` i nacisnął przycisk wykonania dla następnego drona.

Drony nie zderzają się ze sobą.

Użyj `max_drones()`, aby uzyskać maksymalną liczbę dronów, które można stworzyć.
Użyj `num_drones()`, aby uzyskać liczbę dronów, które już są na farmie.
Użyj `get_drone_id()`, aby dowiedzieć się, który dron wykonuje kod.

Przykład:

W pliku o nazwie `farming routine`:
`if get_drone_id() == 0:
    # Tylko pierwszy dron to uruchomi
    while num_drones() < max_drones():
        spawn_drone("farming routine")
        move(East)

while True:
    if can_harvest():
        harvest()
    move(North)`

Spowoduje to, że twój pierwszy dron będzie poruszał się poziomo i tworzył więcej dronów. Stworzone drony będą następnie poruszać się pionowo i zbierać wszystko na swojej drodze.

<spoiler=pokaż wskazówkę>
Najprostszym sposobem na użycie wielu dronów jest podzielenie farmy między nimi. Ulepszenia są zaprojektowane tak, aby każdy dron zawsze mógł mieć pole 6x6.
</spoiler>

Wszystko poniżej jest dość zaawansowane i nie jest wymagane do podstawowej uprawy

## Race Conditions
Wiele dronów może oddziaływać na to samo pole farmy w tym samym czasie. Jeśli dwa drony oddziałują na to samo pole w dokładnie tym samym ticku, akcja drona o niższym ID drona wykona się jako pierwsza.

Na przykład, wyobraź sobie, że drony `0` i `1` są oba nad tym samym drzewem, które jest prawie w pełni wyrośnięte.
Dron `0` wywołuje
`use_item(Items.Fertilizer)`
Dron `1` wywołuje
`harvest()`

Jeśli te akcje wystąpią w tym samym czasie, drzewo zostanie najpierw nawożone, a następnie zebrane. W takim przypadku otrzymasz z niego drewno. Jednak jeśli Dron `1` jest nieco szybszy, drzewo zostanie zebrane, zanim zostanie nawożone, i nie otrzymasz drewna.
Nazywa się to "race condition". Jest to powszechny problem w programowaniu równoległym, gdzie wynik zależy od kolejności, w jakiej wykonywane są operacje.

Oto kolejna problematyczna sytuacja, która może się zdarzyć, gdy wiele dronów uruchamia ten sam kod jednocześnie w tej samej pozycji.
`if get_water() < 0.5:
    use_item(Items.Water)`

Jeśli wiele dronów uruchomi to jednocześnie, wszystkie wykonają pierwszą linię, co umieści je w bloku `if`. Następnie wszystkie użyją wody, marnując jej dużo.
Zanim dron dotrze do drugiej linii, `get_water()` może już nie być mniejsze niż `0.5`, ponieważ inny dron w międzyczasie podlał pole.

## Komunikacja między dronami
Jeśli interesują Cię bardziej zaawansowane strategie, możesz chcieć, aby Twoje drony komunikowały się ze sobą za pomocą funkcji przekazywania wiadomości.

Wyślij dowolną wartość do innego drona:
`send(data, receiver_drone_id)`

Odbierz następną wartość wysłaną przez dowolnego drona:
`data = receive()`

Odbierz następną wartość wysłaną przez konkretnego drona:
`data = receive(sender_drone_id)`

Czas wykonania `send()` zależy od rozmiaru wysyłanych danych. Na przykład, wysłanie dużego słownika wymaga kopiowania, co może zająć chwilę.

`receive()` nie czeka na nadejście wiadomości. Jeśli żadna wiadomość nie została jeszcze wysłana, zwróci `None`.

Możesz zbudować funkcję, która czeka na wiadomość, w ten sposób:
`def blocking_receive(sender_drone_id = -1):
    while True:
        data = receive(sender_drone_id)
        if data != None:
            return data`

Jednym z użytecznych zastosowań przekazywania wiadomości jest posiadanie funkcji, która tworzy drona i wysyła mu funkcję do wykonania.
W pliku o nazwie `drone_spawning`:
`def run_on_new_drone(f):
    id = spawn_drone("drone_spawning")
    send(f, id)

if __name__ == "__main__":
    f = blocking_receive()
    f()`

Wysyłanie funkcji w ten sposób może być bardzo powolne, ponieważ cały przechwycony stan funkcji, w tym wszystkie zmienne globalne, musi zostać skopiowany.
