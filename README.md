This is a repository containing all the text for the game "The Farmer Was Replaced". It allows community members to submit translation corrections and improvements.
The default translations are machine translations. They are reasonably good, but there are sometimes errors, especially in the shorter strings.
Any corrections are greatly appreciated.

# Files
Each language folder contains a `Strings` folder and a `docs` folder. The `Strings` folder contains various strings from the UI and tooltips. 
The `docs` folder contains markdown files that will be displayed in the game's info window.

# Format
Unlike in regular markdown, there are no triple backticks for multi-line code blocks. Single backticks also work across multiple lines.

The `Strings` folder contains `.txt` files containing multiple strings. Each string starts with an @ and can contain newlines. 
The strings support backticks \` to mark code blocks, just like the markdown files. Other markdown features are not supported in the strings.

In both markdown files and string files you may find things enclosed in curly braces or double curly braces like {0} and {{ something }}. 
These are placeholders and will be replaced at runtime.

# Translation Guidelines
Some parts of the game cannot be translated because they are part of the code you write, and obviously it doesn't make sense to break code when switching languages. So in general, code shouldn't be translated.

For consistency, code elements such as "dictionary" and "while" should also not be translated, even if they are referenced outside of code blocks.

Names of items, entities, grounds, unlocks and leaderboards cannot be translated either, because things like 'Items.Carrot' are also a part of the code. 
However, if these things are referred to in normal text, it's fine to translate them if it makes sense.

Templating placeholders like {0} and {{ something }} should never be replaced. Changing them would break things.

If anyone disagrees with these guidelines please let me know and we can still change them.

# How to contribute
To contribute, simply create a pull request with your translation changes. 
Make sure you include the name you want to be credited with in the PR. Otherwise you will be credited under your GitHub name.
