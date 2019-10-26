# BenBot
Python wrapper for BenBot.

[![Requires: Python 3.x](https://img.shields.io/pypi/pyversions/BenBot.svg)](https://pypi.org/project/BenBot/)
[![BenBot Version: 0.0.3](https://img.shields.io/pypi/v/BenBot.svg)](https://pypi.org/project/BenBot/)

## Installing:
### Synchronous:
Windows: ``py -3 -m pip install BenBot``<br>
Linux/macOS: ``python3 -m pip install BenBot``

### Asynchronous:
Windows: ``py -3 -m pip install AsyncBenBot``<br>
Linux/macOS: ``python3 -m pip install AsyncBenBot``

## Example:
```
import BenBot

BenSearch = BenBot.getSkinId("Ghoul Trooper")
print(BenSearch)
```

This would output:<br>
```CID_029_Athena_Commando_F_Halloween```

The list of functions is on the Wiki.
