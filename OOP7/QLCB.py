from abc import ABC , abstractmethod

class TuoiKhongHopLe(Exception):
    def __init__(self, tuoi):
        super().__init__(f"Tuổi không hợp lệ: {tuoi}. Tuổi phải từ 18 đến 63 tuổi.")
    
class BacKhongHopLe(Exception):
    def __init__(self, bac):
        super().__init__(f"Cấp bậc không hợp lệ: {bac}. Cấp bậc phải từ 1 đến 10.")

class CanBo(ABC):
    def __init__(self, ho_ten, nam_sinh, gioi_tinh, dia_chi):
        self._ho_ten = ho_ten
        self._nam_sinh = nam_sinh
        self._gioi_tinh = gioi_tinh
        self._dia_chi = dia_chi

    @property
    def ho_ten(self):
        return self._ho_ten
    
    @property
    def nam_sinh(self):
        return self._nam_sinh
    @nam_sinh.setter
    def nam_sinh(self, value):
        tuoi = 2024 - value
        if tuoi < 18 or tuoi > 63:
            raise TuoiKhongHopLe(tuoi)
        self._nam_sinh = value
    
    @property
    def gioi_tinh(self):
        return self._gioi_tinh

    @property
    def dia_chi(self):
        return self._dia_chi

    @abstractmethod
    def mo_ta(self):
        pass

    def __str__(self):
        return(f"[{self.__class__.__name__}] {self._ho_ten} | ")
        
    def _loai_can_bo(self):
        return "Cán bộ"
    def get_ho_ten(self):
        return self._ho_ten
    
    def __str__(self):
        return (f"[{self.__class__.__name__}] {self._ho_ten} | "
                f"năm sinh: {self._nam_sinh} | giới tính: {self._gioi_tinh} | địa chỉ: {self._dia_chi}")
    
    def __repr__(self):
        return (f"`{self.__class__.__name__}(ho_ten='{self._ho_ten}', nam_sinh={self._nam_sinh}, "
                f"gioi_tinh='{self._gioi_tinh}', dia_chi='{self._dia_chi}')")
    
    def __eq__(self,other):
        if not isinstance(other, CanBo):
            return False
        return (self._ho_ten == other._ho_ten and
                self._nam_sinh == other._nam_sinh and
                self._gioi_tinh == other._gioi_tinh and
                self._dia_chi == other._dia_chi)
        
    def __lt__(self, other):
        return self._ho_ten < other._ho_ten
    
    def __hash__(self):
        return hash((self._ho_ten, self._nam_sinh, self._gioi_tinh, self._dia_chi))
        
    def hien_thi(self):
        print(f"  Họ tên   : {self._ho_ten}")
        print(f"  Năm sinh : {self._nam_sinh}")
        print(f"  Giới tính: {self._gioi_tinh}")
        print(f"  Địa chỉ  : {self._dia_chi}")
        
class CongNhan(CanBo):
    def __init__(self, ho_ten, nam_sinh, gioi_tinh, dia_chi, cap_bac):
        super().__init__(ho_ten, nam_sinh, gioi_tinh, dia_chi)
        self.cap_bac = cap_bac
    @property
    def cap_bac(self):
        return self.__cap_bac
       
    @cap_bac.setter    
    def cap_bac(self, cap_bac):   
        if not (1 <= cap_bac <= 10):
            raise BacKhongHopLe(cap_bac)
        self.__cap_bac = cap_bac
        
    def _loai_can_bo(self):
        return "Công nhân"
    
    def mo_ta(self):
        return f"Công nhân cấp bậc {self.cap_bac}"
    
    def __repr__(self):
        return (f"`{self.__class__.__name__}(ho_ten='{self._ho_ten}', nam_sinh={self._nam_sinh}, "
                f"gioi_tinh='{self._gioi_tinh}', dia_chi='{self._dia_chi}', cap_bac={self.cap_bac})")
        
    def hien_thi(self):
        super().hien_thi()
        print(f"  Cấp bậc  : {self.cap_bac}")
        
