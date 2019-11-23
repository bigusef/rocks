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
import regex as re

class LoadUIWindow(QtWidgets.QWidget):
    switch_window = QtCore.pyqtSignal(list)
    # headers = []
    # units = []
    # info=[]
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
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(
            self, "QFileDialog.getSaveFileName()", "", "All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            #read headers
            df_headers = pd.read_csv(fileName, skiprows=18,nrows=1, header=None)
            rx = r'(?V1)(?<=[^A-Za-z0-9])(?=\d)'

            for index in range(df_headers.shape[1]):
                columnSeriesObj = df_headers.iloc[: , index]
                arr_headers = re.split(rx, ''.join(str(e) for e in columnSeriesObj.values[0]))
                header_result = " ".join(arr_headers[0].split()).split(' ')
            
            #read data
            df = pd.read_csv(fileName, sep='', header=None, names=header_result,
                delimiter=r'\s+', low_memory=False, skiprows=22)

            # replace unneeded values              
            df.replace([65535, -999.250], np.nan, inplace=True)