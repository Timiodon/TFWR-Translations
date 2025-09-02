# ニンジン
`plant(Entities.Carrot)` でニンジンを植える前に、土を耕す必要があります。これにより、地面が `Grounds.Soil` に変わります。土を耕すには、単に `till()` を呼び出します。再度 `till()` を呼び出すと、`Grounds.Grassland` に戻ります。

ニンジンの植え付けには木材と干し草が必要です。これらのアイテムは `plant(Entities.Carrot)` を呼び出すと自動的に削除されます。

各植物のコストは、その[専用ページ](objects/carrot)で確認できます。