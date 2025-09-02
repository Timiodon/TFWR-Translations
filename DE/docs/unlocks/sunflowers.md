# Sonnenblumen
[Sonnenblumen](objects/sunflower) sammeln die Energie der Sonne. Du kannst diese Energie ernten. 

Das Pflanzen funktioniert genauso wie bei Karotten oder Kürbissen. 

Das Ernten einer ausgewachsenen Sonnenblume liefert Energie.
Wenn mindestens 10 Sonnenblumen auf der Farm sind und du die mit der größten Anzahl an Blütenblättern erntest, bekommst du `5` mal mehr Energie!

`measure()` gibt die Anzahl der Blütenblätter der Sonnenblume unter der Drohne zurück.
Sonnenblumen haben mindestens `7` und höchstens `15` Blütenblätter.
Sie können bereits gemessen werden, bevor sie vollständig ausgewachsen sind.

Mehrere Sonnenblumen können die gleiche Anzahl an Blütenblättern haben, sodass es auch mehrere Sonnenblumen mit der größten Anzahl an Blütenblättern geben kann. In diesem Fall ist es egal, welche davon du erntest.

Solange du Energie hast, wird die Drohne sie verwenden, um doppelt so schnell zu laufen. 
Sie verbraucht 1 Energie alle 30 Aktionen (wie Bewegungen, Ernten, Pflanzen...)
Das Ausführen anderer Code-Anweisungen kann auch Energie verbrauchen, aber viel weniger als Drohnenaktionen.

Im Allgemeinen wird alles, was durch Geschwindigkeits-Upgrades beschleunigt wird, auch durch Energie beschleunigt.
Alles, was durch Energie beschleunigt wird, verbraucht auch Energie proportional zur Ausführungszeit, wobei Geschwindigkeits-Upgrades ignoriert werden.