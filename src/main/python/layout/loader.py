from PyQt5 import QtCore, QtWidgets, uic


class LoadUIWindow(QtWidgets.QWidget):
    switch_window = QtCore.pyqtSignal(list)

    def __init__(self, ui_file: str):
        super(LoadUIWindow, self).__init__()
        uic.loadUi(ui_file, self)
        self.handle_ui_controlle()

    def handle_ui_controlle(self):
        self.setFixedSize(471, 280)

        self.btn_open_file = self.findChild(QtWidgets.QPushButton, 'btnReadFile')
        self.btn_open_file.clicked.connect(self.switcher)

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
