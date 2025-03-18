# Dünger
Irgendwann reicht es einfach nicht mehr, auf das langsame Wachsen der Pflanzen zu warten. Ähnlich wie bei Wasser erhältst du automatisch alle 10 Sekunden 1 Dünger, plus einen zusätzlichen für jedes Upgrade.

Dünger kann Pflanzen sofort wachsen lassen. `use_item(Items.Fertilizer)` reduziert die verbleibende Wachstumszeit der Pflanze unter der Drohne um 2 Sekunden.

Das hat einige Nebenwirkungen.
Pflanzen, die mit Dünger gewachsen sind, werden infiziert.

Wenn eine Pflanze infiziert ist, wird die Hälfte ihres Ertrags beim Ernten in `Items.Weird_Substance` umgewandelt.
Seltsame Substanz kann auch auf Pflanzen verwendet werden, was den infizierten Status der Pflanze und aller angrenzenden Pflanzen umschaltet.

Wenn du also `use_item(Items.Weird_Substance)` auf eine infizierte Pflanze anwendest, wird sie geheilt. Verwendest du es jedoch auf eine gesunde Pflanze, wird sie infiziert.

Wenn du es auf eine infizierte Pflanze mit gesunden Nachbarn verwendest, wird die Pflanze geheilt, aber die Nachbarn infiziert und umgekehrt.