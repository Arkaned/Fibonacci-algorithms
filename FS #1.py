def fibonacci(n):
    if n ==1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)

for n in range(1, 100):
    print(n, ";", fibonacci(n))

#the process slows down because it has to keep recalling to previous functions.
# this is called a recursive function
# e.g. fibonacci(5) = fibonacci(4) + fibonacci(3)
#          = fibonacci(3) + fibonacci(2) + fibonacci(2) + fibonacci(1)
#          = fibonacci(2) + fibonacci(1) + fibonacci(2) + fibonacci(2) + fibonacci(1)
#          = 1 + 1 + 1 + 1 + 1
#          = 5