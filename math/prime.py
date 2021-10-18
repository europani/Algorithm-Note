import math

def isPrime(n):         # 2 ~ (n-1)
    for i in range(2, n):
        if n%i==0:
            return False
    return True


def isPrime2(n):        # 2 ~ sqrt(n)
    end = int(math.sqrt(n))

    for i in range(2, end+1):
        if n%i==0:
            return False
    return True


def primeSieve(n):      # 에라토스테네스의 체
    num = [True] * (n+1)

    for i in range(2, n+1):
        if num[i]==True:
            for j in range(i*2, n+1, i):    # i의 배수 False 처리
                num[j]=False
    
    for i in range(2, len(num)):
        if num[i]==True:
            print(i, end=" ")




