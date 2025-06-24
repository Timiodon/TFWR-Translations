# Mega Farm
To niesamowicie potężne odblokowanie znacząco zwiększa rozmiar farmy i daje ci dostęp do wielu dronów.

Aby ułatwić sprawę, zawsze otrzymujesz dokładnie 36 nowych płytek na każdego nowego drona. Stosunek dronów do płytek pozostaje stały.

## Wielokrotne drony
Jak wcześniej, nadal zaczynasz z jednym dronem. Dodatkowe drony muszą najpierw zostać spawnowane i znikną po zakończeniu programu.
Każdy dron uruchamia swoją własną, oddzielną instancję programu. Drony mogą spawnować nowe drony używając
`new_drone_id = spawn_drone("filename")`

To spawnuje nowego drona w tej samej pozycji, co dron, który wykonał komendę `spawn_drone("filename")`. Nowy dron rozpocznie wykonywanie się programu w pliku o nazwie `filename`, więc zastąp `"filename"` nazwą pliku, który chcesz uruchomić.

Możesz myśleć o tym jak o nakazaniu swojemu dronowi, aby poszedł do pliku o nazwie `filename` i kliknął przycisk uruchamiania dla kolejnego drona.

Drony nie kolidują ze sobą.

Użyj `max_drones()`, aby sprawdzić maksymalną liczbę dronów, które można spawnować.
Użyj `num_drones()`, aby sprawdzić, ile dronów już jest na farmie.
Użyj `get_drone_id()`, aby dowiedzieć się, który dron wykonuje kod.

Przykład:

W pliku o nazwie `farming routine`:
`if get_drone_id() == 0:
    # Tylko pierwszy dron to wykona
    while num_drones() < max_drones():
        spawn_drone("farming routine")
        move(East)`

while True:
    if can_harvest():
        harvest()
    move(North)`

To spowoduje, że twój pierwszy dron będzie poruszał się poziomo i spawnował więcej dronów. Spawnowane drony będą się przemieszczać pionowo i zbierać wszystko na swojej drodze.

<spoiler=rozwiń wskazówkę>Najłatwiejszy sposób na użycie wielu dronów to podzielić farmę między nimi. Ulepszenia są zaprojektowane tak, aby każdy dron miał zawsze pole 6x6.
</spoiler>

### Wszystko poniżej jest dość zaawansowane i nie jest wymagane do podstawowego rolnictwa

## Warunki wyścigu
Wiele dronów może wchodzić w interakcję z tą samą płytką farmy jednocześnie. Jeśli dwa drony wchodzą w interakcję z tą samą płytką w dokładnie tym samym ticku, akcja drona o niższym ID będzie wykonana jako pierwsza.

Na przykład, wyobraź sobie, że drony `0` i `1` są nad tym samym drzewem, które prawie urosło.
Dron `0` wywołuje
`use_item(Items.Fertilizer)`
Dron `1` wywołuje
`harvest()`

Jeśli te akcje występują jednocześnie, drzewo najpierw zostanie użyźnione, a potem zebrane. W tym przypadku dostaniesz drewno z niego. Jednakże, jeśli Dron `1` jest trochę szybszy, drzewo zostanie zebrane przed użyźnieniem i nie dostaniesz drewna.
To nazywa się "warunkiem wyścigu". Jest to powszechny problem w programowaniu równoległym, gdzie wynik zależy od kolejności wykonywania operacji.

Oto inna problematyczna sytuacja, która może się zdarzyć, gdy wiele dronów wykonuje ten sam kod równocześnie w tej samej pozycji.
`if get_water() < 0.5:
    use_item(Items.Water)`

Jeśli wiele dronów uruchomi to jednocześnie, wszystkie uruchomią pierwszą linię, co umieszcza je w bloku `if`. Następnie wszystkie użyją wody, marnując jej dużo.
Zanim dron osiągnie drugą linię, `get_water()` może już nie być mniejszy niż `0.5`, ponieważ inny dron nawodnił płytkę w międzyczasie.

## Komunikacja dronów
Jeśli interesują cię bardziej zaawansowane strategie, możesz chcieć, aby twoje drony komunikowały się między sobą za pomocą funkcji przesyłania wiadomości.

Wyślij dowolną wartość do innego drona:
`send(data, receiver_drone_id)`

Odbierz następną wartość wysłaną przez dowolnego drona:
`data = receive()`

Odbierz następną wartość wysłaną przez konkretnego drona:
`data = receive(sender_drone_id)`

Czas wykonania `send()` zależy od rozmiaru przesyłanych danych. Na przykład, przesłanie dużego dictionary wymaga kopiowania, co może zająć trochę czasu.

`receive()` nie czeka na przybycie wiadomości. Jeśli żadna wiadomość nie została jeszcze wysłana, zwróci `None`.

Możesz stworzyć funkcję, która czeka na wiadomość w ten sposób:
`def blocking_receive(sender_drone_id = -1):
    while True:
        data = receive(sender_drone_id)
        if data != None:
            return data`

Jednym z przydatnych zastosowań przekazywania wiadomości jest stworzenie funkcji, która spawnuje drona i wysyła mu funkcję do wykonania.
W pliku o nazwie `drone_spawning`:
`def run_on_new_drone(f):
    id = spawn_drone("drone_spawning")
    send(f, id)

if __name__ == "__main__":
    f = blocking_receive()
    f()`

Przesyłanie funkcji w ten sposób może być bardzo wolne, ponieważ cały przechwycony stan funkcji, w tym wszystkie globalne zmienne, musi być skopiowany.