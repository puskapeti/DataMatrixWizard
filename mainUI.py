# Form implementation generated from reading ui file 'ui\res\layout\main.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(560, 437)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(560, 437))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/logo"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setMaximumSize(QtCore.QSize(363, 376))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(10, 20, 10, 20)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.line_edit_file_path = QtWidgets.QLineEdit(self.widget)
        self.line_edit_file_path.setObjectName("line_edit_file_path")
        self.verticalLayout_4.addWidget(self.line_edit_file_path)
        self.button_open_file = QtWidgets.QPushButton(self.widget)
        self.button_open_file.setObjectName("button_open_file")
        self.verticalLayout_4.addWidget(self.button_open_file)
        self.verticalLayout_2.addLayout(self.verticalLayout_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label)
        self.spinbox_column = QtWidgets.QSpinBox(self.widget)
        self.spinbox_column.setObjectName("spinbox_column")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.spinbox_column)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_2)
        self.spinbox_row = QtWidgets.QSpinBox(self.widget)
        self.spinbox_row.setObjectName("spinbox_row")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.spinbox_row)
        self.verticalLayout_3.addLayout(self.formLayout)
        self.button_reload = QtWidgets.QPushButton(self.widget)
        self.button_reload.setMinimumSize(QtCore.QSize(0, 30))
        self.button_reload.setObjectName("button_reload")
        self.verticalLayout_3.addWidget(self.button_reload)
        self.button_generate_dm = QtWidgets.QPushButton(self.widget)
        self.button_generate_dm.setMinimumSize(QtCore.QSize(0, 30))
        self.button_generate_dm.setObjectName("button_generate_dm")
        self.verticalLayout_3.addWidget(self.button_generate_dm)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.label_image = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_image.sizePolicy().hasHeightForWidth())
        self.label_image.setSizePolicy(sizePolicy)
        self.label_image.setMinimumSize(QtCore.QSize(250, 250))
        self.label_image.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.label_image.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.label_image.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_image.setObjectName("label_image")
        self.horizontalLayout_2.addWidget(self.label_image)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_4 = QtWidgets.QLabel(self.widget_2)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_4)
        self.line_edit_hatch_density = QtWidgets.QLineEdit(self.widget_2)
        self.line_edit_hatch_density.setMaximumSize(QtCore.QSize(50, 16777215))
        self.line_edit_hatch_density.setObjectName("line_edit_hatch_density")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.line_edit_hatch_density)
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_3)
        self.line_edit_hatch_angle = QtWidgets.QLineEdit(self.widget_2)
        self.line_edit_hatch_angle.setMaximumSize(QtCore.QSize(50, 16777215))
        self.line_edit_hatch_angle.setObjectName("line_edit_hatch_angle")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.line_edit_hatch_angle)
        self.verticalLayout_6.addLayout(self.formLayout_2)
        self.horizontalLayout.addWidget(self.widget_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 560, 22))
        self.menubar.setObjectName("menubar")
        self.menu_file = QtWidgets.QMenu(self.menubar)
        self.menu_file.setObjectName("menu_file")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_preferences = QtGui.QAction(MainWindow)
        self.action_preferences.setObjectName("action_preferences")
        self.action_exit = QtGui.QAction(MainWindow)
        self.action_exit.setObjectName("action_exit")
        self.menu_file.addAction(self.action_preferences)
        self.menu_file.addAction(self.action_exit)
        self.menubar.addAction(self.menu_file.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DataMatrix Wizard"))
        self.button_open_file.setText(_translate("MainWindow", "Fájl megnyitása"))
        self.label.setText(_translate("MainWindow", "Oszlop"))
        self.label_2.setText(_translate("MainWindow", "Sor"))
        self.button_reload.setText(_translate("MainWindow", "Újratöltés"))
        self.button_generate_dm.setText(_translate("MainWindow", "Generálás"))
        self.label_image.setText(_translate("MainWindow", "preview"))
        self.label_4.setText(_translate("MainWindow", "Sraffozás sűrűsége"))
        self.label_3.setText(_translate("MainWindow", "Sraffozás szöge"))
        self.menu_file.setTitle(_translate("MainWindow", "Fájl"))
        self.action_preferences.setText(_translate("MainWindow", "Beállítások"))
        self.action_exit.setText(_translate("MainWindow", "Kilépés"))
