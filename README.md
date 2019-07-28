# [Cryptopals Challenges](https://cryptopals.com)
Currently in progress solutions to the Cryptopals challenges written in Python 3.

## Requirements
- Python 3

_Note: I can't guarantee that the code will run correctly in Python 2 since this was all written and tested under Python 3._

## Organization
Challenges are organized in this repository in the same way that they are on the Cryptopals website with a sets directory with individual directories for each solution containing all necessary files, like so:
```
set1/
  challenge1/
    solution.py
    extra.txt
    README.md
  challenge2/
  challenge3/
  ...
set2/
...
```

Each challenge has it's own README with some details on problem and the approach to the solution.

## Running the code
Challenges should be run inividually from within there corresponding directory like so:

`$ python3 solution.py`

Some challenges make assumptions about where to locate data files they may be using and may not work if run outside of their directory.
