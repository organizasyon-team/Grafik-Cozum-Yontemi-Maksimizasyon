import sys
from PyQt5.QtWidgets import QApplication, QWidget
from MainForm import Ui_MainWindow

def window():
    app = QApplication(sys.argv)
    form = QWidget()
    ui = Ui_MainWindow()
    ui.setupUi(form)
    form.show()
    sys.exit(app.exec_())
if __name__ == '__main__':
    window()