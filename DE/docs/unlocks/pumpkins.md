# Kürbisse
[Kürbisse](objects/pumpkin) wachsen wie Karotten auf gepflügtem Boden. Das Pflanzen kostet Karotten.

Wenn alle Kürbisse in einem Quadrat ausgewachsen sind, wachsen sie zu einem riesigen Kürbis zusammen. Leider haben Kürbisse eine 20%ige Chance zu sterben, sobald sie ausgewachsen sind, also musst du die toten neu pflanzen, wenn du willst, dass sie verschmelzen.

Wenn ein Kürbis stirbt, hinterlässt er einen toten Kürbis, der beim Ernten nichts abwirft. Das Pflanzen einer neuen Pflanze an seiner Stelle entfernt den toten Kürbis automatisch, es ist also nicht nötig, ihn zu ernten. `can_harvest()` gibt bei toten Kürbissen immer `False` zurück.

Der Ertrag eines riesigen Kürbisses hängt von der Größe des Kürbisses ab.

Ein 1x1 Kürbis ergibt `1*1*1 = 1` Kürbisse.
Ein 2x2 Kürbis ergibt `2*2*2 = 8` Kürbisse anstelle von `4`.
Ein 3x3 Kürbis ergibt `3*3*3 = 27` Kürbisse anstelle von `9`.
Ein 4x4 Kürbis ergibt `4*4*4 = 64` Kürbisse anstelle von `16`.
Ein 5x5 Kürbis ergibt `5*5*5 = 125` Kürbisse anstelle von `25`.
Ein `n`x`n` Kürbis ergibt `n*n*6` Kürbisse für `n >= 6`.

Es ist eine gute Idee, mindestens 6x6 große Kürbisse zu bekommen, um den vollen Multiplikator zu erhalten.

Das bedeutet, dass selbst wenn du auf jedem Feld in einem Quadrat einen Kürbis pflanzt, einer der Kürbisse sterben und verhindern kann, dass der Mega-Kürbis wächst.
