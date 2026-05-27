# Ma trận ảnh xám ví dụ
image = [
    [0, 10, 20],
    [10, 20, 20],
    [30, 0, 10]
]

# Khởi tạo histogram 256 mức xám
histogram = [0] * 256

# Duyệt từng pixel
for row in image:
    for pixel in row:
        histogram[pixel] += 1

# In các giá trị xuất hiện
for i in range(256):
    if histogram[i] > 0:
        print(f"Muc xam {i}: {histogram[i]} pixel")