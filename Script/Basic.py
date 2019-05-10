from CsvReader import CR
from SqlConn import SC
from XlsReader import XR

class BasicOprts(object):

    def csv_as_reader(self,file_path):
        C = CR(file_path)
        return C

    def csv_as_dir(self,file_path):
        C = CR(file_path)
        return C.get_obj()

    def csv_as_list(self,file_path):
        C = CR(file_path)
        return C.file

    def xls_as_reader(self,file_path,sheet):
        X = XR(file_path,sheet)
        return X

    def xls_as_dir(self,file_path,sheet):
        X = XR(file_path,sheet)
        return X.get_obj()

    def xls_as_list(self,file_path,sheet):
        X = XR(file_path,sheet)
        return [X.get_row(i) for i in range(0,len(X.get_col(0)))]

    def upload_xls(self,file_path,sheet,tbl_name):
        list = self.xls_as_dir(file_path,sheet)
        SC().upload_dir(tbl_name, list)

    def upload_csv(self,file_path,tbl_name):
        list = self.csv_as_dir(file_path)
        SC().upload_dir(tbl_name,list)
