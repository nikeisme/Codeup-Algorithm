# 나올 수 있는 주사위의 숫자를 한 세트씩 줄을 바꿔 모두 출력한다.
# 첫 번째 수는 n, 두 번째 수는 m으로 고정해 1부터 오름차순 순서로 출력하도록 한다.

n,m=input().split()

n=int(n)
m=int(m)

for i in range(1, n+1) :
  for j in range(1, m+1) :
    print(i, j)