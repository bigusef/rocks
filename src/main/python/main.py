import sys
from fbs_runtime.application_context.PyQt5 import ApplicationContext

from layout.loader import LoaderWindow
from layout.statistic import StatisticWindow


class AppContext(ApplicationContext):
    def __init__(self):
        super().__init__()
        self.loader = LoaderWindow()
        self.statistic = None

    def run(self):
        self.show_loader()
        return self.app.exec_()

    def show_loader(self):
        self.loader.switch_window.connect(self.show_statistic)
        self.loader.show()

    def show_statistic(self, data):
        self.statistic = StatisticWindow(data)
        self.statistic.switch_window.connect(self.show_loader)
        self.statistic.show()


if __name__ == '__main__':
    appctxt = AppContext()
    exit_code = appctxt.run()
    sys.exit(exit_code)
