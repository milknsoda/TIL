
# 함수(function)

<center>
    <img src="./images/03/func.png", alt="func.png">
</center>

## 들어가기전에

> 직사각형의 둘레와 면적을 구하는 코드를 작성해주세요.

```python
height = 30
width = 20
```

---
```
예시 출력)
직사각형 둘레: 100, 면적: 600입니다.
```


```python
height = 30
width = 20
# 아래에 코드를 작성하세요.
area = height * width
perimeter = 2 * (height + width)
print(f'직사각형 둘레: {perimeter}, 면적: {area}입니다.')
```

    직사각형 둘레: 100, 면적: 600입니다.
    

* 앞서 작성한 코드에서 매번 사각형의 둘레와 면적을 구하기 위해서는 변수에 값을 바꾸거나 코드를 복사 붙여넣기 해야합니다.
* 코드가 많아질수록 문제가 발생할 확률이 높아지며, 유지 보수하기도 힘들어진다.

<center>
    <img src="./images/03/emc2.png", alt="programming principle">
</center>

<center>
    <img src="./images/03/principle.png", alt="programming principle">
</center>

## 함수의 선언과 호출

```python
def func(parameter1, parameter2):
    code line1
    code line2
    return value
```

* 함수 선언은 `def`로 시작하여 `:`으로 끝나고, 다음은 `4spaces 들여쓰기`로 코드 블록을 만듭니다.

* 함수는 `매개변수(parameter)`를 넘겨줄 수도 있습니다.

* 함수는 동작후에 `return`을 통해 결과값을 전달 할 수도 있습니다. (`return` 값이 없으면, None을 반환합니다.)

* 함수는 호출을 `func(val1, val2)`와 같이 합니다.




```python
# 위의 사각형 면적을 반환 코드를 함수로 아래에 작성해보세요
def rectangle(height, width):
    area = height * width
    perimeter = 2 * (height + width)
    return f'직사각형 둘레: {perimeter}, 면적: {area}입니다.'
    
rectangle(width, height)
```




    '직사각형 둘레: 100, 면적: 600입니다.'




```python
print(rectangle(100, 100))
print(rectangle(40, 50))
```

    직사각형 둘레: 400, 면적: 10000입니다.
    직사각형 둘레: 180, 면적: 2000입니다.
    

<center>
    <img src="./images/03/func_des.png", alt="function descrpition">
</center>

<center>
    <img src="./images/03/function_ex.png", alt="function_example">
</center>


```python
# 우리가 활용하는 print문도 파이썬에 지정된 함수입니다. 
# 아래에서 'hi'는 parameter이고 출력을 하게 됩니다.
print('hi')
```

<center>
    <img src="./images/03/built_in.png", alt="built_in">
</center>

[출처: python 공식문서](https://docs.python.org/3/library/functions.html)


```python
# 내장함수 목록을 직접 볼 수도 있습니다.
dir(__builtins__)
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




```python
dir('i')
```




    ['__add__',
     '__class__',
     '__contains__',
     '__delattr__',
     '__dir__',
     '__doc__',
     '__eq__',
     '__format__',
     '__ge__',
     '__getattribute__',
     '__getitem__',
     '__getnewargs__',
     '__gt__',
     '__hash__',
     '__init__',
     '__init_subclass__',
     '__iter__',
     '__le__',
     '__len__',
     '__lt__',
     '__mod__',
     '__mul__',
     '__ne__',
     '__new__',
     '__reduce__',
     '__reduce_ex__',
     '__repr__',
     '__rmod__',
     '__rmul__',
     '__setattr__',
     '__sizeof__',
     '__str__',
     '__subclasshook__',
     'capitalize',
     'casefold',
     'center',
     'count',
     'encode',
     'endswith',
     'expandtabs',
     'find',
     'format',
     'format_map',
     'index',
     'isalnum',
     'isalpha',
     'isascii',
     'isdecimal',
     'isdigit',
     'isidentifier',
     'islower',
     'isnumeric',
     'isprintable',
     'isspace',
     'istitle',
     'isupper',
     'join',
     'ljust',
     'lower',
     'lstrip',
     'maketrans',
     'partition',
     'replace',
     'rfind',
     'rindex',
     'rjust',
     'rpartition',
     'rsplit',
     'rstrip',
     'split',
     'splitlines',
     'startswith',
     'strip',
     'swapcase',
     'title',
     'translate',
     'upper',
     'zfill']



## 함수를 만들어봅시다.

> 아래의 코드와 동일한 `my_max`함수를 만들어주세요.
>
> 정수를 두개 받아서, 큰 값을 출력합니다. 

```python
max(1, 5)
```
---
```
예상 출력)
5가 더 큽니다
```



```python
# max(1, 5)를 호출 해봅시다.
max(1, 5)
```




    5




```python
# 여기에 my_max 함수를 만들어주세요.
def my_max(x, y):
    if x > y:
        print(x)
        return x
    elif x < y:
        print(y)
        return y
    else:
        print('서로 같다.')
