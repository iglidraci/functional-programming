from decimal import Decimal
from typing import Text


def remove(string: Text, chars: Text):
    if chars:
        return remove(string.replace(chars[0], ''), chars[1:])
    return string


print(remove('igli,igli;', ',;'))
