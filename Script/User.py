from Basic import BasicOprts
from SqlConn import SC
from CsvReader import CR
class UserOprts(BasicOprts):

    def UpCSV(self, file_name,v):
        v.p("正在开启用户表处理进程...")
        v.sleep(1)
        v.p("文件格式校验中...")
        v.sleep(1)
        dirc = ['UrlRefSource','id','pid','create_time','UserIdentify','group_id','mobile','EmployeeId','DId','IsOpenXwAcct','Channel']
        for i in CR(file_name).header:
            if i not in dirc:
                v.p("校验失败，存在未知字段：" + i, 2)
                return
        for i in dirc:
            if i not in CR(file_name).header:
                v.p("校验失败，未找到字段：" + i, 2)
                return
        v.p("数据校验成功,正在上传数据...")
        self.upload_csv(file_name, 'bi_user')
        self.SignChannel()
        # self.SingnOnline()
        v.sleep(1)
        v.p("数据上传成功！", 3)

    def update(self,file_name,v):
        v.p("hello，这里是用户更新的操作框")
        print(file_name)
        dirc = ['id','IsOpenXwAcct', 'Channel', 'UrlRefSource', 'create_time', 'UserIdentify', 'group_id', 'EmployeeId', 'DId',
                'UDF:idAge(idno)', 'UDF:idGender(idno)']
        for i in CR(file_name).header:
            if i not in dirc:
                v.p("校验失败，存在未知字段：" + i, 2)
                return
        for i in dirc:
            if i not in CR(file_name).header:
                v.p("校验失败，未找到字段：" + i, 2)
                return
        v.p("校验成功,正在更新用户表...")
        obj = CR(file_name).get_obj()
        for i in obj:
            i["age"] = i["UDF:idAge(idno)"]
            i['gender'] = i['UDF:idGender(idno)']
            del i["UDF:idAge(idno)"]
            del i["UDF:idGender(idno)"]
        try:
            SC().update_dir("bi_user",obj,"UserIdentify")
            v.p("数据上传成功！",3)
            return
        except:
            v.p("数据上传失败！",2)
            return

    def SignChannel(self):
        # 连接数据库获取数据
        MYSQL = SC()

        ivst_data = MYSQL.query_dir(
            'SELECT  main_id,Channel,UrlRefSource FROM  bi_user WHERE  ISNULL(last_channel)')

        # 初始化渠道字典
        url_dir = {
            "so": "好搜(pc)",
            "m.so": "好搜(pe)",
            "sogou": "搜狗(pc)",
            "m.sogou": "搜狗(pe)",
            "mshenma": "神马",
            "baidu": "百度(pc)",
            "mbaidu": "百度(pe)",
            "m3.qiandw": "自然来源"
        }
        channel_dir = {
            'wxgz': "微信关注",
            'hsxxl': "好搜信息流",
            'weixindl': "微信登录",
            'weixin': '微信',
            'AppStore': 'IOS',
            'baidu': '百度',
            'android': '安卓',
            'android_huawei': '安卓(华为)',
            'android_Oppo': '安卓(oppo)',
            'android_Q360': '安卓(360)',
            'android_QianDW': '安卓(官方)',
            'android_Tencent': '安卓(腾讯)',
            'android_vivo': '安卓(vivo)',
            'android_xiaomi': '安卓(小米)',
            'android_zhaoyang': '安卓(玿阳)',
            'Gofun': 'Gofun', 'gzt': '贵州通',
            'huochepiao': '火车票',
            'qutoutiao': '趣头条',
            'shaizhaopian': '晒照片',
            'shoutouwang': '首投网',
            'mianbaodian': '面包店',
            'mojifen': '魔积分',
            'weilexin': '唯乐信',
            'zhaoyang': '昭阳',
            'touhuiying': '投汇盈',
            'sogou': '搜狗(pc)',
            'msogou': '搜狗(pe)',
            'haosou': '好搜(pc)',
            'mhaosou': '好搜(pe)',
            'mshenma': '神马搜索'
        }

        # 开始遍历
        for i in ivst_data:
            # 生成标识字段
            i["last_channel"] = ""
            # 根据userChannel字段开始识别
            if i["Channel"]:
                for j in channel_dir.keys():
                    if j in i["Channel"]:
                        i["last_channel"] = channel_dir[j]
            # 根据urlRefSource字段开始识别
            if i["UrlRefSource"] and not i["last_channel"]:
                for k in url_dir.keys():
                    if k in i["UrlRefSource"]:
                        i["last_channel"] = url_dir[k]
            if (i["Channel"] or i["UrlRefSource"]) and not i["last_channel"]:
                i["last_channel"] = "未知渠道"
            # 识别失败处理
            if not i["last_channel"]:
                i["last_channel"] = "自然来源"
            # ----------------渠道识别结束,开始修正日期格式---------------------------

            # i["ctime"] = i["ctime"].split(".")[0]
            # i["registerTime"] = i["registerTime"].split(".")[0]
            # i["repayStart"] = i["repayStart"].split(".")[0]
            # i["repayEnd"] = i["repayEnd"].split(".")[0]

            # ----------------------数据预处理结束----------------------------
        # ---------------更新数据库-----------------------
        MYSQL.update_dir("bi_user", ivst_data, " main_id")






