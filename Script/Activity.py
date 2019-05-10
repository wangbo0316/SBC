from Basic import BasicOprts
from CsvReader import CR
from SqlConn import SC
class ActivityOprts(BasicOprts):

    def tuan_UpCSV(self, file_name,v):
        v.p("正在开启团表处理进程...")
        v.sleep(1)
        v.p("文件格式校验中...")
        v.sleep(1)
        dirc = ['ID','RuleID','Name','UserCount','NewUserCount','QdwId','CreateTime','FullTime','EndTime','Status','ShortTime']
        for i in CR(file_name).header:
            if i not in dirc:
                v.p("校验失败，存在未知字段："+i,2)
                return
        for i in dirc:
            if i not in CR(file_name).header:
                v.p("校验失败，未找到字段：" + i, 2)
                return
        v.p("数据校验成功,正在上传数据...")
        SC().trunc_table("bi_tuan")
        self.upload_csv(file_name, 'bi_tuan')
        v.sleep(1)
        v.p("数据上传成功！",3)
        return

    def tuan_user_UpCSV(self, file_name,v):
        v.p("正在开启团及用户表处理进程...")
        v.sleep(1)
        v.p("文件格式校验中...")
        v.sleep(1)
        dirc = ['ID','TuanID','QdwId','Type','CreateTime']
        for i in CR(file_name).header:
            if i not in dirc:
                v.p("校验失败，存在未知字段：" + i, 2)
                return
        for i in dirc:
            if i not in CR(file_name).header:
                v.p("校验失败，未找到字段：" + i, 2)
                return
        v.p("数据校验成功,正在上传数据...")
        SC().trunc_table("bi_tuan_user")
        self.upload_csv(file_name, 'bi_tuan_user')
        v.sleep(1)
        v.p("数据上传成功！", 3)
        return

    def draw_UpCSV(self, file_name,v):
        v.p("正在开启实抽表处理进程...")
        v.sleep(1)
        v.p("文件格式校验中...")
        v.sleep(1)
        dirc = ['ID','CDKey','QdwId','Money','Vacct','PrizeType','Status','LimitNum','StartTime','EndTime','CreateTime','ActivityId']
        for i in CR(file_name).header:
            if i not in dirc:
                v.p("校验失败，存在未知字段：" + i, 2)
                return
        for i in dirc:
            if i not in CR(file_name).header:
                v.p("校验失败，未找到字段：" + i, 2)
                return
        v.p("数据校验成功,正在上传数据...")
        SC().trunc_table("bi_draw")
        self.upload_csv(file_name, 'bi_draw')
        v.sleep(1)
        v.p("数据上传成功！", 3)
        return

    def draw_chance_UpCSV(self, file_name,v):
        v.p("正在开启抽奖机会表处理进程...")
        v.sleep(1)
        v.p("文件格式校验中...")
        v.sleep(1)
        dirc = ['ID','QdwID','AddDrawCount','Remark','Source','Type','CreateTime','ExpireTime','ActivityId']
        for i in CR(file_name).header:
            if i not in dirc:
                v.p("校验失败，存在未知字段：" + i, 2)
                return
        for i in dirc:
            if i not in CR(file_name).header:
                v.p("校验失败，未找到字段：" + i, 2)
                return
        v.p("数据校验成功,正在上传数据...")
        SC().trunc_table("bi_draw_chance")
        self.upload_csv(file_name, 'bi_draw_chance')
        v.sleep(1)
        v.p("数据上传成功！", 3)
        return





