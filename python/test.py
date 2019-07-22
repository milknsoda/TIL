# print(a)에 무엇이 출력되는지 확인해보세요.
a = 1

print(f'글로벌 스코프{globals()}')

print(f'글로벌의 로컬{locals()}')
def localscope(a):
    print(f'로컬 스코프{locals()}')
    print(f'로컬 스코프의 글로벌{globals()}')
    print(a)
    
localscope(3)
print(f'글로벌의 로컬{locals()}')
print(a)