# Continue
`continue` pozwala na zatrzymanie bieżącej iteracji pętli i przejście do następnej iteracji najbardziej wewnętrznej pętli.

`for i in range(10):
	continue
    print("to nigdy nie zostanie wydrukowane")`

To wykonuje wszystkie `10` iteracji pętli, ale instrukcja `print` po `continue` jest zawsze pomijana.

Działa to również na pętlach `while`.

`while True:
	if not can_harvest():
		continue
    
    harvest()`

Ten kod wywołuje `harvest()` tylko wtedy, gdy `can_harvest()` jest `True`.
Ma to taki sam efekt jak

`while True:
	if can_harvest():
		harvest()`

W pętlach zagnieżdżonych `continue` zawsze dotyczy najbardziej wewnętrznej pętli.

`for i in range(10):
	for j in range(10):
	    print("to zostanie wydrukowane 100 razy")
		continue
		print("to nigdy nie zostanie wydrukowane")
	print("to zostanie wydrukowane 10 razy")`