# Sonnenblumen
[Sonnenblumen](objects/sunflower) sammeln die Energie der Sonne. Du kannst diese Energie ernten.

Das Pflanzen funktioniert genau wie das Pflanzen von Karotten oder Kürbissen.

Das Ernten einer ausgewachsenen Sonnenblume liefert Energie.
Wenn es mindestens 10 Sonnenblumen auf dem Hof gibt und du die mit der größten Anzahl an Blütenblättern erntest, bekommst du `5`-mal mehr Energie!

`measure()` gibt die Anzahl der Blütenblätter der Sonnenblume unter der Drohne zurück.
Sonnenblumen haben mindestens `7` und höchstens `15` Blütenblätter.
Sie können schon gemessen werden, bevor sie vollständig ausgewachsen sind.

Mehrere Sonnenblumen können die gleiche Anzahl an Blütenblättern haben, sodass es auch mehrere Sonnenblumen mit der größten Anzahl an Blütenblättern geben kann. In diesem Fall ist es egal, welche du erntest.

Solange du Energie hast, wird die Drohne diese nutzen, um doppelt so schnell zu arbeiten.
Sie verbraucht 1 Energie alle 30 Aktionen (wie Bewegungen, Ernten, Pflanzen...).
Das Ausführen anderer Code-Anweisungen kann ebenfalls Energie verbrauchen, aber viel weniger als Drohnenaktionen.

Generell wird alles, was durch Geschwindigkeits-Upgrades beschleunigt wird, auch durch Energie beschleunigt.
Alles, was durch Energie beschleunigt wird, verbraucht auch Energie proportional zur Ausführungszeit, unabhängig von Geschwindigkeits-Upgrades.