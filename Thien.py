# Hãy viết một chương trình cho phép đọc nội dung của file employees.txt nào đó và
# copy dữ liệu này thả vào file excel dưới dạng hàng và cột(Ma Nhan Vien, Ten Nhan Vien, Email, So Dien Thoai).
# File text sẽ bao gồm dữ liệu như file đính kèm, mỗi nhóm dữ liệu nên được cắt ra và chèn vào 1 dòng mới bên file excel.
# Trong trường hợp không thể tìm thấy file, hãy thông báo tên file mà không tìm thấy được.


from openpyxl import load_workbook
new_list1=[]
t = 0
j = 0
w = 0
try:
    employee = []
    workbook = load_workbook(filename="employees.xlsx")
    sheet = workbook["Sheet1"]
    f = open("employees.txt", 'r')
    data = f.read()

    # Xu ly chuoi
    list_data = data.split('---')

    for i in range(0, len(list_data)):
        if list_data[i] != "":
            new_list1.append(list_data[i].split("\n"))


    for k in range(0, len(new_list1)):
        while j < len(new_list1[k]):
            if new_list1[k][j] == '':
                new_list1[k].pop(j)
                j -= 1
            j += 1
        j = 0

    while t < len(new_list1):
        if new_list1[t] == []:
            new_list1.pop(t)
            t -= 1
        t += 1

    for l in range(0, len(new_list1)):
        for z in range(0, len(new_list1[l])):
            new_list1[l][z] = new_list1[l][z].split(':')

    # Chep chuoi vao excel file
        # Chep vao tung cot: MA_NHAN_VIEN, TEN_NHAN_VIEN, EMAIL, SO_DIEN_THOAI
    char = 'A'
    char_to_int = ord(char[0]) #Return unicode code of the char

    for r in range(0, len(new_list1[0])):
        sheet[chr(char_to_int+r)+"1"] = new_list1[0][r][0]

    # Chep thong tin Nhan Vien vao tung hang tuong ung voi cot
    for q in range(0, len(new_list1)):
        for a in range(0, len(new_list1[q])):
            while w < len(new_list1):
                sheet["A"+str(w+2)] = new_list1[w][0][1]
                sheet["B"+str(w+2)] = new_list1[w][1][1]
                sheet["C"+str(w+2)] = new_list1[w][2][1]
                sheet["D"+str(w+2)] = new_list1[w][3][1]
                w += 1

    workbook.save(filename="employees.xlsx")
except FileNotFoundError as exc_info:
    raise
finally:
    print("All Done!")
