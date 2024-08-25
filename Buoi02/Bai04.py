import math

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def approx_sin(x, n):
    sin_approx = 0
    for i in range(n):
        sin_approx += ((-1) ** i) * (x ** (2 * i + 1)) / factorial(2 * i + 1)
    return sin_approx

def approx_cos(x, n):
    cos_approx = 0
    for i in range(n):
        cos_approx += ((-1) ** i) * (x ** (2 * i)) / factorial(2 * i)
    return cos_approx

def approx_sinh(x, n):
    sinh_approx = 0
    for i in range(n):
        sinh_approx += (x ** (2 * i + 1)) / factorial(2 * i + 1)
    return sinh_approx

def approx_cosh(x, n):
    cosh_approx = 0
    for i in range(n):
        cosh_approx += (x ** (2 * i)) / factorial(2 * i)
    return cosh_approx

# Nhập giá trị x và n từ người dùng
x = float(input("Nhập giá trị x: "))
n = int(input("Nhập giá trị n: "))

# Tính toán và in kết quả
print(f"approx_sin(x={x}, n={n}): {approx_sin(x, n)}")
print(f"approx_cos(x={x}, n={n}): {approx_cos(x, n)}")
print(f"approx_sinh(x={x}, n={n}): {approx_sinh(x, n)}")
print(f"approx_cosh(x={x}, n={n}): {approx_cosh(x, n)}")
