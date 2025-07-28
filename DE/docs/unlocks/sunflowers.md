# Sonnenblumen
[Sonnenblumen](objects/sunflower) sammeln die Energie der Sonne. Du kannst diese Energie ernten.

Sie zu pflanzen funktioniert genau wie das Pflanzen von Karotten oder Kürbissen.

Das Ernten einer ausgewachsenen Sonnenblume bringt Energie.
Wenn mindestens 10 Sonnenblumen auf der Farm sind und du die mit der größten Anzahl an Blütenblättern erntest, erhältst du `5`-mal mehr Energie!

`measure()` gibt die Anzahl der Blütenblätter der Sonnenblume unter der Drohne zurück.
Sonnenblumen haben mindestens `7` und höchstens `15` Blütenblätter.
Sie können bereits gemessen werden, bevor sie vollständig ausgewachsen sind.

Mehrere Sonnenblumen können die gleiche Anzahl an Blütenblättern haben, daher kann es auch mehrere Sonnenblumen mit der größten Anzahl an Blütenblättern geben. In diesem Fall ist es egal, welche davon du erntest.

Solange du Energie hast, wird die Drohne sie verwenden, um doppelt so schnell zu fliegen.
Sie verbraucht alle 30 Aktionen 1 Energie (wie Bewegungen, Ernten, Pflanzen...)
Das Ausführen anderer Code-Anweisungen kann auch Energie verbrauchen, aber viel weniger als Drohnen-Aktionen.

Im Allgemeinen wird alles, was durch Geschwindigkeits-Upgrades beschleunigt wird, auch durch Energie beschleunigt.
Alles, was durch Energie beschleunigt wird, verbraucht auch Energie proportional zur Ausführungszeit, wobei Geschwindigkeits-Upgrades ignoriert werden.