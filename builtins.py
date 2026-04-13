# This file gives Python type definitions to TFWR builtins to allow editing code with Python editors.
# Note that the games language is not Python and these definitions are only an approximation.

# Contributed by @Noon, @KlingonDragon, @dieckie, @Flekay and @Zoroark-Zwart on the TFWR Discord server.
# @SCD-3 on GitHub

# Expose some useful types to allow for typing without using a typing import.
# Typing imports would fail to run in-game as they are not ignored.

# Notes on aliases because of TFWR functions:
# - string -> builtins.str
# - range_class -> builtins.range

from typing import Self, TypeVar, Literal, Final, overload
from collections.abc import Callable, Iterable, Sequence, Container

from builtins import (
    bool, int, float, str as string,
    range as range_class,
    tuple,

    # If you uncomment the custom classes found below then
    # comment this line to prevent conflicts
    list, set, dict
)

# Used for when the builtin type is desirable over a possible
# redefinition using the same name
from builtins import (
    bool as _bool, int as _int, float as _float,
    tuple as _tuple, list as _list, set as _set, dict as _dict
)

from typing import Any as _Any
from enum import Enum as _Enum, auto as _auto

# -------------------------------------------------------------------------------
# Basic Types and Collections
# -------------------------------------------------------------------------------

# -------------------------------------------------------------------------------
"""
Basic immutable types in TFWR.

included:

- `bool`
- `int`
- `float`
- `string`
- `None`
"""
type Primitive = _bool | _int | _float | string | None

# --------------------------------------------------
type Enums = (
	Direction | Entity | Entities |
    Ground | Grounds | Hat | Hats |
    Item | Items | Leaderboard |
    Leaderboards | Unlock | Unlocks
)
"""
Type representing all available enums in TFWR.

included:

- `Direction` (`North`, `East`, `South`, `West`)
- `Hat`, `Entity`, `Item`, `Ground`, `Leaderboard`, `Unlock`
- `Hats`, `Entities`, `Items`, `Grounds`, `Leaderboards`, `Unlocks`
"""

# --------------------------------------------------
type Hashable = Primitive | Enums | range_class | Drone | tuple[Hashable, ...]
"""
Type representing all of the useable types for a dict key or set element in TFWR.

included:

- Primitives: `bool`, `int`, `float`, `string`, `None`
- `tuple` and tuples of tuples that use a `Hashable`
- `range_class`, `function` (hinted as `Callable`)
- `Drone` (from `spawn_drone`)
- Enums:
  - `Direction` (`North`, `East`, `South`, `West`)
  - `Hat`, `Entity`, `Item`, `Ground`, `Leaderboard`, `Unlock`
  - `Hats`, `Entities`, `Items`, `Grounds`, `Leaderboards`, `Unlocks`
"""

_Hashable_ = TypeVar("_Hashable_", Hashable, Hashable, covariant = True)

# --------------------------------------------------
type Any = (
    Primitive | 								# Python builtin    - basic types

	range_class | Callable[..., Any] |			# Python builtin    - functions / modules

	_tuple[Any,...] | _list[Any] |				# Python builtin    - collection types
    _set[Hashable] | _dict[Hashable, Any] |

	Enums | 									# Game builtins		- enum classes

	Drone										# Game builtins		- megafarm classes
)
"""
Type representing all of the useable types in TFWR.

included:

- Primitives: `bool`, `int`, `float`, `string`, `None`
- `tuple`, `list`, `dict`, `set`
- `range_class`, `module`, `function` (hinted as `Callable`)
- `Drone` (from `spawn_drone`)
- Enums:
  - `Direction` (`North`, `East`, `South`, `West`)
  - `Hat`, `Entity`, `Item`, `Ground`, `Leaderboard`, `Unlock`
  - `Hats`, `Entities`, `Items`, `Grounds`, `Leaderboards`, `Unlocks`
"""

_Any_ = TypeVar("_Any_", Any, Any, covariant = True)

# --------------------------------------------------
type AnyIterable = (
	_dict[Hashable, Any] | _list[Any] | _set[Hashable] | _tuple[Any,...] |
	string | range_class |
	Entities | Grounds | Hats | Items | Leaderboard | Unlocks
)
"""
Type representing all of the iterable types in TFWR.

included:

- `tuple`, `list`, `dict`, `set`
- `string`, `range_class`
- Enums:
  - `Direction` (`North`, `East`, `South`, `West`)
  - `Hat`, `Entity`, `Item`, `Ground`, `Leaderboard`, `Unlock`
  - `Hats`, `Entities`, `Items`, `Grounds`, `Leaderboards`, `Unlocks`
"""

# --------------------------------------------------
# Uncomment this class if you want additional game-specific type hints and docstrings for `dict` methods
# This class requires the use of of the `dict()` constructor. Assigning `dict` literals (ex. `{'1':1, '1':2, '1':3}`) will cause typing conflicts with the builtin Python type `builtins.dict`

# Comment out the `dict` builtins import above to prevent conflict errors.

# class dict[key: Hashable, value: Any](_dict):
# 	"""
# 	Builds an unordered collection of key-value pairs

# 	dict() -> new empty dictionary

# 	dict(dictionary[keys, values]) -> new dictionary initialized from an existing `dictionary`

# 	takes `1 + len(keys) + len(values)` ticks to execute if a dictionary is given.
# 	takes `1` tick to execute if no input is given.
# 	"""

# 	def __init__(self: Self, input: _dict[_Hashable_, _Any_] | None | Container[Hashable] = None) -> None:
# 		...

# 	def len(self: Self) -> _int:
# 		"""
# 		Returns the number of items in the dictionary.

# 		returns the length of the dictionary.

# 		takes `1` tick to execute.

# 		example usage:

# 		```
# 		my_dict = {"One": 1, "Two": 2, "Three": 3}
# 		length = len(my_dict)
# 		print(length)
# 		```

# 		Output:

# 		```
# 		3
# 		```
# 		"""
# 		...

# 	def pop(self: Self, key: Hashable) -> Any: # type: ignore
# 		"""
# 		Remove the key-value pair corresponding to the `key` in the dict

# 		returns the value of the removed key-value pair

# 		takes `1` tick to execute.

# 		example usage:

# 		```
# 		my_dict = {"One": 1, "Two": 2, "Three": 3}
# 		print("Old Value:", my_dict.pop("One"))
# 		print("Current Dict:", my_dict)
# 		```

