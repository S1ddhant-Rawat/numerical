def f(x):
    return x**3 - x - 2  

def df(x):
    return 3*x**2 - 1    

def newton_raphson(x0, tol=1e-4, max_iter=25):
    for i in range(max_iter):
        x1 = x0 - f(x0)/df(x0)
        print(f"Iteration {i+1}: x = {x1}")
        if abs(x1 - x0) < tol:
            return x1
        x0 = x1
    return x1

root = newton_raphson(1.5)
print("Approximate root:", root)
