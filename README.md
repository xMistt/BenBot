# BenBot
Python wrapper for BenBot.

[![Requires: Python 3.x](https://img.shields.io/pypi/pyversions/BenBot-async.svg)](https://pypi.org/project/BenBot-async/)
[![BenBot Version: 0.0.3](https://img.shields.io/pypi/v/BenBot-async.svg)](https://pypi.org/project/BenBot-async/)

## Installing:
### Synchronous:
Windows: ``py -3 -m pip install BenBot``<br>
Linux/macOS: ``python3 -m pip install BenBot``

### Asynchronous:
Windows: ``py -3 -m pip install BenBotAsync``<br>
Linux/macOS: ``python3 -m pip install BenBotAsync``

## Example:
```
import BenBot

BenSearch = BenBot.getSkinId("Ghoul Trooper")
print(BenSearch)
```

This would output:<br>
```CID_029_Athena_Commando_F_Halloween```

The list of functions is on the Wiki.
