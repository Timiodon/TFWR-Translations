# Expansion 1
<unlock=for>Voir aussi [Expansion_2](docs/unlocks/expand_2.md)

</unlock>Ta ferme s'est agrandie ! Cet espace n'est pas très utile si tu ne peux pas déplacer le drone, il y a donc une nouvelle fonction `move()` qui déplace le drone. `move()` exige que tu spécifies la direction dans laquelle tu veux que le drone se déplace. Il y a quatre nouvelles constantes pour cela : `North, East, South, West`

Par exemple, `move(North)` déplacera le drone d'une case vers le nord.

Si tu dépasses le bord de la ferme, le drone sera déplacé de l'autre côté de la ferme.
Le code d'exemple suivant continuera à déplacer le drone vers le nord et reviendra au début lorsqu'il atteindra le bord de la ferme :

`while True:
	move(North)`