```


```python
# 그리고 호출 해봅시다.
my_max(2, 8)
```

    8
    




    8




```python
def my_max2(a, b):
    return a if a > b else b
```


```python
my_max2(9919, 512513)
```




    512513




```python
def my_func(a, b):
    return a, b
```


```python
my_func(1, 'a') # 숫자와 문자 두 개를 반환하는 것처럼 보이지만, 실제로는 tuple이다. 즉 하나의 객체!!!
```




    (1, 'a')




```python
type(my_func(1,'a'))
```




    tuple



# 함수의 return

앞서 설명한 것과 마찬가지로 함수는 반환되는 값이 있으며, 이는 어떠한 종류의 객체여도 상관없습니다. 
 
단, 오직 한 개의 객체만 반환됩니다.

함수가 return 되거나 종료되면, 함수를 호출한 곳으로 돌아갑니다.

## 함수를 정의하고 값을 반환해봅시다.

> 함수는 모든 객체를 리턴할 수 있습니다. 
> 
> 리스트 두개를 받아 각각 더한 결과를 비교하여 값이 큰 리스트를 반환합니다.

```python
my_list_max([10, 3], [5, 9])
```
---
```
예상 출력)
[5, 9]
```



```python
# 여기에 my_list_max 함수를 만들어주세요.
def my_list_max(list1, list2):
    if sum(list1) > sum(list2):
        print(list1)
    else:
        print(list2)
#     print(list1 if sum(list1) > sum(list2) else list2)
```


```python
my_list_max([1, 2, 4], [1, 2, 3])
```

    [1, 2, 4]
    

# 함수의 인수

함수는 `인자(parameter)`를 넘겨줄 수 있습니다.

* 인수(arguments) : 함수 호출할 때
> `func(a, b)` => `a`와 `b`
* 인자(parameter) : 함수 정의할 때
> `def func(x, y)` => `x`와 `y`

## 위치 인수

함수는 기본적으로 인수를 위치로 판단합니다.


```python
# 알고 있는 수학 공식의 함수를 하나만 만들어보세요.
def my_sub(a, b):
    # a, b = 1, 3
    # a, b = 3, 1
    return a - b
```


```python
my_sub(1, 3)
```




    -2




```python
my_sub(3, 1)
```




    2




```python
my_sub()
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-54-078ed5892caf> in <module>
    ----> 1 my_sub()
    

    TypeError: my_sub() missing 2 required positional arguments: 'a' and 'b'



```python
my_sub(1)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-55-fce120493363> in <module>
    ----> 1 my_sub(1)
    

    TypeError: my_sub() missing 1 required positional argument: 'b'



```python
my_sub(, 3)
```


      File "<ipython-input-56-fd8ce127a645>", line 1
        my_sub(, 3)
               ^
    SyntaxError: invalid syntax
    


<center>
    <img src="./images/03/func_ex_01.png", alt="function example 02">
</center>

## 기본 값(Default Argument Values)

함수가 호출될 때, 인자를 지정하지 않아도 기본 값을 설정할 수 있습니다. 

**활용법**
```python
def func(p1=v1):
    return p1