# 		Output:

# 		```
# 		Old Value: 1
# 		Current Dict: {"Two":2,"Three":3}
# 		```
# 		"""
# 		...
# 	...


# --------------------------------------------------
# Uncomment this class if you want additional game-specific type hints and docstrings for `list` methods
# This class requires the use of of the `list()` constructor. Assigning `list` literals (ex. `[1, 2, 3]`) will cause typing conflicts with the builtin Python type `builtins.list`

# Comment out the `list` builtins import above to prevent conflict errors.

# class list[value: Any](_list):
# 	"""
# 	Builds an ordered sequence of values.

# 	list() -> new empty list

# 	list(collection: list | tuple | set | str) -> new list from the values of the provided `collection`

# 	list(collection: set | dict) -> new list from the keys of the given `collection`

# 	list(game_enum) -> new list from the values of an in-game enumm `game_enum`

# 	takes `1 + len(collection)` where `collection` is one of the above if an input is given.
# 	takes `1` tick to execute if no input is given.
# 	"""

# 	def __init__(self: Self, input: AnyIterable | None = None) -> None:
# 		...

# 	def append(self: Self, object: Any) -> None:
# 		"""
# 		Add `object` to the end of a list provided as `given_list`.

# 		takes `1` tick to execute.

# 		example usage:

# 		```
# 		my_list = [1, 2, 3]
# 		my_list.append(4)
# 		print(my_list)
# 		```

# 		Output:

# 		```
# 		[1,2,3,4]
# 		```
# 		"""
# 		...

# 	def insert(self: Self, index: _int, object: Any) -> None: # type: ignore
# 		"""
# 		Add a `object` to the specified `index` to a list provided as `given_list`.

# 		takes `1 + len(list) - index` ticks to execute

# 		example usage:

# 		```
# 		my_list = [1, 2, 3]
# 		my_list.insert(1, 4)
# 		print(my_list)
# 		```

# 		Output:

# 		```
# 		[1,4,2,3]
# 		```
# 		"""
# 		...

# 	def len(self: Self) -> _int:
# 		"""
# 		Returns the number of items in the list.

# 		returns the length of the list.

# 		takes `1` tick to execute.

# 		example usage:

# 		```
# 		my_list = [1, 2, 3]
# 		length = len(my_list)
# 		print(length)
# 		```

# 		Output:

# 		```
# 		3
# 		```
# 		"""
# 		...

# 	def pop(self: Self, index: _int) -> Any: # type: ignore
# 		"""
# 		Remove the element corresponding to the `index` in the list. If no index is specified removes the last element in the list.

# 		returns the value of the removed element

# 		takes `len(list) - index` ticks to execute if an `index` is provided
# 		takes `1` tick to execute if no `index` is provided

# 		example usage:

# 		```
# 		my_list = [1, 2, 3]
# 		print("Old Value:", my_list.pop(1))
# 		print("Current List:", my_list)
# 		```

# 		Output:

# 		```
# 		Old Value: 2
# 		Current List: [1,3]
# 		```
# 		"""
# 		...

# 	def remove(self: Self, object: Any) -> None:
# 		"""
# 		Remove the element corresponding to the `object` in the list.

# 		takes `num_comparions + num_shifts` ticks to execute

# 		example usage:

# 		```
# 		my_list = [1, 2, 3]
# 		my_list.remove(1)
# 		print(my_list)
# 		```

# 		Output:

# 		```
# 		[2,3]
# 		```
# 		"""
# 		...
# 	...


# --------------------------------------------------
# Uncomment this class if you want additional game-specific type hints and docstrings for `set` methods
# This class requires the use of of the `set()` constructor. Assigning set literals (ex. `{1, 2, 3}`) will cause typing conflicts with the builtin Python type `builtins.set`

# Comment out the `set` builtins import above to prevent conflict errors.

# class set[value: Hashable](_set):
# 	"""
# 	Builds an unordered collection of elements

# 	set() -> new empty set

# 	set(collection: list | tuple | set | str) -> new set from the values of the provided `collection`

# 	set(collection: set | dict) -> new set from the keys of the given `collection`

# 	set(game_enum) -> new set from the values of an in-game enumm `game_enum`

# 	takes `1 + len(collection)` where `collection` is one of the above if an input is given.
# 	takes `1` tick to execute if no input is given.
# 	"""

# 	def __init__(self: Self, input: AnyIterable | None = None) -> None:
# 		...

# 	def add(self: Self, object: Any) -> None:
# 		"""
# 		Add the `object` to a `given_set`.

# 		takes `1` tick to execute.

# 		example usage:

# 		```
# 		my_set = {1, 2, 3}
# 		my_set.add(4)
# 		print(my_set)
# 		```

# 		Output:

# 		```
# 		{1,2,3,4}
# 		```
# 		"""
# 		...

# 	def len(self: Self) -> _int:
# 		"""
# 		Returns the number of items in the set.

# 		returns the length of the set.

# 		takes `1` tick to execute.

# 		example usage:

# 		```
# 		my_set = {1, 2, 3}
# 		length = len(my_set)
# 		print(length)
# 		```

# 		Output:

# 		```
# 		3
# 		```
# 		"""
# 		...

# 	def remove(self: Self, object: Any) -> None:
# 		"""
# 		Remove the `object` from the set.

# 		takes `1` tick to execute.

# 		example usage:

# 		```
# 		my_set = {1, 2, 3}
# 		my_set.remove(2)
# 		print(my_set)
# 		```

# 		Output:

# 		```
# 		{1,3}
# 		```
# 		"""
# 		...
# 	...

# -------------------------------------------------------------------------------
@overload
def range(stop: _float) -> range_class:  # type: ignore
	"""
	Returns a sequence of numbers from `0` (inclusive) to `stop` (exclusive).

	returns a range object.

	takes `1` tick to execute.

	example usage:

	```
	for i in range(5):
	    print(i)
	```

	Output:

	```
	0
	1
	2
	3
	4
	```

	Note: if you wish to type hint a `range` variable use the alias `range_class` instead
	"""
	...

