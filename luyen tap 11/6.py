danh_sach_sinh_vien = {}
n = int(input("Bạn muốn nhập thông tin cho bao nhiêu người? "))

for i in range(n):
    print(f"\nNhập thông tin người thứ {i + 1}:")
    ten = input(" - Nhập tên: ")
    tuoi = int(input(" - Nhập tuổi: "))

    danh_sach_sinh_vien[ten] = tuoi

print("\n" + "-" * 30)
print("Danh sách thông tin đã lưu:")
print(danh_sach_sinh_vien)
if n > 0:
    tat_ca_tuoi = danh_sach_sinh_vien.values()
    tong_tuoi = sum(tat_ca_tuoi)
    tuoi_trung_binh = tong_tuoi / n

    print("-" * 30)
    print(f"Tổng số người: {n}")
    print(f"Tuổi trung bình của mọi người là: {tuoi_trung_binh:.2f}")
else:
    print("Danh sách rỗng, không thể tính tuổi trung bình.")