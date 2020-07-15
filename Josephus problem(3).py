def get_participants():
    fp = open('information1.txt')    # fp = file points
    # participants_str = information1.readlines()
    fp.close()
    participants = []
    for line in participants_str:
        line = list(line.st  rip().split('  '))    # strip移除字符串头尾的空格
        participants.append(line)
    return (participants)    # 输入是文件information1的路径 输出是得到的数组

def get_survival(start_num, participants, interval):    
    total_num = len(participants)
    for i in range(total_num - 1):
        start_num = (start_num + interval) % len(participants)    
        start_num -= 1
        print('out_participant:' , participants[start_num])
        del participants[start_num]    #删除淘汰人员
        if start_num == -1:
            start_num = 0
    return (participants[0])

class Participant(object):
    def __init__(self, name, height):
        self.name = name
        self.height = height
        self._weight = 0.6 * height

def set_name(self, name):
self.__name = name

@property
    def weight(self):
        return 0.6 * self.height

Betty = Participant(“Betty”, 168)
print(Betty.height)
Betty.height = 170
print(Betty.height)
print(Betty.weight)

if __name__ == '__main__':    # 文件作为脚本直接执行
    participants = get_participants()
    start_num = int(input('the start number is:'))
    interval = int(input('the interval is:'))
    survival = get_survival(start_num, participants, interval)
    name, weight, height = survival[0], survival[1], survival [2]
    survival = Participant(name)
    survival.get_name()
    survival.get_weight(weight)
    survival.get_height(height)
     
test_list = get_list(1)
ret = get_survival(test_list, 4)
assert(ret == [1])

test_list = get_list(3)
ret = get_survival(test_list, 2)
assert(ret == [2, 1, 3])

test_list = get_list(3)
ret = get_survival(test_list, -1)
assert(ret == [])    
