# Mega-Farm
Diese unglaublich mächtige Freischaltung vergrößert die Farm erheblich und gibt dir Zugang zu mehreren Drohnen.

Um die Sache zu vereinfachen, erhältst du für jede neue Drohne immer genau 36 neue Felder. Das Verhältnis von Drohnen zu Feldern bleibt konstant.

## Mehrere Drohnen
Wie zuvor startest du immer noch mit nur einer Drohne. Zusätzliche Drohnen müssen zuerst gespawnt werden und verschwinden nach Beendigung des Programms.
Jede Drohne führt ihre eigene separate Programminstanz aus. Drohnen können neue Drohnen spawnen mit
`new_drone_id = spawn_drone("dateiname")`

Dies spawnt eine neue Drohne an derselben Position wie die Drohne, die den Befehl `spawn_drone("dateiname")` ausgeführt hat. Die neue Drohne beginnt mit der Ausführung des Programms in der Datei namens `dateiname`, ersetze also `"dateiname"` durch den Namen der Datei, die du ausführen möchtest.

Du kannst dir das so vorstellen, als ob du deiner Drohne gesagt hättest, sie solle zur Datei `dateiname` gehen und den Ausführen-Button für die nächste Drohne drücken.

Drohnen kollidieren nicht miteinander.

Benutze `max_drones()`, um die maximale Anzahl von Drohnen zu erhalten, die gespawnt werden können.
Benutze `num_drones()`, um die Anzahl der Drohnen zu erhalten, die bereits auf der Farm sind.
Benutze `get_drone_id()`, um herauszufinden, welche Drohne den Code ausführt.

Beispiel:

In einer Datei namens `farming routine`:
`if get_drone_id() == 0:
    # Nur die erste Drohne führt dies aus
    while num_drones() < max_drones():
        spawn_drone("farming routine")
        move(East)

while True:
    if can_harvest():
        harvest()
    move(North)`

Dies wird dazu führen, dass deine erste Drohne sich horizontal bewegt und mehr Drohnen spawnt. Die gespawnten Drohnen bewegen sich dann vertikal und ernten alles auf ihrem Weg.

<spoiler=Hinweis anzeigen>
Der einfachste Weg, mehrere Drohnen zu verwenden, besteht darin, deine Farm unter ihnen aufzuteilen. Die Upgrades sind so konzipiert, dass jede Drohne immer ein 6x6 Feld haben kann.
</spoiler>

Alles, was hierunter folgt, ist ziemlich fortgeschritten und nicht für das grundlegende Farmen erforderlich.

## Race Conditions
Mehrere Drohnen können gleichzeitig mit demselben Farmfeld interagieren. Wenn zwei Drohnen während desselben Ticks mit demselben Feld interagieren, geschieht die Aktion der Drohne mit der niedrigeren Drohnen-ID zuerst.

Stell dir zum Beispiel vor, dass die Drohnen `0` und `1` beide über demselben Baum stehen, der fast ausgewachsen ist.
Drohne `0` ruft auf
`use_item(Items.Fertilizer)`
Drohne `1` ruft auf
`harvest()`

Wenn diese Aktionen gleichzeitig stattfinden, wird der Baum zuerst gedüngt und dann geerntet. In diesem Fall erhältst du Holz davon. Wenn Drohne `1` jedoch etwas schneller ist, wird der Baum geerntet, bevor er gedüngt wird, und du erhältst kein Holz.
Dies wird als "Race Condition" bezeichnet. Es ist ein häufiges Problem in der parallelen Programmierung, bei dem das Ergebnis von der Reihenfolge abhängt, in der Operationen ausgeführt werden.

Hier ist eine weitere problematische Situation, die auftreten kann, wenn mehrere Drohnen denselben Code gleichzeitig an derselben Position ausführen.
`if get_water() < 0.5:
    use_item(Items.Water)`

Wenn mehrere Drohnen dies gleichzeitig ausführen, führen sie alle die erste Zeile aus, was sie in den `if`-Block bringt. Dann werden sie alle Wasser verwenden und viel davon verschwenden.
Bis eine Drohne die zweite Zeile erreicht, ist `get_water()` möglicherweise nicht mehr kleiner als `0.5`, weil eine andere Drohne das Feld in der Zwischenzeit bewässert hat.

## Drohnen-Kommunikation
Wenn du an fortgeschritteneren Strategien interessiert bist, möchtest du vielleicht, dass deine Drohnen miteinander kommunizieren, indem sie Nachrichten-Passing-Funktionen verwenden.

Sende einen beliebigen Wert an eine andere Drohne:
`send(data, receiver_drone_id)`

Empfange den nächsten von einer beliebigen Drohne gesendeten Wert:
`data = receive()`

Empfange den nächsten von einer bestimmten Drohne gesendeten Wert:
`data = receive(sender_drone_id)`

Die Ausführungszeit von `send()` hängt von der Größe der gesendeten Daten ab. Zum Beispiel erfordert das Senden eines großen Dictionarys das Kopieren, was eine Weile dauern kann.

`receive()` wartet nicht auf das Eintreffen einer Nachricht. Wenn noch keine Nachricht gesendet wurde, gibt es `None` zurück.

Du kannst eine Funktion erstellen, die auf eine Nachricht wartet, so:
`def blocking_receive(sender_drone_id = -1):
    while True:
        data = receive(sender_drone_id)
        if data != None:
            return data`

Eine nützliche Anwendung des Nachrichtenversands ist es, eine Funktion zu haben, die eine Drohne spawnt und ihr eine auszuführende Funktion sendet.
In einer Datei namens `drone_spawning`:
`def run_on_new_drone(f):
    id = spawn_drone("drone_spawning")
    send(f, id)

if __name__ == "__main__":
    f = blocking_receive()
    f()`

Das Senden von Funktionen auf diese Weise kann sehr langsam sein, da der gesamte erfasste Zustand der Funktion, einschließlich aller globalen Variablen, kopiert werden muss.
