# Debug
Manchmal funktioniert dein Code einfach nicht und du musst herausfinden, warum. Es gibt ein paar Werkzeuge, die dir dabei helfen.

Das erste ist, das Programm Schritt für Schritt auszuführen.
Du kannst mit dem Button neben dem Ausführen-Button oder durch Setzen eines Haltepunkts in den Schritt-für-Schritt-Modus wechseln.

Haltepunkte können hinzugefügt werden, indem du auf das Haltepunkt-Panel links vom Code klickst.
![](Breakpoints227)
Wenn die Ausführung die Zeile erreicht, in der sich der Haltepunkt befindet, wechselt sie automatisch in den Schritt-für-Schritt-Modus.

Wenn du mit der Maus über eine Variable fährst, wird ihr aktueller Wert angezeigt.

Die `print()`-Funktion kann auch sehr nützlich sein. Sie schreibt jeden an sie übergebenen Wert direkt in die Luft.

Beispiele:

Gib "0.24" aus.
`print(0.24)`

Gib "True" oder "False" aus.
`print(can_harvest())`

Gib die aktuelle Position aus.
`print(get_pos_x(), get_pos_y())`

Die `print`-Funktion gibt den Wert direkt in die Luft und auf die [Ausgabe](docs/output.md)-Seite aus.

Das Schreiben in die Luft kann manchmal etwas langsam sein, wenn du viele Werte ausgeben möchtest.
In diesem Fall kannst du die `quick_print()`-Funktion verwenden, die nur in das Ausgabefenster schreibt.

Das Ausgabefenster protokolliert auch Warnungen und Fehler. Wenn also etwas nicht wie erwartet funktioniert, kann es nützlich sein, das zu überprüfen.

Wenn die Ausführung stoppt, wird die Ausgabe auch in die Datei output.txt im Spielordner geschrieben. [output.txt](persistent_data_path/output.txt).