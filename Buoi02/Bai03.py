import random
import math

def calculate_loss():
    # Yêu cầu người dùng nhập số lượng mẫu
    try:
        num_samples = int(input("Nhập số lượng samples (num_samples): "))
        if num_samples <= 0:
            print("Số lượng samples phải là số nguyên dương.")
            return
    except ValueError:
        print("Vui lòng nhập một số nguyên hợp lệ.")
        return
    
    # Yêu cầu người dùng nhập loại loss cần tính
    loss_type = input("Nhập loại loss cần tính (MAE, MSE, RMSE): ").upper().split(',')
    
    # Tạo danh sách predict và target với giá trị ngẫu nhiên từ 0 đến 10
    predict = [random.uniform(0, 10) for _ in range(num_samples)]
    target = [random.uniform(0, 10) for _ in range(num_samples)]
    
    # Tính toán các loại loss
    mae = sum(abs(p - t) for p, t in zip(predict, target)) / num_samples
    mse = sum((p - t) ** 2 for p, t in zip(predict, target)) / num_samples
    rmse = math.sqrt(mse)
    
    # In kết quả
    print(f"\nSố lượng samples: {num_samples}")
    print(f"Predict: {predict}")
    print(f"Target: {target}\n")
    
    if 'MAE' in loss_type:
        print(f"MAE: {mae}")
    if 'MSE' in loss_type:
        print(f"MSE: {mse}")
    if 'RMSE' in loss_type:
        print(f"RMSE: {rmse}")

# Gọi hàm
calculate_loss()
