
# 데이터 구조
* 시퀀스 자료형
* set, dictionary
* 제어문

##  문제 1.
* 아래 보기 중, 변경할 수 있는(mutable) 것과 변경 불가능한 것(immutable)을 분류하시오.

`String`    `List`    `Tuple`    `Range`    `Set`    `Dictionary`


```python
string = '안녕하세요'
ls = list(string)
tp = (1, 2, 3)
r = range(10)
s = {1, 2, 3, 4}
d = {'가': 1, '나': 2, '다': 3}

# string[0] = 1 # => 오류!!!
ls[0] = 2 or ls.append() # => 변경 가능 (id값이 변하지 않음)
# tp[0] = 3 # => 오류!!!
# r[0] = 4 # => 오류!!!
s.update(5) # => 변경 가능 (id값이 변하지 않음)
d['가'] = 6 # => 변경 가능
print(string, ls, tp, r, s, d)
```

    안녕하세요 [2, '녕', '하', '세', '요'] (1, 2, 3) range(0, 10) {1, 2, 3, 4, 5} {'가': 1, '나': 2, '다': 3, 0: 6}


## 문제 2.
* range와 slicing을 활용하여 1부터 50까지 숫자 중 홀수로 이루어진 리스트를 만드시오.


```python
a = range(1, 51)
print(list(a[0::2]))
```

    [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]


## 문제 3.
* 반 학생들의 정보를 이용하여 key는 이름, value는 나이인 딕셔너리를 만드시오.


```python
class_1 = {'조선행': 27, '최무연': 28, '서현택': 27}
print(class_1.keys())
print(class_1.values())
```

    dict_keys(['조선행', '최무연', '서현택'])
    dict_values([27, 28, 27])
