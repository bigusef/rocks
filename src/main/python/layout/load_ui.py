# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'load.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoadData(object):
    def setupUi(self, LoadData):
        LoadData.setObjectName("LoadData")
        LoadData.resize(471, 280)
        LoadData.setMinimumSize(QtCore.QSize(471, 280))
        LoadData.setMaximumSize(QtCore.QSize(471, 280))
        self.groupBox_2 = QtWidgets.QGroupBox(LoadData)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 60, 450, 210))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.btn_nswr = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_nswr.setGeometry(QtCore.QRect(10, 10, 200, 40))
        self.btn_nswr.setObjectName("btn_nswr")
        self.btn_dfem = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_dfem.setGeometry(QtCore.QRect(10, 60, 200, 40))
        self.btn_dfem.setObjectName("btn_dfem")
        self.btn_ufe = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_ufe.setGeometry(QtCore.QRect(10, 110, 200, 40))
        self.btn_ufe.setObjectName("btn_ufe")
        self.btn_rsrg = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_rsrg.setGeometry(QtCore.QRect(10, 160, 200, 40))
        self.btn_rsrg.setObjectName("btn_rsrg")
        self.btn_adnstat = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_adnstat.setGeometry(QtCore.QRect(240, 110, 200, 40))
        self.btn_adnstat.setObjectName("btn_adnstat")
        self.btn_nfem = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_nfem.setGeometry(QtCore.QRect(240, 10, 200, 40))
        self.btn_nfem.setObjectName("btn_nfem")
        self.btn_afem = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_afem.setGeometry(QtCore.QRect(240, 60, 200, 40))
        self.btn_afem.setObjectName("btn_afem")
        self.layoutWidget = QtWidgets.QWidget(LoadData)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 19, 451, 32))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_read_file = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_read_file.setObjectName("btn_read_file")
        self.horizontalLayout.addWidget(self.btn_read_file)
        self.progress_read_file = QtWidgets.QProgressBar(self.layoutWidget)
        self.progress_read_file.setProperty("value", 0)
        self.progress_read_file.setObjectName("progress_read_file")
        self.horizontalLayout.addWidget(self.progress_read_file)

        self.retranslateUi(LoadData)
        QtCore.QMetaObject.connectSlotsByName(LoadData)

    def retranslateUi(self, LoadData):
        _translate = QtCore.QCoreApplication.translate
        LoadData.setWindowTitle(_translate("LoadData", "Load Dat File"))
        self.btn_nswr.setText(_translate("LoadData", "NSWR"))
        self.btn_dfem.setText(_translate("LoadData", "DFEM"))
        self.btn_ufe.setText(_translate("LoadData", "UFE1 / UFE2"))
        self.btn_rsrg.setText(_translate("LoadData", "RSRG"))
        self.btn_adnstat.setText(_translate("LoadData", "ADNSTAT "))
        self.btn_nfem.setText(_translate("LoadData", "NFEM "))
        self.btn_afem.setText(_translate("LoadData", "AFEM"))
        self.btn_read_file.setText(_translate("LoadData", "Load Data File"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoadData = QtWidgets.QWidget()
    ui = Ui_LoadData()
    ui.setupUi(LoadData)
    LoadData.show()
    sys.exit(app.exec_())
