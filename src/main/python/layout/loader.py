from PyQt5 import QtCore, QtWidgets, uic
from PyQt5.QtWidgets import (QWidget, QPushButton,
                             QHBoxLayout, QVBoxLayout, QApplication, QMainWindow,  QInputDialog, QLineEdit, QFileDialog)
from PyQt5.QtGui import QIcon


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon
import pandas as pd
import numpy as np
# import matplotlib
# import matplotlib.pyplot as plt
# import regex as re
import uuid
class LoadUIWindow(QtWidgets.QWidget):
    switch_window = QtCore.pyqtSignal(list)
    def __init__(self, ui_file: str):
        super(LoadUIWindow, self).__init__()
        uic.loadUi(ui_file, self)
        self.handle_ui_controlle()

    def handle_ui_controlle(self):
        self.setFixedSize(471, 280)

        self.btn_open_file = self.findChild(QtWidgets.QPushButton, 'btnReadFile')
        self.btn_open_file.clicked.connect(self.saveFileDialog)

        self.btn_nswr = self.findChild(QtWidgets.QPushButton, 'btn_nswr')
        self.btn_nswr.clicked.connect(self.switcher)

        self.btn_nfem = self.findChild(QtWidgets.QPushButton, 'btn_nfem')
        self.btn_nfem.clicked.connect(self.switcher)

        self.btn_dfem = self.findChild(QtWidgets.QPushButton, 'btn_dfem')
        self.btn_dfem.clicked.connect(self.switcher)

        self.btn_ufe = self.findChild(QtWidgets.QPushButton, 'btn_ufe')
        self.btn_ufe.clicked.connect(self.switcher)

        self.btn_rsrg = self.findChild(QtWidgets.QPushButton, 'btn_rsrg')
        self.btn_rsrg.clicked.connect(self.switcher)

        self.btn_afem = self.findChild(QtWidgets.QPushButton, 'btn_afem')
        self.btn_afem.clicked.connect(self.switcher)

        self.btn_adnstat = self.findChild(QtWidgets.QPushButton, 'btn_adnstat')
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

    
    def saveFileDialog(self):
        # open attachment window
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(
            self, "QFileDialog.getSaveFileName()", "", "All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            arr_units=[]
            arr_headers=[]
            # arr_data = []
            # get headers
            # df_data = pd.read_csv(fileName,  skiprows=0,nrows=253, header=None,encoding = 'unicode_escape')
            # print(df_data)
            df_headers = pd.read_csv(fileName, skiprows=254,nrows=1, header=None,encoding = 'unicode_escape')
            # rx = r'(?V1)(?<=[^A-Za-z0-9])(?=\d)'
            
            for index in range(df_headers.shape[1]):
                columnSeriesObj = df_headers.iloc[: , index]
                arr_headers.append(columnSeriesObj.values[0])

            # modify headers and modify duplicates
            final_list = [] 
            for num in arr_headers: 
                if num not in final_list:
                    final_list.append(num)
                else:
                    num += str(uuid.uuid1())
                    final_list.append(num)
            arr_headers = final_list

            # check if there is duplicates in headers
            print('Duplicates in headers: ', len(set([x for x in arr_headers if arr_headers.count(x) > 1]))>0)

            #get units and groups
            df_units_groups = pd.read_csv(fileName, sep='', header=None,nrows=1,
                delimiter=r'\s+', low_memory=False, skiprows=256,encoding = 'unicode_escape')

            for index in range(df_units_groups.shape[1]):
                columnSeriesObj_units = df_units_groups.iloc[0:1 , index]
                arr_units.append(columnSeriesObj_units.values[0][1:-1])
            #####################

            # read data and elimnate un-needed values
            self.df_data = pd.read_csv(fileName,header=None,skiprows=258,encoding = 'unicode_escape', names=arr_headers)
            self.df_data.replace([65535, -999.250], np.nan, inplace=True)
            # print(self.df_data.TIME)