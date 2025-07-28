# Dünger
Irgendwann ist das Warten auf das Wachstum der Pflanzen einfach nicht mehr effizient genug.
Ähnlich wie bei Wasser erhältst du automatisch alle 10 Sekunden 1 Dünger, plus einen zusätzlichen für jedes Upgrade.

Dünger kann Pflanzen sofort wachsen lassen. `use_item(Items.Fertilizer)` reduziert die verbleibende Wachstumszeit der Pflanze unter der Drohne um 2 Sekunden.

Dies hat einige Nebeneffekte.
Pflanzen, die mit Dünger angebaut werden, werden infiziert.

Wenn eine Pflanze infiziert ist, wird die Hälfte ihres Ertrags bei der Ernte in `Items.Weird_Substance` umgewandelt.
Seltsame Substanz kann auch auf Pflanzen angewendet werden, was den infizierten Status der Pflanze und aller benachbarten Pflanzen umschaltet.

Wenn du also `use_item(Items.Weird_Substance)` auf eine infizierte Pflanze anwendest, wird sie geheilt, aber wenn du es auf eine gesunde Pflanze anwendest, wird sie infiziert.

Wenn du es auf eine infizierte Pflanze mit gesunden Nachbarn anwendest, heilt es die Pflanze, infiziert aber die Nachbarn und umgekehrt.