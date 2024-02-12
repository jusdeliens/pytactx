import inspect
import time
from typing import Any,Callable

def caller(depthStack:int or None=None):
    """
    Returns the name of the caller block, e.g. if
    calling from a function, caller() will return
    the name of this function

    ## Arguments
    `depthStack` - If None or 0, will return the name 
    of the caller block. If 1, will return the name of
    the caller's caller. And so on
    """
    if ( depthStack == None ):
        depthStack = 1
    else:
        depthStack += 1
    return inspect.stack()[1][3]

def benchmark(fnToBenchmark:Callable[...,Any]):
    """
    Decorates any function to assess the execution
    time taken in seconds.
    # Sample
    ```python
    @benchmark
    def do_something():
        ...
    ```
    """
    def benchmark_decorator(*args, **kwargs):
        start_time = time.perf_counter()
        result = fnToBenchmark(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'Function {fnToBenchmark.__name__}{args} {kwargs} Took {total_time:.4f} seconds')
        return result
    return benchmark_decorator

