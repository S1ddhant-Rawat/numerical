def gauss_seidel(a, b, x_init, max_iter=25, tol=1e-4):
    n = len(a)
    x = x_init[:]

    for itr in range(max_iter):
        x_old = x[:]
        for i in range(n):
            sum_ = sum(a[i][j] * x[j] for j in range(n) if j != i)
            x[i] = (b[i] - sum_) / a[i][i]

        # Check convergence
        if all(abs(x[i] - x_old[i]) < tol for i in range(n)):
            print(f"Converged in {itr+1} iterations.")
            break

    return x

# Example system:
# 10x + 2y + 1z = 9
# 1x + 5y + 1z = -6
# 2x + 3y + 10z = 7

A = [
    [10, 2, 1],
    [1, 5, 1],
    [2, 3, 10]
]
B = [9, -6, 7]
initial_guess = [0, 0, 0]

solution = gauss_seidel(A, B, initial_guess)
print("Solution:", solution)
