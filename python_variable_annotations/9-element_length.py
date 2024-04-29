#!/usr/bin/env python3
"""Calculate the length of each element in the input list."""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Calculate the length of each element in the input list."""
    return [(i, len(i)) for i in lst]
