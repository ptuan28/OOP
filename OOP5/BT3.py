class CanBo:
    def __init__(self, ho_ten, nam_sinh, gioi_tinh, dia_chi):
        self.__ho_ten = ho_ten
        self.__nam_sinh = nam_sinh
        self.__gioi_tinh = gioi_tinh
        self.__dia_chi = dia_chi
    def _loai_can_bo(self):
        return "Cán bộ"
    def get_ho_ten(self):
        return self.__ho_ten
    
    def hien_thi(self):
        print(f"  Họ tên   : {self.__ho_ten}")
        print(f"  Năm sinh : {self.__nam_sinh}")
        print(f"  Giới tính: {self.__gioi_tinh}")
        print(f"  Địa chỉ  : {self.__dia_chi}")
class CongNhan(CanBo):
    def __init__(self, ho_ten, nam_sinh, gioi_tinh, dia_chi, cap_bac):
        super().__init__(ho_ten, nam_sinh, gioi_tinh, dia_chi)
        if not (1 <= cap_bac <= 10):
            raise ValueError("Cấp bậc phải từ 1 đến 10")
        self.__cap_bac = cap_bac
    def _loai_can_bo(self):
        return "Công nhân"
class KySu(CanBo):
    def __init__(self, ho_ten, nam_sinh, gioi_tinh, dia_chi, nganh_dao_tao):
        super().__init__(ho_ten, nam_sinh, gioi_tinh, dia_chi)
        self.__nganh_dao_tao = nganh_dao_tao
    def _loai_can_bo(self):
        return "Kỹ sư"
class NhanVien(CanBo):
    def __init__(self, ho_ten, nam_sinh, gioi_tinh, dia_chi, cong_viec):
        super().__init__(ho_ten, nam_sinh, gioi_tinh, dia_chi)
        self.__cong_viec = cong_viec
    def _loai_can_bo(self):
        return "Nhân viên"
    

# quản lý cán bộ    
    
class QuanLyCanBo:
    def __init__(self):
        self.__danh_sach_can_bo = []
#thêm cán bộ
    def them_can_bo(self, can_bo : CanBo):
        self.__danh_sach_can_bo.append(can_bo)
        print (f"Đã thêm cán bộ: {can_bo._CanBo__ho_ten} - {can_bo._loai_can_bo()}")
#tìm kiếm theo tên
    def tim_kiem_theo_ten(self, ten):
        return [cb for cb in self.__danh_sach_can_bo
                if ten.lower() in cb.get_ho_ten().lower()]    
#hiển thị danh sách 
    def hien_thi_danh_sach(self):
        if not self.__danh_sach_can_bo:
            print("Không có cán bộ")
            return
        print(f"\n{'─'*50}")
        print(f"  DANH SÁCH CÁN BỘ  ({len(self.__danh_sach_can_bo)} người)")
        print(f"{'─'*50}")
        for i, cb in enumerate(self.__danh_sach_can_bo, 1):
            print(f"\n  #{i}")
            cb.hien_thi()
        print(f"{'─'*50}")
#bảng điều khiển chính
    def _nhap_can_bo_chung(self):
        ho_ten = input("Nhập họ tên: ")
        nam_sinh = int(input("Nhập năm sinh: "))
        gioi_tinh = input("Nhập giới tính: ")
        dia_chi = input("Nhập địa chỉ: ")
        return ho_ten, nam_sinh, gioi_tinh, dia_chi
    def them_can_bo_tu_ban_phim(self):
        print("Chọn loại cán bộ để thêm:")
        print("1. Công nhân")
        print("2. Kỹ sư")
        print("3. Nhân viên")
        choice = input("Lựa chọn (1-3): ")
        if choice == '1':
            ho_ten, nam_sinh, gioi_tinh, dia_chi = self._nhap_can_bo_chung()
            cap_bac = int(input("Nhập cấp bậc (1-10): "))
            can_bo = CongNhan(ho_ten, nam_sinh, gioi_tinh, dia_chi, cap_bac)
        elif choice == '2':
            ho_ten, nam_sinh, gioi_tinh, dia_chi = self._nhap_can_bo_chung()
            nganh_dao_tao = input("Nhập ngành đào tạo: ")
            can_bo = KySu(ho_ten, nam_sinh, gioi_tinh, dia_chi, nganh_dao_tao)
        elif choice == '3':
            ho_ten, nam_sinh, gioi_tinh, dia_chi = self._nhap_can_bo_chung()
            cong_viec = input("Nhập công việc: ")
            can_bo = NhanVien(ho_ten, nam_sinh, gioi_tinh, dia_chi, cong_viec)
        else:
            print("Lựa chọn không hợp lệ.")
            return

        self.them_can_bo(can_bo)
    def tim_kiem_va_hien_thi(self):
        ten = input("Nhập tên cán bộ cần tìm: ")
        ket_qua = self.tim_kiem_theo_ten(ten)     
        if ket_qua:
            print(f"Tìm thấy {len(ket_qua)} cán bộ:")
            for cb in ket_qua:
                cb.hien_thi()
        else:
            print("Không tìm thấy cán bộ nào.")
    def run(self):
        while True:
            print("\nMenu:")
            print("1. Thêm cán bộ")
            print("2. Tìm kiếm cán bộ theo tên")
            print("3. Hiển thị danh sách cán bộ")
            print("4. Thoát")
            choice = input("Lựa chọn (1-4): ")
            if choice == '1':
                self.them_can_bo_tu_ban_phim()
            elif choice == '2':
                self.tim_kiem_va_hien_thi()   
            elif choice == '3':
                self.hien_thi_danh_sach()
            elif choice == '4':
                print("Thoát chương trình.")
                break
            else:
                print("Lựa chọn không hợp lệ.")

if __name__ == "__main__":
    quan_ly = QuanLyCanBo()
        
    quan_ly.them_can_bo(NhanVien("Phan Anh T", 1995, "Nam", "DN", "Lập trình viên"))
    quan_ly.them_can_bo(KySu("Nguyen Thi H", 1992, "Nu", "HN", "CNTT"))
    quan_ly.them_can_bo(CongNhan("Phan Van N A", 1990, "Nam", "Hanoi", 3))

    quan_ly.run() 
        
    
    

