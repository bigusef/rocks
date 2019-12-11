# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'statistic.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_StatisticForm(object):
    def setupUi(self, StatisticForm):
        StatisticForm.setObjectName("StatisticForm")
        StatisticForm.resize(367, 233)
        self.list_names = QtWidgets.QListWidget(StatisticForm)
        self.list_names.setGeometry(QtCore.QRect(0, 0, 121, 351))
        self.list_names.setObjectName("list_names")

        self.retranslateUi(StatisticForm)
        QtCore.QMetaObject.connectSlotsByName(StatisticForm)

    def retranslateUi(self, StatisticForm):
        _translate = QtCore.QCoreApplication.translate
        StatisticForm.setWindowTitle(_translate("StatisticForm", "Statistics"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StatisticForm = QtWidgets.QWidget()
    ui = Ui_StatisticForm()
    ui.setupUi(StatisticForm)
    StatisticForm.show()
    sys.exit(app.exec_())
