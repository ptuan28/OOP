import json 
import pickle
import csv
import os
from abc import ABC, abstractmethod

from QLCB import CongNhan, KySu, QuanLyCanBo, NhanVien



class CanBo:
    def __init__(self, name, age, gender, address):
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address
    def tinh_luong(self):
        return 0
    
    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
            "address": self.address,
            "loai": "CanBo"
        }
    
    @staticmethod
    def from_dict(data):
        loai = data["loai"]
        if loai == "CongNhan":
            return CongNhan(data["name"], data["age"], data["gender"], data["address"], data["bac"])
        elif loai == "KySu":
            return KySu(data["name"], data["age"], data["gender"], data["address"], data["chuyen_nganh"])
        else:
            return CanBo(data["name"], data["age"], data["gender"], data["address"])
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Address: {self.address}"

class CongNhan(CanBo):
    def __init__(self, name, age, gender, address, bac):
        super().__init__(name, age, gender, address)
        self.bac = bac
        
    def tinh_luong(self):
        return self.bac * 1000000
    def to_dict(self):
        data = super().to_dict()
        data["loai"] = "CongNhan"
        data["bac"] = self.bac
        return data

class KySu(CanBo):
    def __init__(self, name, age, gender, address, chuyen_nganh):
        super().__init__(name, age, gender, address)
        self.chuyen_nganh = chuyen_nganh

    def tinh_luong(self):
        return 1500000

    def to_dict(self):
        data = super().to_dict()
        data["loai"] = "KySu"
        data["chuyen_nganh"] = self.chuyen_nganh
        return data
    
    def __str__(self):
        return super().__str__() + f", Chuyen Nganh: {self.chuyen_nganh}" + f", Luong: {self.tinh_luong()}"
    
class NhanVien(CanBo):
    def __init__(self, name, age, gender, address, cong_viec):
        super().__init__(name, age, gender, address)
        self.cong_viec = cong_viec
    def tinh_luong(self):
        return 1200000
    def to_dict(self):
        data = super().to_dict()
        data["loai"] = "NhanVien"
        data["cong_viec"] = self.cong_viec
        return data
    def __str__(self):
        return super().__str__() + f", Cong Viec: {self.cong_viec}" + f", Luong: {self.tinh_luong()}"

