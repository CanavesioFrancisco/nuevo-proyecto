def fib_33 ( m ) :
    a, b = 0, 1
    while a < m :
        print ( a, end = '' )
        a, b = b, a + b
    print()
fib_33 ( 1000 )
