import time
from unicodedata import decimal
import pylightxl as xl
import canmatrix
from General import *
import os
import canmatrix.formats.dbc as db_module
import sys
from PySide6 import QtCore, QtGui, QtWidgets

from ui_DbcGenBaseWindow import *
import pylightxl as xl
import openpyxl as openxl
import canmatrix
from General import *

class DbcGenMainWin(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super(DbcGenMainWin, self).__init__()

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("DbcGen")
        self.setWindowIcon(QIcon('dbc.ico'))
        self.setObjectName("MainWindow")
        self.setStyleSheet("#MainWindow{background-color:grey}")
        self.cwd = os.getcwd()


        # set slot
        self.ui.matrix_choose.clicked.connect(self.choose_matrix)
        self.ui.matrix_demo_choose.clicked.connect(self.choose_matrix_demo)
        self.ui.dbc_demo_choose.clicked.connect(self.choose_dbc_demo)
        self.ui.start_generate.clicked.connect(self.start_dbc_generate)
        self.ui.comboBox_comSheet.currentIndexChanged.connect(self.comSheetComboxChange)
        self.ui.cur_node_combox.currentIndexChanged.connect(self.choose_cur_node)

        # some attr
        self.matrix_file = None


    def choose_matrix(self):
        self.matrix_path, file_type = QtWidgets.QFileDialog.getOpenFileName(self,
                                                                            "Please your matrix file:",
                                                                            os.getcwd(),
                                                                            "*.xlsx *.xlsm"
                                                                            )
        if self.matrix_path is not None:
            self.ui.matrix_path.setText(str(self.matrix_path))

        self.base_path = os.path.dirname(self.matrix_path)
        self.db_name = os.path.splitext(os.path.basename(self.matrix_path))[0]
        self.ws = xl.readxl(fn=self.matrix_path)
        self.sheet_list = openxl.load_workbook(self.matrix_path).sheetnames
        for s in self.sheet_list :
            self.ui.comboBox_comSheet.addItem(s)

    def choose_matrix_demo(self):
        pass

    def choose_dbc_demo(self):
        demo_db_path, file_type = QtWidgets.QFileDialog.getOpenFileName(self,
                                                                            "Please your dbc file:",
                                                                            os.getcwd(),
                                                                            "*.dbc")
        if demo_db_path is not None:
            self.ui.dbc_demo_path.setText(str(demo_db_path))

        self.demo_dbc = canmatrix.formats.loadp(demo_db_path).get("")

    def choose_com_sheet(self):
        # self.com_sheet =
        pass

    def choose_cur_node(self):#TODO
        self.cur_node = self.ui.cur_node_combox.currentData(role=0)
        pass
    def comSheetComboxChange(self):#TODO
        sheet_name = self.sheet_list[self.ui.comboBox_comSheet.currentIndex()]
        self.com_sheet = self.ws.ws(ws=sheet_name)

        self.ecu_list = []
        #
        # if self.com_sheet

        for row in range(xlMtrixColData['dataStartRow'],self.com_sheet.maxrow):
            node = str.strip(self.com_sheet.index(row,xlMtrixColData['sendNode']))
            if node not in self.ecu_list:
                self.ecu_list.append(node)
            node = str.strip(self.com_sheet.index(row,xlMtrixColData['recvNode']))
            if node not in self.ecu_list:
                self.ecu_list.append(node)

        for e in self.ecu_list:
            self.ui.cur_node_combox.addItem(e)

    def start_dbc_generate(self):

        dbc = canmatrix.CanMatrix()

        dbc.add_ecu(canmatrix.Ecu('FC'))
        GeneralAttributeAdd(dbc, self.demo_dbc)

        ecu_list = []
        # add frame
        frame = CreatCanFrame(dbc=dbc, comSheet=self.com_sheet, is_fd=True, data_row=xlMtrixColData['dataStartRow'],
                              data_cfg=xlMtrixColData)

        for row in range(2, self.com_sheet.maxrow):

            try:
                id_str = str(self.com_sheet.index(row=row, col=xlMtrixColData['id']))
                id = int(id_str, 16)
            except:
                print("row", row, "Message Id error !")
                while True:
                    pass

            if id != frame.arbitration_id.id:
                # frame has been processed
                dbc.add_frame(frame)
                # new frame , is_fd TODO
                frame = CreatCanFrame(dbc=dbc, comSheet=self.com_sheet, is_fd=True, data_row=row, data_cfg=xlMtrixColData)

            signal = CreateCanSignal(frame=frame, comSheet=self.com_sheet, row=row, data_cfg=xlMtrixColData,
                                     ecu_list=ecu_list)

            frame.add_signal(signal)

        # add all related ecu
        for ecu in ecu_list:
            dbc.add_ecu(canmatrix.Ecu(ecu))

        fileOut = open(os.path.splitext(self.matrix_path)[0] + '.dbc', "wb")

        # output dbc
        # canmatrix.formats.dump(dbc, fileOut,"dbc", dbcExportEncoding='GBK')
        db_module.dump(dbc, fileOut)

        print('dbc generate ok!')

        pass




if __name__ == '__main__':
    cfg_command = open(os.path.join(os.getcwd(),'MatrixSheetCfg.txt'),'rb').read()
    exec(cfg_command)
    app = QtWidgets.QApplication(sys.argv)
    main_win = DbcGenMainWin()
    main_win.show()
    sys.exit(app.exec())