@overload
def range(start: _float, stop: _float) -> range_class:  # type: ignore
	"""
	Returns a sequence of numbers from `start` (inclusive) to `stop` (exclusive).

	returns a range object.

	takes `1` tick to execute.

	example usage:

	```
	for i in range(2, 5):
	    print(i)
	```

	Output:

	```
	2
	3
	4
	```

	Note: if you wish to type hint a `range` variable use the alias `range_class` instead
	"""
	...

@overload
def range(start: _float, stop: _float, step: _float) -> range_class:  # type: ignore
	"""
	Returns a sequence of numbers from `start` (inclusive) to `stop` (exclusive) every `step` interval.

	returns a range object.

	takes `1` tick to execute.

	example usage:

	```
	for i in range(2, 5, 2):
	    print(i)
	```

	Output:

	```
	2
	4
	```

	Note: if you wish to type hint a `range` variable use the alias `range_class` instead
	"""
	...

# --------------------------------------------------
"""
The following definitions are functions that mirror the methods that `lists`, `sets`, and `dicts` have. These definitions can be used as both a method and a function in TFWR.

example usage (method):

```
list_numbers = [1, 2, 3]
last_number = list_numbers.pop()
print(last_number)
```

example usage (function):

```
list_numbers = [1, 2, 3]
last_number = pop(list_numbers)
print(last_number)
```
"""

# --------------------------------------------------
def add(given_set: _set[_Hashable_], object: Any):
	"""
	Add the `object` to a `given_set`.

	takes `1` tick to execute.

	example usage:

	```
	my_set = {1, 2, 3}
	my_set.add(4)
	print(my_set)
	```

	Output:

	```
	{1,2,3,4}
	```
	"""
	...

# --------------------------------------------------
def append(given_list: _list[_Any_], object: Any):
	"""
	Add `object` to the end of a list provided as `given_list`.

	takes `1` tick to execute.

	example usage:

	```
	my_list = [1, 2, 3]
	my_list.append(4)
	print(my_list)
	```

	Output:

	```
	[1,2,3,4]
	```
	"""
	...

# --------------------------------------------------
def insert(given_list: _list[_Any_], index: _int, object: Any):
	"""
	Add a `object` to the specified `index` to a list provided as `given_list`.

	takes `1 + len(list) - index` ticks to execute

	example usage:

	```
	my_list = [1, 2, 3]
	my_list.insert(1, 4)
	print(my_list)
	```

	Output:

	```
	[1,4,2,3]
	```
	"""
	...

# --------------------------------------------------
def len(object : string | _dict[_Hashable_, _Any_] | _list[_Any_] | _set[_Hashable_] | _tuple[_Any_]) -> _int:
	"""
	Returns the number of items in the dict, list, set or str provided as `collection`.

	returns the length of the dict, list, set or str.

	takes `1` tick to execute.

	example usage:

	```
	my_list = [1, 2, 3]
	length = len(my_list)
	print(length)
	```

	Output:

	```
	3
	```
	"""
	...

# --------------------------------------------------
def pop(collection: _dict[_Hashable_, _Any_] | _list[_Any_], object: Any):
	"""
	Remove the element corresponding to the `key` in a dict or list provided as `collection`. If it is a list and no `key` is specified removes the last element in the list.

	returns the value of the removed element

	takes `len(list) - index` ticks to execute if an index is provided
	takes `1` tick to execute if no `key` is provided, of if a dict is provided

	example usage:

	```
	my_list = [1, 2, 3]
	print("Old Value:", my_list.pop(1))
	print("Current List:", my_list)
	```

	Output:

	```
	Old Value: 2
	Current List: [1,3]
	```
	"""
	...

# --------------------------------------------------
def remove(collection: _list[_Any_] | _set[_Hashable_], object: Any):
	"""
	Remove the element corresponding to the `object` in a list or set provided as `collection`.

	takes `num_comparions + num_shifts` ticks to execute if a list is provided.
	takes `1` tick to execute if a set is provided.

	example usage:

	```
	my_set = {1, 2, 3}
	my_set.remove(2)
	print(my_set)
	```

	Output:

	```
	{1,3}
	```
	"""
	...

# --------------------------------------------------
def str(object: Any) -> string:
	"""
	Converts an object to its string representation.

	returns the string representation of the object.

	takes `1` tick to execute.

	example usage:

	```
	string = str(1000)
	print(string)
	```

	Output:

	```
	"1000"
	```

	Note: if you wish to type hint a `str` variable use the alias `string` instead
	"""
	...




# -------------------------------------------------------------------------------
# In-Game Enums
# -------------------------------------------------------------------------------

# -------------------------------------------------------------------------------
class Direction:
    """
    A direction, e.g. North.
    """
    ...


# --------------------------------------------------
North = Direction()
"""
The direction north, i.e. up.
"""

East = Direction()
"""
The direction east, i.e. right.
"""

South = Direction()
"""
The direction south, i.e. down.
"""

West = Direction()
"""
The direction west, i.e. left.
"""


# -------------------------------------------------------------------------------
class Entity:
	"""
	A member of the Entities class
	"""
	...


# --------------------------------------------------
class Entities(_Enum):
	@staticmethod
	def _generate_next_value_(name: string, start: _int, count: _int, last_values: _list[_Any]) -> Entity:
		return Entity()

	Apple = _auto()
	"""
	Dinosaurs love them apparently.
	"""

	Bush = _auto()
	"""
	A small bush that drops `Items.Wood`.

	Average seconds to grow: 4
	Grows on: grassland or soil
	"""

	Cactus = _auto()
	"""
	Cacti come in 10 different sizes (0-9). When harvested, adjacent cacti that are in sorted order will also be harvested recursively.
	You receive cactus equal to the number of harvested cacti squared.

	Average seconds to grow: 1
	Grows on: soil
	"""

	Carrot = _auto()
	"""
	Carrots!

	Average seconds to grow: 6
	Grows on: soil
	"""

	Dead_Pumpkin = _auto()
	"""
	One in five pumpkins dies when it grows up, leaving behind a dead pumpkin. Dead pumpkins are useless and disappear when something new is planted.
	`can_harvest()` always returns `False` on dead pumpkins.
	"""

	Dinosaur = _auto()
	"""
	A piece of the tail of the dinosaur hat. When wearing the dinosaur hat, the tail is dragged behind the drone filling previously moved tiles.

	Average seconds to grow: 0.2
	Grows on: grassland or soil
	"""

	Grass = _auto()
	"""
	Grows automatically on grassland. Harvest it to obtain `Items.Hay`.

	Average seconds to grow: 0.5
	Grows on: grassland or soil
	"""

	Hedge = _auto()
	"""
	Part of the maze.
	"""

	Pumpkin = _auto()
	"""
	Pumpkins grow together when they are next to other fully grown pumpkins. About 1 in 5 pumpkins dies when it grows up.
	When you harvest a pumpkin you get `Items.Pumpkin` equal to the number of pumpkins in the mega pumpkin cubed.

	Average seconds to grow: 2
	Grows on: soil
	"""

	Sunflower = _auto()
	"""
	Sunflowers collect the power from the sun. Harvesting them will give you `Items.Power`.
	If you harvest a sunflower with the maximum number of petals (and there are at least 10 sunflowers) you get 5x bonus power.

	Average seconds to grow: 5
	Grows on: soil
	"""

	Treasure = _auto()
	"""
	A treasure that contains gold equal to the side length of the maze in which it is hidden. It can be harvested like a plant.
	"""

	Tree = _auto()
	"""
	Trees drop more wood than bushes. They take longer to grow if other trees grow next to them.

	Average seconds to grow: 7
	Grows on: grassland or soil
	"""


