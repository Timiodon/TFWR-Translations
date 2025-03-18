# Carrots
キャロットを植える前に、`plant(Entities.Carrot)`を使うためには、まず土を耕さないといけません。これで地面が`Grounds.Soil`になります。土を耕すには、ただ`till()`を呼び出すだけです。再度`till()`を呼び出すと、地面は`Grounds.Grassland`に戻ります。

キャロットを植えるには、木材と干草が必要です。これらのアイテムは、`plant(Entities.Carrot)`を呼び出すと自動的に消費されます。

各植物のコストは、その[専用ページ](objects/carrot)で確認できます。