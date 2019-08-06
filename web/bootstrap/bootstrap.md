# bootstrap

* 웹 사이트를 쉽게 만들 수 있도록 도와주는 프레임워크
## 0.  bootstrap을 사용하기 위한 준비

```html
 ...
 <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/ ... >
</head>

<body>   
 <script src="https://code.jquery.com/ ... ></script>
 <script src="https://cdnjs.cloudflare.com/ ... ></script>
 <script src="https://stackpath.bootstrapcdn.com/ ... ></script>
</body>
</html>
```

* bootstrap 사이트에 있는 코드를 작성하고자 하는 html 파일에 붙여넣는 것으로 bootstrap을 이용할 수 있다.

## 1. spacing

```html
<div class="mt-5">mt-5</div>
<div class="mx-auto my-5">mx-auto</div>
<div class="ml-auto">ml-auto</div>
<div class="mr-auto">mr-auto</div>
<div class="p-5 mt-3">p-5</div>
<div class="mt-n5">mt-n5</div>
```

* html에서 `margin`, `padding`을 bootstrap에 미리 설정된 클래스로 쉽게 설정이 가능하다.