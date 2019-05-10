import csv

DATE_MAP = [
    'ctime','repayStart','repayEnd','registerTime','create_time',
    'StartTime','EndTime','CreateTime','ExpireTime','use_date','FullTime','createTime'
]

class CR:
    def __init__(self,file_path):
        self.file = [i for i in csv.reader(open(file_path,'r', encoding='UTF-8'))]
        self.header = self.file[0]
        self.content = self.file[1:]
        self.col_size = len(self.header)
        pass

    def get_row(self,row_index):
        return self.content[row_index]

    def get_col(self,col_index):
        return [i[col_index] for i in self.content]

    def get_area(self,left_up_coordinate,right_down_coordinate):
        results = []
        for i in range(left_up_coordinate[0],right_down_coordinate[0]+1):
            results.append(self.get_row(i)[left_up_coordinate[1]:right_down_coordinate[1]+1])
        return results

    def get_obj(self):
        results = []
        for i in self.content:
            vo = {}
            for index,item in enumerate(i):
                if self.header[index] in DATE_MAP:
                    vo[self.header[index]] = item.split(".")[0]
                else:
                    vo[self.header[index]] = item
            results.append(vo)
        return results

