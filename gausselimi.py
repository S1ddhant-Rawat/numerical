def gauss_elimination(a):
    n = len(a)

    # Forward Elimination
    for i in range(n):
        # Make the diagonal element 1
        if a[i][i] == 0:
            raise ValueError("Zero pivot encountered!")

        for j in range(i+1, n):
            ratio = a[j][i] / a[i][i]
            for k in range(n+1):
                a[j][k] -= ratio * a[i][k]

    # Back Substitution
    x = [0 for _ in range(n)]
    for i in range(n-1, -1, -1):
        x[i] = a[i][n]
        for j in range(i+1, n):
            x[i] -= a[i][j] * x[j]
        x[i] = x[i] / a[i][i]

    return x


# Example input
aug_matrix = [
    [2, 3, 1, 1],
    [4, 1, -2, -2],
    [-2, 5, 7, 9]
]

result = gauss_elimination(aug_matrix)
print("Solution:", result)
