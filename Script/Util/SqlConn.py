import pymysql
import re


class SC:

    def __init__(self):
        self.con = pymysql.Connect(
            host='10.1.1.16',
            port=3306,
            user='wangbo',
            passwd='qdw2019.',
            db="sme_bi",
            charset='utf8'
        )
        self.cur = self.con.cursor()

    def __del__(self):
        self.con.close()

    def execute(self,query,args=None):
        self.cur.execute(query,args)
        pass

    def executemany(self,query,args=None):
        self.cur.executemany(query,args)
        pass

    def commit(self):
        self.con.commit()
        pass

    def fetall(self):
        return self.cur.fetchall()

    def close(self):
        self.con.close()
        pass

    def upload_dir(self,tbl_name,list):
        tupp = []
        keys = list[0].keys()
        sql = "insert into " + tbl_name + " ("
        for k in keys:
            sql += "`" + k + "`,"
        sql = sql[:-1] + ") values ("
        for k in keys:
            sql += "%s,"
        sql = sql[:-1] + ")"
        print(sql)
        for i in list:
            tup = []
            for k in keys:
                if type(i[k]) != str:
                    tup.append(str(i[k]))
                else:
                    tup.append(i[k])
            tupp.append(tuple(tup))
        self.executemany(sql,tupp)
        self.commit()
        pass

    def upload_obj(self,tbl_name,list):
        obj = list[0]
        keys = obj.__dict__.keys()
        sql = "insert into " + tbl_name + " ("
        for k in keys:
            sql += "`" + k + "`,"
        sql = sql[:-1] + ") values ("
        for k in keys:
            sql += "%s,"
        sql = sql[:-1] + ")"
        tupList = []
        for l in list:
            di = l.__dict__
            tup = []
            for k in keys:
                tup.append(di[k])
            tupp = tuple(tup)
            tupList.append(tupp)
        self.executemany(sql, tupList)
        self.commit()
        print("已将对象列表插入到",tbl_name,"数据表中！")
        pass

    def trunc_table(self,tbl_name):
        self.execute("TRUNCATE TABLE "+tbl_name)
        self.commit()
        pass

    def query_dir(self,sql):
        col_names = re.findall(r'SELECT (.*) FROM',sql)[0]
        col_list = col_names.split(",")
        self.execute(sql)
        result = self.fetall()
        dircList = []
        for r in result:
            dirc = {}
            for i in range(0,len(r)):
                dirc[col_list[i].replace("`","")] = r[i]
            dircList.append(dirc)
        return dircList

    def update_dir(self,tbl_name,list,main_id):
        tupp = []
        first = list[0]
        keys = [i for i in first.keys()]
        keys.remove(main_id)
        sql = "UPDATE " + tbl_name + " SET "
        for k in keys:
            sql += "`" + k + "`=%s,"
        sql = sql[:-1] + " WHERE " + main_id + " = %s"
        for i in list:
            tup = []
            for k in keys:
                if type(i[k]) != str:
                    tup.append(str(i[k]))
                else:
                    tup.append(i[k])
            tup.append(i[main_id])
            tupp.append(tuple(tup))
        self.executemany(sql,tupp)
        self.commit()
        pass

