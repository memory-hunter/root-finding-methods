def fun(x):
    return x*x + x - 9

def invFun(x):
    return 9 / (x+1)

def fixedPoint(x0, epsilon, n = 20):
    i = 0
    x = x0
    while(abs(fun(x)) > epsilon) and i < n:
        x = invFun(x)
        i+=1
        print("The root is: ", x, " iterated ", i, " times")
    
fixedPoint(2, 0.0000001)