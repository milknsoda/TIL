# CSS - day 2

## 01. style 참조

### 01 - 1. inline

```html
<h1 style="color: red">
    inline
</h1>
```

* HTML 태그들은 `style`을 가질 수 있고, 이것을 통해 디자인을 변경할 수 있다.
* 하지만 재사용하기 쉽게 하기 위해서는 피해야할 형태이다.

### 01 - 2. 내부 참조(embed)

```html
<head>
    <style>
        h1 {
            color: red;
        }
    </style>
</head>
```

* `inline`과 달리 HTML 문서의 `<head>` 부분에 `<style>` 태그를 사용하여 입력한다.
* `inline`보다는 가독성은 좋지만 재사용의 측면에서는 좋지 않다.

### 01 - 3. 외부 파일 링크

```html
<!-- link:css + tab -->
<link rel="stylesheet" href="style.css">
```

* 외부에 저장된 `css`파일을 통해 style을 적용한다.
* `inline`이나 `내부 참조(embed)`에 비해 재사용성이 높아 개발에 유리하다.



## 02. Selector(선택자)

### 02 - 1. 선택자의 우선순위

* 선택자에는 우선순위가 있다.
* `id` > `class` > `tag`

```css
/* 클래스 선택자 : .클래스명 */
.blue {
  color: blue;
}
.brown {
  color: brown !important;
}
/* 아이디 선택자 : #아이디명 */
#green {
  color: green;
}
```

```html
<p id="green" style="color: purple">인라인 CSS 활용</p>
<p id="green" class="brown blue" style="color: purple">무슨 색일까요?</p>
```

* `id` 선택자와 `inline` 이 동시에 존재할 경우에는 `inline`을 우선한다.
* `id`와 `class`, `inline`이 동시에 존재하면서 `class` 내에 `!important`가 존재할 경우에는 `class`를 우선한다.
* `!important`가 여러 개 존재하면 나중에 쓰인 것을 참조한다. (**사용에 주의하자!**)

### 02 - 2. 그룹선택자

```css
h1, h2, h3, h4, h5, h6, .palevioletred {
  color: palevioletred;
}
```

* 한번에 여러 선택자를 사용하여 style을 지정할 수 있다.

### 02 - 3. 자식/후손 선택자

```css
/* 자식 선택자 */
.parent > li {
  color: red;
}

/* 후손 선택자 */
.ancestor li {
  color: blue;
}
```

```html
<!-- 자식 -->
<ol class="parent">
  <ul>
    <li>ol>ul>li</li>
  </ul>
</ol>
<!-- 자식 -->
<ol class="parent">
  <li>ol>li</li>
</ol>

<!-- 후손 -->
<ol class="ancestor">
  <ul>
    <li>ol>ul>li</li>
  </ul>
</ol>
<!-- 후손 -->
<ol class="ancestor">
  <li>ol>li</li>
</ol>
```

* 자식 선택자 : `.parent` 안에 있는 `li`에만 스타일을 적용한다.
* 후손 선택자: `.ancestor` 안에서 `li`를 가지고 있는 모든 항목에 대해 스타일을 적용한다.

## 03. 단위

* CSS에는 다양한 크기의 단위들이 존재한다.
* `em`, `rem`, `vw`, `vh`, `vmax`, `vmin`

### 03 - 1. em / rem

* `em` : 상위 요소의 배수

  ```html
  <ul>
    <li>2em</li>
  </ul>
  ```

  * html : 16px
  * ul : 2em == 32px
  * li : 32 * 2 == 64px
  * **아직 이해가 안된다...**

* `rem` : root 요소의 배수
  * html : 16px (브라우저 기본)
  * N `rem` =  ( 16 * N ) px

### 03 - 2. vw / vh / vmax / vmin

* `vw` / `vh` : 각각 보여지는 화면의 크기의 너비와 높이의 `1/100`을 기준으로 하는 단위이다.
* `vmax` / `vmin` : 너비와 높이 중 큰 / 작은 쪽의 `1/100`을 기준으로 하는 단위이다.



