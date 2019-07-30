# WEB - day 1

## 00. emmet

* HTML을 작성하는 데에 있어서 편의성을 제공해주는 emmet이라는 것이 있다.
* 대표적으로 `! + tab`을 할 경우에 HTML 문서의 기본적인 구조가 자동완성된다.
* 그 밖에도 다양한 축약어들이 존재하며, 숙지할 경우 비교적 편하게 작성할 수 있다.
* [emmet](https://docs.emmet.io/cheat-sheet/) 



## 01. 시맨틱 태그

```html
<header> Header </header>
<nav>Navigation</nav>
<section>
    Section
    <article>
        Article
    </article>
</section>
<aside>
    Aside
</aside>
<footer>
    Footer
</footer>
```

![](./images/semantic.png)



## 02. HTML 태그

### 02 - 1. Heading

```html
<h1> 문서의 제목 </h1>
<h2> </h2>
...
<h6> </h6>
```

* 제목을 표시하는 태그로 `h6`까지 존재한다.
* 기본적으로 **볼드체**로 표기되며, 항상 새로운 줄에 입력된다.
* 반드시 제목을 표시하기 위해 사용해야하는 것은 아니지만, 개발을 하는 입장에서 가독성을 위해서는 제목을 표시하기 위해서만 사용하도록 한다.

### 02 - 2. paragraph

* `<p>` 태그를 사용하며, 글의 문단에 해당하는 부분이다.
* 단락을 구분하는 용도로 쓰이며, 같은 태그 내에서는 줄바꿈을 위해서 `<br>`태그를 사용해야 한다.

### 02 - 3. br

* HTML 문서에서는 enter가 줄바꿈으로 반영되지 않기 때문에 줄바꿈을 위해서는 `<br>`태그를 입력해야한다.

### 02 - 4. bold

* HTML 문서에서 굵은 글씨를 표현하기 위해서는 두 가지 태그가 존재한다.
* 기본적으로 `<b>`태그가 볼드체를 표현하며, 시맨틱 태그 중 하나인 `<strong>`태그도 볼드체를 표현한다.

### 02 - 5. italic

* 이탤릭체 또한 두 가지 표현 방법이 존재한다.
* `<i>`태그를 이용하는 방법과 `<em>` 태그를 이용하는 방법이 있다.

### 02 - 6. 기타 텍스트 꾸미기

```html
이건 <mark>주목</mark>해주세요. <!-- 주목 부분이 하이라이팅 되어서 출력된다. -->
이건 <del>취소</del>해주세요. <!-- 취소 부분이 가로줄이 그어진 상태로 출력된다. -->
이건 <ins>추가</ins>해주세요. <!-- 추가 부분이 밑줄이 그어친 상태로 출력된다. -->
하이! <sub>안녕하세요.</sub> <!-- 안녕하세요. 부분이 아래로 정렬된 상태로 출력된다. -->
하이! <sup>안녕하세요.</sup> <!-- 안녕하세요. 부분이 위로 정렬된 상태로 출력된다. -->
```

![](./images/text_shape.png)

### 02 - 7. blockquote

* HTML에서 인용문을 작성하는 방법은 두 가지가 있다.
* `<q>`태그를 사용하면 인용문을 나타낼 수 있다.
* `<blockquote>`를 사용해도 인용문을 나타낼 수 있다. `<blockquote>`는 새로운 문단을 인용문으로 나타낼 때 많이 사용하며, 사용할 경우에 좌우에 여백이 들어간다.

### 02 - 8. 수평선

* `<hr>` 을 사용하면 수평선이 출력된다.

### 02 - 9. 리스트

```html
<ol>
    <li> 순서가 </li>
    <li> 있는 </li>
    <li> 리스트 </li>
</ol>

<ul>
    <li> 순서가 </li>
    <li> 없는 </li>
    <li> 리스트 </li>
</ul>

<li> 아무것도 아닌 그냥 리스트 </li>

ol>li*3
ul>li*3
<!-- 위와 같이 emmet을 활용하여 빠르게 리스트 구조를 작성할 수 있다. -->
```

* `<ol>` 태그는 순서가 있는 리스트를 출력할 때 사용한다. 일반적으로 `1. 2. 3.`과 같이 앞에 숫자로 순서가 표시된다.
* `<ul>` 태그는 순서가 없는 리스트를 출력할 때 사용한다. `<ol>` 태그와 달리 점과 같은 형태가 앞머리에 붙는다.
* `<ol>`이나 `<ul>`과 같은 태그를 사용하지 않고도 리스트를 작성할 수 있다. 하지만 그럴 경우에는 자동으로 들여쓰기가 되지 않는다.

### 02 - 10. 이미지, 비디오

```html
<img src="bonobono.png" alt="보노보노" width="100" height="100">
```

```html
<iframe width="560" height="315" src="https://www.youtube.com/embed/CiRocVoKDDk" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```

* 이미지나 비디오는 다음과 같이 불러와 사용할 수 있다.
* `src`에는 파일의 경로 (로컬/웹) 를 입력하고, `alt`에는 대체 텍스트를 입력한다. `alt`에 입력된 대체 텍스트는 이미지가 존재하지 않거나, 접근성이 요구되는 상황에서 활용된다.
* `iframe`은 외부 사이트의 내용을 내 사이트에 표시하기 위해 사용된다.

### 02 - 11. 링크 태그

```html
<a href="google.com">구글로 가보자</a>
```

* `<a href="">` 태그는 링크를 만들기 위한 태그이며, 입력된 텍스트나 이미지를 클릭할 경우 입력된 URL로 연결된다.



## 03. Table

```html
<table border="1px solid black" summary="20주차 대전 점심 메뉴">
    <caption>대전 유성연수원 점심메뉴표</caption> <!-- 표의 제목 -->
    <thead> <!-- table head -->
        <tr> <!-- table row(행) -->
            <th scope="row"></th> <!-- font-weight: bold 적용 -->
            <th>월</th>
            <th>화</th>
            <th>수</th>
        </tr>
    </thead>
    <tbody> <!-- table body -->
        <tr>
            <td>A코스</td> <!-- table data -->
            <td rowspan="2">짬뽕</td>
            <td colspan="2">초밥</td>
        </tr>
        <tr>
            <td>B코스</td>
            <td>김치찌개</td>
            <td>삼계탕</td>
        </tr>
    </tbody>
    <tfoot> <!-- table foot : col 요약 -->
        <td>식수</td>
        <td colspan="3">총 150명 식사</td>
    </tfoot>
</table>
```

* `<caption>` 태그를 이용하여 표의 제목을 나타낼 수 있다.
* `<thead>`, `<tbody>`, `<tfoot>` 태그는 반드시 넣어야할 요소는 아니지만 `Markup`하는 측면에서 조금 더 보기 좋은 형태로 개발하는 것이 가능하다.
* `<td rowspan="2">` 태그의 `rowspan`과 `colspan`을 통해서 행과 열을 병합하여 표시할 수 있다.

## 04. Markup

* HTML은 `Hyper Text Markup Language` 의 약자인 만큼 HTML 문서를 작성함에 있어서 markup은 중요한 요소이다.

```html
<body>
  <h1>프로그래밍 교육</h1>
  <hr>
  <section>
    <header>
        <h2><a href="https://docs.python.org/ko/3/tutorial/index.html" target="_blank">파이썬</a></h2>
    </header>
    <h3>Number type</h3>
    <p>파이썬에서 숫자형은 아래와 같이 있다.</p>
    <ol>
      <li style="list-style-type: circle">int</li>
      <li style="list-style-type: none">float</li>
      <li style="list-style-type: lower-alpha">complex</li>
      <li style="list-style-type: upper-alpha"><del>str</del></li>
    </ol>
  </section>
</body>
```

* 위의 구조에서 `<section>` `<header>` 과 같은 구조는 기능함에 있어서 없어도 문제가 없는 부분이지만 HTML 문서 자체를 구조화하는 데에 있어서 가독성을 높여주는 역할을 한다.

## 05. Form

* `<form>` 태그를 통해서 사용자의 입력을 받아 요청을 보내는 작업을 수행할 수 있다.
* 기본적으로 사용자의 입력은 `<input>` 태그를 이용하여 받으며, `type`에 따라서 다양한 입력을 받을 수 있다.

```html
<!-- form 태그의 기본 구조 -->
<form action="#" method="POST">
    <!-- label을 작성해주면, for에 특정 input의 id를 작성하면 해당 input에 포커싱이 된다.-->
    <label for="name">이름 :</label>
    <input id="name" type="text" placeholder="이름을 입력해주세요."><br>
    
    <!-- radio 버튼은 동일한 name 속성값을 가지고 있는 것 중에 하나만 선택 가능 -->
    <h3>1. 샌드위치 선택</h3>
    <input type="radio" name="sandwich" value="egg"> 에그 마요<br>
    <input type="radio" name="sandwich" value="bmt"> 이탈리안 비엠티
    <hr>
    
    <!-- number type은 숫자의 범위를 지정 가능 -->
    <h3>2. 사이즈 선택</h3>
    <input type="number" name="size" min="15" max="30" step="15" placeholder="15">cm
    <hr>

    <!-- select + option : dropdown 메뉴
        select 태그에 name을 지정하고,
        option에 value를 지정한다.
        selected, disabled를 사용할 수 있다. -->
    <h3>3. 빵</h3>
    <select name="bread">
      <option value="0" selected>허니 오트</option>
      <option value="1" disabled>플랫 브레드</option>
    </select>
    <hr>
    
    <!-- checkbox : 여러 가지 항목을 선택 가능하다. -->
    <h3>4. 야채/소스</h3>
    <input type="checkbox" name="topping" value="토마토">토마토<br>
    <input type="checkbox" name="topping" value="오이">오이<br>
    <input type="checkbox" name="topping" value="할라피뇨">할라피뇨<br>
    <input type="checkbox" name="topping" value="핫 칠리">핫 칠리<br>
    <input type="checkbox" name="topping" value="바베큐">바베큐<br>
    <hr>
   
    <!-- submit 버튼을 누르면 해당 폼 데이터를 action으로 전송 -->
    <input type="submit" value="주문!">
</form>
```

* `<form>` 태그의 `action`부분은 어디로 내용을 보낼 것인지 결정하고, `method` 부분은 어떻게 보낼 것인지 그 방식을 결정한다.

![](./images/form.png)

