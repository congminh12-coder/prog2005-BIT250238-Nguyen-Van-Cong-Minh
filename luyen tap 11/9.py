def nhap_ma_tran(ten_mt, hang, cot):
    ma_tran = []
    print(f"\n--- Nhập dữ liệu cho {ten_mt} ---")
    for i in range(hang):
        hang_tam = []
        for j in range(cot):
            while True:
                gia_tri = input(f"Nhập phần tử [{i + 1}][{j + 1}]: ").strip()
                if not gia_tri:
                    print("Lỗi: Bạn không được để trống giá trị! Vui lòng nhập lại.")
                    continue
                try:
                    so = float(gia_tri)
                    hang_tam.append(so)
                    break
                except ValueError:
                    print("Lỗi: Giá trị nhập vào phải là số! Vui lòng nhập lại.")
        ma_tran.append(hang_tam)
    return ma_tran
try:
    m = int(input("Nhập số hàng của ma trận: "))
    n = int(input("Nhập số cột của ma trận: "))

    ma_tran_A = nhap_ma_tran("Ma trận A", m, n)
    ma_tran_B = nhap_ma_tran("Ma trận B", m, n)
    ma_tran_tong = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            ma_tran_tong[i][j] = ma_tran_A[i][j] + ma_tran_B[i][j]
    print("\n" + "=" * 20)
    print("Kết quả tổng hai ma trận:")
    for hang in ma_tran_tong:
        print("\t".join([str(x) for x in hang]))

except ValueError:
    print("Lỗi: Số hàng và số cột phải là số nguyên!")