from functools import lru_cache

def foo1():
    @lru_cache(maxsize=5) # stores the  lastest values
    def fib(n):
        if n<= 1:
            return n
        return fib(n-1) + fib(n-2)

    for i in range(400):
        print(i, fib(i))
    print("done")

def main():
    x = 1
    y = 3
    z = x | y
    print(z)

if __name__ == '__main__':
    main()
