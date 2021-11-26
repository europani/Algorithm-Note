import sys
sys.setrecursionlimit(100000)

i = int(input())

def fibo(n):
    if n <=1:
        return n
    return fibo(n-2) + fibo(n-1)

print(fibo(i))