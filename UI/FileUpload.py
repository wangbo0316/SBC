# -*- coding: utf-8 -*-
'''
Created On 18-8-16 下午2:47
    @Author  : WangBo
    @File    : C_Mark.py
    @Software: PyCharm
    @Tag     :
'''
from PyQt5.QtWidgets import QWidget,QGridLayout,QLabel,QPushButton,QFileDialog,QButtonGroup,QRadioButton
from PyQt5.QtCore import  Qt,pyqtSignal,QThread
import threading
from setting import *
from router import *
from MainScript import runScript

class Job(QThread):
    signal=pyqtSignal(str,int)

    tbl_name = ""

    def p(self,var:str,num:int=1):
        self.signal.emit(var,num)

    def setFileName(self,var:str):
        self.filename = var

    def __init__(self, *args, **kwargs):
        super(Job, self).__init__(*args, **kwargs)
        self.__flag = threading.Event()     # 用于暂停线程的标识
        self.__flag.set()       # 设置为True
        self.__running = threading.Event()      # 用于停止线程的标识
        self.__running.set()      # 将running设置为True

    def run(self):
        self.p("文件路径读取成功，正在启动解析程序...")
        self.sleep(1)
        self.p("当前文件路径:" + self.filename)
        self.sleep(1)
        self.p("当前上传的表格类型为："+self.tbl_name)
        self.sleep(1)
        runScript(self)

        # upload.UploadRo(self.filename,self)

    def pause(self):
        self.__flag.clear()     # 设置为False, 让线程阻塞

    def resume(self):
        self.__flag.set()    # 设置为True, 让线程停止阻塞

    def stop(self):
        self.__flag.set()       # 将线程从暂停状态恢复, 如何已经暂停的话
        self.__running.clear()


class DrawMain(QWidget):
    fileName = ""
    def __init__(self,*args):
        super(DrawMain, self).__init__(*args)
        self.grid = QGridLayout(self)
        self.grid.addWidget(QLabel(),0,0,1,23)
        self.grid.addWidget(QLabel(), 0, 23, 24, 1)
        self.Excel_Loader()
        self.Logo_Print()

    def Excel_Loader(self):
        # ------------title----------------------------------
        self.csv_title = QLabel()
        self.csv_title.setObjectName("title_label")
        self.csv_title.setText('路径')
        self.grid.addWidget(self.csv_title, 2,1,1,22, Qt.AlignLeft | Qt.AlignVCenter)
        # ------------lable----------------------------------
        self.csv_lable = QLabel()
        self.csv_lable.setObjectName("normal_label")
        self.csv_lable.setText('请点击右侧按钮选择市场预算表......')
        self.grid.addWidget(self.csv_lable, 5,2,2,19, Qt.AlignLeft | Qt.AlignVCenter)
        # ------------load_btn----------------------------------
        self.csv_btn = QPushButton('...')
        self.csv_btn.setObjectName('load_btn_CSV')
        self.csv_btn.clicked.connect(self.msg)
        self.grid.addWidget(self.csv_btn, 5,21,2,2, Qt.AlignRight | Qt.AlignVCenter)
        # ------------title----------------------------------
        self.csv_title = QLabel()
        self.csv_title.setObjectName("title_label")
        self.csv_title.setText('表名')
        self.grid.addWidget(self.csv_title, 9, 1, 1, 22, Qt.AlignLeft | Qt.AlignVCenter)
        #-----------------rb---------------------------------
        self.bg1 = QButtonGroup()
        for index,item in enumerate(ROUTER.keys()):
            rb = QRadioButton(item)
            rb.setObjectName('rb_btn')
            if index < 4:
                self.grid.addWidget(rb, 11, 3+index*5, 2, 5, Qt.AlignLeft | Qt.AlignVCenter)
            elif index < 8:
                self.grid.addWidget(rb, 14, index*5-17, 2, 5, Qt.AlignLeft | Qt.AlignVCenter)
            else:
                self.grid.addWidget(rb, 17, index * 5 - 37, 2, 5, Qt.AlignLeft | Qt.AlignVCenter)
            self.bg1.addButton(rb, index)
         # -------------submit_btn-------------------------------
        self.sub_btn = QPushButton('点          击          上          传')
        self.sub_btn.setObjectName('submit_btn')
        self.sub_btn.clicked.connect(self.submit)
        self.grid.addWidget(self.sub_btn, 21, 2, 2, 18, Qt.AlignRight | Qt.AlignVCenter)

    def submit(self):
        if self.bg1.checkedButton():
            self.pL(self.bg1.checkedButton().text(),1)
            if self.fileName[-4:] == '.csv':
                str = self.fileName
                if len(str) > 40:
                    self.csv_lable.setText(str[0:40] + '......')
                else:
                    self.csv_lable.setText(str)
                self.csv_lable.setStyleSheet('#normal_label{color:gray}')
                self.threads = Job()
                self.threads.signal.connect(self.pL)
                self.threads.tbl_name = self.bg1.checkedButton().text()
                self.threads.setFileName(self.fileName)
                self.threads.start()
            else:
                self.csv_lable.setText('您选择的文件不是csv格式，请重新选择......')
                self.csv_lable.setStyleSheet('#normal_label{color:red}')
        else:
            self.pL("选择表名啊凶dei！",2)
            self.csv_lable.setText('选择表名啊凶dei！')
            self.csv_lable.setStyleSheet('#normal_label{color:red}')

    def msg(self):
        fileName, filetype = QFileDialog.getOpenFileName(self, "选取文件", DEFAULT_OPEN_PATH,
                                                          "All Files (*);;Text Files (*.txt)")
        self.fileName = fileName
        if fileName[-4:] == '.csv':
            str = fileName
            if len(str) > 40:
                self.csv_lable.setText(str[0:40] + '......')
            else:
                self.csv_lable.setText(str)
            self.csv_lable.setStyleSheet('#normal_label{color:gray}')
        else:
            self.csv_lable.setText('您选择的文件不是csv格式，请重新选择......')
            self.csv_lable.setStyleSheet('#normal_label{color:red}')

    def Logo_Print(self):
        # ------------title----------------------------------
        self.logo_label = QLabel()
        self.logo_label.setText('log......')
        self.logo_label.setObjectName("logo_label")
        self.grid.addWidget(self.logo_label, 23, 0, 1, 23, Qt.AlignLeft | Qt.AlignBottom)

    def pL(self,var,num=1):
        self.logo_label.setText(var)
        if num == 1:
            self.logo_label.setStyleSheet('#logo_label{color:gray}')
        elif num == 2 :
            self.csv_lable.setStyleSheet('#normal_label{color:red}')
            self.logo_label.setStyleSheet('#logo_label{color:red}')
        elif num == 3 :
            self.csv_lable.setStyleSheet('#normal_label{color:#69AAE0}')
            self.logo_label.setStyleSheet('#logo_label{color:#69AAE0}')