```

### 기본 값 활용 예제

> 이름을 받아서 다음과 같이 인사하는 함수 greeting을 만들어보세요. 이름이 길동이면, "길동, 안녕?" 이름이 없으면 "익명, 안녕?" 으로 출력해주세요.


```python
# 아래에 greeting 함수를 만들어보세요.
def greeting(name='익명'):
    print(f'{name}, 안녕?')
```


```python
greeting()
```

    익명, 안녕?
    


```python
greeting('너')
```

    너, 안녕?
    

* 기본 인자 값이 설정되어 있더라도 기존의 함수와 동일하게 호출 가능합니다.
<center>
    <img src="./images/03/func_ex_02.png", alt="function example 02">
</center>

* 호출시 인자가 없으면 기본 인자 값이 활용됩니다.
<center>
    <img src="./images/03/func_ex_03.png", alt="function example 03">
</center>

* 단, 기본 매개변수 이후에 기본 값이 없는 매개변수를 사용할 수는 없습니다.


```python
# 오류를 확인해봅시다.
def greeting(name='익명', age):
    print(f'{name}은 {age}살!')
```


      File "<ipython-input-58-8f5b9429363b>", line 2
        def greeting(name='익명', age):
                    ^
    SyntaxError: non-default argument follows default argument
    



```python
# 수정해 봅시다.
def greeting(age, name='익명'):
    print(f'{name}은(는) {age}살!')
```


```python
greeting(12, '명수')
greeting(79)
```

    명수은(는) 12살!
    익명은(는) 79살!
    

## 키워드 인자(Keyword Arguments)

키워드 인자는 직접적으로 변수의 이름으로 특정 인자를 전달할 수 있습니다.


```python
# 키워드 인자 예시
print('123', end='\t') # end='' 과 같은 부분이 키워드 인자!!
print('123', end='\t')
```

    123	123	

* 단 아래와 같이 활용할 수는 없습니다. 키워드 인자를 활용한 뒤에 위치 인자를 활용할 수는 없습니다.


```python
# 확인 해봅시다.
print(end=',', '123') # 위치 인자 먼저, 키워드 인자는 뒤로
```


      File "<ipython-input-70-25406e9dd3d3>", line 2
        print(end=',', '123') # 위치 인자 먼저, 키워드 인자는 뒤로
                      ^
    SyntaxError: positional argument follows keyword argument
    


우리가 주로 활용하는 `print()` 함수는 [파이썬 표준 라이브러리의 내장함수](https://docs.python.org/ko/3.6/library/functions.html) 중 하나이며, 다음과 같이 구성되어 있다.

<br>
<br>
<center>
    <img src="./images/03/print.png", alt="print">
</center>


```python
# print 함수를 활용 해봅시다.
print('안녕', '하세요', sep='/', end='끝!')
```

    안녕/하세요끝!

## 가변 인자 리스트

앞서 설명한 `print()`처럼 정해지지 않은 임의의 숫자의 인자를 받기 위해서는 가변인자를 활용합니다. 

가변인자는 `tuple` 형태로 처리가 되며, `*`로 표현합니다. 

**활용법**

```python
def func(*args):
```


```python
# 가변 인자 예시 (print문은 *obejcts를 통해 임의의 숫자의 인자를 모두 처리합니다.)
print('hi', '안녕', 'Gutne Tag', '곤니치와', sep=',')
```

    hi,안녕,Gutne Tag,곤니치와
    


```python
# args는 tuple!
def my_func(*args):
    print(type(args))
    print(args, sep='/', end='끝!')
```


```python
my_func(1, 2, 3, 'a')
```

    <class 'tuple'>
    (1, 2, 3, 'a')끝!

### 가변인자 리스트를 사용해봅시다.

> 정수를 여러 개 받아서 가장 큰 값을 반환(return)하는 `my_max()`을 만들어주세요.

```python
my_max(10, 20, 30, 50)
```
---
```
예시출력)
50
```


```python
max(1, 2, 3, 4)
```




    4




```python
# 아래에 코드를 작성해주세요.
def my_max(*args):
    max_num = 1e-10
    for i in args:
        if max_num < i:
            max_num = i
