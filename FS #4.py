from functools import lru_cache

@lru_cache(maxsize = 1000)
def fibonacci(n):
    # make sure that the input is a positive integer
    if n ==1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)

# now let's calculate the fibonacci ratio (golden ratio)
for n in range(1, 101):
    print(fibonacci(n+1)/fibonacci(n))
