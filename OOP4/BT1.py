class Nhanvien:
    Luong_Max = 20000000
    
    def __init__(self, ten, luongcb, hesoluong):
        self.__ten = ten
        self.__luongcb = luongcb
        self.__hesoluong = hesoluong
    def get_ten(self):
        return self.__ten
    def get_luongcb(self):
        return self.__luongcb
    def get_hesoluong(self):
        return self.__hesoluong
    
    
    
    def set_ten(self, ten):
        self.__ten = ten
    def set_luongcb(self, luongcb):
        self.__luongcb = luongcb
    def set_hesoluong(self, hesoluong):
        self.__hesoluong = hesoluong
        
        
        
        
    def tinhluong(self):
        return self.__luongcb * self.__hesoluong
    
    
    def tangluong(self, giaTri):
        hesomoi = self.__hesoluong + giaTri
        luongmoi = self.__luongcb * hesomoi
        if luongmoi > Nhanvien.Luong_Max:
            print("Luong moi vuot qua muc luong toi da")
            return False
        else:
            self.__hesoluong = hesomoi
            print("Luong moi sau khi tang: ", luongmoi)
            return True
    def inTTin(self):
        print("Ten: ", self.__ten)
        print("Luong co ban: ", self.__luongcb)
        print("He so luong: ", self.__hesoluong)
        print("Luong: ", self.tinhluong())
nv = Nhanvien("Phan Anh Tuan", 5000000000, 5 ,)
#nv.inTTin()
print("Tên Nhân Viên: ", nv.get_ten())
print("Lương cơ bản: ", nv.get_luongcb())
print("Hệ số lương: ", nv.get_hesoluong())
print("Lương mới: ", nv.tangluong(1.5))
