# Maliyetler
Herhangi bir maliyet, öğeleri sayılara eşleyen bir dictionary olarak temsil edilebilir.

`get_cost()` fonksiyonu böyle bir dictionary döndürür. Bir bitkinin veya kilidin maliyetini döndürür.

`get_cost(Entities.Pumpkin)`
`{Items.Carrot:1}` döner.

Kilit açmalar için, istediğiniz kilit açma seviyesinin maliyetini almak için isteğe bağlı ikinci bir argument olarak geçilebilir. Varsayılan olarak, şu anki kilit açma seviyesidir.

`get_cost(Unlocks.Loops, 0)`
`{Items.Hay:5}` döner.

Zaten maksimum seviyede olan kilit açmalar için, `get_cost()` `None` döndürecektir.

Şöyle kullanılabilir:
`cost = get_cost(something)
for item in cost:
	amount_of_this_item_needed = cost[item]`