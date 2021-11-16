from PyQt6.QtCore import QCoreApplication, QSettings

ORG_NAME = "Lasram Engineering Kft."
ORG_DOMAIN = "https://lasram.hu"
APP_NAME = "DataMatrix Wizard"

"""KEYS"""
DEFAULT_FILE_DIR = "defaultFileDir"


class Settings:
    def __init__(self):
        QCoreApplication.setOrganizationName(ORG_NAME)
        QCoreApplication.setOrganizationDomain(ORG_DOMAIN)
        QCoreApplication.setApplicationName(APP_NAME)

        self.__settings = QSettings()

    @property
    def default_file_dir(self):
        return self.__settings.value(DEFAULT_FILE_DIR, "C:\\")

    @default_file_dir.setter
    def default_file_dir(self, value: str):
        self.__settings.setValue(DEFAULT_FILE_DIR, value)
