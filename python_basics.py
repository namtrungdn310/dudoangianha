can_nha = {
    "dien_tich": 75,
    "so_tang": 3
}

def tinh_gia(nha, gia_moi_m2):
    gia_dat = nha["dien_tich"] * gia_moi_m2
    phu_thu = nha["so_tang"] * 100_000_000
    return gia_dat + phu_thu

print(tinh_gia(can_nha, 40_000_000))