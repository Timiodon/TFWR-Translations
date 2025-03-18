# Expand 1
<unlock=for>Voir aussi [Expand_2](docs/unlocks/expand_2.md)

</unlock>Ta ferme a grandi ! Cet espace ne sert pas à grand-chose si tu ne peux pas déplacer le drone, alors il y a une nouvelle fonction `move()` qui déplace le drone. `move()` nécessite que tu spécifies la direction dans laquelle tu veux que le drone se déplace. Il y a quatre nouvelles constantes pour ça : `North, East, South, West`

Par exemple, `move(North)` déplacera le drone d'une case vers le nord.

Si tu te déplaces au bord de la ferme, le drone sera déplacé de l'autre côté de la ferme. Le code d'exemple suivant fera en sorte que le drone continue de se déplacer vers le nord et revienne au départ lorsqu'il atteint le bord de la ferme :

`while True:
	move(North)`