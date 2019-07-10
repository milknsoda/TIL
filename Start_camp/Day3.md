# Python 기본 코딩

## 1. 입출력

* 문자열을 입력받아 문자열의 첫 글자와 마지막 글자를 출력하는 프로그램을 작성하시오.

  ```python
  string = input('문자를 입력하세요: ')
  
  print(string[0])
  print(string[-1])
  ```

  * `문자열`도 `list`처럼 인덱스로 접근이 가능하다.
  * 하지만 `string[0] = 'a'`처럼 직접 할당하는 것은 불가능하다.
  * `string[-1]`과 같이 인덱스에 `-n`을 넣으면 오른쪽에서부터 `n번째`문자를 반환한다.

## 2. 반복

* 자연수 N이 주어졌을 때, 1부터 N까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.

  ```python
  numbers = int(input('숫자를 입력하세요: '))
  
  for number in range(1, numbers + 1):
      print(number)
  ```

  * `range(1, numbers + 1)`를 `range(numbers)`로 수정할 수 있으며, 그럴 경우 `print(number)`를 `pirnt(number + 1)`로 수정해야 결과값이 동일하다.

## 3. 조건(1)

* 숫자를 입력받아 짝수/홀수를 구분하는 코드를 작성하시오.

  ```python
  number = int(input('숫자를 입력하세요: '))
  
  if number % 2: # => 홀수일 경우 1 (True), 짝수일 경우 0 (False)
      print('홀수입니다.')
  else:
      print('짝수입니다.')
  ```

  * `number % 2` 같은 경우에는 `0` 또는 `1`의 값만 나오기 때문에 `number % 2 == 0`과 같이 조건을 주지 않아도 된다.

## 4. 조건(2)

* 표준 입력으로 4과목의 성적이 입력되면 기준에 따라 True, False를 반환하는 코드를 작성하시오.

  > 국어는 90점 이상, 영어는 80점 초과, 수학은 85점 초과, 과학은 80점 이상
  >
  > 한 과목이라도 조건을 만족하지 못하면 불합격이고 False가 출력되도록 작성한다.

  ```python
  a = int(input('국어: '))
  b = int(input('영어: '))
  c = int(input('수학: '))
  d = int(input('과학: '))
  
  if a >= 90 and b > 80 and c > 85 and d >= 80:
      print(True)
  else:
      print(False)
  ```

  * 파이썬에서 bool값은 True, False와 같이 첫 글자를 대문자로 쓴다.

## 5. 문자열 조작

* 표준 입력으로 물품 가격 여러 개가 문자열 한 줄로 입력되고, 각 가격은 ;(세미콜론)으로 구분되어 있다. 입력된 가격을 높은 가격순으로 출력하는 프로그램을 만드시오.

  ```python
  prices = input('물품 가격을 입력하세요: ')
  
  prices = prices.split(';')
  ```

  * `.split('*')` 을 사용하면 문자열을 `*`을 기준으로 나눈 리스트를 반환한다.
  
* 입력받은 문자열을 `.split()`을 통해 나누면 각 원소의 타입은 `str(문자열)`이다. 

* 문자열을 `int(정수)`타입으로 변환하기 위해서 변환 과정을 거쳐야한다.

  1. 반복문을 통한 변환
  
     ```python
     int_price = []
     
     for price in prices:
         int_price.append(int(price))
     ```
  
     * 반복문을 이용하여 각 원소를 변환하고 새로운 리스트에 넣어준다.
  
  2. list comprehension
  
     ```python
     int_price2 = [int(x) for x in prices]
     print(int_price2)
     ```
  
     * `list comprehension`을 이용하여 손쉽게 리스트를 만들 수 있다.
  
  3. `map` : 첫 번째 인자의 함수를  두 번째 인자를 반복하며 적용.
  
     * 반복 가능한 객체에 함수를 각각 적용한다.
  
     ```python
     int_price3 = list(map(int, prices))
     print(int_price3)
     ```
  
     * `map()` 함수를 사용하면 반복 가능한 자료형에 손쉽게 동일한 함수의 결과를 적용할 수 있다.
  
  
  
# Day3

## HTML/CSS

### HTML

`HTML`은 Hyper Text Markup Language의 약자로 웹 문서를 구조화하는데 사용되는 언어이다.

1. HTML 기본 구조

   ```html
   <!DOCTYPE html>
   <html lang="en">
   	<head>
       	<meta charset="UTF-8">
       	<title>밥먹을 시간!</title>
   	</head>
   	<body>
      		<h2>{{name}}아, {{menu}} 먹어!</h2>
   	</body>
   </html>
   ```

   * `<head> </head>`는 문서의 정보를 담고 있다.
   * `<body> </body>`는 문서의 본문을 담고 있다.

2. 태그의 종류
  
   1. 기본적으로 태그는 `여는태그`와 `닫는태그`로 구성된다.
   
      ```html
      <h1>제목1</h1>
      ```
      
   2. `닫는태그`가 없는 경우도 있다.(self-closing tag)
    
      ```html
   <img src='__'/>
      ```
   
3. 태그의 구성

   ```html
   <img src="___" width="300" height="300"/>
   <a href="https://google.com" class="blue">구글</a>
   ```

   * 태그별로 공통적으로 가질 수 있는 속성 : `id`, `class`, `style`
   * 각 태그별로 가질 수 있는 속성이 추가적으로 있다.
     * img - `src`, `width`, `height`
     * a - `href`

### CSS

css는 Cascading Style Sheets의 약자로, HTML을 꾸며주는 역할을 한다.

HTML을 꾸며주기 위하여, `선택자(selector)`를 통해 특정한 element를 지정하여야 한다.

1. 선택자

   * 태그 선택자

     ```css
     p {
         color: red;
     }
     ```

   * class 선택자

     ```css
     .blue {
         color: blue;
     }
     ```

   * id 선택자

     ```css
     #pink {
         color: pink;
     }
     ```

   선택자 우선순위는 id선택자 -> class선택자 -> 태그선택자 순서로 적용된다.



## Flask

`Flask`는 파이썬 기반의 micro framework이다.

### 기본 활용법

1. 설치

   ```bash
   $ pip install flask
   ```

2. 기본 코드

   ```python
   # app.py
   from flask import Flask
   
   app = Flask(__name__)
   
   @app.route('/')
   def hello():
       return 'Hello!'
   
   if __name__ == '__main__':
       app.run(debug=True)
   ```

3. 서버 실행

   ```bash
   $ flask run
   ```

   * 기본적으로 `flask run` 명령어는 `app.py`파일을 실행시킨다. 만약 다른 파일명으로 만들었다면, 옵션을 추가해야 한다.
   * 마지막 두 줄을 작성해놓았다면, 아래와 같이 실행도 가능하다.

   ```bash
   $ python app.py
   ```

### Variable routing

요청 오는 url을 변수화 하여 값을 사용할 수 있다.

```python
@app.route('/hi/<string:name>')
def hi(name):
    return f'{name}아 안녕'
```

### Rendering Template

`HTML` 파일을 만들어 활용할 수 있다. 기본적으로 `templates` 폴더에 파일을 만들어야 한다.

```
app.py
templates/
	hi.html
	lunch.html
```

```python
from flask import Flask, render_template
# ...
@app.route('/hi')
def hi():
    return render_template('hi.html')
```

`HTML` 파일에서 변수의 값을 출력하고자 한다면, 키워드 인자로 그 값을 넘겨줘야한다.

```python
return render_template('hi.html', name=name)
```

그리고 출력을 위해서는 `{{ }}` 사용한다.

```jinja2
<h1>{{name}} 안녕?</h1>
```





  