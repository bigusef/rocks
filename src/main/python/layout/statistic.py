from PyQt5 import QtCore, QtWidgets, uic


class StatisticUIWindow(QtWidgets.QWidget):
    switch_window = QtCore.pyqtSignal()

    def __init__(self, ui_file: str, data):
        super(StatisticUIWindow, self).__init__()
        uic.loadUi(ui_file, self)
        self.data = data
        self.handle_ui_controlle()

    def handle_ui_controlle(self):
        self.list_widget = self.findChild(QtWidgets.QListWidget, 'listWidget')
        self.list_widget.addItems(self.data)

    def closeEvent(self, event):
        self.switcher()

    def switcher(self):
        self.switch_window.emit()
