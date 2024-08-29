from typing import Callable, TypeVar
from functools import wraps

T = TypeVar("T",int,float) # only expected int or float 


def decorator_func(func: Callable) -> Callable:
    """
    The @wraps(func) decorator is used to ensure that the wrapper function keeps the
    metadata (such as the name and docstring) of the original function func

    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Wrapper function")

        return func(*args, **kwargs)

    return wrapper


@decorator_func
def add(a: T, b: T) -> T:
    return a + b


if __name__ == "__main__":
    add(1, "a")
