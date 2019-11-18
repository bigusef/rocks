import sys

from fbs_runtime.application_context.PyQt5 import ApplicationContext, cached_property

from layout.loader import LoadUIWindow
from layout.statistic import StatisticUIWindow


class AppContext(ApplicationContext):
    def run(self):
        self.show_loader()
        return self.app.exec_()

    @cached_property
    def get_ui(self):
        return {
            "load": self.get_resource('theme/load.ui'),
            "statistic": self.get_resource('theme/statistic.ui'),
        }

    def show_loader(self):
        self.loader = LoadUIWindow(self.get_ui.get('load'))
        self.loader.switch_window.connect(self.show_statistic)
        self.loader.show()

    def show_statistic(self, data):
        self.statistic = StatisticUIWindow(self.get_ui.get('statistic'), data)
        self.statistic.switch_window.connect(self.show_loader)
        self.loader.close()
        self.statistic.show()


if __name__ == '__main__':
    appctxt = AppContext()
    exit_code = appctxt.run()
    sys.exit(exit_code)
