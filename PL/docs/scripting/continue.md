# Continue
continue pozwala na przerwanie aktualnej iteracji pętli i przejście do kolejnej iteracji najgłębszej pętli.

`for i in range(10):
	continue
    print("this is never printed")`

To wykonuje wszystkie `10` iteracji pętli, ale polecenie `print` po `continue` jest zawsze pomijane.

Działa to również z pętlami `while`.

`while True:
	if not can_harvest():
		continue
    
    harvest()`

Ten kod wywołuje `harvest()` tylko wtedy, gdy `can_harvest()` jest `True`. 
Ma to taki sam efekt jak:

`while True:
	if can_harvest():
		harvest()`

W zagnieżdżonych pętlach `continue` zawsze wpływa na najgłębszą pętlę.

`for i in range(10):
	for j in range(10):
	    print("this is printed 100 times")
		continue
		print("this is never printed")
	print("this is printed 10 times")`