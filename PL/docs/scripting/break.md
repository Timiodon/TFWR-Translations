# Break
`break` pozwala na wcześniejsze zakończenie pętli. Gdy instrukcja `break` zostanie osiągnięta, natychmiast wyjdzie z najbardziej wewnętrznej pętli i zacznie wykonywać kod po pętli.

`for i in range(10):
	break
print(i)`
To drukuje `0`, ponieważ `i` wynosi `0` w pierwszej iteracji pętli, a następnie instrukcja break kończy pętlę.

Działa to również na pętlach `while`.

`while True:
	if can_harvest():
		break`

Ten kod wykonuje pętlę `while`, dopóki `can_harvest()` nie będzie `True`.
Ma to taki sam efekt jak

`while not can_harvest():
	pass`

W pętlach zagnieżdżonych `break` zawsze wychodzi z najbardziej wewnętrznej pętli.

`for i in range(10):
	for j in range(10):
		break
		print("to nigdy nie zostanie wydrukowane")
	print("to zostanie wydrukowane 10 razy")`