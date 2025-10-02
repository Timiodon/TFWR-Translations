# Mega-Farm
Diese unglaublich mächtige Freischaltung gibt dir Zugriff auf mehrere Drohnen.

Wie zuvor startest du immer noch mit nur einer Drohne. Zusätzliche Drohnen müssen zuerst gespawnt werden und verschwinden nach Beendigung des Programms.
Jede Drohne führt ihr eigenes separates Programm aus. Neue Drohnen können mit der Funktion `spawn_drone(function)` gespawnt werden.

`def drone_function():
    move(North)
    do_a_flip()

spawn_drone(drone_function)`

Dies spawnt eine neue Drohne an derselben Position wie die Drohne, die den Befehl `spawn_drone(function)` ausgeführt hat. Die neue Drohne beginnt dann mit der Ausführung der angegebenen Funktion. Nachdem sie fertig ist, verschwindet sie automatisch.

Drohnen kollidieren nicht miteinander.

Verwende `max_drones()`, um die maximale Anzahl an Drohnen zu erhalten, die gespawnt werden können.
Verwende `num_drones()`, um die Anzahl der Drohnen zu erhalten, die sich bereits auf der Farm befinden.


## Beispiel:
`def harvest_column():
    for _ in range(get_world_size()):
        harvest()
        move(North)

while True:
    if spawn_drone(harvest_column):
        move(East)`

Dies bewirkt, dass deine erste Drohne sich horizontal bewegt und weitere Drohnen spawnt. Die gespawnten Drohnen bewegen sich dann vertikal und ernten alles auf ihrem Weg.

Wenn alle verfügbaren Drohnen bereits gespawnt wurden, tut `spawn_drone()` nichts und gibt `None` zurück.

<spoiler=zeige Hinweis> Schau dir diese super nützliche parallele `for_all`-Funktion an, die eine beliebige Funktion nimmt und sie auf jedem Farmfeld ausführt. Sie nutzt alle verfügbaren Drohnen dafür.

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

Ein besonders nützliches Muster ist es, eine Drohne zu spawnen, wenn eine verfügbar ist, und es andernfalls selbst zu tun.

`if not spawn_drone(task):
	task()`
</spoiler>

## Auf eine andere Drohne warten
Verwende die Funktion `wait_for(drone)`, um auf das Ende einer anderen Drohne zu warten. Du erhältst das `drone`-Handle, wenn du die Drohne spawnst.
`wait_for(drone)` gibt den Rückgabewert der Funktion zurück, die die andere Drohne ausgeführt hat.

`def get_entity_type_in_direction(dir):
    move(dir)
    return get_entity_type()

def zero_arg_wrapper():
    return get_entity_type_in_direction(North)
drone = spawn_drone(zero_arg_wrapper)
print(wait_for(drone))`

Beachte, dass das Spawnen von Drohnen Zeit braucht, daher ist es keine gute Idee, für jede Kleinigkeit eine neue Drohne zu spawnen.

Du kannst `has_finished(drone)` benutzen, um zu checken, ob die Drohne fertig ist, ohne dass du warten musst.

## Kein gemeinsamer Speicher
Jede Drohne hat ihren eigenen Speicher und kann nicht direkt die globalen Variablen einer anderen Drohne lesen oder schreiben.

`x = 0

def increment():
    global x
    x += 1

wait_for(spawn_drone(increment))
print(x)`

Dies wird `0` ausgeben, da die neue Drohne ihre eigene Kopie des globalen `x` erhöht hat, was das `x` der ersten Drohne nicht beeinflusst.

## Race Conditions
Mehrere Drohnen können gleichzeitig mit demselben Farmfeld interagieren. Wenn zwei Drohnen während desselben Ticks mit demselben Feld interagieren, finden beide Interaktionen statt, aber die Ergebnisse können je nach Reihenfolge der Interaktionen unterschiedlich sein.

Stell dir zum Beispiel vor, dass die Drohnen `0` und `1` beide über demselben Baum sind, der fast ausgewachsen ist.
Drohne `0` ruft auf
`use_item(Items.Fertilizer)`
Drohne `1` ruft auf
`harvest()`

Wenn diese Aktionen gleichzeitig stattfinden, wird der Baum zuerst gedüngt und dann geerntet. In diesem Fall erhältst du Holz davon. Wenn jedoch Drohne `1` etwas schneller ist, wird der Baum geerntet, bevor er gedüngt wird, und du erhältst kein Holz.
Dies wird als "Race Condition" bezeichnet. Es ist ein häufiges Problem bei der parallelen Programmierung, bei dem das Ergebnis von der Reihenfolge abhängt, in der Operationen ausgeführt werden.

Hier ist eine weitere problematische Situation, die auftreten kann, wenn mehrere Drohnen denselben Code gleichzeitig an derselben Position ausführen.
`if get_water() < 0.5:
    use_item(Items.Water)`

Wenn mehrere Drohnen dies gleichzeitig ausführen, werden sie alle die erste Zeile ausführen, was sie in den `if`-Block bringt. Dann werden sie alle Wasser verwenden und viel davon verschwenden.
Bis eine Drohne die zweite Zeile erreicht, könnte `get_water()` nicht mehr kleiner als `0.5` sein, weil eine andere Drohne das Feld in der Zwischenzeit bewässert hat.