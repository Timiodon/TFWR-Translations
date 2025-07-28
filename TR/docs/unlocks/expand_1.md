# Genişleme 1
<unlock=for>Ayrıca [Genişleme_2](docs/unlocks/expand_2.md)'ye de bak

</unlock>Çiftliğin büyüdü! Drone'u hareket ettiremezsen bu alanın pek bir faydası olmaz, bu yüzden drone'u hareket ettiren yeni bir `move()` fonksiyonu var. `move()` drone'u hareket ettirmek istediğin yönü belirtmeni gerektirir. Bunun için dört yeni sabit var: `North, East, South, West`

Örneğin, `move(North)` drone'u bir kare kuzeye hareket ettirecektir.

Çiftliğin kenarından dışarı çıkarsan drone çiftliğin diğer tarafına taşınır.
Aşağıdaki örnek kod, drone'u sürekli kuzeye hareket ettirecek ve çiftliğin kenarına ulaştığında başlangıca geri dönecektir:

`while True:
	move(North)`
