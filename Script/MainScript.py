from Activity import ActivityOprts
from Invest import InvestOprts
from Prize import PrizeOprts
from User import UserOprts


def runScript(v):
    # 初始化对象及参数
    # filename = v.filename
    # tbl_name = v.tbl_name
    A = ActivityOprts()
    I = InvestOprts()
    P = PrizeOprts()
    U = UserOprts()
    if v.tbl_name == "翻牌_抽奖机会":
        A.draw_chance_UpCSV(v.filename,v)
    if v.tbl_name == "翻牌_实抽":
        A.draw_UpCSV(v.filename,v)
    if v.tbl_name == "福利表":
        P.UpCSV(v.filename,v)
    if v.tbl_name == "拼团_团表":
        A.tuan_UpCSV(v.filename,v)
    if v.tbl_name == "拼团_团及用户":
        A.tuan_user_UpCSV(v.filename,v)
    if v.tbl_name == "投资表":
        I.UpCSV(v.filename,v)
    if v.tbl_name == "用户表":
        U.UpCSV(v.filename,v)
    if v.tbl_name == "在投表":
        I.online_UpCSV(v.filename,v)
    if v.tbl_name == "首投表":
        I.first_UpCSV(v.filename,v)
    if v.tbl_name == '活动投资表':
        I.activity_UpCSV(v.filename,v)
    if v.tbl_name == '开通存管' :
        U.update(v.filename,v)
