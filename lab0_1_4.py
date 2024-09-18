a, b = map(int, open('input1.txt').read().split())
if 10**9> a> -10**9 and 10**9> b > -10**9:
    open('output1.txt', 'w').write(str(a+b*b))
else: 
    print('The numbers are too big')



