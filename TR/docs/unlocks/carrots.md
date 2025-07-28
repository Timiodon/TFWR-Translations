# Havuçlar
`plant(Entities.Carrot)` ile havuç ekmeden önce, toprağı sürmelisin. Bu, zemini `Grounds.Soil`'e dönüştürür. Toprağı sürmek için, sadece `till()` çağır. Tekrar `till()` çağırmak onu tekrar `Grounds.Grassland`'e dönüştürür.

Havuç ekmek odun ve saman maliyetine sahiptir. Bu eşyalar, `plant(Entities.Carrot)` çağrıldığında otomatik olarak kaldırılacaktır.

Herhangi bir bitkinin maliyetini [kendi sayfasında](objects/carrot) görebilirsin.