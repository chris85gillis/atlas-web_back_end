#!/usr/bin/env python3
"""Calculate the sum of integers and floats in a mixed list."""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Calculate the sum of integers and floats in a mixed list."""
    return sum(mxd_lst)
