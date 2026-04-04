from abc import ABC , abstractmethod


class GiaKhongHopLe(Exception):
    def __init__(self, gia):
        super().__init__(f"Giá không hợp lệ: {gia}. Giá phải >= 0.")


class MaHangTrungLap(Exception):
    def __init__(self, ma):
        super().__init__(f"Mã hàng bị trùng lặp: {ma}.")



class HangHoa(ABC):
    def __init__(self, ma_hang, ten_hang, ng_sx,gia):
        self._ma_hang = ma_hang
        self._ten_hang = ten_hang
        self._ng_sx = ng_sx
        self.don_gia = gia
        
    @property
    def ma_hang(self):
        return self._ma_hang
    
    @property
    def ten_hang(self):
        return self._ten_hang

    @property
    def ng_sx(self):
        return self._ng_sx

    @property
    def don_gia(self):
        return self._don_gia
    
    @don_gia.setter
    def don_gia(self, value):
        if value < 0:
            raise GiaKhongHopLe(value)
        self._don_gia = value
        
    @abstractmethod
    def loai_hang(self):
        pass
    def inTTin(self):
        pass
    
    def __str__(self):
        return (f"[{self.loai_hang()}] {self._ma_hang} - {self._ten_hang} - {self._ng_sx} - {self._don_gia:,.0f} VND")
    
    def __eq__(self, other):
        if not isinstance(other, HangHoa):
            return False
        return self._ma_hang == other._ma_hang
    
    def __lt__(self, other):
        return self._ma_hang < other._ma_hang
    
    def __hash__(self):
        return hash(self._ma_hang)

    def hienthi(self):
        print(f"Mã hàng: {self._ma_hang}")
        print(f"Tên hàng: {self._ten_hang}")
        print(f"Ngày sản xuất: {self._ng_sx}")
        print(f"Đơn giá: {self._don_gia:,.0f} VND")


class HangDienMay(HangHoa):
    def __init__(self, ma_hang ,ten_hang , ng_sx , gia , tg_baohanh , dien_ap, cong_suat):
        super().__init__(ma_hang, ten_hang, ng_sx, gia)
        self.tg_baohanh = tg_baohanh
        self.dien_ap = dien_ap
        self.cong_suat = cong_suat
        
        
    def loai_hang(self):
        return "Điện máy"
    
    def inTTin(self):
        print(f"{self} | bảo hành: {self.tg_baohanh} tháng - {self.dien_ap}V - {self.cong_suat}W")
    
        
    def hienthi(self):
        super().hienthi()
        print(f"Thời gian bảo hành: {self.tg_baohanh} tháng")
        print(f"Điện áp: {self.dien_ap} V")
        print(f"Công suất: {self.cong_suat} W")
class HangSanhSu(HangHoa):
    def __init__(self, ma_hang, ten_hang, ng_sx, gia, loai_nguyenlieu):
        super().__init__(ma_hang, ten_hang, ng_sx, gia)
        self.loai_nguyenlieu = loai_nguyenlieu
        
    def loai_hang(self):
        return "Sành sứ"
    
    def inTTin(self):
        print(f"{self} | loại nguyên liệu: {self.loai_nguyenlieu}")
    
    def hienthi(self):
        super().hienthi()
        print(f"Loại nguyên liệu: {self.loai_nguyenlieu}")
        
        
class HangThucPham(HangHoa):
    def __init__(self, ma_hang, ten_hang, ng_sx, gia, ngay_sx, ngay_hethan):
        super().__init__(ma_hang, ten_hang, ng_sx, gia)
        self.ngay_sx = ngay_sx
        self.ngay_hethan = ngay_hethan
        
    def loai_hang(self):
        return "Thực phẩm"
    
    def inTTin(self):
       print(f"{self} | hạn sử dụng: {self.ngay_hethan}")
    
    
    def hienthi(self):
        super().hienthi()
        print(f"Ngày sản xuất: {self.ngay_sx}")
        print(f"Ngày hết hạn: {self.ngay_hethan}")
        
        
        
class DanhSachHangHoa:
    def __init__(self):
        self.danh_sach = []
        
    def them_hang(self, sp: HangHoa):
        for existing_sp in self.danh_sach:
            if existing_sp.ma_hang == sp.ma_hang:
                raise MaHangTrungLap(sp.ma_hang)
        self.danh_sach.append(sp)
        print(f"Đã thêm hàng hóa: {sp}")

        
    def hien_thi_danh_sach(self):
        for sp in self.danh_sach:
            sp.inTTin()
            
    def sap_xep_theo_gia(self):
        return sorted(self.danh_sach, key=lambda sp: sp.don_gia)
    FILE_NAME = "danh_sach_hang_hoa.txt"
    def luu_file(self):
        with open("self.FILE_NAME", "w", encoding="utf-8") as f:
            for sp in self.danh_sach:
                f.write(str(sp) + "\n")
        print("Đã lưu danh sách hàng hóa vào file.")
                
    def doc_file(self):
        try:
            with open("self.FILE_NAME", "r", encoding="utf-8") as f:
                lines = f.readlines()
            for line in lines:
                print(line.strip())
                
        except FileNotFoundError:
            print("File không tồn tại.")

if __name__ == "__main__":
    ds = DanhSachHangHoa()
    
    ds.them_hang(HangDienMay("T1", "Tivi Samsung", "2034-01-01", 15000000, 24, 220, 100))
    ds.them_hang(HangSanhSu("SGP", "Gốm sứ cao cấp", "2034-01-01", 10000000000 , "kim cương"))
    ds.them_hang(HangThucPham("FLASH", "Thực phẩm", "2034-01-01", 50000, "2034-01-01", "2034-12-31"))
    
    
    print("Thông tin hàng điện máy:")
    ds.danh_sach[0].hienthi()
    print("\nThông tin hàng sành sứ:")
    ds.danh_sach[1].hienthi()
    print("\nThông tin hàng thực phẩm:")
    ds.danh_sach[2].hienthi()
    
    ds.hien_thi_danh_sach()
    #thử mã trùng
    print("\nThử thêm hàng hóa với mã trùng")
    try:
        ds.them_hang(HangDienMay("T1", "Tivi LG", "2034-01-01", 12000000, 24, 220, 100))
    except MaHangTrungLap as e:
        print(e)
        
    #thử giá âm
    print("\nThử thêm hàng hóa với giá âm")
    try:
        ds.them_hang(HangDienMay("T2", "Tivi LG", "2034-01-01", -12000000, 24, 220, 100))
    except GiaKhongHopLe as e:
        print(e)
        
    #lưu và đọc file
    print("\nLưu file")
    ds.luu_file()
    ds.doc_file()
        
    