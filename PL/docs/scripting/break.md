# Break
`break` pozwala na wcześniejsze zakończenie pętli. Gdy instrukcja `break` zostanie osiągnięta, natychmiast opuści najbardziej wewnętrzną pętlę i rozpocznie wykonywanie kodu po pętli.

`for i in range(10):
	break
print(i)`
To wyświetla `0`, ponieważ `i` wynosi `0` w pierwszej iteracji pętli, a następnie instrukcja break kończy pętlę.

Działa również na pętlach `while`.

`while True:
	if can_harvest():
		break`

Ten kod wykonuje pętlę `while`, dopóki `can_harvest()` nie zwróci `True`. 
Ma to taki sam efekt jak

`while not can_harvest():
	pass`

W zagnieżdżonych pętlach `break` zawsze opuszcza najbardziej wewnętrzną pętlę.

`for i in range(10):
	for j in range(10):
		break
		print("to nigdy nie zostanie wyświetlone")
	print("to zostanie wyświetlone 10 razy")`