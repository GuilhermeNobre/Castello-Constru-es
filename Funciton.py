def somar():
    a = 5
    b = 6
    c = a + b
    print("SOMA a={0} e b={1} igual c={2}".format(a,b, c))

def fib(n):
    a, b = 0,1
    while a < n:
        print(a, ' ')
        a,b = b, a+b
    print()

