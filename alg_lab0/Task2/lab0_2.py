fib1 = fib2 = 1
num = open("Task2/input2.txt").read()
n = int(num)

if 0<n<45:
    for i in range(2, n):
        fib1, fib2 = fib2, fib1 + fib2
    open('Task2/output2.txt', 'w').write(str(fib2))
else: 
    print("The numbers are too big!")