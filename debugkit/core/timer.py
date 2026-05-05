import time 
from functools import wraps
from ..style.colors import *
def timer(func):
    @wraps(func)
    def wrapper(*args , **kwargs):
        start = time.time()

        result = func(*args , **kwargs)
        end = time.time()
        elapsed = end - start
        print(f"{GREEN}[TIMER]{RESET} {func.__name__} took {elapsed:.4f}s")
        return result
    return wrapper