#         max_num = i if m < i else m
    return max_num

```


```python
# 함수를 호출 해보세요.
my_max(10000, 128102, 1234517, 12231, 6134875, 5738796, 5674523)
```




    6134875




```python
def my_max2(*args):
    max_value = args[0] # 비교할 값을 선언하는 것 자체가 정확하지 않을 수 있기 때문에 첫번째 값을 그냥 할당하는 것이 정확함!!!
    # 하나씩 반복하면서, 큰 값을 기록한다.
    for value in args:
#     for idx, value in enumerate(args):  # 이런 식으로도 첫번째 값을 지정해줄 수 있다.
#         if idx == 0:                    #
#             max_value = value           #
        # 만약에 큰 값보다 지금 값이 더 크면, 값을 바꾼다.
        if value > max_value:
            max_value = value
    # 반복문이 끝나면 반환한다.
    return max_value
```


```python
my_max2(123, 112366, 175447, 54266, 2725643, 43137215, 1461576593, 1252345)
```




    1461576593



## 정의되지 않은 인자들 처리하기

정의되지 않은 인자들은 `dict` 형태로 처리가 되며, `**`로 표현합니다. 

주로 `kwagrs`라는 이름을 사용하며, `**kwargs`를 통해 인자를 받아 처리할 수 있습니다.

**활용법**

```python
def func(**kwargs):
```

우리가 dictionary를 만들 때 사용할 수 있는 `dict()` 함수는 [파이썬 표준 라이브러리의 내장함수](https://docs.python.org/ko/3.6/library/functions.html) 중 하나이며, 다음과 같이 구성되어 있다.
<br>
<br>
<center>
    <img src="./images/03/dict.png", alt="dictionary">
</center>


```python
# 딕셔너리 생성 함수 예시
dict(사과='apple', 바나나='banana', 고양이='cat')
```




    {'사과': 'apple', '바나나': 'banana', '고양이': 'cat'}




```python
def my_fdict(**kwargs):
    print(type(kwargs))
    print(kwargs)
```


```python
my_fdict(사과='apple')
```

    <class 'dict'>
    {'사과': 'apple'}
    

### 정의되지 않은 인자를 처리해봅시다. 

> `my_dict()` 함수를 만들어 실제로 dictionary 모습으로 출력 함수를 만들어보세요.
>
>

```
예시 출력)
한국어: 안녕, 영어: hi
```


```python
# 아래에 코드를 작성해주세요.
def my_dict(**kwargs):
    count = 0
    for key, value in kwargs.items():
        count += 1
#         if count == len(kwargs):
#             print(f"'{key}': '{value}'")
#         else:
#             print(f"'{key}': '{value}'", end=',')
        print(f"'{key}': '{value}'") if count == len(kwargs) else print(f"'{key}': '{value}'", end=',')
    # 리스트로 만들어서 푸는 방법
    result = []
    for key, value in kwargs.items():
        result.append(f'{key} : {value}')
    print(result)
    print(', '.join(result)) # '무언가'.join(대상) 무언가로 대상을 연결한다. 
```


```python
# 함수를 호출 해보세요.
my_dict(한국어='안녕', 영어='hi')
```

    '한국어': '안녕','영어': 'hi'
    ['한국어 : 안녕', '영어 : hi']
    한국어 : 안녕, 영어 : hi
    


```python
# 사실은 dict()는 출력이 아니라 딕셔너리를 리턴(반환)합니다. 
# 리턴하는 my_fake_dict를 만들어주세요.
def my_fake_dict(**kwargs):
    return kwargs    
