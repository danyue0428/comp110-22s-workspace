"""Union type gives felxibility to singe vars."""

from typing import Union


def log(info: Union[str, int]) -> None:
    """Info can be str or int!"""
    # single parameters, and pass different types of values to it
    if isinstance(info, str):
        print(f"str: {info}")
    else:
        print(f"int: {info}")
        
        
log("hello110")
log(110)

