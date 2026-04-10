import os

FILE_NAME = "so_nguyen.txt"

def tao_file_du_lieu():
    
    so_nguyen = [1, 2, 3, 4, 5]
    try:
        
        with open(FILE_NAME, 'w') as f:
            for so in so_nguyen:
                f.write(f"{so}\n")
        print(f"Đã tạo file {FILE_NAME} với dữ liệu.")
    except Exception as e:
        print(f"Lỗi khi tạo file: {e}")
    


def tinh_trung_binh_cong():
    if not os.path.exists(FILE_NAME):
        print("File không tồn tại !")
        return
    
    tong = 0
    so_luong = 0

    try:

        with open(FILE_NAME, 'r', encoding='utf-8') as f:
            for line in f:

                so = int(line.strip())
                tong += so
                so_luong += 1

        if so_luong > 0:
            trung_binh = tong / so_luong 

            print(f"Trung bình cộng của các số nguyên là: {trung_binh}")

        else:
            print("Không có số nguyên nào trong file.")
    except Exception as e:
        print(f"Lỗi khi đọc file: {e}")

if  __name__ == "__main__":
    tao_file_du_lieu()
    tinh_trung_binh_cong()
    