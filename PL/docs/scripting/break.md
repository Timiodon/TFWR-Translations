# Break
`break` pozwala na wcześniejsze zakończenie pętli. Gdy zostanie osiągnięty wiersz z `break`, natychmiast wychodzi z najgłębszej pętli i rozpoczyna wykonanie kodu po pętli.

`for i in range(10):
	break
print(i)`
To drukuje `0`, ponieważ `i` wynosi `0` w pierwszej iteracji pętli, a następnie instrukcja break kończy pętlę.

Działa również w pętlach `while`.

`while True:
	if can_harvest():
		break`

Ten kod uruchamia pętlę `while` aż `can_harvest()` wynosi `True`.
Daje to taki sam efekt jak

`while not can_harvest():
	pass`

W zagnieżdżonych pętlach `break` zawsze wychodzi z najgłębszej pętli.

`for i in range(10):
	for j in range(10):
		break
		print("this is never printed")
	print("this is printed 10 times")`