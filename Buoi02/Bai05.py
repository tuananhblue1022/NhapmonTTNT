import numpy as np

def custom_loss(y, y_hat, n=2, p=1):
    
# Hàm tính toán custom loss dựa trên các giá trị đầu vào.

# Args:
# y (array-like): Giá trị thực tế.
# y_hat (array-like): Giá trị dự đoán.
# n (int): Căn bậc n để tính n-th Root Error.
# p (int): Bậc của hàm loss.
    
# Returns:
# float: Giá trị của hàm loss.
    
    y = np.array(y)
    y_hat = np.array(y_hat)
    error = y_hat - y
    n_root_error = np.abs(error) ** (1/n)
    loss = np.mean(n_root_error ** p)
    return loss

# Ví dụ sử dụng
y = [90, 85, 80, 75, 70]
y_hat = [92.5, 84.5, 79.5, 75.5, 69.5]

result = custom_loss(y, y_hat, n=2, p=1)
print(f"Kết quả của hàm loss: {result}")