# -------------------------------------------------------------------------------
class Ground:
	"""
	A member of the Grounds class
	"""
	...


# --------------------------------------------------
class Grounds:
	@staticmethod
	def _generate_next_value_(name: string, start: _int, count: _int, last_values: _list[_Any]) -> Ground:
		return Ground()

	Grassland = _auto()
	"""
	The default ground. Grass will automatically grow on it.
	"""

	Soil = _auto()
	"""
	Calling `till()` turns the ground into this. Calling `till()` again changes it back to grassland.
	"""


# -------------------------------------------------------------------------------
class Hat:
	"""
	A member of the Hats class
	"""
	...


# --------------------------------------------------
class Hats:
	@staticmethod
	def _generate_next_value_(name: string, start: _int, count: _int, last_values: _list[_Any]) -> Hat:
		return Hat()

	Brown_Hat = _auto()
	"""
	A brown hat.
	"""

	Cactus_Hat = _auto()
	"""
	A hat shaped like a cactus.
	"""

	Carrot_Hat = _auto()
	"""
	A hat shaped like a carrot.
	"""

	Dinosaur_Hat = _auto()
	"""
	Equip it to start the dinosaur game.
	"""

	Gold_Hat = _auto()
	"""
	A golden hat.
	"""

	Gold_Trophy_Hat = _auto()
	"""
	A golden trophy hat.
	"""

	Golden_Cactus_Hat = _auto()
	"""
	A golden hat shaped like a cactus.
	"""

	Golden_Carrot_Hat = _auto()
	"""
	A golden hat shaped like a carrot.
	"""

	Golden_Gold_Hat = _auto()
	"""
	A golden version of the gold hat.
	"""

	Golden_Pumpkin_Hat = _auto()
	"""
	A golden hat shaped like a pumpkin.
	"""

	Golden_Sunflower_Hat = _auto()
	"""
	A golden hat shaped like a sunflower.
	"""

	Golden_Tree_Hat = _auto()
	"""
	A golden hat shaped like a tree.
	"""

	Gray_Hat = _auto()
	"""
	A gray hat.
	"""

	Green_Hat = _auto()
	"""
	A green hat.
	"""

	Pumpkin_Hat = _auto()
	"""
	A hat shaped like a pumpkin.
	"""

	Purple_Hat = _auto()
	"""
	A purple hat.
	"""

	Silver_Trophy_Hat = _auto()
	"""
	A silver trophy hat.
	"""

	Straw_Hat = _auto()
	"""
	The default hat.
	"""

	Sunflower_Hat = _auto()
	"""
	A hat shaped like a sunflower.
	"""

	The_Farmers_Remains = _auto()
	"""
	Unlocks the special hat 'The Farmers Remains'.
	"""

	Top_Hat = _auto()
	"""
	Unlocks the fancy Top Hat.
	"""

	Traffic_Cone = _auto()
	"""
	A traffic cone hat.
	"""

	Traffic_Cone_Stack = _auto()
	"""
	A stack of traffic cones as a hat.
	"""

	Tree_Hat = _auto()
	"""
	A hat shaped like a tree.
	"""

	Wizard_Hat = _auto()
	"""
	A magical wizard hat.
	"""

	Wood_Trophy_Hat = _auto()
	"""
	A wooden trophy hat.
	"""


# -------------------------------------------------------------------------------
class Item:
    """
    A member of the Items Class
    """
    ...


# --------------------------------------------------
class Items:
    @staticmethod
    def _generate_next_value_(name: string, start: _int, count: _int, last_values: _list[_Any]) -> Item:
        return Item()

    Bone = _auto()
    """
    The bones of an ancient creature.
    """

    Cactus = _auto()
    """
    Obtained by harvesting sorted cacti.
    """

    Carrot = _auto()
    """
    Obtained by harvesting carrots.
    """

    Fertilizer = _auto()
    """
    Call `use_item(Items.Fertilizer)` to instantly remove 2s from the plants remaining grow time.
    """

    Gold = _auto()
    """
    Found in treasure chests in mazes.
    """

    Hay = _auto()
    """
    Obtained by cutting grass.
    """

    Piggy = _auto()
    """
    This item has been removed from the game but remains as a nostalgia trophy.
    """

    Power = _auto()
    """
    Obtained by harvesting sunflowers. The drone automatically uses this to move twice as fast.
    """

    Pumpkin = _auto()
    """
    Obtained by harvesting pumpkins.
    """

    Water = _auto()
    """
    Used to water the ground by calling `use_item(Items.Water)`.
    """

    Weird_Substance = _auto()
    """
    Call `use_item(Items.Weird_Substance)` on a bush to grow a maze, or on other plants to toggle their infection status.
    """

    Wood = _auto()
    """
    Obtained from bushes and trees.
    """


# -------------------------------------------------------------------------------
class Leaderboard:
	"""
	A member of the Leaderboards class
	"""
	...


