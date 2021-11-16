import os.path
import sys

from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QMainWindow, QApplication, QFileDialog

from Settings import Settings
from dxfgen import Generator
from mainUI import Ui_MainWindow


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.__settings = Settings()  # init settings

        """Connecting signals"""
        self.button_open_file.clicked.connect(self.open_file_callback)
        self.__generator = Generator()

    def open_file_callback(self):
        # todo finish importing excel

        self.__open_file_dialog()

        data = "H-1234-5678"
        preview = self.__generator.generate_png(data)

        pixmap = QPixmap(preview)
        self.label_image.setPixmap(pixmap)
        self.label_image.setScaledContents(True)

    def __open_file_dialog(self):
        file_name = QFileDialog.getOpenFileName(
            self,
            'Fájl megnyitása',
            self.__settings.default_file_dir,
            "Excel (*.xls, *xlsx)"
        )[0]  # returns a tuple of the abs file name and filetype

        if file_name == "":
            return None

        file_dir = os.path.dirname(os.path.abspath(file_name))
        self.__settings.default_file_dir = file_dir

        # set line edit text
        self.line_edit_file_path.setText(file_dir)

        return file_name

    def __open_excel(self):
        pass

    def __load_data(self):
        pass


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
