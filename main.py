import click 
import time
while 1:
    #Menu 
    dict_vocabulary = {}
    print("{:^20}".format("Menu"))
    print("1. Thêm 1 từ")
    print("2. Xoá 1 từ")
    print("3. Tìm 1 từ")
    print("4. In tất cả từ")
    print("5. Thoát")

    #Input choose
    choose = None 
    while 1:
        try:
            choose = int(input("Nhập lựa chọn của bạn 1->5: "))
        except:
            print("Vui lòng chỉ nhập các số!")
        if choose not in [1,2,3,4,5]:
            print("Vui lòng nhập số trong phạm vi 1->5!")
        else:
            break


    if choose == 1:
    #Add 1 vocabulary
        vocabulary = input("Nhập từ: ")
        vocabulary.lower()
        mean = input("Nhập nghĩa của từ: ")
        mean.lower()
        with open('vocabulary.txt','r') as file:
            data = file.readlines()

        for item in data:
            key,value = item.split("-")
            value = value[:-1]
            dict_vocabulary[key] = value
        keys = dict_vocabulary.keys()
        if vocabulary in keys:
            str_temp = dict_vocabulary.get(vocabulary) + ", "+ mean 
            dict_vocabulary.update({vocabulary:str_temp})
            with open('vocabulary.txt','w') as file:
                for key,value in dict_vocabulary.items():
                    file.write(key.lower()+"-"+value.lower()+"\n")
        else:
             with open('vocabulary.txt','a') as file:
                file.write(vocabulary.strip()+"-"+mean.strip()+"\n")
        print("Đã thêm!")

    elif choose == 2:
    #Delete 1 vocabulary
        with open('vocabulary.txt','r') as file:
            data = file.readlines()
        for item in data:
            key,value = item.split("-")
            value = value[:-1]
            dict_vocabulary[key] = value
        vocabulary_delete = input("Nhập từ cần xoá: ")
        if vocabulary_delete in dict_vocabulary.keys():
            del dict_vocabulary[vocabulary_delete]
            with open('vocabulary.txt','w') as file:
                for key,value in dict_vocabulary.items():
                    file.write(key.lower()+"-"+value.lower()+"\n")
                print("Đã xoá")
        else:
            print("Không có từ này")

    elif choose == 3:
    #Find 1 vocabulary
        vocabulary_find = input("Nhập từ cần tìm: ")
        with open('vocabulary.txt','r') as file:
            data = file.readlines()
        for item in data:
            key,value = item.split("-")
            value = value[:-1]
            dict_vocabulary[key] = value
        print(f'{vocabulary_find}: {dict_vocabulary.get(vocabulary_find)}' if dict_vocabulary.get(vocabulary_find) is not None else f'Không tìm thấy từ {vocabulary_find}')
   
    elif choose == 4:

        with open('vocabulary.txt','r') as file:
            data = file.readlines()
        for item in data:
            key,value = item.split("-")
            value = value[:-1]
            print(f"{key}: {value}")
    else:
        print("Đang thoát...")
        break;
    time.sleep(3)
    click.clear()