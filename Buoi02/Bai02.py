import math

# Hàm kiểm tra tính hợp lệ 
def is_number(n):
    try:
        float(n)
    except ValueError:
        return False
    return True

# Hàm mô phỏng các activation functions
def exercise2():
    # Nhập giá trị x
    x = input("Input x: ")
    
    # Kiểm tra tính hợp lệ của x
    if not is_number(x):
        print("x must be a number")
        return
    
    # Chuyển x sang kiểu float
    x = float(x)
    
    # Nhập tên của activation function
    activation_function = input("Input activation function (sigmoid | relu | elu): ").strip().lower()
    
    # Giá trị alpha cho ELU
    alpha = 0.01
    
    # Tính toán dựa trên activation function
    if activation_function == "sigmoid":
        result = 1 / (1 + math.exp(-x))
        print(f"sigmoid: f({x}) = {result}")
    
    elif activation_function == "relu":
        result = max(0, x)
        print(f"relu: f({x}) = {result}")
    
    elif activation_function == "elu":
        if x <= 0:
            result = alpha * (math.exp(x) - 1)
        else:
            result = x
        print(f"elu: f({x}) = {result}")
    
    else:
        print(f"{activation_function} is not supported")

# Ví dụ sử dụng hàm
exercise2()