```


```python
my_fake_dict(한국어='안녕', 영어='hi')
```




    {'한국어': '안녕', '영어': 'hi'}



## dictionary를 인자로 넘기기(unpacking arguments list)

`**dict`를 통해 함수에 인자를 넘길 수 있습니다.


```python
my_dict = {'한국어': '안녕','영어': 'hi'}
my_fake_dict(**my_dict)
```




    {'한국어': '안녕', '영어': 'hi'}



### 회원가입 검증 예제

> 회원가입 로직을 검증하는 코드를 작성 해봅시다. 

* signup 함수는 `username`, `password`, `password_confirmation`을 인자로 받습니다.
* `password`가 8자리 이상인지 확인을 합니다.
* `password`와 `password_confirmation`이 일치하는지 확인을 합니다.


```python
my_account = {
    'username': '홍길동',
    'password': '1q2w3e4r',
    'password_confirmation': '1q2w3e4r'
}
```


```python
# signup 함수를 작성 해주세요.
# def signup(**kwargs):
#     if 'username' in kwargs and 'password' in kwargs:
#         if len(kwargs['password']) >= 8:
#             if kwargs['password'] != kwargs['password_confirmation']:
#                 print('비밀번호가 일치하지 않습니다.')
#             else:
#                 print('정상적으로 가입되었습니다.')
#         else:
#             print('비밀번호는 8자리 이상 입력해주세요.')
            
def signup(username, password, password_confirmation):
    if len(password) >= 8:
        if password != password_confirmation:
            print('비밀번호가 일치하지 않습니다.')
        else:
            print('정상적으로 가입되었습니다.')
    else:
        print('비밀번호는 8자리 이상 입력해주세요.')
```


```python
def signup(username, password, password_confirmation):
    if len(password) < 8:
        return False
    else:
        if password == password_confirmation:
            return True
        else:
            return False
```


```python
# signup 함수를 my_account를 넘겨 확인 해보세요.
signup(**my_account)
```




    True




```python
signup('홍길동', '123qwe1q', '123qwe1q')
```




    True




```python
signup('123qwe1q', '123qwe1q', '홍길동')
```




    False




```python
signup(username='홍길동', password='123qwe1q', password_confirmation='123qwe1q')
```




    True




```python
signup(password='123qwe1q', password_confirmation='123qwe1q', username='홍길동')
```




    True



###  URL 편하게 만들기

> url 패턴을 만들어 문자열을 반환하는  `my_url` 함수를 만들어봅시다.
>
> 영진위에서 제공하는 일별 박스오피스 API 서비스는 다음과 같은 방식으로 요청을 받습니다.

```
기본 요청 URL : http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?
```

* key : 발급받은 키값(abc)
* targetDt : yyyymmdd
* itemPerPage : 1 ~ 10 **기본 10**


```
예시)
my_url(key='abc', targetDt='yyyymmdd')

api = {
    'key': 'abc',
    'targetDt': 'yyyymmdd'
}
my_url(**api)

예시 출력)
'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?itemPerPage=10&key=abc&targetDt=yyyymmdd&'
```


```python
# 여기에 코드를 작성해주세요.
```

### URL 검증하기

> 이제 우리는 만들어진 요청 보내기전에 URL을 검증해야합니다. 
>
> 앞선 설명을 참고하여 검증 로직을 구현하고 문자열을 반환하세요.

```
> 아래의 두가지 상황만 만들도록 하겠습니다. <

key, targetDt가 없으면, '필수 요청변수가 누락되었습니다.'

