from PyQt5 import QtCore, QtWidgets

from .statistic_ui import Ui_StatisticForm


class StatisticWindow(QtWidgets.QWidget, Ui_StatisticForm):
    switch_window = QtCore.pyqtSignal()

    def __init__(self, data, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data = data
        self.setupUi(self)
        self.handle_ui_controller()

    def handle_ui_controller(self):
        self.list_names.addItems(self.data)

    def closeEvent(self, event):
        self.switcher()

    def switcher(self):
        self.switch_window.emit()
