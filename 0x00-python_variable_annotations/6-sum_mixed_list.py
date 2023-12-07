#!/usr/bin/env python3

"""
    Write a type-annotated function
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """

    Args:
        mxd_lst: int and float

    Returns:
        float
    """
    return float(sum(mxd_lst))
