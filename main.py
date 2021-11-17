import os.path
import sys

import pandas
import pylibdmtx.pylibdmtx
from PyQt6 import QtGui
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QMainWindow, QApplication, QFileDialog

import Matrix
from Settings import Settings
from dxfgen import Generator
from preferences import Preferences
from mainUI import Ui_MainWindow


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        """Initializing variables"""
        self.__settings = Settings()  # init settings
        self.__generator = Generator()  # init dxf generator
        self.__data = None  # type: None or str
        self.__excel = None
        self.__preferences = Preferences(parent=None)

        """Initializing ui elements"""
        self.spinbox_column.setValue(self.__settings.excel_column)
        self.spinbox_row.setValue(self.__settings.excel_row)

        self.line_edit_hatch_angle.setText(str(self.__settings.hatch_angle))
        self.line_edit_hatch_density.setText(str(self.__settings.hatch_density))

        self.label_image.setText('')
        self.label_hatch_preview.setText('')

        """Connecting signals"""
        # buttons
        self.button_open_file.clicked.connect(self.open_file_callback)
        self.button_reload.clicked.connect(self.reload_callback)
        self.button_generate_dm.clicked.connect(self.generate_callback)

        # lineEdit
        self.line_edit_file_path.textChanged.connect(self.line_edit_changed_callback)
        self.line_edit_hatch_angle.textChanged.connect(self.line_edit_changed_callback)
        self.line_edit_hatch_density.textChanged.connect(self.line_edit_changed_callback)

        # actions
        self.action_exit.triggered.connect(self.close)
        self.action_preferences.triggered.connect(self.open_preferences)

    """ OVERRIDES --------------------------------------------------------------------------------------------------"""

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        # save the state of values
        # spinbox
        self.__settings.excel_row = self.spinbox_row.value()
        self.__settings.excel_column = self.spinbox_column.value()

        # lineEdit
        hatch_angle = self.line_edit_hatch_angle.text()
        try:
            angle_float = float(hatch_angle)
            self.__settings.hatch_angle = angle_float

        except ValueError:
            pass

        hatch_density = self.line_edit_hatch_density.text()
        try:
            density_float = float(hatch_density)
            self.__settings.hatch_density = density_float

        except ValueError:
            pass

        super().closeEvent(a0)

    """ CALLBACKS --------------------------------------------------------------------------------------------------"""

    def open_file_callback(self):
        filename = self.__open_file_dialog()

        if filename is None:
            return
        self.__excel = self.__open_excel(filename)
        self.__data = self.__load_data(self.__excel)

        self.__set_preview(self.__data)

    def reload_callback(self):
        self.__data = self.__load_data(self.__excel)

        self.__set_preview(self.__data)

    def line_edit_changed_callback(self):
        # file path
        file_name = self.line_edit_file_path.text()

        if not os.path.isfile(file_name):
            self.line_edit_file_path.setStyleSheet("color: red;")

        else:
            self.line_edit_file_path.setStyleSheet("color: black;")

        # hatch angle
        try:
            float(self.line_edit_hatch_angle.text())
            self.line_edit_hatch_angle.setStyleSheet("color: black;")

        except ValueError:
            self.line_edit_hatch_angle.setStyleSheet("color: red;")

        # hatch density
        try:
            float(self.line_edit_hatch_density.text())
            self.line_edit_hatch_density.setStyleSheet("color: black;")

        except ValueError:
            self.line_edit_hatch_density.setStyleSheet("color: red;")

    def generate_callback(self):
        if self.__data is None:
            self.statusbar.showMessage("Nincs adat beolvasva", msecs=-1)
            return

        dxf_name = self.__settings.dxf_name
        dxf_path = self.__settings.dxf_path
        encoded_data = pylibdmtx.pylibdmtx.encode(self.__data.encode('utf-8'))
        self.__generator.matrix = Matrix.load_from_encoded_data(encoded_data)
        self.__generator.generate(filename=dxf_path + '/' + dxf_name)

        self.statusbar.showMessage(f"DataMatrix generálva {dxf_path + '/' + dxf_name}-ként")

    def open_preferences(self):
        self.__preferences.show()

    """ METHODS ----------------------------------------------------------------------------------------------------"""

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
        self.line_edit_file_path.setText(file_name)

        return file_name

    def __open_excel(self, filename: str) -> pandas.DataFrame:
        dataframe = pandas.read_excel(filename, sheet_name=0, header=None)  # type: pandas.DataFrame
        print(dataframe)

        return dataframe

    def __load_data(self, dataframe: pandas.DataFrame):
        row = self.spinbox_row.value() - 1  # zero indexed
        column = self.spinbox_column.value() - 1

        try:
            data = dataframe.at[row, column]
            print(data)
            return data

        except KeyError:
            return None

    def __set_preview(self, data):
        if data is None:
            self.label_image.setText("Nem megfelelő oszlop/sor")

        else:
            preview = self.__generator.generate_png(data)

            pixmap = QPixmap(preview)
            self.label_image.setPixmap(pixmap)

        self.label_image.setScaledContents(True)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())

    # TODO: display the loaded data
    # TODO: rewrite the load data method to only load the excel file once
