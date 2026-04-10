import os

FILE_NAME = "tong_chan_le.txt"

def tao_file_du_lieu():
    num = [1,2,3,4,5,6,7,8,9]

    try:
        with open(FILE_NAME, "w") as f:
            for so in num:
                f.write(f"{so}\n")
        
        print(f"Đã tạo file {FILE_NAME}")
    except Exception as e:
        print(f"Lỗi khi tạo file: {e}")


def tong_chan_le():

    if not os.path.exists(FILE_NAME):
        print("File không tồn tại !")
        return
    
    tong_chan = 0
    tong_le = 0

    try:

        with open(FILE_NAME, 'r', encoding='utf-8') as f:
            num = f.read().replace('\n','')

            for i in num:
                i = int(i)
                if i % 2 == 0:
                    tong_chan += i
                else:
                    tong_le += i
           
            print(f"Tổng chẵn: {tong_chan} , Tổng lẻ: {tong_le}")

    except Exception as e:
        print(f"Lỗi khi đọc file: {e}")

if __name__ == "__main__":
    tao_file_du_lieu()
    tong_chan_le()

