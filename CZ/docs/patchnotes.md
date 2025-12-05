# Verze 1.0 je konečně tady!
Po více než třech a půl letech vývoje, více než 20 aktualizacích a díky vašim skvělým ohlasům skončila fáze předběžného přístupu.

## Co je nového ve verzi 1.0?
- Více dronů pro maximální efektivitu farmy  
- Přepracovaný strom odemykání s plynulejší progresí  
- 60 achievementů k otestování tvých dovedností  
- Některé achievementy odemknou pro drona speciální klobouky  
- Kompletně přepracovaný zvukový doprovod  
- Nová hudební skladba  
- Vylepšení kvality života a různé opravy  
- Změny kompatibility: Vylepšení budou částečně resetována. Opětovné používání bludišť funguje trochu jinak.

Děkuji všem, kdo podporovali hru The Farmer Was Replaced od Early Access až po plné vydání.  
Nemůžu se dočkat, až uvidím, jak využijete více dronů k tvůrčím a chytrým strategiím!  
– Timon

Nezapomeň se připojit i na Discord:  
[Discord](https://discord.com/invite/kj33cJkeJn)

## Kompletní poznámky k patchi
### Změny kompatibility:
- Kvůli přepracování technologického stromu již čísla vylepšení ze starých uložených her nebudou platná. Po načtení starého save se všechny upgrady resetují na odpovídající úroveň.  
- Při opětovném používání bludišť je nyní třeba nejdříve přemístit poklad a **pak** změřit pozici, místo opačného postupu.

### Hratelnost:
- Přidány tooltipy s užitečnými informacemi při najetí kurzorem na dlaždici farmy.  
- Použití `measure()` kdekoliv v bludišti nyní vždy vrátí pozici aktuálního pokladu – není třeba měřit přímo na něm.  
- Přidána funkce `can_move()` pro bludiště.  
- Dýně nyní dorůstají až do velikosti 6×6 (dříve 5×5).  
- Sušení půdy bylo upraveno – místo 1 % každých 0,8–1,2 s má nyní každá dlaždice 10 % šanci vyschnout každých 0,1 s.  
- Kaktusy nyní rostou vždy přesně 1 sekundu.  
- Dýně nyní po sobě zanechávají „mrtvou dýni“ jako indikaci, že uhynuly.  
- Přidána funkce `pet_the_piggy()`.  
- Funkce `num_unlocked()` je nyní dostupná už s odemknutím „Smyslů“ (Senses).

### Zvuk:
- Zvuky byly kompletně předělány.  
- Nyní hraje hudba už při spuštění hry!

### Grafika:
- Technologický strom byl kompletně přepracován.  
- Inventář v levém horním rohu má nyní efektní animaci při sbírání předmětů.  
- Kaktusy, které nejsou správně seřazeny, jsou nyní hnědé – lépe viditelné.  
- Rostliny jsou nyní viditelné okamžitě po zasazení, i když ještě nevyrostly.

### Editor kódu:
- Dvojité kliknutí na identifikátory s podtržítky nyní označí celý název.  
- Pokud je vypnuta volba „tabs to spaces“, mezery pro odsazení se nyní převádějí zpět na tabulátory.  
- Zoomování je nyní mnohem plynulejší.  
- Doplnění kódu nyní správně rozpoznává importy z jiných souborů.  
- Přidány různé kurzory pro úpravu textu a změnu velikosti oken.  
- Kroky debuggeru se nyní řídí podle řádku kódu místo ticků simulace.

### Ostatní:
- Lze nyní řetězit porovnávací operátory stejně jako v Pythonu.  
- `get_cost(Entities.Hedge)` a `get_cost(Entities.Treasure)` nyní vrací cenu bludiště 1×1.  
- Přidáno nastavení rozlišení.  
- Přidána možnost vypnout blikající zvýraznění při běhu kódu.  
- Výkon provádění kódu byl dále optimalizován – hra běží plynuleji i při spuštěném kódu.  
- Přidána klávesová zkratka „Toggle HUD“.

### Opravy:
- Opraveny případy, kdy zvýraznění kódu bylo viditelné přes jiná okna.  
- Akce jako orání nyní nemohou ovlivňovat vysychání vody.  
- Opraveny problémy s klávesovými zkratkami na ne-US klávesnicích.  
- Opraveno, že prasátko občas uteklo daleko od farmy.  
- Opraveno, že hnojivo nenakazilo plně vyrostlé rostliny.  
- Opraveno `set_world_size(get_world_size())`, které resetovalo pozici dronu.  
- Opraveno chování simulace s dinosaury, které zanechávalo mnoho jablek.  
- Opraven bug, kdy se chybové zprávy posouvaly po minimalizaci okna.  
- Opraveno zobrazování chybových zpráv během psaní.

### Změny z dřívějších patchů, které jsi mohl přehlédnout:
- Funkce definované v jiných souborech se již nenačítají automaticky. Nyní je nutné je importovat výslovně přes `import` (viz odemknutí „Import“).  
- `Items.Bones` bylo přejmenováno na `Items.Bone`, aby byly všechny položky v jednotném čísle.  
- `Entities.Carrots` bylo přejmenováno na `Entities.Carrot` ze stejného důvodu.  
- `Grounds.Turf` bylo přejmenováno na `Grounds.Grassland` pro lepší srozumitelnost.  
- `Items.Water_Tank` bylo přejmenováno na `Items.Water`, protože doplňování nádrže bylo odstraněno.  
- `Unlocks.Benchmark` bylo nahrazeno odemknutím `Unlocks.Timing`.  
- `get_op_count()` bylo přejmenováno na `get_tick_count()`.  
- `set_farm_size()` bylo přejmenováno na `set_world_size()`, aby bylo jednotné s `get_world_size()`.  
- `get_companion()` nyní vrací dvojici `(entity, (x, y))` místo seznamu.  
- Funkce `trade()` byla ze hry odstraněna.