[<- Hız Yükseltmesi](docs/unlocks/speed.md)
---
# If
Kodu bir koşula bağlı olarak çalıştırmak için `if`, `elif` ve `else` kullanabilirsin.

{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 1, "y": 1},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
condition1 = False
condition2 = False
condition3 = True

if condition1:
	do_a_flip()
elif condition2:
	harvest()
else:
	do_a_flip()
	harvest()
}}

## Sözdizimi
`if` ifadeleri, kodu yalnızca bir koşul `True` olduğunda çalıştırmanı sağlar. Tekrar etmeyen bir `while` döngüsü gibidirler.
Bir `if` ifadesi, tıpkı `while` döngüsü gibi bir koşul alır ve koşulun sonucu `True` olursa kendi kod bloğunu çalıştırır:

{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 1, "y": 1},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
condition = True

if condition:
	do_a_flip()
}}

`if` bloğundan sonra bir `else` bloğu da ekleyebilirsin. `else` bloğu, koşulun sonucu `False` olursa çalışır.

{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 1, "y": 1},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
condition = False

if condition:
	do_a_flip()
else:
	harvest()
}}

`elif`, "else if"in kısaltmasıdır.

`if condition1:
	#a
else:
	if condition2:
		#b
	else:
		#c`

şu şekilde kısaltılabilir:

`if condition1:
	#a
elif condition2:
	#b
else:
	#c`

---

[While Döngüsü](docs/scripting/while.md)      [Operatörler](docs/scripting/operators.md)      [Duyular](docs/unlocks/senses.md)
