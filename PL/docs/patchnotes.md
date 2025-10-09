# Nareszcie 1.0!
Po ponad trzech i pół roku ciągłego rozwoju, ponad 20 aktualizacjach i waszych niesamowitych opiniach, Wczesny Dostęp wreszcie dobiegł końca.

## Co nowego w 1.0?
- Wiele dronów, aby zmaksymalizować wydajność farmy
- Przerobione drzewko odblokowań z bardziej wykładniczym postępem
- 60 osiągnięć, aby sprawdzić swoje umiejętności
- Odblokowanie niektórych osiągnięć da twojemu dronowi specjalne kapelusze
- Całkowicie przerobiony dźwięk
- Jeden nowy utwór muzyczny
- Ulepszenia jakości gry i różne poprawki
- Ważne zmiany: Ulepszenia zostaną częściowo zresetowane. Ponowne używanie labiryntów działa nieco inaczej.

Bardzo wam wszystkim dziękuję za wspieranie The Farmer Was Replaced od Wczesnego Dostępu aż do pełnego wydania. 
Nie mogę się doczekać, aby zobaczyć, jak wykorzystacie wiele dronów w kreatywny i sprytny sposób!
-Timon

Pamiętajcie też, aby dołączyć do nas na Discordzie: 
[Discord](https://discord.com/invite/kj33cJkeJn)

## Pełna lista zmian
Ważne zmiany:
-Z powodu przeróbki drzewka technologicznego, liczby ulepszeń w starych zapisach gry nie będą już ważne. Gra zresetuje wszystkie ulepszenia do rozsądnego poziomu po otwarciu starego zapisu.
-Jeśli ponownie używasz labiryntów, musisz teraz najpierw zmienić pozycję skarbu, a potem zmierzyć pozycję, zamiast najpierw mierzyć, a potem zmieniać pozycję.

Rozgrywka:
-Dodano podpowiedzi z przydatnymi informacjami po najechaniu na pola na farmie.
-Użycie `measure()` w dowolnym miejscu labiryntu teraz zawsze zwraca pozycję obecnego skarbu. Nie musisz już mierzyć konkretnie skarbu.
-Dla labiryntu jest teraz dostępna funkcja `can_move()`.
-Dynie skalują się teraz do 6x6 zamiast 5x5.
-Zachowanie wysychania ziemi nieznacznie się zmieniło. Zamiast wysychać o 1% co 0.8 do 1.2 sekundy, każde pole ma teraz 10% szansy na wyschnięcie co 0.1 sekundy.
-Czas wzrostu kaktusa wynosi teraz zawsze dokładnie 1 sekundę.
-Dynie pozostawiają teraz po sobie martwą dynię, aby zasygnalizować, że obumarły.
-Dodano `pet_the_piggy()`.
-`num_unlocked()` jest teraz odblokowywane już wraz ze Zmysłami.

Dźwięk:
-Dźwięk został całkowicie przerobiony.
-Jest teraz muzyka po uruchomieniu gry!

Grafika:
-Wygląd drzewka technologicznego został całkowicie przerobiony.
-Panel ekwipunku w lewym górnym rogu ekranu ma teraz ładny efekt wizualny podnoszenia przedmiotów.
-Kaktusy są teraz brązowe, gdy nie są poprawnie posortowane, aby było to bardziej widoczne.
-Rośliny są teraz widoczne natychmiast po posadzeniu, nawet jeśli jeszcze nie urosły.

Edytor kodu:
-Podwójne kliknięcie identyfikatorów z podkreśleniami zaznacza teraz cały identyfikator.
-Jeśli opcja „tabulatory na spacje” jest wyłączona, spacje wcięć są teraz konwertowane na tabulatory.
-Powiększanie jest teraz znacznie płynniejsze.
-Uzupełnianie kodu jest teraz świadome importów i może podawać sugestie z innych plików.
-Dodano różne kursory do edycji tekstu i zmiany rozmiaru okien.
-Kroki debugera są teraz oparte na linii kodu, a nie na tickach symulacji.

Inne:
-Można teraz łączyć operatory porównania, tak jak w Pythonie.
-`get_cost(Entities.Hedge)` i `get_cost(Entities.Treasure)` zwracają teraz koszt labiryntu 1x1.
-Dodano ustawienie rozdzielczości.
-Dodano ustawienie wyłączające migające podświetlenia podczas działania kodu.
-Wykonywanie kodu zostało dodatkowo zoptymalizowane, co pozwala na płynniejsze działanie gry podczas działania kodu.
-Dodano skrót klawiszowy „Przełącz HUD”.

Poprawki:
-Naprawiono niektóre z najczęstszych przypadków, w których podświetlenia kodu były widoczne przez inne okna.
-Działania takie jak orka nie mogą już wpływać na zachowanie wysychania wody.
-Naprawiono problemy ze skrótami klawiszowymi na klawiaturach innych niż amerykańskie.
-Naprawiono skarbonkę, która czasami oddalała się bardzo daleko od farmy.
-Naprawiono problem z nawozem, który nie rozprzestrzeniał się na w pełni wyrośnięte rośliny.
-Naprawiono resetowanie pozycji drona przez `set_world_size(get_world_size())`.
-Naprawiono interakcję symulacji i dinozaura, która powodowała pozostawianie dużej ilości jabłek.
-Naprawiono błąd, który powodował przesuwanie się komunikatów o błędach po kliknięciu minimalizacji, a następnie otwarciu menu.
-Naprawiono komunikaty o błędach pojawiające się podczas pisania.

Ważne zmiany z poprzednich patchy, które mogłeś przegapić:
-Funkcje zdefiniowane w innych plikach (oknach w grze) nie są już importowane niejawnie. Musisz teraz odblokować i używać jawnych instrukcji importu, tak jak w Pythonie (zobacz odblokowanie importu).
-`Items.Bones` zostało zmienione na `Items.Bone`, aby wszystkie przedmioty były w liczbie pojedynczej.
-`Entities.Carrots` zostało zmienione na `Entities.Carrot`, aby wszystkie obiekty były w liczbie pojedynczej.
-`Grounds.Turf` zostało zmienione na `Grounds.Grassland`, aby było łatwiejsze do zrozumienia.
-`Items.Water_Tank` zostało zmienione na `Items.Water`, ponieważ funkcja napełniania zbiornika została usunięta.
-`Unlocks.Benchmark` zostało zastąpione przez `Unlocks.Timing`.
-`get_op_count()` zostało zmienione na `get_tick_count()`.
-`set_farm_size()` zostało zmienione na `set_world_size()`, aby było spójne z `get_world_size()`.
-`get_companion()` zwraca teraz krotkę w formie (obiekt, (x, y)) zamiast listy.
-`trade()` zostało usunięte z gry.