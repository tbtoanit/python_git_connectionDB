from nhan_vien import Nhan_Vien

def nhap_nhan_vien():
    ds_nhan_vien = []
    so_luong = int(input("Ban muon nhap bao nhieu nhan vien? "))
    i = 1
    while(i<=so_luong):
        #code cho nhap nhan vien vao day
        e = Nhan_Vien(input("Vui long nhap ma nhan vien"), input("vui long nhap ten nv"), input("vui long nhap chuc vu"))
        ds_nhan_vien.append(e)
        i+=1
    return ds_nhan_vien

def xuat_thong_tin(list_nv):
    for nv in list_nv:
        print(nv.get_ma_nhan_vien(), "---", nv.get_ten_nhan_vien(),"---",nv.get_chuc_vu())
