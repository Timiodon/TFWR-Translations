# Dinosaurier
Dinosaurier sind alte, majestätische Kreaturen, die für antike Knochen gefarmt werden können.

Leider sind Dinosaurier schon vor langer Zeit ausgestorben, also ist das Beste, was wir jetzt tun können, sich als einer zu verkleiden.
Zu diesem Zweck hast du den neuen Dinosaurier-Hut erhalten.

Der Hut kann mit
`change_hat(Hats.Dinosaur_Hat)`
ausgestattet werden.

Leider sieht er nicht ganz so aus wie in der Werbung...

Wenn du den Dinosaurier-Hut trägst und genug Kürbisse hast, wird automatisch ein [apple](objects/apple) gekauft und unter die Drohne platziert.
Wenn die Drohne über einem Apfel steht und sich wieder bewegt, wird sie den Apfel essen und ihr Schwanz wird um eins wachsen. Wenn du es dir leisten kannst, wird ein neuer Apfel gekauft und an einem zufälligen Ort platziert.
Der Apfel kann nicht erscheinen, wenn an der gewünschten Stelle etwas anderes gepflanzt ist.

Der Schwanz des Dinosauriers wird hinter die Drohne gezogen und füllt die vorherigen Felder, über die sich die Drohne bewegt hat. Wenn eine Drohne versucht, auf den Schwanz zu ziehen, wird `move()` scheitern und `False` zurückgeben. 
Das letzte Segment des Schwanzes wird während der Bewegung aus dem Weg geräumt, sodass du darauf ziehen kannst. Wenn die Schlange jedoch die gesamte Farm ausfüllt, kannst du dich nicht mehr bewegen. Du kannst also überprüfen, ob die Schlange vollständig gewachsen ist, indem du feststellst, ob du dich nicht mehr bewegen kannst.

Die Verwendung von `measure()` auf einem Apfel gibt die Position des nächsten Apfels als Tupel zurück.

`next_x, next_y = measure()`

Wenn der Hut durch das Anziehen eines anderen Hutes abgenommen wird, wird der Schwanz geerntet.
Du erhältst Knochen in Höhe der Länge des Schwanzes im Quadrat. Also für einen Schwanz der Länge `n` erhältst du `n**2` `Items.Bone`. 
Zum Beispiel:
Länge 1 => 1 Knochen
Länge 2 => 4 Knochen
Länge 3 => 9 Knochen
Länge 4 => 16 Knochen
Länge 16 => 256 Knochen
Länge 100 => 10000 Knochen

Der Dinosaurier-Hut ist sehr schwer, daher werden bei seiner Ausrüstung 800 Ticks verwendet, anstatt 200. Jedoch wird die Anzahl der Ticks, die `move()` benötigt, jedes Mal um 3% (abgerundet) reduziert, wenn du einen Apfel aufhebst, da ein längerer Schwanz beim Bewegen hilfreich sein kann.

Die folgende Schleife gibt die Anzahl der Ticks an, die von `move()` nach einer beliebigen Anzahl von Äpfeln verwendet werden:

`ticks = 800
for i in range(100):
    print("ticks after ", i, " apples: ", ticks)
    ticks -= ticks * 0.03 // 1`

<spoiler=show hint 1>Wenn du weiterhin denselben Weg gehst, der das ganze Feld abdeckt, kannst du leicht eine Schlange bekommen, die jedes Mal das ganze Feld abdeckt, da du jeden freien Platz abdeckst, bevor du zurück zu deinem Schwanz kommst. Es ist nicht sehr effizient, aber es funktioniert.
Ungewöhnlich große Felder können schwieriger sein. Wenn du `Unlocks.Debug2` freigeschaltet hast, kannst du die Größe des Feldes auf etwas Annehmbareres ändern.</spoiler>