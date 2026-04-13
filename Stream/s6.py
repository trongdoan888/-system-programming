import os 
FILE_NAME = "bai6.txt"
# A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z.
def tao_file_du_lieu(bai_6: list):

    list_char = ( n.upper() for n in bai_6)
     
    try:
        with open(FILE_NAME, 'w') as f:
            for ki_tu in list_char:
                f.write(f"{ki_tu}\n")
            
            print(f"Đã tạo file {FILE_NAME} thành công.")
    except Exception as e:
        print(f"Lỗi: {e}")

def sap_xep_ki_tu():

    alphabet_dict = {
    'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5,
    'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10,
    'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15,
    'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20,
    'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25,
    'Z': 26 }

    reverse_dict = {value: key for key, value in alphabet_dict.items()}
    
    if not os.path.exists(FILE_NAME):
        print("File không tồn tại!")
        return

    list_result = []

    try:
        with open(FILE_NAME, 'r', encoding ='utf-8') as f:
            list_ban_dau = f.read().replace("\n","")


        for ki_tu in list_ban_dau:
            if ki_tu in alphabet_dict:
                vi_tri = alphabet_dict[ki_tu] 
                list_result.append(vi_tri)
        
        list_result.sort()

        for n,vi_tri in enumerate(list_result):
            
            ki_tu = reverse_dict[vi_tri]
            list_result[n] = ki_tu
        
        with open(FILE_NAME, 'w', encoding = 'utf-8') as f:
            for phan_tu in list_result:
                f.write(f"{phan_tu}\n")
        
        print(f"Chỉnh sửa thành công.....")
    except Exception as e:
        print(f"Lỗi: {e}")

if __name__ == "__main__":
    
    bai_6 = input("Nhập chuỗi kí tự, cách nhau bởi dấu cách: ")

    bai_6 = bai_6.split()
            
    tao_file_du_lieu( bai_6)
    sap_xep_ki_tu()