itemPerPage의 범위가 1~10을 넘어가면, '1~10까지의 값을 넣어주세요.'
```


```python
# 여기에 코드를 작성해주세요
```

## 이름공간 및 스코프(Scope)

파이썬에서 사용되는 이름들은 이름공간(namespce)에 저장되어 있습니다.
그리고, LEGB Rule을 가지고 있습니다. 

변수에서 값을 찾을 때 아래와 같은 순서대로 이름을 찾아나갑니다.
* `L`ocal scope: 정의된 함수
* `E`nclosed scope: 상위 함수 
* `G`lobal scope: 함수 밖의 변수 혹은 import된 모듈
* `B`uilt-in scope: 파이썬안에 내장되어 있는 함수 또는 속성


```python
# 따라서 첫시간에 내장함수의 식별자를 사용할 수 없었던 예제에서 오류가 생기는 이유를 확인할 수 있습니다.
print(str(4))
str = 4
print(str(4))
```

    4
    


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-176-8c23451a07ab> in <module>
          2 print(str(4))
          3 str = 4
    ----> 4 print(str(4))
    

    TypeError: 'int' object is not callable


* `str()` 코드가 실행되면
* str을 Global scope에서 먼저 찾아서 `str = 4`를 가져오고, 
* 이는 함수가 아니라 변수이기 때문에 `not callable`하다라는 오류를 내뱉게 됩니다.
* 우리가 원하는 `str()`은 Built-in scope에 있기 때문입니다.


```python
del str
```


```python
# print(a)에 무엇이 출력되는지 확인해보세요.
a = 1
def localscope(a):
    print(a)
    
localscope(3)
print(a)
```

    3
    1
    


```python
# 전역 변수를 바꿀 수 있을까요?
```


```python
global_num = 3
def localscope2():
    global_num = 5
    print(f'global_num이 {global_num}으로 설정되었습니다.')
print(global_num)
localscope2()
print(global_num)
```

    3
    global_num이 5으로 설정되었습니다.
    3
    


```python
def localscope3():
    takhee = 'takhee'
    return None

localscope3()
print(takhee)
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-180-c5b36322916f> in <module>
          4 
          5 localscope3()
    ----> 6 print(takhee)
    

    NameError: name 'takhee' is not defined



```python
for takhee in range(3):  # global scope!! 함수 안이랑 다름
    print(takhee)

print(takhee)
```

    0
    1
    2
    2
    


```python
# 굳이 전역에 있는 변수를 바꾸고 싶다면, 아래와 같이 선언할 수 있습니다.
global_num = 5
def localscope4():
    global global_num
    global_num = 3
    print('local에서 설정함', global_num)
print(global_num)
localscope4()
print(global_num)
```

    5
    local에서 설정함 3
    3
    


```python
# 만약 로컬 스코프에서 내가 글로벌 값을 쓰고 싶다면, 인자로 넘겨라!!!
global_num = 5
def localscope5(g):
    print(g)

localscope(global_num)
```

    5
    


```python
# 만약 로컬 스코프에 있는 값을 글로벌에서 쓰고 싶다면, 리턴을 해라!!!

def localscope6():
    global_num = 6
    return global_num

global_num = localscope6()
print(global_num)
```

    6
    

이름공간은 각자의 수명주기가 있습니다.

* built-in scope : 파이썬이 실행된 이후부터 끝까지 

* Global scope : 모듈이 호출된 시점 이후 혹은 이름 선언된 이후부터 끝까지

* Local/Enclosed scope : 함수가 실행된 시점 이후부터 리턴할때 까지

# 재귀 함수(recursive function)

재귀 함수는 함수 내부에서 자기 자신을 호출 하는 함수를 뜻한다.

## 팩토리얼 계산

> `팩토리얼(factorial)`을 계산하는 함수 `fact(n)`를 작성해봅시다. 
>
> n은 1보다 큰 정수라고 가정하고, 팩토리얼을 계산한 값을 반환합니다.

$$
\displaystyle n! = \prod_{ k = 1 }^{ n }{ k }
$$

$$
\displaystyle n! = 1*2*3*...*(n-1)*n
$$

---
```
예시 출력)
120
```


```python
# 아래에 코드를 작성해주세요.
```


```python
fact(5)
```

## 재귀를 이용한 팩토리얼 계산

```
1! = 1
2! = 1 * 2 = 1! * 2 
3! = 1 * 2 * 3 = 2! * 3
```


```python
# 아래에 코드를 작성해주세요.
```


```python
factorial(5)
```

## 반복문과 재귀함수
```
factorial(3)
3 * factorail(2)
3 * 2 * factorial(1)
3 * 2 * 1
3 * 2
6
```

* 두 코드 모두 원리는 같다! 

