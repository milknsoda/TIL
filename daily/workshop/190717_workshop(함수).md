
# 함수
* 조건문 및 반복문에 대한 이해
* 함수에 대한 이해

## 문제
* Palindrome은 앞에서부터 읽었을 때와 뒤에서부터 읽었을 때 같은 단어를 뜻한다. 따라서, 'a' 'nan' '토마토' 모두 palindrome에 해당합니다.
* 단어를 입력받아 Palindrome을 검증하고 True나 False를 리턴하는 함수 palindrome(word)를 만들어보세요.


```python
def palindrome(word):
    r_word = ''
    for alph in word:
        r_word = alph + r_word
    # r_word = word[::-1] => 거꾸로 뒤집기(거의 모든 것을 뒤집을 수 있음)
    if r_word == word:
        return True
    else:
        return False
```


```python
palindrome('word')
```




    False




```python
palindrome('wow')
```




    True




```python
def palindrome2(word):
    # word 단어를 처음값 - 끝값 => len(word) // 2
    for i in range(len(word)//2):
        # 단어의 처음 - 끝을 비교해서 다르면 False 리턴하고 더이상 확인하지 않는다.
        if word[i] != word[-i-1]:
            return False
    # 다 끝나면 팰린드롬이 맞으니까 True 리턴
    return True
```


```python
palindrome2('12342341')
```




    False




```python
def palindrome3(word):
    return True if word == word[::-1] else False
```


```python
palindrome3('wow')
```




    True




```python
def palindrome4(word):
    return word == word[::-1]
```


```python
palindrome4('wow')
```




    True


