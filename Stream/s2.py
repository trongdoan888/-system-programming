import  os 

FILE_NAME = "chu_cai.txt"

def tao_file_du_lieu():
    chu_cai = ["a","b","c","d"]

    try:

        with open(FILE_NAME, "w") as f:
            for chu in chu_cai:
                f.write(f"{chu}\n")
        
        print(f"đã tạo file {FILE_NAME} với dữ liệu.")
    except Exception as e:
        print(f"Lỗi khi tạo file: {e}")



def chuyen_chu_thuong_sang_hoa():
    if not os.path.exists(FILE_NAME):
        print("File không tồn tại !")
        return

    try: 
        with open(FILE_NAME, "r+", encoding= 'utf-8') as f:
            noidung = f.read()

            noidung = noidung.upper()

            print(noidung)

            f.seek(0)

            f.write(noidung)

            f.truncate()
            

    except Exception as e:
        print(f"Lỗi khi đọc file: {e}")

def chuyen_chu_hoa_sang_thuong():
    if not os.path.exists(FILE_NAME):
        print("File không tồn tại !")
        return

    try: 
        with open(FILE_NAME, 'r+', encoding= 'utf-8') as f:
            noidung = f.read()

            noidung = noidung.lower()

            print(noidung)

            f.seek(0)

            f.write(noidung)

            f.truncate()
    except Exception as e:
        print(f"Lỗi khi đọc file: {e}")

if __name__ == "__main__":
    tao_file_du_lieu()
    chuyen_chu_thuong_sang_hoa()
    chuyen_chu_hoa_sang_thuong()
