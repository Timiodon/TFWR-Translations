# Dünger
Irgendwann ist es einfach nicht mehr effizient genug, auf das Wachsen der Pflanzen zu warten. 
Ähnlich wie bei Wasser erhältst du automatisch alle 10 Sekunden 1 Dünger, wobei sich die Menge mit jedem Upgrade verdoppelt.

Dünger kann Pflanzen sofort wachsen lassen. `use_item(Items.Fertilizer)` reduziert die verbleibende Wachstumszeit der Pflanze unter der Drohne um 2 Sekunden.

Dies hat einige Nebenwirkungen.
Pflanzen, die mit Dünger angebaut werden, werden infiziert.

Wenn eine Pflanze infiziert ist, wird die Hälfte ihres Ertrags beim Ernten in `Items.Weird_Substance` umgewandelt.
Seltsame Substanz kann auch auf Pflanzen angewendet werden, was den Infektionsstatus der Pflanze und aller benachbarten Pflanzen umschaltet.

Wenn du also `use_item(Items.Weird_Substance)` auf eine infizierte Pflanze anwendest, wird sie geheilt, aber wenn du es auf eine gesunde Pflanze anwendest, wird sie infiziert.

Wenn du es auf eine infizierte Pflanze mit gesunden Nachbarn anwendest, wird die Pflanze geheilt, aber die Nachbarn infiziert und umgekehrt.