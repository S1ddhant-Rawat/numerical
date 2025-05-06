def f(x):
    return x**3 - x - 2  

def secant(x0, x1, tol=1e-4, max_iter=100):
    for i in range(max_iter):
        if f(x1) - f(x0) == 0:
            print("Division by zero error.")
            return None

        x2 = x1 - (f(x1) * (x1 - x0)) / (f(x1) - f(x0))
        print(f"Iteration {i+1}: x = {x2}, f(x) = {f(x2)}")

        if abs(x2 - x1) < tol:
            return x2

        x0, x1 = x1, x2

    return x2

root = secant(1, 2)
print("Approximate root:", root)
