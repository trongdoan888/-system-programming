import os

FILE_NAME = "xoa_phan_tu.txt"

def tao_file_du_lieu():
    trung_lap = [1,2,3,4,1,2,4,5]

    try:

        with open(FILE_NAME,"w") as f:
            for phan_tu in trung_lap:
                f.write(f"{phan_tu}\n")

        print (f"Đã tạo file {FILE_NAME} với dữ liêu.")
    except Exception as e:
        print (f"Lỗi tạo file: {e}")

    
def xoa_phan_tu_trung_lap():
    if not os.path.exists(FILE_NAME):
        print("File không tồn tại !")
        return 
    
    list_new = []
    try:
        with open(FILE_NAME, "r", encoding='utf-8') as f:
            list_phan_tu = f.read().replace('\n','')

        for phan_tu in list_phan_tu:
            if phan_tu not in list_new:
                list_new.append(phan_tu)

        with open(FILE_NAME, 'w', encoding='utf-8') as f:
            for i in list_new:
                f.write(f"{i}\n")
    except Exception as e:
        print(f"Lỗi khi đọc file: {e}")
    
if __name__ == "__main__":
    tao_file_du_lieu()
    xoa_phan_tu_trung_lap()


            

            

                
            

