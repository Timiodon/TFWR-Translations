# Dinosaurier
Dinosaurier sind uralte, majestätische Kreaturen, die für antike Knochen gefarmt werden können.

Leider sind Dinosaurier vor langer Zeit ausgestorben, also ist das Beste, was wir jetzt tun können, uns als einer zu verkleiden.
Zu diesem Zweck hast du den neuen Dinosaurierhut erhalten.

Der Hut kann ausgerüstet werden mit
`change_hat(Hats.Dinosaur_Hat)`

Leider sieht er nicht ganz so aus wie in der Werbung...

Wenn du den Dinosaurierhut ausrüstest und genug Kürbisse hast, wird automatisch ein [Apfel](objects/apple) gekauft und unter der Drohne platziert.
Wenn die Drohne über einem Apfel ist und sich wieder bewegt, isst sie den Apfel und ihr Schwanz wächst um eins. Wenn du es dir leisten kannst, wird ein neuer Apfel gekauft und an einem zufälligen Ort platziert.
Der Apfel kann nicht spawnen, wenn an der Stelle, an der er sein möchte, etwas anderes gepflanzt ist.

Der Schwanz des Dinosauriers wird hinter der Drohne hergezogen und füllt die vorherigen Felder, über die sich die Drohne bewegt hat. Wenn eine Drohne versucht, auf den Schwanz zu fliegen, schlägt `move()` fehl und gibt `False` zurück.
Das letzte Segment des Schwanzes wird während der Bewegung aus dem Weg geräumt, sodass du darauf fahren kannst. Wenn die Schlange jedoch die ganze Farm ausfüllt, kannst du dich nicht mehr bewegen. Du kannst also prüfen, ob die Schlange ausgewachsen ist, indem du prüfst, ob du dich nicht mehr bewegen kannst.

Die Verwendung von `measure()` auf einem Apfel gibt die Position des nächsten Apfels als Tupel zurück.

`next_x, next_y = measure()`

Wenn der Hut wieder abgelegt wird, indem ein anderer Hut ausgerüstet wird, wird der Schwanz geerntet.
Du erhältst Knochen in Höhe der Schwanzlänge im Quadrat. Für einen Schwanz der Länge `n` erhältst du also `n**2` `Items.Bone`.
Zum Beispiel:
Länge 1 => 1 Knochen
Länge 2 => 4 Knochen
Länge 3 => 9 Knochen
Länge 4 => 16 Knochen
Länge 16 => 256 Knochen
Länge 100 => 10000 Knochen

Der Dinosaurierhut ist sehr schwer, wenn du ihn also ausrüstest, dauert `move()` 800 Ticks statt 200. Jedes Mal, wenn du einen Apfel aufhebst, wird die Anzahl der von `move()` verwendeten Ticks um 3 % (abgerundet) reduziert, da ein längerer Schwanz dir helfen kann, dich zu bewegen.

Die folgende Schleife gibt die Anzahl der von `move()` verwendeten Ticks nach einer beliebigen Anzahl von Äpfeln aus:

`ticks = 800
for i in range(100):
    print("ticks nach ", i, " Äpfeln: ", ticks)
    ticks -= ticks * 0.03 // 1`

<spoiler=Hinweis 1 anzeigen>Wenn du dich immer auf demselben Weg bewegst, der das ganze Feld abdeckt, kannst du leicht eine Schlange bekommen, die jedes Mal das ganze Feld abdeckt, weil du jeden freien Platz abdeckst, bevor du dorthin zurückkehrst, wo dein Schwanz ist. Es ist nicht sehr effizient, aber es funktioniert.
Felder mit ungerader Größe können schwieriger sein. Wenn du `Unlocks.Debug2` freigeschaltet hast, kannst du die Größe des Feldes auf etwas Bequemeres ändern.</spoiler>