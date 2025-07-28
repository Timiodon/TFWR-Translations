# 自動アンロック
ゲームを完全に自動化するには、`unlock()`関数を使用して機能を自動的にアンロックできます。
たとえば、`unlock(Unlocks.Speed)`や`unlock(Unlocks.Expand)`を使用して、スピードや拡張機能をアンロックできます。

アンロックのコストを決定するには、作物やアイテムの場合と同じように`get_cost()`関数を使用します。
例:
`get_cost(Unlocks.Loops)`
`{Items.Hay:5}`を返します

特定のアンロックをいくつ持っているかを知りたい場合は、`num_unlocked(unlock)`関数を使用します。

例えば、`num_unlocked(Unlocks.Speed)`は持っているスピードアップグレードの数を返します。

`num_unlocked(Unlocks.Senses)`は、感覚がアンロックされていれば`1`を、されていなければ`0`を返します。

`num_unlocked()`はItems、Entities、Groundsにも使用できます。これは、アンロックされていれば`1`を、そうでなければ`0`を返します。

`num_unlocked(Unlocks.Carrots)`はアンロック/アップグレードされた回数を返すことに注意してください。
`num_unlocked(Items.Carrot)`は`0`か`1`しか返しません。（他の作物も同様です）
