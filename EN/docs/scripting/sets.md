# Sets
Sets are like [dictionaries](docs/scripting/dicts.md), but without values. They're just an unordered set of keys. 

They are created like dictionaries, but without values.
`set = {North, East, West}`

Use `set()` to create an empty set. Note that `{}` creates an empty dictionary.

Use `set.add(elem)` to add a new element to the set.

Use `set.remove(elem)` to remove an element from a set.

Use `if elem in set:` to check if the set contains an element.

Use `for elem in set:` to iterate all elements in the set.
For larger sets the `in` operator performs much faster than it would on a list.

Just like dictionaries, sets are unordered, so there are no guarantees about the order in which the elements are iterated.

Also, elements in sets are unique, so adding an element that is already in the set will not change the set.