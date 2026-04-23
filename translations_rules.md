# Fordítási Szabályok és Tapasztalatok

Ez a dokumentum a "The Farmer Was Replaced" játék magyar fordítási szabályait és tanulságait tartalmazza.

## Alapvető Szabályok (README.md-ből átvéve)

### Nem Fordítható Elemek

1. **Kód részek**: A játék kód részeit nem szabad lefordítani, mert a kód részei és nem lenne értelme kódot törni nyelv váltásakor.

2. **Kód elemek**: Konzisztencia miatt a kód elemeket mint "dictionary" és "while" sem szabad lefordítani, még ha kód blokkon kívül szerepelnek.

3. **Nevek**: Az item, entity, ground, unlock és leaderboard neveket sem szabad lefordítani, mert ezek a kód részei (pl. `Items.Carrot`, `Entities.Bush`, `Unlocks.Carrots`).
   - Ha viszont normál szövegben szerepelnek, le lehet fordítani ha értelmes.

4. **Placeholder-ek**: A `{0}` és `{{ something }}` formájú templating placeholder-eket soha nem szabad lecserélni. Módosításuk törné a dolgokat.

5. **String Azonosítók (@-prefix)**: A `@` karakterrel kezdődő sorok az egyedi string azonosítók a programban. Az `@` prefix és a hozzá tartozó kulcs (az `=` jelig) NEM fordítható!
   Pl.:
   - `@button_tooltip_save` - ez az azonosító, nem szabad lefordítani
   - `Saves the game.` - ez a szöveg, ez fordítható

   Tehát:
   ```
   @button_tooltip_save = Mentés     ✓ helyes
   mentés = Mentés                  ✗ helytelen (az azonosító kulcsot fordítottuk)
   ```

### Formázási Szabályok

- Backticks (`) használhatók kód blokkok jelölésére, mint a markdown fájlokban
- Egy soros backticks több soron is átnyúlhat
- A curlys zárójelek közötti dolgok `{0}` placeholder-ek, amiket runtimekor cserélnek ki

## Tapasztalatok a Fordításból (Lesson Learned)

### 1. Backticks Megőrzése Számok Körül

**A szabály**: Bármi ami backticks (` `) között van, az NEM fordítható!

Ez azt jelenti, hogy ha az eredeti szövegben ilyen van:
- `200` ticks → `200` ticket (NEM: 200 ticket)
- `1` tick → `1` ticket (NEM: 1 ticket)
- `0` ticks → `0` ticket (NEM: 0 ticket)
- `1` second → `1` másodperc (NEM: 1 másodperc)
- `30` seconds → `30` másodperc (NEM: 30 másodperc)

**Miért fontos**: A számok backticks között kód értékeket jelölnek, nem számszöveget. A játék ezeket a ticks-ként értelmezi.

### 2. Összetett Kifejezések

Az ilyen kifejezéseknél is meg kell őrizni a backticks-t:
- `1 + len(collection)` ticket
- `key size` ticket
- `#comparisons` ticket
- `element size` ticket

### 3. Python Kulcsszavak és Beépített Funkciók

Ezeket nem szabad lefordítani (már kód részként kezelendők):
- `True` / `False`
- `None`
- `def`, `if`, `else`, `elif`, `while`, `for`, `in`, `and`, `or`, `not`
- `return`, `break`, `continue`, `pass`
- `range`, `list`, `dict`, `set`, `tuple`
- `len`, `max`, `min`, `abs`, `str`, `print`

### 4. Irányok (Direction)

A `North`, `South`, `East`, `West` direction-ök nem fordítandók, mert kód részek:
- `North` → fel
- `South` → le
- `East` → jobbra
- `West` → balra

Ezeket Ki KELL írni a szövegben, de a kódban meghagyjuk eredeti formában.

### 5. Entity, Item, Unlock Nevek

Ezek mind kód részek, NEM fordítandók:
- `Entities.Bush`, `Entities.Grass`, stb.
- `Items.Water`, `Items.Fertilizer`, stb.
- `Unlocks.Carrots`, `Grounds.Soil`, stb.
- `Hats.Dinosaur_Hat`, stb.
- `Leaderboards.Fastest_Reset`, stb.

### 6. Minidg dokumentáld a fordításokat

A fordítási eredméynekt mindig dokumentáld a `./translation_report.md` fájlba, hogy később vissza lehessen nézni, milyen fordítási döntések születtek és miért. A cím legyen a fordított fájl alatta egy táblázat első oszlop az eredeti angol szöveg, a második az eklkészült magyar fordítás.

### 7. Lessions Learned:

Ha a felhasználó kritikát vagy észrevételet, vagy újabb kérést fogalmaz meg a fordítással kapcsolatban, azt mindig dokumentálni kell ebbe a fálba a `./translation_rules.md` fájlba, ha hasznos!

## Fordítási Checklist

Mielőtt elküldesz egy fordítást, ellenőrizd:

- [ ] Minden szám, ami az eredetiben backticks között van, megőrizte a backticks-t?
- [ ]所有 placeholder-ek (`{0}`, `{{ x }}`) érintetlenek maradtak?
- [ ] Kód részek (Python kulcsszavak, beépített függvények) nem lettek lefordítva?
- [ ] Entity/Item/Unlock nevek nem lettek lefordítva?
- [ ] A template-ek (pl. `{Items.Hay : 100}`) megfelelően vannak írva?

## Példák

### Helytelenül:
```
takes 200 ticks to execute → 200 ticket vesz igénybe
```

### Helyesen:
```
takes `200` ticks to execute → `200` ticket vesz igénybe
```

### Helytelenül:
```
The step size cannot be zero. → A lépés mérete nem lehet nulla.
```

### Helyesen:
```
The step size cannot be zero. → A lépés mérete nem lehet `0`.
```

---

*Ez a dokumentum folyamatosan bővül a fordítási tapasztalatok alapján.*