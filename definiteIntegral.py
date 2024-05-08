def rectangle_method(f, a, b, n):
    dx = (b - a) / n
    integral = 0
    for i in range(n):
        x_mid = a + (i + 0.5) * dx
        integral += f(x_mid)
    integral *= dx
    return integral

# Example usage:
def f(x):
    return x ** 2
a = 0
b = 1
n = 100
result_rect = rectangle_method(f, a, b, n)
print("Rectangle Method:", result_rect)