import os 


FILE_NAME = "s7.txt"

def tao_file_du_lieu(s7:list):

    try:
        with open(FILE_NAME, 'w') as f:
            for phan_tu in s7:
                f.write(f"{phan_tu}\n")
        
        print("Tạo file thành công......")
    except Exception as e:
        print(f"Lỗi: {e}")

def tim_max_min():

    if not os.path.exists(FILE_NAME):
        print("File không tồn tại...")
   
    try:
        with open(FILE_NAME,'r',encoding='utf-8') as f:
            data = f.readlines()

        list_data = []
        for i in data:
            list_data.append(i)
        
        list_data.sort()
        max = list_data[len(list_data) - 1]
        min = list_data[0]
        count_min = list_data.count(min)
        count_max = list_data.count(max)

        while min in list_data:
            list_data.remove(min)
        
        print(list_data)
        min_two = list_data[0]

        count_min_two = list_data.count(min_two)
        

        
        print(f"Gía trị min: {min} | Với số lần xuất hiện: {count_min}")
        print(f"Gía trị nhỏ thứ 2 là: {min_two} | Với số lần xuất hiện: {count_min_two}")
        print(f"Gía trị max: {max} | Với số lần xuát hiện: {count_max}") 
    except Exception as e:
        print(f"Lỗi : {e}")

if __name__ == "__main__":
    
    s7 = input("Nhập giá trị cách nhau bởi dấu cách: ")
    s7 = s7.split()

    tao_file_du_lieu(s7)
    tim_max_min()

