import time
start_time = time.perf_counter()

fib1 = fib2 = 1
num = open("input.txt").read()
n = int(num)
if 0<n<45:
    for i in range(2, n):
        fib1, fib2 = fib2, fib1 + fib2
    open('output.txt', 'w').write(str(fib2))
else:   
    print("The numbers are too big!")

finish_time = time.perf_counter()
print('Time: ' + str(finish_time - start_time))

start_time = time.perf_counter()
fib1 = fib2 = 1
num = open("input3.txt").read()
n = int(num)
if 0<n<10**7:
    for i in range(2, n):
        fib1, fib2 = fib2, fib1 + fib2

    open('output3.txt', 'w').write(str(fib2%10))

else: 
    print("The numbers are too big!")
finish_time = time.perf_counter()
print('Time: ' + str(finish_time - start_time))