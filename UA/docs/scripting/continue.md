# Continue
Continue дозволяє зупинити поточну ітерацію циклу та одразу перейти до наступної ітерації найвнутрішнього циклу:

`for i in range(10):
	continue
    print("це не буде виведено")`

Цей код виконує всі `10` ітерацій циклу, але інструкція `print` після `continue` завжди пропускається.

Це також працює з циклами `while`:

`while True:
	if not can_harvest():
		continue
    
    harvest()`

Цей код викликає `harvest()` лише тоді, коли `can_harvest()` дорівнює `True`. 
Він має той же ефект, що й

`while True:
	if can_harvest():
		harvest()`

У вкладених циклах `continue` завжди впливає лише на найвнутрішній цикл:

`for i in range(10):
	for j in range(10):
	    print("це буде виведено 100 разів")
		continue
		print("це не буде виведено")
	print("це буде виведено 10 разів")`