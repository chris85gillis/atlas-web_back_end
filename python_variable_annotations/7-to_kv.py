#!/usr/bin/env python3
"""Return a tuple with k and the square of v."""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple with k and the square of v."""
    return (k, float(v ** 2))
