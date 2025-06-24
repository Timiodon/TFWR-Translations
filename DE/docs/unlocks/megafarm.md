# Mega Farm
Diese unglaublich mächtige Freischaltung vergrößert die Farm erheblich und gibt dir Zugang zu mehreren Drohnen.

Um es einfacher zu machen, bekommst du immer genau 36 neue Felder für jede neue Drohne. Das Verhältnis von Drohnen zu Feldern bleibt konstant.

## Mehrere Drohnen
Wie zuvor startest du immer noch mit nur einer Drohne. Zusätzliche Drohnen müssen zuerst gespawnt werden und verschwinden nach dem Ende des Programms.
Jede Drohne führt ihr eigenes separates Programm aus. Drohnen können neue Drohnen mit
`new_drone_id = spawn_drone("filename")`
spawnen.

Dies spawnt eine neue Drohne an derselben Position wie die Drohne, die den Befehl `spawn_drone("filename")` ausgeführt hat. Die neue Drohne startet das Programm in der Datei mit dem Namen `filename`, ersetze also `"filename"` mit dem Namen der Datei, die du ausführen möchtest.

Du kannst dir das so vorstellen, als ob du deiner Drohne gesagt hast, sie solle zur Datei `filename` gehen und auf den Ausführen-Knopf für die nächste Drohne klicken.

Drohnen kollidieren nicht miteinander.

Verwende `max_drones()`, um die maximale Anzahl von Drohnen zu erfahren, die gespawnt werden können.
Verwende `num_drones()`, um die Anzahl der Drohnen zu erfahren, die bereits auf der Farm sind.
Verwende `get_drone_id()`, um herauszufinden, welche Drohne den Code ausführt.

Beispiel:

In einer Datei namens `farming routine`:
`if get_drone_id() == 0:
    # Nur die erste Drohne wird dies ausführen
    while num_drones() < max_drones():
        spawn_drone("farming routine")
        move(East)`

while True:
    if can_harvest():
        harvest()
    move(North)`

Dies wird dazu führen, dass deine erste Drohne horizontal bewegt wird und mehr Drohnen spawnt. Die gespaunten Drohnen werden sich dann vertikal bewegen und alles auf ihrem Weg ernten.

<spoiler=Tipp anzeigen>Der einfachste Weg, mehrere Drohnen zu verwenden, besteht darin, deine Farm unter ihnen aufzuteilen. Die Upgrades sind so gestaltet, dass jede Drohne immer ein 6x6 Feld haben kann.</spoiler>

### Alles, was hier drunter steht, ist ziemlich fortgeschritten und nicht für die grundlegende Landwirtschaft erforderlich

## Race Conditions
Mehrere Drohnen können gleichzeitig mit demselben Farmfeld interagieren. Wenn zwei Drohnen zur exakt gleichen Tick-Zeit mit demselben Feld interagieren, wird die Aktion der Drohne mit der niedrigeren Drohnen-ID zuerst ausgeführt.

Beispielsweise stell dir vor, dass Drohnen `0` und `1` über demselben Baum stehen, der fast ausgewachsen ist.
Drohe `0` ruft
`use_item(Items.Fertilizer)`
an
Drohe `1` ruft
`harvest()`
an

Wenn diese Aktionen gleichzeitig auftreten, wird der Baum zuerst gedüngt und dann geerntet. In diesem Fall erhältst du Holz davon. Wenn jedoch Drohe `1` etwas schneller ist, wird der Baum geerntet, bevor er gedüngt wird, und du erhältst das Holz nicht.
Dies nennt man eine "Race Condition". Es ist ein häufig auftretendes Problem in der parallelen Programmierung, bei dem das Ergebnis davon abhängt, in welcher Reihenfolge die Operationen ausgeführt werden.

Hier ist eine weitere problematische Situation, die passieren kann, wenn mehrere Drohnen denselben Code gleichzeitig an derselben Position ausführen.
`if get_water() < 0.5:
    use_item(Items.Water)`

Wenn mehrere Drohnen dies gleichzeitig ausführen, laufen sie alle in die erste Zeile, die sie in den `if` Block führt. Dann verwenden sie alle Wasser und verschwenden es damit.
Sobald eine Drohne die zweite Zeile erreicht, könnte `get_water()` bereits nicht mehr unter `0.5` liegen, da eine andere Drohne das Feld inzwischen mit Wasser versorgt hat.

## Drohnenkommunikation
Wenn dich fortgeschrittenere Strategien interessieren, möchtest du vielleicht, dass sich deine Drohnen mit Nachrichtenübermittlungsfunktionen untereinander verständigen können.

Sende einen beliebigen Wert an eine andere Drohne:
`send(data, receiver_drone_id)`

Empfange den nächsten Wert, der von einer beliebigen Drohne gesendet wurde:
`data = receive()`

Empfange den nächsten Wert, der von einer bestimmten Drohne gesendet wurde:
`data = receive(sender_drone_id)`

Die Ausführungszeit von `send()` hängt von der Größe der gesendeten Daten ab. Zum Beispiel erfordert das Senden eines großen Dictionaries Kopiervorgänge, die einige Zeit in Anspruch nehmen können.

`receive()` wartet nicht darauf, dass eine Nachricht ankommt. Wenn noch keine Nachricht gesendet wurde, wird `None` zurückgegeben.

Du kannst eine Funktion erstellen, die auf eine Nachricht wartet, wie folgt:
`def blocking_receive(sender_drone_id = -1):
    while True:
        data = receive(sender_drone_id)
        if data != None:
            return data`

Eine nützliche Anwendung des Nachrichtenaustauschs ist, eine Funktion zu haben, die eine Drohne spawnt und ihr eine auszuführende Funktion sendet.
In einer Datei namens `drone_spawning`:
`def run_on_new_drone(f):
    id = spawn_drone("drone_spawning")
    send(f, id)

if __name__ == "__main__":
    f = blocking_receive()
    f()`

Das Senden solcher Funktionen kann sehr langsam sein, da der gesamte erfasste Zustand der Funktion, einschließlich aller globalen Variablen, kopiert werden muss.