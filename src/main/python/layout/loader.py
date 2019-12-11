import uuid
import numpy as np
import pandas as pd
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog

from .load_ui import Ui_LoadData


class LoaderWindow(QtWidgets.QWidget, Ui_LoadData):
    switch_window = QtCore.pyqtSignal(list)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.handle_ui_controller()

    def handle_ui_controller(self):
        self.btn_read_file.clicked.connect(self.save_file_dialog)
        self.progress_read_file.setRange(0, 100)
        self.btn_nswr.clicked.connect(self.switcher)
        self.btn_nfem.clicked.connect(self.switcher)
        self.btn_dfem.clicked.connect(self.switcher)
        self.btn_ufe.clicked.connect(self.switcher)
        self.btn_rsrg.clicked.connect(self.switcher)
        self.btn_afem.clicked.connect(self.switcher)
        self.btn_adnstat.clicked.connect(self.switcher)

    def switcher(self):
        data = [
            "Mahmud",
            "Mohamed",
            "Ahmed",
            "Ali",
            "Moustafa",
        ]
        self.switch_window.emit(data)

    def save_file_dialog(self):
        pass
        # open attachment window
        # options = QFileDialog.Options()
        # options |= QFileDialog.DontUseNativeDialog
        # fileName, _ = QFileDialog.getOpenFileName(
        #     self,
        #     "QFileDialog.getSaveFileName()", "", "All Files (*);;Text Files (*.txt)", options=options
        # )
        # if fileName:
        #     self.arr_units = []
        #     self.arr_headers = []
        #     self.df_info = pd.read_csv(fileName, skiprows=0, nrows=253, header=None, encoding='unicode_escape')
        #
        #     df_headers = pd.read_csv(fileName, skiprows=254, nrows=1, header=None, encoding='unicode_escape')
        #
        #     for index in range(df_headers.shape[1]):
        #         columnSeriesObj = df_headers.iloc[:, index]
        #         self.arr_headers.append(columnSeriesObj.values[0])
        #
        #     # modify headers and modify duplicates
        #     final_list = []
        #     for num in self.arr_headers:
        #         if num not in final_list:
        #             final_list.append(num)
        #         else:
        #             num += str(uuid.uuid1())
        #             final_list.append(num)
        #     self.arr_headers = final_list
        #
        #     # check if there is duplicates in headers
        #     print('Duplicates in headers: ',
        #           len(set([x for x in self.arr_headers if self.arr_headers.count(x) > 1])) > 0)
        #
        #     # get units and groups
        #     df_units_groups = pd.read_csv(fileName, sep='', header=None, nrows=1,
        #                                   delimiter=r'\s+', low_memory=False, skiprows=256, encoding='unicode_escape')
        #
        #     for index in range(df_units_groups.shape[1]):
        #         columnSeriesObj_units = df_units_groups.iloc[0:1, index]
        #         self.arr_units.append(columnSeriesObj_units.values[0][1:-1])
        #     #####################
        #
        #     # read data and elimnate un-needed values
        #     self.df_data = pd.read_csv(fileName, header=None, skiprows=258, encoding='unicode_escape',
        #                                names=self.arr_headers)
        #     self.df_data.replace([65535, -999.250], np.nan, inplace=True)
