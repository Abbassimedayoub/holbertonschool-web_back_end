#!/usr/bin/env python3
""" Complex types_functions """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ define the function make_multiplier """

    def mult_func(n: float):
        return n * multiplier
    return mult_func
