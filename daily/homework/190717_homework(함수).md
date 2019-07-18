
# 함수
* 제어문
* 함수의 선언과 호출

## 문제
* Python에서 기본으로 사용할 수 있는 Built in function 5개를 찾아서 작성하세요.


```python
import pprint
pprint.pprint(dir(__builtin__))
```

    ['ArithmeticError',
     'AssertionError',
     'AttributeError',
     'BaseException',
     'BlockingIOError',
     'BrokenPipeError',
     'BufferError',
     'BytesWarning',
     'ChildProcessError',
     'ConnectionAbortedError',
     'ConnectionError',
     'ConnectionRefusedError',
     'ConnectionResetError',
     'DeprecationWarning',
     'EOFError',
     'Ellipsis',
     'EnvironmentError',
     'Exception',
     'False',
     'FileExistsError',
     'FileNotFoundError',
     'FloatingPointError',
     'FutureWarning',
     'GeneratorExit',
     'IOError',
     'ImportError',
     'ImportWarning',
     'IndentationError',
     'IndexError',
     'InterruptedError',
     'IsADirectoryError',
     'KeyError',
     'KeyboardInterrupt',
     'LookupError',
     'MemoryError',
     'ModuleNotFoundError',
     'NameError',
     'None',
     'NotADirectoryError',
     'NotImplemented',
     'NotImplementedError',
     'OSError',
     'OverflowError',
     'PendingDeprecationWarning',
     'PermissionError',
     'ProcessLookupError',
     'RecursionError',
     'ReferenceError',
     'ResourceWarning',
     'RuntimeError',
     'RuntimeWarning',
     'StopAsyncIteration',
     'StopIteration',
     'SyntaxError',
     'SyntaxWarning',
     'SystemError',
     'SystemExit',
     'TabError',
     'TimeoutError',
     'True',
     'TypeError',
     'UnboundLocalError',
     'UnicodeDecodeError',
     'UnicodeEncodeError',
     'UnicodeError',
     'UnicodeTranslateError',
     'UnicodeWarning',
     'UserWarning',
     'ValueError',
     'Warning',
     'WindowsError',
     'ZeroDivisionError',
     '__IPYTHON__',
     '__build_class__',
     '__debug__',
     '__doc__',
     '__import__',
     '__loader__',
     '__name__',
     '__package__',
     '__spec__',
     'abs',
     'all',
     'any',
     'ascii',
     'bin',
     'bool',
     'breakpoint',
     'bytearray',
     'bytes',
     'callable',
     'chr',
     'classmethod',
     'compile',
     'complex',
     'copyright',
     'credits',
     'delattr',
     'dict',
     'dir',
     'display',
     'divmod',
     'enumerate',
     'eval',
     'exec',
     'filter',
     'float',
     'format',
     'frozenset',
     'get_ipython',
     'getattr',
     'globals',
     'hasattr',
     'hash',
     'help',
     'hex',
     'id',
     'input',
     'int',
     'isinstance',
     'issubclass',
     'iter',
     'len',
     'license',
     'list',
     'locals',
     'map',
     'max',
     'memoryview',
     'min',
     'next',
     'object',
     'oct',
     'open',
     'ord',
     'pow',
     'print',
     'property',
     'range',
     'repr',
     'reversed',
     'round',
     'set',
     'setattr',
     'slice',
     'sorted',
     'staticmethod',
     'str',
     'sum',
     'super',
     'tuple',
     'type',
     'vars',
     'zip']
    

`ArithmeticError`, `AssertionError`, `AttributeError`, `BaseException`, `BlockingIOError`, `BrokenPipeError`, `BufferError`, `BytesWarning`, `ChildProcessError`, `ConnectionAbortedError`, `ConnectionError`, `ConnectionRefusedError`, `ConnectionResetError`, `DeprecationWarning`, `EOFError`, `Ellipsis`, `EnvironmentError`, `Exception`, `False`, `FileExistsError`, `FileNotFoundError`, `FloatingPointError`, `FutureWarning`, `GeneratorExit`, `IOError`, `ImportError`, `ImportWarning`, `IndentationError`, `IndexError`, `InterruptedError`, `IsADirectoryError`, `KeyError`, `KeyboardInterrupt`, `LookupError`, `MemoryError`, `ModuleNotFoundError`, `NameError`, `None`, `NotADirectoryError`, `NotImplemented`, `NotImplementedError`, `OSError`, `OverflowError`, `PendingDeprecationWarning`, `PermissionError`, `ProcessLookupError`, `RecursionError`, `ReferenceError`, `ResourceWarning`, `RuntimeError`, `RuntimeWarning`, `StopAsyncIteration`, `StopIteration`, `SyntaxError`, `SyntaxWarning`, `SystemError`, `SystemExit`, `TabError`, `TimeoutError`, `True`, `TypeError`, `UnboundLocalError`, `UnicodeDecodeError`, `UnicodeEncodeError`, `UnicodeError`, `UnicodeTranslateError`, `UnicodeWarning`, `UserWarning`, `ValueError`, `Warning`, `WindowsError`, `ZeroDivisionError`, `__IPYTHON__`, `__build_class__`, `__debug__`, `__doc__`, `__import__`, `__loader__`, `__name__`, `__package__`, `__spec__`, `abs`, `all`, `any`, `ascii`, `bin`, `bool`, `breakpoint`, `bytearray`, `bytes`, `callable`, `chr`, `classmethod`, `compile`, `complex`, `copyright`, `credits`, `delattr`, `dict`, `dir`, `display`, `divmod`, `enumerate`, `eval`, `exec`, `filter`, `float`, `format`, `frozenset`, `get_ipython`, `getattr`, `globals`, `hasattr`, `hash`, `help`, `hex`, `id`, `input`, `int`, `isinstance`, `issubclass`, `iter`, `len`, `license`, `list`, `locals`, `map`, `max`, `memoryview`, `min`, `next`, `object`, `oct`, `open`, `ord`, `pow`, `print`, `property`, `range`, `repr`, `reversed`, `round`, `set`, `setattr`, `slice`, `sorted`, `staticmethod`, `str`, `sum`, `super`, `tuple`, `type`, `vars`, `zip`

## 문제
* 다음과 같이 함수가 정의되어 있다. 보기 중, 오류가 발생하는 코드를 고르시오.


```python
def ssafy(name, location='서울'):
    print(f'{name}의 지역은 {location}입니다.')

ssafy(location='대전', name='철수')
ssafy('길동', location='광주')
ssafy(name='허준', '구미') # 오류 발생! 키워드 인자는 위치 인자 뒤쪽으로 가야한다.
ssafy('구미', name='허준') # 오류 발생! '구미'와 '허준'이 모두 name 인자에 할당되어 오류가 난다.
```

    철수의 지역은 대전입니다.
    길동의 지역은 광주입니다.
    


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-8-20d29b567d60> in <module>
          4 ssafy(location='대전', name='철수')
          5 ssafy('길동', location='광주')
    ----> 6 ssafy('구미', name='허준') # 오류 발생! 키워드 인자는 위치 인자 뒤쪽으로 가야한다.
    

    TypeError: ssafy() got multiple values for argument 'name'


## 문제
* 다음과 같이 코드가 작성되어 있을 때, 변수 result에 저장된 값을 작성하시오.


```python
def my_func(a, b):
    c = a + b
    print(c)

result = my_func(4, 7)
print(result)
```

    11
    None
    

* `my_func()` 함수는 return 값을 지정해주지 않았기 때문에 `None`이 저장되어 있다.
