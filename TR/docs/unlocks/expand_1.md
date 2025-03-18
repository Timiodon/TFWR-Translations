# Expand 1
<unlock=for>Ayrıca [Expand_2](docs/unlocks/expand_2.md)'e de bak

</unlock>Çiftliğin büyüdü! Eğer dronu hareket ettiremezsen bu alan pek işe yaramaz, bu yüzden dronu hareket ettiren yeni bir fonksiyon olan `move()` var. `move()` fonksiyonu, dronu hangi yöne hareket ettirmek istediğinizi belirtmenizi gerektirir. Bunun için dört yeni sabit var: `North, East, South, West`

Örneğin, `move(North)` dronu bir kare kuzeye hareket ettirir.

Eğer çiftliğin kenarından dışarı çıkarsanız, dron çiftliğin diğer tarafına taşınır.
Aşağıdaki örnek kod, dronu sürekli olarak kuzeye hareket ettirir ve çiftliğin kenarına ulaştığında başlangıca döner:

`while True:
	move(North)`