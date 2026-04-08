ds = []    
n = int(input("Nhập số lượng phân số: "))
for i in range(n):
    while True:
        try:
            s = input(f"Nhập phân số {i+1} (dạng tu/mau): ")
            tu, mau = map(int, s.split('/'))
            ps = PhanSo(tu, mau)
            ds.append(ps)
            break
        except MauSoBangKhong as e:
            print(e)
        except ValueError:
            print("không phải phân số")
        except Exception as e:
            print(f"Lỗi không xác định: {e}")

for ps in sor