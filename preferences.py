import os

from PyQt6 import QtGui
from PyQt6.QtWidgets import QWidget, QFileDialog

from Settings import Settings
from preferencesUI import Ui_preferences


class Preferences(QWidget, Ui_preferences):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        """Initialize variables"""
        self.__settings = Settings()

        """Initialize UI elements"""
        self.line_edit_dxf_name.setText(self.__settings.dxf_name)
        self.line_edit_dxf_path.setText(self.__settings.dxf_path)
        self.line_edit_dxf_size.setText(str(self.__settings.dxf_size))

        """Connect signals"""
        self.line_edit_dxf_name.textChanged.connect(self.line_edit_text_changed_callback)
        self.line_edit_dxf_path.textChanged.connect(self.line_edit_text_changed_callback)
        self.line_edit_dxf_size.textChanged.connect(self.line_edit_text_changed_callback)

        self.button_browse_path.clicked.connect(self.button_browse_path_clicked_callback)

        """Adding focus handlers"""
        self.line_edit_dxf_name_fh = self.line_edit_dxf_name.focusOutEvent
        self.line_edit_dxf_name.focusOutEvent = self.focus_handler

    def line_edit_text_changed_callback(self):
        # DXF name
        dxf_name = self.line_edit_dxf_name.text()
        self.__settings.dxf_name = dxf_name

        # DXF path
        dxf_path = self.line_edit_dxf_path.text()
        if os.path.exists(dxf_path):
            self.line_edit_dxf_path.setStyleSheet('color: black;')

        else:
            self.line_edit_dxf_path.setStyleSheet('color: red;')

        # DXF size
        dxf_size = self.line_edit_dxf_size.text()
        try:
            float(dxf_size)
            self.line_edit_dxf_size.setStyleSheet('color: black;')

        except ValueError:
            # not a float
            self.line_edit_dxf_size.setStyleSheet('color: red;')

    def button_browse_path_clicked_callback(self):
        dir_path = QFileDialog.getExistingDirectory()

        if dir_path == '':
            return

        self.line_edit_dxf_path.setText(dir_path)

    def focus_handler(self, event):
        self.line_edit_dxf_name_fh(event)
        dxf_name = self.line_edit_dxf_name.text()

        if not dxf_name.endswith('.dxf'):
            self.line_edit_dxf_name.setText(dxf_name + '.dxf')

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        """save the line edit values"""
        # dxf name
        # no need to check extension, the closeEvent happens after lineEdit loses focus
        self.__settings.dxf_name = self.line_edit_dxf_name.text()

        # dxf path
        dxf_path = self.line_edit_dxf_path.text()
        if os.path.exists(dxf_path):
            self.__settings.dxf_path = dxf_path

        # dxf size
        try:
            dxf_size = float(self.line_edit_dxf_size.text())
            self.__settings.dxf_size = dxf_size

        except ValueError:
            # not a float
            pass

        super().closeEvent(a0)
