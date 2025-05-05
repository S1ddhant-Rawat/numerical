def f(x):
    return x**3 - x - 2

def regula_falsi(a, b, tol=1e-4, max_iter=100):
    if f(a) * f(b) >= 0:
        print("Invalid initial guesses.")
        return None

    for i in range(max_iter):
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))

        print(f"Iteration {i+1}: c = {c}, f(c) = {f(c)}")

        if abs(f(c)) < tol:
            return c

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    return c

root = regula_falsi(1, 2)
print("Approximate root:", root)