```
반복문 코드:
    n이 1보다 큰 경우 반복문을 돌며, n은  1씩 감소한다. 
    마지막에 n이 1이면 더 이상 반복문을 돌지 않는다.
  
재귀 함수 코드:
    재귀 함수를 호출하며, n은 1씩 감소한다. 
    마지막에 n이 1이면 더 이상 추가 함수를 호출을 하지 않는다.
```


* 재귀 함수는 기본적으로 같은 문제이지만 점점 범위가 줄어드는 문제를 풀게 된다.

* 재귀함수를 작성시에는 반드시, `base case`가 존재 하여야 한다. 

* `base case`는 점점 범위가 줄어들어 반복되지 않는 최종적으로 도달하는 곳이다. 

재귀를 이용한 팩토리얼 계산에서의 base case는 n이 1일때, 함수가 아닌 정수 반환하는 것이다.

* 자기 자신을 호출하는 재귀함수는 알고리즘 구현시 많이 사용된다.
* 코드가 더 직관적이고 이해하기 쉬운 경우가 있음. (하지만, 만들기는 어려움)
* [Python Tutor](https://goo.gl/k1hQYz)에 보면, 함수가 호출될 때마다 메모리 공간에 쌓이는 것을 볼 수 있다. 
* 이 경우, 메모리 스택이 넘치거나(Stack overflow) 프로그램 실행 속도가 늘어지는 단점이 생긴다.
* 파이썬에서는 이를 방지하기 위해 1,000번이 넘어가게 되면 더이상 함수를 호출하지 않고, 종료된다.


```python
# 여기에서 오류를 확인 해봅시다.
```

## 피보나치 수열

> 피보나치 수열은 다음과 같은 점화식이 있다. 
>
> 피보나치 값을 리턴하는 두가지 방식의 코드를 모두 작성해보자.

$$
\displaystyle F_0 = F_1 = 1
$$

$$
F_n=F_{n-1}+F_{n-2}\qquad(n\in\{2,3,4,\dots\})
$$

1) `fib(n)` : 재귀함수

2) `fib_loop(n)` : 반복문 활용한 함수

---
```
예시 입력)
fib(10)

예시 호출)
89
```


```python
# 재귀를 이용한 코드를 작성해주세요.
```


```python
fib(4)
```


```python
# 반복문을 이용한 코드를 작성해주세요.
```


```python
fib_loop(4)
```

## 반복문과 재귀 함수의 차이


```python
# 큰 숫자를 재귀로 짜여진 fib()함수의 인자로 넘겨보세요.
```


```python
# 100배 되는 숫자를 반복문으로 짜여진 fib_loop()인자로 넘겨보세요.
```

#### 속도의 차이를 느껴보자


###### for문이 더 빠른데 왜 재귀씀? (https://kldp.org/node/134556)
- 알고리즘 자체가 재귀적인 표현이 자연스러운 경우
- 재귀 호출은 '변수 사용'을 줄여줄 수 있다.

## 실습문제 - 하노이의 탑

> 다음은 하노이의 탑이다. 
>
> 하노이의 탑을 풀이하는 해법(한쪽 탑의 원판을 다른 탑으로 모두 옮기는 법을 출력하는 함수를 만드세요.
> 
> 참고링크 : https://ko.khanacademy.org/computing/computer-science/algorithms/towers-of-hanoi/a/towers-of-hanoi

<br>
<br>
<center>
    <img src="./images/03/hanoi.gif", alt="">
</center>

1. 한 번에 한개의 층만을 다른 기둥으로 옮길 수 있다
2. 옮기려는 기둥에는 아무것도 없거나 옮기려는 층보다 큰 층이 있을 경우에만 옮길 수 있다
3. 옮기려는 기둥에 옮기려는 층보다 작은 층이 이미 있을 경우 그 기둥으로 옮길 수 없다.
4. 가능한 적은 회수로 전체 탑을 다른 기둥으로 옮긴다.


```python
# 아래에 코드를 작성해주세요.
```
