# Wczytywanie kopii zapasowych
Niestety, czasami plik zapisu ulega uszkodzeniu lub tracisz niektóre pliki z kodem. Jeśli ci się to przydarzy, możesz spróbować wczytać kopię zapasową. Jeśli zdarza się to regularnie, spróbuj wyłączyć Steam Cloud.

Kopia zapasowa jest tworzona za każdym razem, gdy gra jest zapisywana, a niewielka liczba kopii zapasowych jest przechowywana na wypadek, gdybyś musiał coś przywrócić.
Te kopie zapasowe można znaleźć w [katalogu kopii zapasowych](persistent_data_path/Backup). Są to kopie zapisów z [katalogu zapisów](persistent_data_path/Saves).
Najłatwiejszym sposobem wczytania kopii zapasowej jest skopiowanie folderu konkretnej kopii zapasowej, którą chcesz wczytać, do katalogu zapisów.

Zapis to folder z plikiem `save.json` i kilkoma plikami `.py`.
Jeśli straciłeś tylko kilka plików z kodem lub pliki z kodem wciąż tam są, ale plik `save.json` jest uszkodzony, możesz również zastąpić tylko uszkodzone części odpowiadającymi im plikami z kopii zapasowej.