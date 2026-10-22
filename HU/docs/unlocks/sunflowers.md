# Napraforgók
A [napraforgók](objects/sunflower) a nap erejét gyűjtik. Betakaríthatod azt az erőt.

Ültetésük pontosan úgy működik, mint a répák vagy tökök ültetése.

Teljesen megnőtt napraforgó betakarítása erőt hoz.
Ha a farmon van legalább 10 napraforgó és te takarítod be a legtöbb szirmú napraforgót, `8`x több erőt kapsz!
Ha napraforgót takarítasz be, amikor van egy másik napraforgó több szirmokkal, a következő napraforgó, amit betakarítasz, csak a normál mennyiségű erőt adja (nem a 8x bónuszt).

A `measure()` a napraforgó szirmainak számát adja vissza a drón alatt.
A napraforgóknak legalább `7` és legfeljebb `15` szirmuk van.
Már mérhetők, mielőtt teljesen megnőnének.

Több napraforgónak lehet ugyanannyi szirma, szóval több napraforgó is lehet a legtöbb szirmokkal. Ebben az esetben mindegy, melyiküket takarítod be.

Amíg van erőd, a drón azt fogja használni, hogy kétszer olyan gyorsan fusson.
Minden 30 műveletben (mint mozgások, betakarítások, ültetések...) 1 erőt fogyaszt.
Más kód utasítások végrehajtása is használhat erőt, de sokkal kevesebbet, mint a drón műveletek.

Általában minden, ami a sebességfejlesztések által felgyorsítva van, az erő által is felgyorsítva van.
Bármi, ami erő által felgyorsítva van, az erőt is használ a végrehajtási idővel arányosan, a sebességfejlesztések figyelmen kívül hagyásával.