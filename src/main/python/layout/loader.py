from PyQt5 import QtCore, QtWidgets, uic


class LoadUIWindow(QtWidgets.QWidget):
    switch_window = QtCore.pyqtSignal(list)

    def __init__(self, ui_file: str):
        super(LoadUIWindow, self).__init__()
        uic.loadUi(ui_file, self)
        self.handle_ui_controlle()

    def handle_ui_controlle(self):
        self.setFixedSize(350, 200)

        self.btn_open_file = self.findChild(QtWidgets.QPushButton, 'btnReadFile')
        self.btn_open_file.clicked.connect(self.switcher)

    def switcher(self):
        data = [
            "Mahmud",
            "Mohamed",
            "Ahmed",
            "Ali",
            "Moustafa",
        ]
        self.switch_window.emit(data)
