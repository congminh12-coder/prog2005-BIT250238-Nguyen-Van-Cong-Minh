import math
danh_sach = []
n = int(input("Bạn muốn nhập bao nhiêu số vào danh sách? "))
for i in range(n):
    so = int(input(f"Nhập phần tử thứ {i + 1}: "))
    danh_sach.append(so)
print("Danh sách hiện tại:", danh_sach)
k = int(input("Nhập giá trị k cần kiểm tra: "))
dem_k = 0
for x in danh_sach:
    if x == k:
        dem_k = dem_k + 1
print(f"Số lần xuất hiện của {k} trong danh sách là: {dem_k} lần")
def kiem_tra_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
tong_nguyen_to = 0
danh_sach_snt = []
for x in danh_sach:
    if kiem_tra_nguyen_to(x):
        tong_nguyen_to = tong_nguyen_to + x
        danh_sach_snt.append(x)
print(f"Các số nguyên tố tìm thấy: {danh_sach_snt}")
print(f"Tổng các số nguyên tố là: {tong_nguyen_to}")

danh_sach.sort()
print("Danh sách sau khi sắp xếp tăng dần:", danh_sach)
danh_sach.clear()
print("Danh sách sau khi xóa tất cả phần tử:", danh_sach)
