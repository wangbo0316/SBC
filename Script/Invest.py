from Basic import BasicOprts
from SqlConn import SC
from CsvReader import CR


class InvestOprts(BasicOprts):

    def UpCSV(self,file_name,v):
        v.p("正在开启投资表处理进程...")
        v.sleep(1)
        v.p("文件格式校验中...")
        v.sleep(1)
        dirc = ['product','Id','ctime','orderAmount','qdwId','interestRate','duration','durationUnit','repayStart','repayEnd','mobile','depId','userChannel','urlRefSource','isBidTrans']
        dirc_2 = ['product','Id','ctime','orderAmount','qdwId','interestRate','duration','durationUnit','repayStart','repayEnd','mobile','empId','depId','emp','dep','registerTime','userChannel','urlRefSource','isBidTrans']
        for i in CR(file_name).header:
            if i not in dirc_2:
                v.p("校验失败，存在未知字段：" + i, 2)
                return
        for i in dirc:
            if i not in CR(file_name).header:
                v.p("校验失败，未找到字段：" + i, 2)
                return
        v.p("数据校验成功,正在上传数据...")
        self.upload_csv(file_name, 'bi_invest')
        # self.SingnOnline()
        v.sleep(1)
        v.p("数据上传成功！", 3)
        return

    def online_UpCSV(self, file_name,v):
        v.p("正在开启在投表处理进程...")
        v.sleep(1)
        v.p("文件格式校验中...")
        v.sleep(1)
        dirc = ['product','Id','ctime','amount','qdwId','interestRate','duration','durationUnit','repayStart','repayEnd','mobile','depId','userChannel','urlRefSource','enterDate']
        for i in CR(file_name).header:
            if i not in dirc:
                v.p("校验失败，存在未知字段：" + i, 2)
                return
        for i in dirc:
            if i not in CR(file_name).header:
                v.p("校验失败，未找到字段：" + i, 2)
                return
        v.p("数据校验成功,正在上传数据...")
        # data = CR(file_name).get_obj()
        # for i in data:
        #     i["enterDate"] = "2019-3-13"
        # SC().upload_dir("bi_invest_online",data)
        self.upload_csv(file_name, 'bi_invest_online')
        # self.SingnOnline()
        v.sleep(1)
        v.p("数据上传成功！", 3)
        return

    def SingnOnline(self):
        M = SC()
        invest_data = M.query_dir("SELECT main_id,qdwId,ctime FROM bi_invest")
        online_data = M.query_dir("SELECT qdwId,ctime FROM bi_invest_online")
        online_ids = []
        offline_ids = []
        for i in invest_data:
            a = False
            for j in online_data:
                if i['qdwId'] == j['qdwId'] and i['ctime'] == j['ctime']:
                    a = True
            if a :
                online_ids.append(i["main_id"])
            else:
                offline_ids.append(i["main_id"])
        print(len(online_ids))
        print(len(offline_ids))
        print(len(invest_data))
        print(len(online_data))

    def first_UpCSV(self, file_name,v):
        v.p("正在开启在投表处理进程...")
        v.sleep(1)
        v.p("文件格式校验中...")
        v.sleep(1)
        dirc = ['product','Id','ctime','orderAmount','qdwId','interestRate','duration','repayStart','repayEnd']
        for i in CR(file_name).header:
            if i not in dirc:
                v.p("校验失败，存在未知字段：" + i, 2)
                return
        for i in dirc:
            if i not in CR(file_name).header:
                v.p("校验失败，未找到字段：" + i, 2)
                return
        v.p("数据校验成功,正在上传数据...")
        # data = CR(file_name).get_obj()
        # for i in data:
        #     i["enterDate"] = "2019-3-13"
        # SC().upload_dir("bi_invest_online",data)
        SC().trunc_table('bi_invest_first')
        self.upload_csv(file_name, 'bi_invest_first')
        # self.SingnOnline()
        v.sleep(1)
        v.p("数据上传成功！", 3)
        return

    def activity_UpCSV(self, file_name,v):
        v.p("正在开启在投表处理进程...")
        v.sleep(1)
        v.p("文件格式校验中...")
        v.sleep(1)
        dirc = ['id','productId','type','money','createTime','qdwId','mobile','term','rate','channel','yearAmount']
        for i in CR(file_name).header:
            if i not in dirc:
                v.p("校验失败，存在未知字段：" + i, 2)
                return
        for i in dirc:
            if i not in CR(file_name).header:
                v.p("校验失败，未找到字段：" + i, 2)
                return
        v.p("数据校验成功,正在上传数据...")
        SC().trunc_table('bi_invest_activity')
        self.upload_csv(file_name, 'bi_invest_activity')
        # self.SingnOnline()
        v.sleep(1)
        v.p("数据上传成功！", 3)
        return


