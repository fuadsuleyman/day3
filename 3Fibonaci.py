def fibonacci(n):
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            break
        yield a
        a, b = b, a + b
        counter += 1
        
f = fibonacci(10)
print(f)
for x in f:
    print (x)
print