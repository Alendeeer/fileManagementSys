# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setting.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Setting(object):
    def setupUi(self, Setting):
        Setting.setObjectName("Setting")
        Setting.resize(525, 334)
        self.setting = QtWidgets.QPushButton(Setting)
        self.setting.setGeometry(QtCore.QRect(200, 200, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.setting.setFont(font)
        self.setting.setObjectName("setting")
        self.labelName = QtWidgets.QLineEdit(Setting)
        self.labelName.setGeometry(QtCore.QRect(150, 120, 241, 21))
        self.labelName.setObjectName("labelName")
        self.settingInfo = QtWidgets.QLabel(Setting)
        self.settingInfo.setGeometry(QtCore.QRect(200, 250, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.settingInfo.setFont(font)
        self.settingInfo.setText("")
        self.settingInfo.setAlignment(QtCore.Qt.AlignCenter)
        self.settingInfo.setObjectName("settingInfo")
        self.label_4 = QtWidgets.QLabel(Setting)
        self.label_4.setGeometry(QtCore.QRect(120, 65, 300, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Setting)
        QtCore.QMetaObject.connectSlotsByName(Setting)

    def retranslateUi(self, Setting):
        _translate = QtCore.QCoreApplication.translate
        Setting.setWindowTitle(_translate("Setting", "Form"))
        self.setting.setText(_translate("Setting", "Confirmed"))
        self.label_4.setText(_translate("Setting", "Label(Separate with space): "))
