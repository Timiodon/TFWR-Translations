# Maliyetler
Herhangi bir maliyet, eşyaları sayılarla eşleyen bir dictionary olarak temsil edilebilir.

`get_cost()` fonksiyonu böyle bir dictionary döndürür. Bir bitkinin veya bir kilit açmanın maliyetini döndürür.

`get_cost(Entities.Pumpkin)`
`{Items.Carrot:1}` döndürür

Kilit açmalar için, maliyetini almak istediğin kilit açma seviyesi için isteğe bağlı ikinci bir argüman geçirilebilir. Varsayılan olarak, mevcut kilit açma seviyesidir.

`get_cost(Unlocks.Loops, 0)`
`{Items.Hay:5}` döndürür

Zaten son seviyede olan kilit açmalar için `get_cost()` `None` döndürür.

Şu şekilde kullanılabilir:
`cost = get_cost(bir_sey)
for item in cost:
	bu_esyadan_gereken_miktar = cost[item]`
