import inspect
import time
import traceback
from typing import Any,Callable

def asserEqual(returned:Any, expected:Any, message: str) -> None:
    assert returned == expected, \
        f"""{message}\n\t\t🎯 EXPECT: {expected}\n\t\t❌ RETURN: {returned}"""

def assertNotEqual(returned:Any, notExpected:Any, message: str) -> None:
    assert returned != notExpected, \
        f"""{message}\n\t\t🎯 EXPECT NOT: {notExpected}\n\t\t❌ RETURN: {returned}"""

def test(fnToTest:Callable[[],Any]):
    """
    Decorates a single fonction to test automatically
    without having to call anything for launching test.
    # Sample
    ```python
    @test
    def do_something():
        ...
    ```
    """
    def test_decorator():
        print(f"🧪 Unit {fnToTest.__name__} from {inspect.getfile(fnToTest)}:{inspect.getsourcelines(fnToTest)[1]} ... ", end="")
        error = None
        start_time = time.perf_counter()
        result = None
        try:
            result = fnToTest()
        except Exception as e:
            error = traceback.format_exc()
        end_time = time.perf_counter()
        total_time = end_time - start_time
        if error == None:
            print(f'✅ after {total_time:.4f} secs')
        else:
            print(f"❌ after {total_time:.4f} secs:")
            print(f"\t⚠️  {str(error)}")

        return (error==None)
    return test_decorator()
    
def tests(classToTest):
    """
    Run all methods of a class decorated 
    with @tests decorator as soon as test()
    method is called from this class.

    # Sample
    ```python
    @tests
    class ManyTestsToPerform:
        def test1_something_first():
            ...
        def test2_this_then():
            ...

    # Launching tests 🚀
    ManyTestsToPerform().test()
    ```
    """
    mainTestMethodName = "test"
    breakOnFirstError = True
    def tests_decorator():
        
        print(f"⏳ Starting {classToTest.__name__} from {inspect.getfile(classToTest)}:{inspect.getsourcelines(classToTest)[1]}")
        nErrors, nTests = 0,0
        start_time = time.perf_counter()
        for member in inspect.getmembers(classToTest):
            unitTestMethodName:str = member[0]
            unitTestMethod:Any = member[1]
            # to remove private and protected functions
            # and other methods that start with a underscore
            # as well as this function
            if unitTestMethodName.startswith('_'): continue
            if unitTestMethodName == mainTestMethodName: continue
            nTests+=1
            # Test method and count errors
            if not test(unitTestMethod): 
                nErrors+=1
                if breakOnFirstError:
                    break
        end_time = time.perf_counter()
        total_time = end_time - start_time
        if ( nErrors == 0 ): print('✅', end="")
        else: print('❌', end="")
        print(f' Passed {nTests-nErrors}/{nTests} test(s) of {classToTest.__name__} after {total_time:.4f} secs\n')
        if ( nErrors > 0 and breakOnFirstError ):
            exit(0)
    setattr(classToTest, mainTestMethodName, tests_decorator)
    return classToTest
