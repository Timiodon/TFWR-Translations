# Dinosaurier
Dinosaurier sind uralte, majestätische Kreaturen, die für uralte Knochen gefarmt werden können.

Leider sind Dinosaurier schon vor langer Zeit ausgestorben, also ist das Beste, was wir jetzt tun können, uns als einer zu verkleiden.
Zu diesem Zweck hast du den neuen Dinosaurierhut erhalten.

Der Hut kann ausgerüstet werden mit
`change_hat(Hats.Dinosaur_Hat)`

Leider sieht er nicht ganz so aus wie in der Werbung...

Wenn du den Dinosaurierhut ausrüstest und genug Kürbisse hast, wird automatisch ein [Apfel](objects/apple) gekauft und unter der Drohne platziert.
Wenn die Drohne über einem Apfel ist und sich wieder bewegt, isst sie den Apfel und ihr Schwanz wächst um eins. Wenn du es dir leisten kannst, wird ein neuer Apfel gekauft und an einem zufälligen Ort platziert.
Der Apfel kann nicht spawnen, wenn dort, wo er sein möchte, etwas anderes gepflanzt ist.

Der Schwanz des Dinosauriers wird hinter der Drohne hergezogen und füllt die Felder, über die sich die Drohne zuvor bewegt hat. Wenn eine Drohne versucht, sich auf den Schwanz zu bewegen, schlägt `move()` fehl und gibt `False` zurück. 
Das letzte Segment des Schwanzes wird sich während der Bewegung aus dem Weg bewegen, sodass du dich darauf bewegen kannst. Wenn die Schlange jedoch die ganze Farm ausfüllt, kannst du dich nicht mehr bewegen. Du kannst also prüfen, ob die Schlange ausgewachsen ist, indem du prüfst, ob du dich nicht mehr bewegen kannst.

Die Verwendung von `measure()` auf einen Apfel gibt die Position des nächsten Apfels als Tupel zurück.

`next_x, next_y = measure()`

Wenn der Hut wieder abgelegt wird, indem ein anderer Hut ausgerüstet wird, wird der Schwanz geerntet.
Du erhältst Knochen in Höhe der Schwanzlänge zum Quadrat. Also für einen Schwanz der Länge `n` erhältst du `n**2` `Items.Bone`. 
Zum Beispiel:
Länge 1 => 1 Knochen
Länge 2 => 4 Knochen
Länge 3 => 9 Knochen
Länge 4 => 16 Knochen
Länge 16 => 256 Knochen
Länge 100 => 10000 Knochen

Der Dinosaurierhut ist sehr schwer, also wenn du ihn ausrüstest, wird `move()` 400 Ticks anstelle von 200 dauern. Jedoch wird jedes Mal, wenn du einen Apfel aufhebst, die Anzahl der von `move()` verwendeten Ticks um 3% (abgerundet) reduziert, da ein längerer Schwanz dir bei der Bewegung helfen kann.

Die folgende Schleife gibt die Anzahl der von `move()` verwendeten Ticks nach einer beliebigen Anzahl von Äpfeln aus:

`ticks = 400
for i in range(100):
    print("Ticks nach ", i, " Äpfeln: ", ticks)
    ticks -= ticks * 0.03 // 1`

Du hast nur einen Dinosaurierhut, also kann ihn nur eine Drohne tragen.

<spoiler=zeige Hinweis 1>Wenn du dich immer auf demselben Pfad bewegst, der das ganze Feld abdeckt, kannst du leicht eine Schlange bekommen, die jedes Mal das ganze Feld abdeckt. Es ist nicht sehr effizient, aber es funktioniert.
Eine sehr große Farm vollständig zu durchqueren kann lange dauern, und du brauchst vielleicht gar nicht so viele Knochen. Fühle dich frei, `set_farm_size()` zu verwenden, um die Größe der Farm auf etwas Praktischeres zu ändern.</spoiler>