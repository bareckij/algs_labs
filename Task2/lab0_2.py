<<<<<<< HEAD
fib1 = fib2 = 1
num = open("input2.txt").read()
n = int(num)
if 0<n<45:
    for i in range(2, n):
        fib1, fib2 = fib2, fib1 + fib2
    open('output2.txt', 'w').write(str(fib2))
else: 
=======
fib1 = fib2 = 1
num = open("input2.txt").read()
n = int(num)
if 0<n<45:
    for i in range(2, n):
        fib1, fib2 = fib2, fib1 + fib2
    open('output2.txt', 'w').write(str(fib2))
else: 
>>>>>>> 67bfe4c (renamed + modified)
    print("The numbers are too big!")