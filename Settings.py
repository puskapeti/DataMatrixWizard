from PyQt6.QtCore import QCoreApplication, QSettings

ORG_NAME = "Lasram Engineering Kft."
ORG_DOMAIN = "https://lasram.hu"
APP_NAME = "DataMatrix Wizard"

"""KEYS"""
DEFAULT_FILE_DIR = "defaultFileDir"
DEFAULT_FILE_DIR_DEF_VAL = "C:\\"
EXCEL_ROW = "excelRow"
EXCEL_ROW_DEF_VAL = 1
EXCEL_COLUMN = "excelColumn"
EXCEL_COLUMN_DEF_VAL = 1
DXF_NAME = "DXFName"
DXF_NAME_DEF_VAL = "generated.dxf"
DXF_PATH = "DXFPath"
DXF_PATH_DEF_VAL = "generated"
DXF_SIZE = "DXFSize"
DXF_SIZE_DEF_VAL = 8
HATCH_ANGLE = "hatchAngle"
HATCH_ANGLE_DEF_VAL = 0
HATCH_DENSITY = "hatchDensity"
HATCH_DENSITY_DEF_VAL = 27


class Settings:
    def __init__(self):
        QCoreApplication.setOrganizationName(ORG_NAME)
        QCoreApplication.setOrganizationDomain(ORG_DOMAIN)
        QCoreApplication.setApplicationName(APP_NAME)

        self.__settings = QSettings()

    @property
    def default_file_dir(self):
        return self.__settings.value(DEFAULT_FILE_DIR, DEFAULT_FILE_DIR_DEF_VAL)

    @default_file_dir.setter
    def default_file_dir(self, value: int):
        self.__settings.setValue(DEFAULT_FILE_DIR, value)

    @property
    def excel_row(self):
        return self.__settings.value(EXCEL_ROW, EXCEL_ROW_DEF_VAL)

    @excel_row.setter
    def excel_row(self, value: int):
        self.__settings.setValue(EXCEL_ROW, value)

    @property
    def excel_column(self):
        return self.__settings.value(EXCEL_COLUMN, EXCEL_COLUMN_DEF_VAL)

    @excel_column.setter
    def excel_column(self, value: int):
        self.__settings.setValue(EXCEL_COLUMN, value)

    @property
    def dxf_name(self):
        return self.__settings.value(DXF_NAME, DXF_NAME_DEF_VAL)

    @dxf_name.setter
    def dxf_name(self, value: str):
        self.__settings.setValue(DXF_NAME, value)

    @property
    def dxf_path(self):
        return self.__settings.value(DXF_PATH, DXF_PATH_DEF_VAL)

    @dxf_path.setter
    def dxf_path(self, value: str):
        self.__settings.setValue(DXF_PATH, value)

    @property
    def dxf_size(self):
        return self.__settings.value(DXF_SIZE, DXF_SIZE_DEF_VAL)

    @dxf_size.setter
    def dxf_size(self, value: float):
        self.__settings.setValue(DXF_SIZE, value)

    @property
    def hatch_angle(self):
        return self.__settings.value(HATCH_ANGLE, HATCH_ANGLE_DEF_VAL)

    @hatch_angle.setter
    def hatch_angle(self, value: float):
        self.__settings.setValue(HATCH_ANGLE, value)

    @property
    def hatch_density(self):
        return self.__settings.value(HATCH_DENSITY, HATCH_DENSITY_DEF_VAL)

    @hatch_density.setter
    def hatch_density(self, value: float):
        self.__settings.setValue(HATCH_DENSITY, value)
