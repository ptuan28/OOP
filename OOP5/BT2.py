class PhongBan:
    luong_mac_dinh = 5000000
    def __init__(self, ma_nhanvien , ho_ten , nam_sinh , gioi_tinh , dia_chi , he_soluong , luong_max):
        if  he_soluong <= 0:
            raise ValueError("Hệ số lương không được âm")
        self.ma_nhanvien = ma_nhanvien
        self.ho_ten = ho_ten
        self.nam_sinh = nam_sinh
        self.gioi_tinh = gioi_tinh
        self.dia_chi = dia_chi
        self.he_soluong = he_soluong
        self.luong_max = luong_max
    def tinhluong(self):
        luong = self.he_soluong * self.luong_mac_dinh
        return min(luong, self.luong_max)
    
    def hienthi(self):
        print(f"Mã nhân viên: {self.ma_nhanvien}")
        print(f"Họ tên: {self.ho_ten}")
        print(f"Năm sinh: {self.nam_sinh}")
        print(f"Giới tính: {self.gioi_tinh}")
        print(f"Địa chỉ: {self.dia_chi}")
        print(f"Hệ số lương: {self.he_soluong}")
        print(f"Lương tối đa: {self.luong_max}")
    
    def __str__(self):
        return f"[{self.__class__.__name__}] {self.ma_nhanvien} - {self.ho_ten}"
class CongTacVien(PhongBan):
    def __init__(self, ma_nhanvien , ho_ten , nam_sinh , gioi_tinh , dia_chi , he_soluong , luong_max , han_hopdong:str , phu_cap: float):
        super().__init__(ma_nhanvien , ho_ten , nam_sinh , gioi_tinh , dia_chi , he_soluong , luong_max)
        if han_hopdong not in ["3 tháng","6 tháng", "12 tháng"]:
            raise ValueError("Hạn hợp đồng không hợp lệ")
        self.han_hopdong = han_hopdong
        self.phu_cap = phu_cap
    
    def tinhluong(self) -> float:
        luong_ctv = super().tinhluong() + self.phu_cap
        return min(luong_ctv, self.luong_max)

    def hienthi(self):
        super().hienthi()
        print(f"Hạn hợp đồng: {self.han_hopdong}")
        print(f"Phụ cấp: {self.phu_cap}")
class NhanVienChinhthuc(PhongBan):
    def __init__(self, ma_nhanvien , ho_ten , nam_sinh , gioi_tinh , dia_chi , he_soluong , luong_max , vi_tri_cong_viec:str):
        super().__init__(ma_nhanvien , ho_ten , nam_sinh , gioi_tinh , dia_chi , he_soluong , luong_max)
        self.vi_tri_cong_viec = vi_tri_cong_viec
    
    def tinhluong(self) -> float:
        luong_nhan_vienchinhthuc = self.he_soluong * self.luong_mac_dinh
        return min(luong_nhan_vienchinhthuc, self.luong_max)
    
    def hienthi(self):
        super().hienthi()
        print(f"Vị trí công việc: {self.vi_tri_cong_viec}")
    
class TruongPhong(PhongBan):
    def __init__(self, ma_nhanvien , ho_ten , nam_sinh , gioi_tinh , dia_chi , he_soluong , luong_max , ngay_bat_dau_quan_ly:str , phu_cap_ql: float):
        super().__init__(ma_nhanvien , ho_ten , nam_sinh , gioi_tinh , dia_chi , he_soluong , luong_max)
        self.ngay_bat_dau_quan_ly = ngay_bat_dau_quan_ly
        self.phu_cap_ql = phu_cap_ql

    def tinhluong(self) -> float:
        luong_truong_phong = super().tinhluong() + self.phu_cap_ql
        return min(luong_truong_phong, self.luong_max)
    
    def hienthi(self):
        super().hienthi()
        print(f"Ngày bắt đầu quản lý: {self.ngay_bat_dau_quan_ly}")
        print(f"Phụ cấp quản lý: {self.phu_cap_ql}")
if __name__ == "__main__":
    ctv = CongTacVien("CTV001", "Nguyen Van A", "1990-01-01", "Nam", "123 Đường ABC", 2.5, 20000000, "6 tháng", 2000000)
    nvc = NhanVienChinhthuc("NVC001", "Le Thi B", "1985-05-15", "Nữ", "456 Đường XYZ", 3.0, 30000000, "Nhân viên kinh doanh")
    tp = TruongPhong("TP001", "Tran Van C", "1980-10-20", "Nam", "789 Đường DEF", 4.0, 50000000, "2020-01-01", 5000000)
    
    print("Thông tin Cộng tác viên:")
    ctv.hienthi()
    print(f"Lương Cộng tác viên: {ctv.tinhluong()}\n")
    
    print("Thông tin Nhân viên chính thức:")
    nvc.hienthi()
    print(f"Lương Nhân viên chính thức: {nvc.tinhluong()}\n")
    
    print("Thông tin Trưởng phòng:")
    tp.hienthi()
    print(f"Lương Trưởng phòng: {tp.tinhluong()}\n")
