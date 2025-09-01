# Megafarm
Diese unglaublich mächtige Freischaltung gibt dir Zugriff auf mehrere Drohnen.

Wie zuvor startest du immer noch mit nur einer Drohne. Zusätzliche Drohnen müssen erst gespawnt werden und verschwinden, nachdem das Programm beendet ist.
Jede Drohne führt ihr eigenes, separates Programm aus. Neue Drohnen können mit der `spawn_drone(function)`-Funktion gespawnt werden.

`def drone_function():
    move(North)
    do_a_flip()

spawn_drone(drone_function)`

Dies spawnt eine neue Drohne an der gleichen Position wie die Drohne, die den `spawn_drone(function)`-Befehl ausgeführt hat. Die neue Drohne beginnt dann mit der Ausführung der angegebenen Funktion. Nachdem sie fertig ist, verschwindet sie automatisch.

Drohnen kollidieren nicht miteinander.

Benutze `max_drones()`, um die maximale Anzahl an Drohnen zu erhalten, die gespawnt werden können.
Benutze `num_drones()`, um die Anzahl der Drohnen zu erhalten, die sich bereits auf der Farm befinden.


## Beispiel:
`def harvest_column():
    for _ in range(get_world_size()):
        harvest()
        move(North)

while True:
    if spawn_drone(harvest_column):
        move(East)`

Dies bewirkt, dass sich deine erste Drohne horizontal bewegt und weitere Drohnen spawnt. Die gespawnten Drohnen bewegen sich dann vertikal und ernten alles auf ihrem Weg.

Wenn bereits alle verfügbaren Drohnen gespawnt wurden, macht `spawn_drone()` nichts und gibt `None` zurück.

<spoiler=zeige Hinweis> Schau dir diese super nützliche parallele `for_all`-Funktion an, die eine beliebige Funktion entgegennimmt und sie auf jedem Farmfeld ausführt. Sie nutzt dafür alle verfügbaren Drohnen.

`def for_all(f):
	def row():
		for _ in range(get_world_size()-1):
			f()
			move(East)
		f()
	for _ in range(get_world_size()):
		if not spawn_drone(row):
			row()
		move(North)

for_all(harvest)`

Ein besonders nützliches Muster ist, eine Drohne zu spawnen, wenn eine verfügbar ist, und es andernfalls selbst zu tun.

`if not spawn_drone(task):
	task()`
</spoiler>

## Auf eine andere Drohne warten
Benutze die `wait_for(drone)`-Funktion, um auf eine andere Drohne zu warten, bis sie fertig ist. Du erhältst den `drone`-Handle, wenn du die Drohne spawnst.
`wait_for(drone)` gibt den Rückgabewert der Funktion zurück, die die andere Drohne ausgeführt hat.

`def get_entity_type_in_direction(dir):
    move(dir)
    return get_entity_type()

def zero_arg_wrapper():
    return get_entity_type_in_direction(North)
drone = spawn_drone(zero_arg_wrapper)
print(wait_for(drone))`

Beachte, dass das Spawnen von Drohnen Zeit braucht, also ist es keine gute Idee, für jede Kleinigkeit eine neue Drohne zu spawnen.

## Kein gemeinsamer Speicher
Jede Drohne hat ihren eigenen Speicher und kann die Globals einer anderen Drohne nicht direkt lesen oder schreiben.

`x = 0

def increment():
    global x
    x += 1

wait_for(spawn_drone(increment))
print(x)`

Dies gibt `0` aus, weil die neue Drohne ihre eigene Kopie des globalen `x` inkrementiert hat, was das `x` der ersten Drohne nicht beeinflusst.

## Race Conditions
Mehrere Drohnen können gleichzeitig mit demselben Farmfeld interagieren. Wenn zwei Drohnen während desselben Ticks mit demselben Feld interagieren, finden beide Interaktionen statt, aber die Ergebnisse können sich je nach der Reihenfolge der Interaktionen unterscheiden.

Stell dir zum Beispiel vor, dass die Drohnen `0` und `1` beide über demselben Baum schweben, der fast ausgewachsen ist.
Drohne `0` ruft
`use_item(Items.Fertilizer)`
Drohne `1` ruft
`harvest()`

Wenn diese Aktionen zur gleichen Zeit stattfinden, wird der Baum zuerst gedüngt und dann geerntet. In diesem Fall erhältst du Holz von ihm. Wenn jedoch Drohne `1` etwas schneller ist, wird der Baum geerntet, bevor er gedüngt wird, und du erhältst kein Holz.
Dies wird als „Race Condition“ bezeichnet. Es ist ein häufiges Problem bei der parallelen Programmierung, bei dem das Ergebnis von der Reihenfolge abhängt, in der die Operationen ausgeführt werden.

Hier ist eine weitere problematische Situation, die auftreten kann, wenn mehrere Drohnen denselben Code gleichzeitig an derselben Position ausführen.
`if get_water() < 0.5:
    use_item(Items.Water)`

Wenn mehrere Drohnen dies gleichzeitig ausführen, werden sie alle die erste Zeile ausführen, was sie in den `if`-Block bringt. Dann werden sie alle Wasser verwenden und eine Menge davon verschwenden.
Bis eine Drohne die zweite Zeile erreicht, ist `get_water()` möglicherweise nicht mehr kleiner als `0.5`, weil eine andere Drohne das Feld in der Zwischenzeit bewässert hat.