# --------------------------------------------------
class Leaderboards:
	@staticmethod
	def _generate_next_value_(name: string, start: _int, count: _int, last_values: _list[_Any]) -> Leaderboard:
		return Leaderboard()

	Cactus = _auto()
	"""
	Farm 33_554_432 cacti with multiple drones.
	"""

	Cactus_Single = _auto()
	"""
	Farm 131_072_cacti with a single drone on an 8x8 farm.
	"""

	Carrots = _auto()
	"""
	Farm 2_000_000_000 carrots with multiple drones.
	"""

	Carrots_Single = _auto()
	"""
	Farm 100_000_000 carrots with a single drone on an 8x8 farm.
	"""

	Dinosaur = _auto()
	"""
	Farm 33_488_928 bones with multiple drones.
	"""

	Fastest_Reset = _auto()
	"""
	The most prestigious category. Completely automate the game from a single farm plot to unlocking the leaderboards again.
	"""

	Hay = _auto()
	"""
	Farm 2_000_000_000 hay with multiple drones.
	"""

	Hay_Single = _auto()
	"""
	Farm 100_000_000 hay with a single drone on an 8x8 farm.
	"""

	Maze = _auto()
	"""
	Farm 9_863_168_gold with multiple drones.
	"""

	Maze_Single = _auto()
	"""
	Farm 616_448 gold with a single drone on an 8x8 farm.
	"""

	Pumpkins = _auto()
	"""
	Farm 200_000_000 pumpkins with multiple drones.
	"""

	Pumpkins_Single = _auto()
	"""
	Farm 10_000_000 pumpkins with a single drone on an 8x8 farm.
	"""

	Sunflowers = _auto()
	"""
	Farm 100_000 power with multiple drones.
	"""

	Sunflowers_Single = _auto()
	"""
	Farm 10_000 power with a single drone on an 8x8 farm.
	"""

	Wood = _auto()
	"""
	Farm 10_000_000_000 wood with multiple drones.
	"""

	Wood_Single = _auto()
	"""
	Farm 500_000_000 wood with a single drone on an 8x8 farm.
	"""


# -------------------------------------------------------------------------------
class Unlock:
	"""
	A member of the Unlocks class
	"""
	...


# --------------------------------------------------
class Unlocks:
	@staticmethod
	def _generate_next_value_(name: string, start: _int, count: _int, last_values: _list[_Any]) -> Unlock:
		return Unlock()

	Auto_Unlock = _auto()
	"""
	Automatically unlock things.
	"""

	Cactus = _auto()
	"""
	Unlock: Cactus!
	Upgrade: Increases the yield and cost of cactus.
	"""

	Carrots = _auto()
	"""
	Unlock: Till the soil and plant carrots.
	Upgrade: Increases the yield and cost of carrots.
	"""

	Costs = _auto()
	"""
	Allows access to the cost of things.
	"""

	Debug = _auto()
	"""
	Tools to help with debugging programs.
	"""

	Debug_2 = _auto()
	"""
	Functions to temporarily slow down the execution and make the grid smaller.
	"""

	Dictionaries = _auto()
	"""
	Get access to dictionaries and sets.
	"""

	Dinosaurs = _auto()
	"""
	Unlock: Majestic ancient creatures.
	Upgrade: Increases the yield and cost of dinosaurs.
	"""

	Expand = _auto()
	"""
	Unlock: Expands the farm land and unlocks movement.
	Upgrade: Expands the farm. This also clears the farm.
	"""

	Fertilizer = _auto()
	"""
	Reduces the remaining growing time of the plant under the drone by 2 seconds.
	"""

	Functions = _auto()
	"""
	Define your own functions.
	"""

	Grass = _auto()
	"""
	Increases the yield of grass.
	"""

	Hats = _auto()
	"""
	Unlocks new hat colors for your drone.
	"""

	Import = _auto()
	"""
	Import code from other files.
	"""

	Leaderboard = _auto()
	"""
	Join the leaderboard for the fastest time in farming a specific crop or for the fastest reset of the farm.
	"""

	Lists = _auto()
	"""
	Use lists to store lots of values.
	"""

	Loops = _auto()
	"""
	Unlocks a simple while loop.
	"""

	Mazes = _auto()
	"""
	Unlock: A maze with a treasure in the middle.
	Upgrade: Increases the gold in treasure chests.
	"""

	Megafarm = _auto()
	"""
	Unlocks multiple drones and drone management functions.
	"""

	Operators = _auto()
	"""
	Arithmetic, comparison and logic operators.
	"""

	Plant = _auto()
	"""
	Unlocks planting.
	"""

	Polyculture = _auto()
	"""
	Use companion planting to increase the yield.
	"""

	Pumpkins = _auto()
	"""
	Unlock: Pumpkins!
	Upgrade: Increases the yield and cost of pumpkins.
	"""

	Senses = _auto()
	"""
	The drone can see what's under it and where it is.
	"""

	Simulation = _auto()
	"""
	Unlocks simulation functions for testing and optimization.
	"""

	Speed = _auto()
	"""
	Increases the speed of the drone.
	"""

	Sunflowers = _auto()
	"""
	Unlock: Sunflowers and Power.
	Upgrade: Increases the power gained from sunflowers.
	"""

	The_Farmers_Remains = _auto()
	"""
	Unlocks the special hat 'The Farmers Remains'.
	"""

	Timing = _auto()
	"""
	Functions to help measure performance.
	"""

	Top_Hat = _auto()
	"""
	Unlocks the fancy Top Hat.
	"""

	Trees = _auto()
	"""
	Unlocks trees.
	Upgrade: Increases the yield of bushes and trees.
	"""

	Utilities = _auto()
	"""
	Unlocks the `min()`, `max()` and `abs()` functions.
	"""

	Variables = _auto()
	"""
	Assign values to variables.
	"""

	Watering = _auto()
	"""
	Water the plants to make them grow faster.
	"""





# -------------------------------------------------------------------------------
# Crop Management
# -------------------------------------------------------------------------------

# -------------------------------------------------------------------------------
def harvest() -> _bool:
	"""
	Harvests the entity under the drone.
	If you harvest an entity that can't be harvested, it will be destroyed.

	returns `True` if an entity was removed, `False` otherwise.

	takes `200` ticks to execute if an entity was removed, `1` tick otherwise.

	example usage:

	```
	harvest()
	```
	"""
	...


# --------------------------------------------------
def can_harvest() -> _bool:
	"""
	Used to find out if plants are fully grown.

	returns `True` if there is an entity under the drone that is ready to be harvested, `False` otherwise.

	takes `1` tick to execute.

	example usage:

	```
	if can_harvest():
		harvest()
	```
	"""
	...


