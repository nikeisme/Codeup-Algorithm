# 시작 값(a), 곱할 값(m), 더할 값(d), 몇 번째 인지를 나타내는 정수(n)가공백을 두고 입력된다.(a, m, d는 -50 ~ +50, n은 10이하의 자연수)
# n번째 수를 출력한다.

a, m, d, n = input().split()

a = int(a)
m = int(m)
d = int(d)
n = int(n)

for i in range(1, n) :
  a = a*m+d

print(a)