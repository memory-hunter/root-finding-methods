def fun(x):
    return x*x + x - 9

def Secant(a, b, epsilon, n=20):
    i = 0
    x = a
    while abs(fun(x)) > epsilon and i < n:
        print("x{0} = {1:.4f}".format(i, x), " Iteration: ", i)
        x = a - (b - a)*fun(a)/(fun(b) - fun(a))
        a = b
        b = x
        i+=1
    print("The root is: ", x, " iterated ", i, " times")

Secant(2, 3, 0.0000001)