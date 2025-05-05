def f(x):
    return x**3 - x - 2  # Example function

def bisection(a, b, tol=0.0001):
    if f(a) * f(b) > 0:
        print("Invalid interval. f(a) and f(b) must have opposite signs.")
        return

    while (b - a) / 2 > tol:
        c = (a + b) / 2
        if f(c) == 0:
            break
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c

    print(f"Root = {c:.4f}")

# Example use
bisection(1, 2)
