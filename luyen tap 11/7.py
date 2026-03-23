import csv

# 1. Nhập thông tin từ bàn phím
print("--- Nhập thông tin nhân viên ---")
id_nv = input("Nhập ID: ")
ten_nv = input("Nhập Tên: ")
tuoi_nv = input("Nhập Tuổi: ")
data = [id_nv, ten_nv, tuoi_nv]
with open("nhanvien.txt", "a", encoding="utf-8") as txt_file:
    line = f"ID: {id_nv} | Tên: {ten_nv} | Tuổi: {tuoi_nv}\n"
    txt_file.write(line)

with open("nhanvien.csv", "a", newline="", encoding="utf-8") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(data)

print("\n[Thông báo] Đã lưu dữ liệu vào nhanvien.txt và nhanvien.csv thành công!")

print("\n--- Nội dung file TEXT hiện tại ---")
with open("nhanvien.txt", "r", encoding="utf-8") as f:
    print(f.read())

print("--- Nội dung file CSV hiện tại ---")
with open("nhanvien.csv", "r", encoding="utf-8") as f:
    print(f.read())