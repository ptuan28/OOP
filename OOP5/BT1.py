class HangHoa:
    def __init__(self, ma_hang, ten_hang, ng_sx,gia):
        self.ma_hang = ma_hang
        self.ten_hang = ten_hang
        self.ng_sx = ng_sx
        self.don_gia = gia
    def hienthi(self):
        print(f"Mã hàng: {self.ma_hang}")
        print(f"Tên hàng: {self.ten_hang}")
        print(f"Ngày sản xuất: {self.ng_sx}")
        print(f"Đơn giá: {self.don_gia}")
    # def __str__(self):
    #     return f"Mã Hàng: {self.__class__}"
class HangDienMay(HangHoa):
    def __init__(self, ma_hang ,ten_hang , ng_sx , gia , tg_baohanh , dien_ap, cong_suat):
        super().__init__(ma_hang, ten_hang, ng_sx, gia)
        self.tg_baohanh = tg_baohanh
        self.dien_ap = dien_ap
        self.cong_suat = cong_suat
    def hienthi(self):
        super().hienthi()
        print(f"Thời gian bảo hành: {self.tg_baohanh} tháng")
        print(f"Điện áp: {self.dien_ap} V")
        print(f"Công suất: {self.cong_suat} W")
class HangSanhSu(HangHoa):
    def __init__(self, ma_hang, ten_hang, ng_sx, gia, loai_nguyenlieu):
        super().__init__(ma_hang, ten_hang, ng_sx, gia)
        self.loai_nguyenlieu = loai_nguyenlieu
    def hienthi(self):
        super().hienthi()
        print(f"Loại nguyên liệu: {self.loai_nguyenlieu}")
class HangThucPham(HangHoa):
    def __init__(self, ma_hang, ten_hang, ng_sx, gia, ngay_sx, ngay_hethan):
        super().__init__(ma_hang, ten_hang, ng_sx, gia)
        self.ngay_sx = ngay_sx
        self.ngay_hethan = ngay_hethan
    def hienthi(self):
        super().hienthi()
        print(f"Ngày sản xuất: {self.ngay_sx}")
        print(f"Ngày hết hạn: {self.ngay_hethan}")
if __name__ == "__main__":
    hang_dien_may = HangDienMay("T1", "Tivi Samsung", "2034-01-01", 15000000, 24, 220, 100)
    hang_sanh_su = HangSanhSu("SGP", "Gốm sứ cao cấp", "2034-01-01", 10000000000 , "kim cương")
    hang_thuc_pham = HangThucPham("FLASH", "Thực phẩm", "2034-01-01", 50000, "2034-01-01", "2034-12-31")
    
    
    
    print("Thông tin hàng điện máy:")
    hang_dien_may.hienthi()
    print("\nThông tin hàng sành sứ:")
    hang_sanh_su.hienthi()
    print("\nThông tin hàng thực phẩm:")
    hang_thuc_pham.hienthi()
