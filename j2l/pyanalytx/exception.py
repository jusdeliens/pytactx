import inspect
import time

def toBeImplemented(message=None):
    """
    Raise an exception NotImplementedError
    To be used in interface method bodies or 
    anywhere else where a todo is required
    before use.
    """
    stack = inspect.stack()
    if ( message == None ):
        message = ""
    elif (len(message) > 0 and message[0] != "\n"):
        message = "\n" + message        
    raise NotImplementedError(f"🚧 {stack[1][3]}() not implemented yet!{message}")


def retry(maxRetries=1, sleepBetween=1):
    """
    Decorates any function to be called maxRetries
    time if an exception is raised
    ## Sample
    ```python
    @retry(maxRetries=2, sleepBetween=1)
    def might_fail():
        print("might_fail")
        raise Exception
    ```
    """
    def retry_decorator(func):
        def __wrapper(*args, **kwargs):
            for _ in range(maxRetries):
                try:
                    func(*args, **kwargs)
                except:
                    time.sleep(sleepBetween)
        return __wrapper
    return retry_decorator