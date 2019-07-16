# 문제 1번

* Python에서 사용할 수 없는 식별자(예약어)를 찾아 작성하세요.

```python
import keyword
print(keyword.kwlist)

# 결과
#['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
```

* `False` `None` `True` `and` `as` `assert` `async` `await` `break` `class` `continue` `def` `del` `elif` `else` `except` `finally` `for` `from` `global` `if` `import` `in` `is` `lambda` `nonlocal` `not` `or` `pass` `raise` `return` `try` `while` `with` `yield`

# 문제 2번

* 파이썬에서 float는 실수를 표현하는 과정에서 같은 값으로 일치되지 않습니다. (`floating point rounding error`)

* 따라서, 아래의 값을 비교하기 위해 작성해야하는 코드를 작성하세요.

  ```python
  a = 0.1 * 3
  b = 0.3
  
  # 풀이
  if abs(a-b) <= 2e-16:
      print('a와 b는 같다.')
  ```

  * 두 값의 차이의 절대값이 아주 작은 수보다 작다면 두 값이 서로 같다고 생각할 수 있다.



# 문제 3번

* 이스케이프 문자열 중 1) 줄바꿈 2) 탭 3) \ 을 작성하세요

```
\n => 줄바꿈
\t => 탭
\\ => \

print('H\ni\t\\')
# 결과
H
i	\
```



#  문제 4번

* *"안녕, 철수야"*를 `string interpolation`을 사용하여 출력하세요.

```python
name = '철수'
print(f'안녕, {name}야')

# 결과
안녕, 철수야
```



# 문제 5번

* 다음 중 형변환시 오류가 발생하는 것은?

  * 1) str(1)	2) int('30')	3) int(5)	4) bool('50')	**5) int('3.5')**

  ```python
  str(1) # => '1'
  int('30') # => 30
  int(5) # => 5
  bool('50') # => True
  int('3.5') # => 오류가 난다.
  ```

  ```
  --------------------------------------------------------------------
  ValueError                        Traceback (most recent call last)
  <ipython-input-10-6ec468255209> in <module>
        3 int(5) # => 5
        4 bool('50') # => True
  ----> 5 int('3.5') # => 오류가 난다.
  
  ValueError: invalid literal for int() with base 10: '3.5'
  
  ```
  
  