# --------------------------------------------------
def plant(entity: Entity) -> _bool:
	"""
	Spends the cost of the specified `entity` and plants it under the drone.
	It fails if you can't afford the plant, the ground type is wrong or there's already a plant there.

	returns `True` if it succeeded, `False` otherwise.

	takes `200` ticks to execute if it succeeded, `1` tick otherwise.

	example usage:

	```
	plant(Entities.Bush)
	```
	"""
	...


# --------------------------------------------------
def swap(direction: Direction) -> _bool:
	"""
	Swaps the entity under the drone with the entity next to the drone in the specified `direction`.

	- Doesn't work on all entities.
	- Also works if one (or both) of the entities are `None`.

	returns `True` if it succeeded, `False` otherwise.

	takes `200` ticks to execute on success, `1` tick otherwise.

	example usage:

	```
	swap(North)
	```
	"""
	...


# --------------------------------------------------
def till() -> None:
	"""
	Tills the ground under the drone into soil. If it's already soil it will change the ground back to grassland.

	returns `None`

	takes `200` ticks to execute.

	example usage:

	```
	till()
	```
	"""
	...


# --------------------------------------------------
def use_item(item: Item, n: _int = 1) -> _bool:
	"""
	Attempts to use the specified `item` `n` times. Can only be used with some items including `Items.Water`, `Items.Fertilizer` and `Items.Weird_Substance`.

	returns `True` if an item was used, `False` if the item can't be used or you don't have enough.

	takes `200` ticks to execute if it succeeded, `1` tick otherwise.

	example usage:

	```
	if use_item(Items.Fertilizer):
		print("Fertilizer used successfully")
	```
	"""
	...


# --------------------------------------------------
def clear() -> None:
	"""
	Removes everything from the farm, moves the drone back to position `(0,0)` and changes the hat back to the default.

	returns `None`

	takes `200` ticks to execute.

	example usage:

	```
	clear()
	```
	"""
	...


# --------------------------------------------------
def change_hat(hat: Hat) -> None:
	"""
	Changes the hat of the drone to the specified `hat`.

	returns `None`

	takes `200` ticks to execute.

	example usage:

	```
	change_hat(Hats.Dinosaur_Hat)
	```
	"""
	...




# -------------------------------------------------------------------------------
# Movement
# -------------------------------------------------------------------------------

# -------------------------------------------------------------------------------
def move(direction: Direction) -> _bool:
	"""
	Moves the drone into the specified `direction` by one tile.
	If the drone moves over the edge of the farm it wraps back to the other side of the farm.

	- `East ` = right
	- `West ` = left
	- `North` = up
	- `South` = down

	returns `True` if the drone has moved, `False` otherwise.

	takes `200` ticks to execute if the drone has moved, `1` tick otherwise.

	example usage:

	```
	move(North)
	```
	"""
	...


# --------------------------------------------------
def can_move(direction: Direction) -> _bool:
	"""
	Checks if the drone can move in the specified `direction`.

	returns `True` if the drone can move, `False` otherwise.

	takes `1` tick to execute.

	example usage:

	```
	if can_move(North):
	    move(North)
	```
	"""
	...


# --------------------------------------------------
def get_pos_x() -> _int:
	"""
	Gets the current x position of the drone.
	The x position starts at `0` in the `West` and increases in the `East` direction.

	returns a number representing the current x coordinate of the drone.

	takes `1` tick to execute.

	example usage:

	```
	x, y = get_pos_x(), get_pos_y()
	```
	"""
	...


# --------------------------------------------------
def get_pos_y() -> _int:
	"""
	Gets the current y position of the drone.
	The y position starts at `0` in the `South` and increases in the `North` direction.

	returns a number representing the current y coordinate of the drone.

	takes `1` tick to execute.

	example usage:

	```
	x, y = get_pos_x(), get_pos_y()
	```
	"""
	...


# --------------------------------------------------
def get_world_size() -> _int:
	"""
	Get the current size of the farm.

	returns the side length of the grid in the north to south direction.

	takes `1` tick to execute.

	example usage:

	```
	for i in range(get_world_size()):
	    move(North)
	```
	"""
	...




# -------------------------------------------------------------------------------
# Senses
# -------------------------------------------------------------------------------

# -------------------------------------------------------------------------------
def get_entity_type() -> Entity | None:
	"""
	Find out what kind of entity is under the drone.

	returns `None` if the tile is empty, otherwise returns the type of the entity under the drone.

	takes `1` tick to execute.

	example usage:

	```
	if get_entity_type() == Entities.Grass:
	    harvest()
	```
	"""
	...


# --------------------------------------------------
def get_ground_type() -> Ground:
	"""
	Find out what kind of ground is under the drone.

	returns the type of the ground under the drone.

	takes `1` tick to execute.

	example usage:

	```
	if get_ground_type() != Grounds.Soil:
	    till()
	```
	"""
	...


# --------------------------------------------------
def get_water() -> _float:
	"""
	Get the current water level under the drone.

	returns the water level under the drone as a number between `0` and `1`.

	takes `1` tick to execute.

	example usage:

	```
	if get_water() < 0.5:
	    use_item(Items.Water)
	```
	"""
	...


# --------------------------------------------------
def num_items(item: Item) -> _int | _float:
	"""
	Find out how much of `item` you currently have.

	returns the number of `item` currently in your inventory.
	`Items.Power` may return a number as float

	takes `1` tick to execute.

	example usage:

	```
	if num_items(Items.Fertilizer) > 0:
	    use_item(Items.Fertilizer)
	```
	"""
	...


# --------------------------------------------------
def get_companion() -> _tuple[Entity, _tuple[_int, _int]] | None:
	"""
	Get the companion preference of the plant under the drone.

	returns a tuple of the form `(companion_type, (companion_x_position, companion_y_position))` or `None` if there is no companion.

	takes `1` tick to execute.

	example usage:

	```
	companion = get_companion()
	if companion != None:
	    plant_type, (x, y) = companion
	    print("Companion:", plant_type, "at", x, ",", y)
	```
	"""
	...


