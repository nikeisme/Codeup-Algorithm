# 시작 값(a), 등비의 값(r), 몇 번째 인지를 나타내는 정수(n)가공백을 두고 입력된다.(모두 0 ~ 10)
# n번째 수를 출력한다.

a, r, n = input().split()

a = int(a)
r = int(r)
n = int(n)

for i in range(1, n) :
  a = a*r

print(a)