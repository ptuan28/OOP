from abc import ABC, abstractmethod
import math

class MauSoBangKhong(Exception):
    def __init__(self, message):
        super().__init__(f"mẫu không được bằng không {message}")
        

class PhanSo():
    def __init__(self, tu_so , mau_so):
        self.tu_so = tu_so
        self.mau_so = mau_so
        
    @property
    def tu_so(self):
        return self._tu_so
    
    @tu_so.setter
    def tu_so(self, value):
        self._tu_so = value
        
    @property
    def mau_so(self):
        return self._mau_so

    @mau_so.setter
    def mau_so(self, value):
        if value == 0:
            raise MauSoBangKhong(f"mẫu số không được bằng 0")
        self._mau_so = value
#ktra có tối giản hay không
    #@abstractmethod
    def is_toi_gian(self):
        return math.gcd(abs(self.tu_so), abs(self.mau_so)) == 1
    #rút gọn
    def toi_gian(self):
        g = math.gcd(abs(self.tu_so), abs(self.mau_so))
        tu_so = self.tu_so // g
        mau_so = self.mau_so // g
        return PhanSo(tu_so, mau_so)
        # g = math.gcd(abs(self.tu_so), abs(self.mau_so))
        # return PhanSo(self.tu_so // g, self.mau_so // g)
    #cộng
    def __add__(self, other):
        if not isinstance(other, PhanSo):
            return NotImplemented
        tu_so_moi = self.tu_so * other.mau_so + other.tu_so * self.mau_so
        mau_so_moi = self.mau_so * other.mau_so
        return PhanSo(tu_so_moi, mau_so_moi).toi_gian()
    #trừ
    def __sub__(self, other):
        if not isinstance(other, PhanSo):
            return NotImplemented
        tu_so_moi = self.tu_so * other.mau_so - other.tu_so * self.mau_so
        mau_so_moi = self.mau_so * other.mau_so
        return PhanSo(tu_so_moi, mau_so_moi).toi_gian()
    #nhân
    def __mul__(self, other):
        if not isinstance(other, PhanSo):
            return NotImplemented
        tu_so_moi = self.tu_so * other.tu_so
        mau_so_moi = self.mau_so * other.mau_so
        return PhanSo(tu_so_moi, mau_so_moi).toi_gian()
  #chia  
    def __truediv__(self, other):
        if not isinstance(other, PhanSo):
            return NotImplemented
        if other.tu_so == 0:
            raise MauSoBangKhong("không thể chia cho phân số có tử số bằng 0")
        tu_so_moi = self.tu_so * other.mau_so
        mau_so_moi = self.mau_so * other.tu_so
        return PhanSo(tu_so_moi, mau_so_moi).toi_gian()
#so sánh
    def __eq__(self, other):
        if not isinstance(other, PhanSo):
            return NotImplemented
        return self.tu_so * other.mau_so == other.tu_so * self.mau_so
    
    def __lt__(self, other):
        if not isinstance(other, PhanSo):
            return NotImplemented
        return self.tu_so * other.mau_so < other.tu_so * self.mau_so
    def __gt__(self, other):
        if not isinstance(other, PhanSo):
            return NotImplemented
        return self.tu_so * other.mau_so > other.tu_so * self.mau_so
    def __hash__(self):
        g = math.gcd(abs(self.tu_so), abs(self.mau_so))
        return hash((self.tu_so // g, self.mau_so // g))
    
    def __str__(self):
        ps = self.toi_gian()
        if ps.mau_so == 1:
            return str(ps.tu_so)
        return f"{ps.tu_so}/{ps.mau_so}"
        # g = math.gcd(abs(self._tu_so), abs(self._mau_so))
        # t, m = self._tu_so // g, self._mau_so // g
        # if m == 1: return str(t)
        # return f"{t}/{m}"
    def __repr__(self):
        return f"PhanSo({self.tu_so}, {self.mau_so})"
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

for ps in sorted(ds):
    print(ps)    
    
    
    