# --------------------------------------------------
def measure(direction: Direction | None = None) -> _int | _tuple[_int, _int] | None:
	"""
	Can measure some values on some entities. The effect of this depends on the entity.
	Will work anynore inside of a maze and only on a `Entities.Apple`

	overloads:
	`measure()`: measures the entity under the drone.
	`measure(direction)`: measures the neighboring entity in the `direction` of the drone.

	Sunflower: returns the number of petals.
	Maze: returns the position of the current treasure from anywhere in the maze.
	Cactus: returns the size.
	Dinosaur: returns the number corresponding to the type.
	All other entities: returns `None`.

	takes `1` tick to execute.

	example usage:

	```
	num_petals = measure()
	treasure_pos = measure()
	```
	"""
	...





# -------------------------------------------------------------------------------
# Megafarm
# -------------------------------------------------------------------------------

# -------------------------------------------------------------------------------
class Drone:
    """
    A class representing a spawned drone given a task to execute.
    """
    ...

# -------------------------------------------------------------------------------
def spawn_drone(task: Callable[[], Any], *args: _Any) -> Drone:
	"""
	Spawns a new drone in the same position as the drone that ran `spawn_drone(task, *args)`. The new drone then begins executing the specified `task` function. The rest of the arguments are copied and passed into the specified function. After the drone is done, it will disappear automatically.

	returns a `Drone` object for the new drone or `None` if all drones are already spawned.

	takes `200` ticks to execute if a drone was spawned, `1` otherwise.

	example:
	```
	def harvest_column(message):
		for _ in range(get_world_size()):
			harvest()
			move(North)
		print(message)

	i = 0
	while True:
		if spawn_drone(harvest_column, i):
			move(East)
			i = (i + 1) % 10
	```
	"""
	...


# --------------------------------------------------
def wait_for(drone: Drone) -> Any:
	"""
	Waits until the given `drone` terminates.

	returns the return value of the function that the `drone` was running.

	takes `1 + remaining task ticks` remaining in the given drone's task function.
	takes `1` tick to execute if the awaited `drone` is already done.

	example:

	```
	def get_entity_type_in_direction(dir):
		move(dir)
		return get_entity_type()

	def zero_arg_wrapper():
		return get_entity_type_in_direction(North)
	handle = spawn_drone(zero_arg_wrapper)
	print(wait_for(handle))
	```
	"""
	...


# --------------------------------------------------
def has_finished(drone: Drone) -> _bool:
	"""
	Checks if the given 1drone1 has finished.

	returns `True` if the drone has finished, `False` otherwise.

	takes `1` tick to execute.

	example:

	```
	drone = spawn_drone(function)
	while not has_finished(drone):
		do_something_else()
	result = wait_for(drone)
	```
	"""
	...


# --------------------------------------------------
def max_drones() -> _int:
	"""
	Gets the maximum number of drones available on the farm.

	returns the maximum number of drones that you can have in the farm.

	takes `1` tick to execute.

	example:

	```
	while num_drones() < max_drones():
		spawn_drone("some_file_name")
		move(East)
	```
	"""
	...


# --------------------------------------------------
def num_drones() -> _int:
	"""
	Gets the current number of drones running a task on the farm.

	returns the number of drones currently in the farm.

	takes `1` tick to execute.

	example:

	```
	while num_drones() < max_drones():
		spawn_drone("some_file_name")
		move(East)
	```
	"""
	...




# -------------------------------------------------------------------------------
# Debug
# -------------------------------------------------------------------------------

# -------------------------------------------------------------------------------
def get_time() -> _float:
	"""
	Get the current game time.

	returns the time in seconds since the start of the game.

	takes `0` tick to execute.

	example usage:

	```
	start = get_time()
	do_something()
	time_passed = get_time() - start
	```
	"""
	...


# --------------------------------------------------
def get_tick_count() -> _int:
	"""
	Used to measure the number of ticks performed.

	returns the number of ticks performed since the start of execution.

	takes `0` tick to execute.

	example usage:

	```
	do_something()
	print(get_tick_count())
	```
	"""
	...


# --------------------------------------------------
def set_execution_speed(speed: _float) -> None:
	"""
	Limits the speed at which the program is executed to better see what's happening.

	- A `speed` of `1` is the speed the drone has without any speed upgrades.
	- A `speed` of `10` makes the code execute `10` times faster and corresponds to the speed of the drone after `9` speed upgrades.
	- A `speed` of `0.5` makes the code execute at half of the speed without speed upgrades. This can be useful to see what the code is doing.

	If `speed` is faster than the execution can currently go it will just go at max speed.

	If `speed` is `0` or negative, the speed is changed back to max speed.
	The effect will also stop when the execution stops.

	returns `None`

	takes `200` ticks to execute.

	example usage:

	```
	set_execution_speed(1)
	```
	"""
	...


# --------------------------------------------------
def set_world_size(size: _float) -> None:
	"""
	Limits the size of the farm to better see what's happening.
	Also clears the farm and resets the drone position.

	- Sets the farm to a `size` x `size` grid.
	- The smallest `size` possible is `3`.
	- A `size` smaller than `3` will change the grid back to its full size.
	- The effect will also stop when the execution stops.

	returns `None`

	takes `200` ticks to execute.

	example usage:

	```
	set_world_size(5)
	```
	"""
	...


# --------------------------------------------------
type SimulateUnlocks = _dict[Unlock, _int] | _tuple[_tuple[Unlock, _int]] | _list[_tuple[Unlock, _int]] | _tuple[Unlock] | _list[Unlock] | Unlocks

