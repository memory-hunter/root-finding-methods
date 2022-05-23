def fun(x):
    return x*x + x - 9

def fun_der(x):
    return 2*x + 1

def Newton(x0, epsilon, n=20):
    i = 0
    x = x0
    while abs(fun(x)) > epsilon and i < n:
        print("x{0} = {1:.4f}".format(i, x), " Iteration: ", i)
        x = x - fun(x)/fun_der(x)
        i+=1
    print("The root is: ", x, " iterated ", i, " times")

Newton(2, 0.0000001)