## 04. box model

* 우리가 꾸미는 HTML에서는 오직 사각형만이 존재하며, 이를 변형시켜 모양을 만든다.

![](./images/box_model.png)

* 공간은 `margin`과 `border`, `padding`, `content`로 구분된다.

### 04 - 1. margin

* `margin` : `border` 바깥쪽에 있는 바깥 여백.

* `display` 상태에 따라 `margin`은 **없을 수도 있다.**

  ```css
  /* 상하좌우 */
  .margin-shorthand-1 {
    margin: 10px;
  }
  /*  상하 / 좌우 */
  .margin-shorthand-2 {
    margin: 10px 20px;
  }
  /* 상 / 좌우 / 하 */
  .margin-shorthand-3 {
    margin: 10px 20px 30px;
  }
  /* 상 / 우 / 하 / 좌 - 시계방향 */
  .margin-shorthand-4 {
    margin: 10px 20px 30px 40px;
  }
  ```

* `margin` 을 설정하는 기본적인 방법은 `margin-top`, `margin-bottom`과 같은 옵션을 주어 하나하나 설정하는 것이지만, 위와 같이 하면 빠르게 설정할 수 있다. (`padding`도 마찬가지..!)

### 04 - 2. border

* `margin`과 `padding` 사이의 테두리를 말한다.
* `border`는 그 종류가 다양해서 `dashed(점선)`, `dotted(가는 점선)` 등 여러 옵션이 존재한다.
* 색과 두께도 설정이 가능하다.

### 04 - 3. padding

* `padding`은 안쪽 여백 공간을 의미한다.
* `background-color`를 지정할 경우에 `content` 부분과 함께 색깔이 변경된다.

### 04 - 4. content

* `content`가 담기는 공간



## 05. display

### 05 - 1. block

* 기본적으로 `<div>` 태그는 `block` 속성을 가지고 있기 때문에, 한 줄에 하나씩 공간을 차지한다.
* 임의로 크기를 지정해주더라도 `block` 속성을 가지고 있다면, `margin`으로 채워지게 된다.

### 05 - 2. inline

* `content` 영역만을 가지고 있다. 따라서 내용이 없으면 존재할 수 없다.
* 임의로 크기를 지정해주더라도 적용되지 않고, `content`에 따라 크기가 바뀐다.

### 05 - 3. inline-block

* `block` 속성 + `inline` 속성
* 크기(width, height)를 지정해줄 수 있으며, `inline` 속성을 가지기 때문에 오른쪽 `margin`이 사라진다.

### 05 - 4. 그 외

* `display: none` : 공간 자체가 사라져서 보이지 않는다.
* `visibility: hidden` : 공간은 유지되지만, 내용은 보이지 않는다.



## 06. position

### 06 - 1. static

* 원래 있어야 하는 위치를 말한다.
* `왼쪽 위`가 보통 static

### 06 - 2. relative

* 자신의 `static`을 기준으로 이동한 위치
* `static`의 정보가 남아있어서 다른 공간을 만들 때 `static`을 고려해야한다.

### 06 - 3. absolute

* 가까운 조상 중에 `static`이 아닌 요소를 기준으로 한 위치
* 모든 요소가 `static`이라면 가장 위의 요소인 `body`를 기준으로 한 위치에 있다.
* `absolute`는 `static`에 대한 정보가 남아있지 않는다.

### 06 - 4. fixed

* 화면 상의 특정 위치에 고정한다.
* 브라우저 위치에 따라 변경된다.



## 07. float

* `float`는 일반적인 공간과 별개로 위에 떠다니는 공간이다.

* 하나의 `float` 안에서는 다시 왼쪽 위로 정렬되는 방식을 따른다.

  ![](./images/float.png)



* 그림과 같이 `float`은 순서에 따라 왼쪽에서는 오른쪽으로 쌓이고, 오른쪽에서는 왼쪽으로 쌓인다.
* `clear: left / right / both ` 를 통해서 왼쪽 / 오른쪽 / 양쪽 모두의 `float`을 무시할 수 있다.



