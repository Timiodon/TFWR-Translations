# Debug
Manchmal funktioniert dein Code einfach nicht und du musst herausfinden, warum. Es gibt ein paar Werkzeuge, die dir dabei helfen können.

Das erste ist, das Programm Schritt für Schritt auszuführen.  
Du kannst den Schritt-für-Schritt-Modus mit dem Button neben dem Ausführen-Button oder durch Setzen eines Breakpoints aktivieren.

Breakpoints können hinzugefügt werden, indem du auf das Breakpoint-Panel links vom Code klickst.
![](Breakpoints227)
Wenn die Ausführung die Zeile mit dem Breakpoint erreicht, wird automatisch in den Schritt-für-Schritt-Modus gewechselt.

Wenn du deine Maus über eine Variable bewegst, wird ihr aktueller Wert angezeigt.

Die `print()`-Funktion kann ebenfalls sehr nützlich sein. Sie schreibt jeden übergebenen Wert direkt in die Luft.

Beispiele:

"0.24" ausdrucken.
`print(0.24)`

"True" oder "False" ausdrucken.
`print(can_harvest())`

Die aktuelle Position ausdrucken.
`print(get_pos_x(), get_pos_y())`

Die print-Funktion druckt den Wert direkt in die Luft und auf die [Ausgabe](docs/output.md)-Seite.

Das Schreiben in die Luft kann manchmal etwas langsam sein, wenn du viele Werte ausdrucken möchtest. 
In diesem Fall kannst du die `quick_print()`-Funktion verwenden, die nur in das Ausgabe-Fenster druckt.

Das Ausgabefenster protokolliert auch Warnungen und Fehler. Wenn etwas nicht wie erwartet funktioniert, kann es nützlich sein, dort nachzusehen.

Wenn die Ausführung stoppt, wird die Ausgabe auch in die output.txt-Datei im Spielordner geschrieben. [output.txt](persistent_data_path/output.txt).