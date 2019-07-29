# WEB - day 1

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

## 02. Table

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