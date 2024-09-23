<<<<<<< HEAD

a, b = map(int, open('input.txt').read().split())

open('output.txt', 'w').write(str(a+b))
=======

a, b = map(int, open('input.txt').read().split())
if 10**9> a> -10**9 and 10**9> b > -10**9:
    print(a+b*b)
else: 
    print('The numbers are too big')
open('output.txt', 'w').write(str(a+b))
>>>>>>> 67bfe4c (renamed + modified)
