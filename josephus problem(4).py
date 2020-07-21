import zipfile    # 第三方

import participants    # 项目内其他文件

class Reader(object):    # 创建一个Reader类，包含.txt、.csv和.zip格式文件的读取，并返回所有人员的数据 
    def read_txt(self, path = "cast.txt"):    # 读取txt文件的数据，并返回一个列表
        with open(path, "r", encoding = "UTF-8-sig") as f_txt    # 读取人员
            cast_lst_txt = list(f_txt)    # 名单由txt转为列表
        cast_list_txt = []    # 创建一个新列表，用于整理数据
        for i in range(len(cast_lst_txt)):
            cast_lst_txt[i] = cast_lst_txt[i].strip("\n")
            cast_list_txt.append(cast_lst_txt[i].split(" "))
            return cast_list_txt

    def read_csv(self, path_c = "cast.csv":    # 读取csv文件的数据，返回一个列表
        self.path_csv = path_c
        import csv
        
        cast_lst_csv = []
        csv_temp = open(self.path_csv, "r", encoding = "UTF-8-sig"
        f_csv = csv.reader(csv_temp)    # csv自带reader函数 用于读取数据 
        for i in f_csv:
            cast_lst_csv.append(i)    # 将csv文件内的数据重新存入一个列表
        csv_temp.close()
        return cast_lst_csv

    def read_zip(self, path_z = "cast.zip/cast_zip.txt"):    # 该zip文件包含一个txt文件
        self.path_zip = path_z
        import zipfile
        
        zf = zipfile.ZipFile(self.path_zip, "r")
        get_path_zip_txt = zf.extract("cast_zip.txt")    # 解压zip文件 获取zip文件里txt文件的地址
        self.read_txt(get_path_zip_txt)    # 调用本类的其他方法

def create_participants(file_str, participants):    # 输入参数可以设计为文件名
    with open(file_str) as file_:
    participants = []
    for line in file_:
        line = list(line.strip().split(' '))    # strip:移除字符串头尾的空格
        participants.append(line)
    return (participants) 

def get_survival(start_num, participants, interval):    
    total_num = len(participants)
    for i in range(total_num - 1):
        start_num = (start_num + interval) % len(participants)    
        start_num -= 1
        print('out_participant:' , participants[start_num])
        del participants[start_num]    #删除淘汰人员
        if start_num == -1:
            start_num = 0
    return (participants[0])

class Participant():
    def __init__(self, name, height):
        self.name = name
        self.height = height
        self._weight = 0.6 * height

    def get_name(self):
        return self.name

    def get_height(self):
        return self.height 

    @property
    def weight(self):
        return 0.6 * self.height

Betty = Participant(“Betty”, 168)
print(Betty.height)
Betty.height = 170
print(Betty.height)
print(Betty.weight)

if __name__ == '__main__':    # 文件作为脚本直接执行
    test = Reader()
    func = test.read_txt
    func(path_t = "cast.txt")
    func = test.read_csv
    func(path_c = "cast.csv")
    print(func)
    participants = get_participants()
    start_num = int(input('the start number is:'))
    interval = int(input('the interval is:'))
    survival = get_survival(start_num, participants, interval)
    name, weight, height = survival[0], survival[1], survival [2]
    survival = Participant(name)
    survival.get_name()
    survival.get_weight(weight)
    survival.get_height(height)
     
test_participants = get_participants(1)
ret = out_participant(test_participants, 4)
assert(ret == [1])

test_participants = get_participants(3)
ret = out_participant(test_participants, 2)
assert(ret == [2, 1, 3])

test_participants = get_participants(3)
ret = out_participant(test_participants, -1)
assert(ret == [])    

