tu_dien = {
    "ten": "Hoàng",
    "tuoi": 20,
    "nghe_nghiep": "Sinh vien"
}
key_can_tim = input("Nhập tên khóa (key) bạn muốn kiểm tra: ")
if key_can_tim in tu_dien:
    print(f"Chúc mừng! Khóa '{key_can_tim}' CÓ tồn tại.")
    print(f"Giá trị của nó là: {tu_dien[key_can_tim]}")
else:
    print(f"Rất tiếc, khóa '{key_can_tim}' KHÔNG tồn tại trong từ điển.")