class QLCB:
    def __init__(self):
        self.ds = {}
    
    def doc_csv(self, filename):
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    try:
                        name = row["name"]
                        age = int(row["age"])
                        gender = row["gender"]
                        address = row["address"]
                        loai = row["loai"]
                        
                        if type == "CongNhan":
                            CanBo = CongNhan(name, age, gender, address, int(row["bac"]))
                        elif type == "KySu":
                            CanBo = KySu(name, age, gender, address, row["chuyen_nganh"])
                        else:
                            CanBo = NhanVien(name, age, gender, address, row["cong_viec"])

                        self.ds[name] = CanBo
                    except ValueError:
                        print("lỗi dữ liệu" , row)
        except FileNotFoundError:
            print("File not found!")  
    def them_csv(self, filename, can_bo):
        file_ton_tai = os.path.exists(filename)

        fieldnames = ["name", "age", "gender", "address", "loai", "bac", "chuyen_nganh", "cong_viec"]

        with open(filename, 'a', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)

            if not file_ton_tai:
                writer.writeheader()

            data = can_bo.to_dict()

            row = {
                "name": data.get("name", ""),
                "age": data.get("age", ""),
                "gender": data.get("gender", ""),
                "address": data.get("address", ""),
                "loai": data.get("loai", ""),
                "bac": data.get("bac", ""),
                "chuyen_nganh": data.get("chuyen_nganh", ""),
                "cong_viec": data.get("cong_viec", "")
            }

            writer.writerow(row)
        print(row)
        with open(filename, 'r', encoding='utf-8') as f:
            lines = len(f.readlines())
        print(f"Dòng thứ {lines} vừa được thêm")
        
    def nhap_csv(self, filename):
        print("=== Nhập dữ liệu (0 để thoát) ===")

        while True:
            loai = input("Loại: ")
            if loai == "0":
                break

            if loai not in ["CongNhan", "KySu", "NhanVien"]:
                print("❌ Loại không hợp lệ!")
                continue

            ten = input("Tên: ")
            tuoi = int(input("Tuổi: "))
            gt = input("Giới tính: ")
            dc = input("Địa chỉ: ")

            if loai == "CongNhan":
                bac = int(input("Bậc: "))
                cb = CongNhan(ten, tuoi, gt, dc, bac)
            elif loai == "KySu":
                nganh = input("Ngành: ")
                cb = KySu(ten, tuoi, gt, dc, nganh)
            else:
                cv = input("Công việc: ")
                cb = NhanVien(ten, tuoi, gt, dc, cv)

            self.add(cb)
            self.them_csv(filename, cb)
                
    def add(self, can_bo):
        if can_bo.name in self.ds:
            print("Đã tồn tại cán bộ này!")
        else:
            self.ds[can_bo.name] = can_bo
            print("Thêm cán bộ thành công!")
    
    def delete(self, name):
        if name in self.ds:
            del self.ds[name]
            print("Xóa cán bộ thành công!")
        else:
            print("Không tìm thấy cán bộ này!")
            
    def search(self, name):
        if name in self.ds:
            print(self.ds[name])
        else:
            print("Không tìm thấy cán bộ này!")
    
    def loc_theo_loai(self, loai):
        for can_bo in self.ds.values():
            if (loai == "CongNhan" and isinstance(can_bo, CongNhan)) or (loai == "KySu" and isinstance(can_bo, KySu)) or (loai == "NhanVien" and isinstance(can_bo, NhanVien)):
                print(can_bo)
    
    def top_luong(self, n):
        sorted_ds = sorted(self.ds.values(), key=lambda x: x.tinh_luong(), reverse=True)
        for can_bo in sorted_ds[:n]:
            print(can_bo)
    
    def hien_thi(self):
        for can_bo in self.ds.values():
            print(can_bo)
            
    def luu_json(self, filename = "can_bo.json"):
        data = [cb.to_dict() for cb in self.ds.values()]
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    
    def tai_json(self, filename = "can_bo.json"):
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.ds = {cb["name"]: CanBo.from_dict(cb) for cb in data}
        except :
            self.ds = {}
            
    def luu_pickle(self, filename = "can_bo.pkl"):
        with open(filename, 'wb') as f:
            pickle.dump(self.ds, f)
    
    def tai_pickle(self, filename = "can_bo.pkl"):
        try:
            with open(filename, 'rb') as f:
                self.ds = pickle.load(f)
        except:
            self.ds = {}
            
def menu():
    ql = QLCB()
    ql.tai_json()

    while True:

        print("1. Đọc CSV")
        print("2. Thêm")
        print("3. Nhập CSV")
        print("4. Xóa")
        print("5. Tìm")
        print("6. Hiển thị")
        print("7. Top 3 lương")
        print("8. Lưu JSON")
        print("0. Thoát")

        try:
            chon = int(input("Chọn: "))

            if chon == 1:
                ql.doc_csv("canbo.csv")

            elif chon == 2:
                loai = input("Loại: ")
                ten = input("Tên: ")
                tuoi = int(input("Tuổi: "))
                gt = input("Giới tính: ")
                dc = input("Địa chỉ: ")

                if loai == "CongNhan":
                    bac = int(input("Bậc: "))
                    cb = CongNhan(ten, tuoi, gt, dc, bac)
                elif loai == "KySu":
                    nganh = input("Ngành: ")
                    cb = KySu(ten, tuoi, gt, dc, nganh)
                else:
                    cv = input("Công việc: ")
                    cb = NhanVien(ten, tuoi, gt, dc, cv)

                ql.add(cb)
                ql.them_csv("canbo.csv", cb) 
            elif chon == 3:
                ql.nhap_csv("canbo.csv")
                
            elif chon == 4:
                ql.delete(input("Tên: "))

            elif chon == 5:
                ql.search(input("Tên: "))

            elif chon == 6:
                ql.hien_thi()

            elif chon == 7:
                n = int(input("Số lượng cán bộ muốn hiển thị: "))
                ql.top_luong(n)

            elif chon == 8:
                ql.luu_json()

            elif chon == 0:
                break

        except Exception as e:
            print("Lỗi:", e)



menu()