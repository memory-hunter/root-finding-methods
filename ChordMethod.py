def fun(x):
    return x*x + x - 9

def Chord(a, b, epsilon, n=20):
    i = 0
    r = (fun(b) - fun(a)) / (b - a)
    x = a
    while abs(x) > epsilon and i < n:
        print("x{0} = {1:.4f}".format(i, x), " Iteration: ", i)
        x = x - fun(x)/r
        i += 1
    print("The root is: ", x, " iterated ", i, " times")

Chord(2, 3, 0.0000001)