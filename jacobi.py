def jacobi(a, b, x_init, max_iter=25, tol=1e-4):
    n = len(a)
    x = x_init[:]
    x_new = x[:]

    for itr in range(max_iter):
        for i in range(n):
            sum_ = sum(a[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - sum_) / a[i][i]

        # Check for convergence
        if all(abs(x_new[i] - x[i]) < tol for i in range(n)):
            print(f"Converged in {itr+1} iterations.")
            break

        x = x_new[:]

    return x_new

# Example system
A = [
    [10, 2, 1],
    [1, 5, 1],
    [2, 3, 10]
]
B = [9, -6, 7]
initial_guess = [0, 0, 0]

solution = jacobi(A, B, initial_guess)
print("Solution:", solution)