class KySu(CanBo):
    def __init__(self, ho_ten, nam_sinh, gioi_tinh, dia_chi, nganh_dao_tao):
        super().__init__(ho_ten, nam_sinh, gioi_tinh, dia_chi)
        self.__nganh_dao_tao = nganh_dao_tao
        
    @property
    def nganh_dao_tao(self):
        return self.__nganh_dao_tao
    
    def mo_ta(self):
        return super().mo_ta() + f" - Kỹ sư ngành {self.nganh_dao_tao}"    
    
    def __repr__(self):
        return (f"`{self.__class__.__name__}(ho_ten='{self._ho_ten}', nam_sinh={self._nam_sinh}, "
                f"gioi_tinh='{self._gioi_tinh}', dia_chi='{self._dia_chi}', nganh_dao_tao='{self.nganh_dao_tao}')")
        
    def _loai_can_bo(self):
        return "Kỹ sư"
    
    def hien_thi(self):
        super().hien_thi()
        print(f"  Ngành đào tạo: {self.nganh_dao_tao}")
    
class NhanVien(CanBo):
    def __init__(self, ho_ten, nam_sinh, gioi_tinh, dia_chi, cong_viec):
        super().__init__(ho_ten, nam_sinh, gioi_tinh, dia_chi)
        self.__cong_viec = cong_viec
        
    @property
    def cong_viec(self):
        return self.__cong_viec
    
    def mo_ta(self):
        return super().mo_ta() + f" - Nhân viên làm công việc {self.cong_viec}"
    
    def __repr__(self):
        return (f"`{self.__class__.__name__}(ho_ten='{self._ho_ten}', nam_sinh={self._nam_sinh}, "
                f"gioi_tinh='{self._gioi_tinh}', dia_chi='{self._dia_chi}', cong_viec='{self.cong_viec}')")
        
    def _loai_can_bo(self):
        return "Nhân viên"
    
    def hien_thi(self):
        super().hien_thi()
        print(f"  Công việc : {self.cong_viec}")
        
# quản lý cán bộ    
    
class QuanLyCanBo:
    FILE_NAME = "danh_sach_can_bo.txt"
    def __init__(self):
        self.__danh_sach_can_bo = []
#thêm cán bộ
    def them_can_bo(self, can_bo : CanBo):
        self.__danh_sach_can_bo.append(can_bo)
        print (f"Đã thêm cán bộ: {can_bo.ho_ten} - {can_bo._loai_can_bo()}")
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
        choice = input("Lựa chọn (1-3): ").strip()
        if choice not in ('1', '2', '3'):
            print("Lựa chọn không hợp lệ.")
            return
        
        try:
            ho_ten, nam_sinh, gioi_tinh, dia_chi = self._nhap_can_bo_chung()
         #################

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
        except ValueError:
                print("Dữ liệu nhập vào không hợp lệ.")
                return    
        
    def tim_kiem_va_hien_thi(self):
        ten = input("Nhập tên cán bộ cần tìm: ")
        ket_qua = self.tim_kiem_theo_ten(ten)     
        if ket_qua:
            print(f"Tìm thấy {len(ket_qua)} cán bộ:")
            for cb in ket_qua:
                cb.hien_thi()
        else:
            print("Không tìm thấy cán bộ nào.")
            
    def luu_file(self):
        with open(self.FILE_NAME, 'w', encoding='utf-8') as f:
            for cb in self.__danh_sach_can_bo:
                f.write(repr(cb) + '\n')
        print(f"Đã lưu danh sách cán bộ vào file '{self.FILE_NAME}'")
        
    def doc_file(self):
        try:
            with open(self.FILE_NAME, 'r', encoding = 'utf-8') as f:
                line = f.readline()
                for line in f:
                    print(line.strip())
        except FileNotFoundError:
            print(f"File '{self.FILE_NAME}' không tồn tại.")
              
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

#thử tuổi khác 
    try:
        CongNhan("test tuổi:", 2008, "Nam", "Hanoi", 3)
    except TuoiKhongHopLe as e:
        print(f"Lỗi: {e}")
#thử cấp bậc khác
    try:
        CongNhan("test cấp bậc:", 1990, "Nam", "Hanoi", 15)
    except BacKhongHopLe as e:
        print(f"Lỗi: {e}")

#so sánh
    a = CongNhan("Phan Van N A", 1990, "Nam", "Hanoi", 3)
    b = CongNhan("Phan Van N A", 1990, "Nam", "Hanoi", 3)
    print(f"a == b: {a == b}")

#thay thế
    #print(repr(quan_ly._QuanLyCanBo__danh_sach_can_bo[0]))
    
    quan_ly.luu_file()
    quan_ly.doc_file()
    quan_ly.run() 
        
    
    

 