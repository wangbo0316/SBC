from Basic import BasicOprts
from SqlConn import SC
from CsvReader import CR
class PrizeOprts(BasicOprts):

    def UpCSV(self, file_name,v):
        v.p("正在开启福利表处理进程...")
        v.sleep(1)
        v.p("文件格式校验中...")
        v.sleep(1)
        dirc = ['id','qdw_id','prize_status','prize_type','prize_value','min_term','min_amount','create_date','effective_date','expired_date','target_id','use_date','source_id','source_type','prize_source','target_order_id','target_type','freeze','available_types','prize_use_logs','max_amount' ]
        for i in CR(file_name).header:
            if i not in dirc:
                v.p("校验失败，存在未知字段：" + i, 2)
                return
        for i in dirc:
            if i not in CR(file_name).header:
                v.p("校验失败，未找到字段：" + i, 2)
                return
        v.p("数据校验成功,正在上传数据...")

        self.upload_csv(file_name, 'bi_prize')
        # self.SingnOnline()
        v.sleep(1)
        v.p("数据上传成功！", 3)
        return





