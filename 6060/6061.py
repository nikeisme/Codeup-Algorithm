# 입력된 정수 두 개를 비트단위로 or 연산한 후 그 결과를 정수로 출력해보자.
# 비트단위(bitwise) 연산자 |(or, vertical bar, 버티컬바)를 사용하면 된다.
# 비트 단위 or연산은 둘 중 하나라도 1인 자리를 1로 만들어주는 것과 같다.

a,b = input().split()
print(int(a)|int(b))