def simulate(
		filename: string,
		sim_unlocks: SimulateUnlocks,
		sim_items: _dict[Item, _float],
		sim_globals: _dict[string, Any],
		seed: _float, speedup: _float
	) -> _float:
	"""
	Starts a simulation for the leaderboard using the specified `file_name` as a starting point.

	`sim_unlocks`: A sequence containing the starting unlocks. These unlocks can be one of these:

	- `dict[Unlock, int]` - Example: `{Unlocks.Expand: 2, Unlocks.Cactus: 1}`
	- `tuple[tuple[Unlock, int]]` - Example: `((Unlocks.Expand, 2), (Unlocks.Cactus, 1))`
	- `list[tuple[Unlock, int]]` - Example: `[(Unlocks.Expand, 2), (Unlocks.Cactus, 1)]`
	- `tuple[Unlock]` - Captures your current unlock level of specific unlocks from your main farm. Example: `(Unlocks.Expand, Unlocks.Cactus)`
	- `list[Unlock]` - Captures your current unlock level of specific unlocks from your main farm. Example: `[Unlocks.Expand, Unlocks.Cactus]`
	- `Unlocks` - Captures all of your current unlock levels from your main farm.

	`sim_items`: A dict mapping items to amounts. The simulation starts with these items.

	`sim_globals`: A dict mapping variable names to values. The simulation starts with these variables in the global scope. Make sure any variables assigned in here are not assigned in the simulation code as that will override the vales from this dict.

	`seed`: The random seed of the simulation. Must be a positive integer.

	`speedup`: The starting speedup. The simulation may not reach the stated `speedup` value if it cannot properly speedup computation. Common causes for this include use of multiple drones or eating up too many ticks in a loop per iteration (for example a wait loop using pass).

	returns the time it took to run the simulation.

	takes `200` ticks to execute.

	example usage:

	```
	filename = "f1"
	sim_unlocks = Unlocks
	sim_items = {Items.Carrot : 10000, Items.Hay : 50}
	sim_globals = {"a" : 13}
	seed = 0
	speedup = 64
	run_time = simulate(filename, sim_unlocks, sim_items, sim_globals, seed, speedup)
	```
	"""
	...




# -------------------------------------------------------------------------------
# Auto Unlock
# -------------------------------------------------------------------------------

# -------------------------------------------------------------------------------
def get_cost(thing: Entity | Item | Unlock, level: _int | None = None) -> _dict[Item, _int] | None:
	"""
	Gets the cost of a `thing`

	If `thing` is an entity: get the cost of planting it.
	If `thing` is an unlock: get the cost of unlocking it at the specified level.

	- returns a dictionary with items as keys and numbers as values. Each item is mapped to how much of it is needed.
	- returns `None` for unlocks that are already unlocked (when no level specified).
	- The optional `level` parameter specifies the upgrade level for unlocks.

	takes `1` tick to execute.

	example usage:

	```
	cost = get_cost(Unlocks.Carrots)
	for item in cost:
	    if num_items(item) < cost[item]:
	        print('not enough items to unlock carrots')
	```
	"""
	...


# --------------------------------------------------
def unlock(unlock: Unlock) -> _bool:
	"""
	Has exactly the same effect as clicking the button corresponding to `unlock` in the research tree.

	returns `True` if the unlock was successful, `False` otherwise.

	takes `200` ticks to execute if it succeeded, `1` tick otherwise.

	example usage:

	```
	unlock(Unlocks.Carrots)
	```
	"""
	...


# --------------------------------------------------
def num_unlocked(thing: Unlock | Entity | Ground | Item | Hat) -> _int:
	"""
	Used to check if an unlock, entity, ground, item or hat is already unlocked.

	returns `1` plus the number of times `thing` has been upgraded if `thing` is upgradable. Otherwise returns `1` if `thing` is unlocked, `0` otherwise.

	takes `1` tick to execute.

	example usage:

	```
	if num_unlocked(Unlocks.Carrots) > 0:
	    plant(Entities.Carrot)
	else:
	    print("Carrots not unlocked yet")
	```
	"""
	...




# -------------------------------------------------------------------------------
# Math
# -------------------------------------------------------------------------------

# -------------------------------------------------------------------------------
def random() -> _float:
	"""
	Samples a random number between 0 (inclusive) and 1 (exclusive).

	returns the random number.

	takes `1` ticks to execute.

	example usage:

	```
	def random_elem(list):
	    index = random() * len(list) // 1
	    return list[index]
	```
	"""
	...


# --------------------------------------------------
def min(*args: Any) -> Any:
	"""
	Gets the minimum of a sequence of elements or several passed arguments.
	Can be used on numbers and strings.

	`min(a,b,c)`: Returns the minimum of `a`, `b` and `c`.
	`min(sequence)`: Returns the minimum of all values in a sequence.

	returns the minimum value from the arguments.
	"""
	...


# --------------------------------------------------
def max(*args: Any) -> Any:
	"""
	Gets the maximum of a sequence of elements or several passed arguments.
	Can be used on numbers and strings.

	`max(a,b,c)`: Returns the maximum of `a`, `b` and `c`.
	`max(sequence)`: Returns the maximum of all values in a sequence.

	returns the maximum value from the arguments.
	"""
	...


# --------------------------------------------------
def abs(x: _float) -> _float:
	"""
	Returns the absolute value of a number.

	returns the absolute value of x.

	takes `1` tick to execute.

	example usage:

	```
	positive = abs(-5)
	print(positive)
	```

	Output:

	```
	5
	```
	"""
	...




# -------------------------------------------------------------------------------
# Utility
# -------------------------------------------------------------------------------

# -------------------------------------------------------------------------------
def print(*something: _Any) -> None:
	"""
	Prints `something` into the air above the drone using smoke. This action is not affected by speed upgrades.
	Multiple values can be printed at once.

	returns `None`

	takes 1s to execute.

	example usage:

	```
	print('ground:', get_ground_type())
	```
	"""
	...


# --------------------------------------------------
def quick_print(*something: _Any) -> None:
	"""
	Prints a value just like `print()` but it doesn't stop to write it into the air so it can only be found on the output page.

	returns `None`

	takes `0` ticks to execute.

	example usage:

	```
	quick_print('hi mom')
	```
	"""
	...




# -------------------------------------------------------------------------------
# Miscelaneous
# -------------------------------------------------------------------------------

# -------------------------------------------------------------------------------
def do_a_flip() -> None:
	"""
	Makes the drone do a flip! This action is not affected by speed upgrades.

	returns `None`

	takes 1s to execute.

	example usage:

	```
	while True:
		do_a_flip()
	```
	"""
	...


# --------------------------------------------------
def pet_the_piggy() -> None:
	"""
	Pets the piggy! This action is not affected by speed upgrades.

	returns `None`

	takes 1s to execute.

	example usage:

	```
	while True:
		pet_the_piggy()
	```
	"""
	...


# --------------------------------------------------
def leaderboard_run(leaderboard: Leaderboard, file_name: string, speedup: _float) -> None:
	"""
	Starts a timed run for the `leaderboard` using the specified `file_name` as a starting point.
	`speedup` sets the starting speedup.

	returns `None`

	takes `200` ticks to execute.

	example usage:

	```
	leaderboard_run(Leaderboards.Fastest_Reset, "full_run", 256)
	```
	"""
	...
