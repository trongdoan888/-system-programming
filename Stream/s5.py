import os

FILE_NAME = 'dem_chuoi.txt'

def tao_file_du_lieu():
    # Giả sử đây là danh sách các chuỗi cần kiểm tra
    chuoi = ["apple", "banana", "ant", "cat", "album", "dog"]

    try:
        with open(FILE_NAME, 'w', encoding="utf-8") as f:
            for phan_tu in chuoi:
                f.write(f"{phan_tu}\n") # Nên có dấu xuống dòng để phân biệt các chuỗi
        
        print(f"[OK] Đã tạo file {FILE_NAME}.")

    except Exception as e:
        print(f"[!] Lỗi tạo file: {e}")

def dem_chuoi_theo_chu_cai(chu_cai_bat_dau):
    if not os.path.exists(FILE_NAME):
        print("File không tồn tại!")
        return

    count = 0
    try:
        with open(FILE_NAME, 'r', encoding="utf-8") as f:
            # Cách làm chuẩn Stream: Đọc từng dòng (line) để xử lý
            for line in f:
                chuoi_hien_tai = line.strip() # Xóa dấu xuống dòng \n
                
                # Kiểm tra ký tự đầu tiên (không phân biệt hoa thường)
                if chuoi_hien_tai and chuoi_hien_tai.lower().startswith(chu_cai_bat_dau.lower()):
                    count += 1
                    print(f" -> Tìm thấy: {chuoi_hien_tai}")

        print(f"==> Kết quả: Có {count} chuỗi bắt đầu bằng chữ '{chu_cai_bat_dau}'")

    except Exception as e:
        print(f"[!] Lỗi đọc file: {e}")

if __name__ == "__main__":
    tao_file_du_lieu()
    ky_tu = input("Nhập chữ cái bắt đầu cần đếm: ")
    dem_chuoi_theo_chu_cai(ky_tu)