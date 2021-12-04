# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Gera_SenhaFLiMHAz.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(288, 311)
        MainWindow.setContextMenuPolicy(Qt.DefaultContextMenu)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lblTamSen = QLabel(self.centralwidget)
        self.lblTamSen.setObjectName(u"lblTamSen")
        self.lblTamSen.setMinimumSize(QSize(95, 38))
        self.lblTamSen.setMaximumSize(QSize(91, 39))

        self.horizontalLayout.addWidget(self.lblTamSen, 0, Qt.AlignRight)

        self.inpTamSen = QLineEdit(self.centralwidget)
        self.inpTamSen.setObjectName(u"inpTamSen")
        self.inpTamSen.setMaximumSize(QSize(90, 16777215))
        self.inpTamSen.setTabletTracking(False)
        self.inpTamSen.setStyleSheet(u"border-color: rgb(255, 0, 0);")
        self.inpTamSen.setInputMethodHints(Qt.ImhNone)
        self.inpTamSen.setEchoMode(QLineEdit.Normal)
        self.inpTamSen.setDragEnabled(False)
        self.inpTamSen.setCursorMoveStyle(Qt.VisualMoveStyle)
        self.inpTamSen.setClearButtonEnabled(False)

        self.horizontalLayout.addWidget(self.inpTamSen, 0, Qt.AlignLeft)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.cbSimb = QCheckBox(self.centralwidget)
        self.cbSimb.setObjectName(u"cbSimb")

        self.gridLayout_2.addWidget(self.cbSimb, 3, 0, 1, 1)

        self.lblAdcSen = QLabel(self.centralwidget)
        self.lblAdcSen.setObjectName(u"lblAdcSen")
        self.lblAdcSen.setWordWrap(False)

        self.gridLayout_2.addWidget(self.lblAdcSen, 0, 0, 1, 1, Qt.AlignHCenter)

        self.cbEspec = QCheckBox(self.centralwidget)
        self.cbEspec.setObjectName(u"cbEspec")

        self.gridLayout_2.addWidget(self.cbEspec, 5, 0, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"")
        self.label.setTextFormat(Qt.AutoText)
        self.label.setWordWrap(False)

        self.gridLayout_2.addWidget(self.label, 7, 0, 1, 1)

        self.cbMinus = QCheckBox(self.centralwidget)
        self.cbMinus.setObjectName(u"cbMinus")

        self.gridLayout_2.addWidget(self.cbMinus, 2, 0, 1, 1)

        self.cbMaius = QCheckBox(self.centralwidget)
        self.cbMaius.setObjectName(u"cbMaius")
        self.cbMaius.setCursor(QCursor(Qt.ArrowCursor))
        self.cbMaius.setCheckable(True)
        self.cbMaius.setChecked(False)
        self.cbMaius.setAutoRepeat(False)
        self.cbMaius.setTristate(False)

        self.gridLayout_2.addWidget(self.cbMaius, 1, 0, 1, 1)

        self.lblEspec = QLineEdit(self.centralwidget)
        self.lblEspec.setObjectName(u"lblEspec")
        self.lblEspec.setEnabled(True)
        self.lblEspec.setReadOnly(False)

        self.gridLayout_2.addWidget(self.lblEspec, 6, 0, 1, 1)

        self.cbNum = QCheckBox(self.centralwidget)
        self.cbNum.setObjectName(u"cbNum")

        self.gridLayout_2.addWidget(self.cbNum, 4, 0, 1, 1)

        self.checkBox = QCheckBox(self.centralwidget)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout_2.addWidget(self.checkBox, 6, 1, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_2, 1, 0, 1, 1)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.btnGeraSen = QPushButton(self.centralwidget)
        self.btnGeraSen.setObjectName(u"btnGeraSen")
        self.btnGeraSen.setMinimumSize(QSize(75, 23))
        self.btnGeraSen.setMaximumSize(QSize(75, 23))

        self.gridLayout_4.addWidget(self.btnGeraSen, 1, 0, 1, 1)

        self.leSenha = QLineEdit(self.centralwidget)
        self.leSenha.setObjectName(u"leSenha")
        self.leSenha.setReadOnly(True)

        self.gridLayout_4.addWidget(self.leSenha, 1, 1, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_4, 2, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 288, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Gerador de Senhas", None))
        self.lblTamSen.setText(QCoreApplication.translate("MainWindow", u"Tamanho da senha:", None))
        self.inpTamSen.setInputMask("")
        self.inpTamSen.setText("")
        self.inpTamSen.setPlaceholderText("")
        self.cbSimb.setText(QCoreApplication.translate("MainWindow", u"S\u00edmbolos (@, #, $, %, &, (, ))", None))
        self.lblAdcSen.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\">Adicionar a senha:</p></body></html>", None))
        self.cbEspec.setText(QCoreApplication.translate("MainWindow", u"Palavar espic\u00edfica", None))
        self.label.setText("")
        self.cbMinus.setText(QCoreApplication.translate("MainWindow", u"Caracteres Mai\u00fasculos (A, B, C, D)", None))
        self.cbMaius.setText(QCoreApplication.translate("MainWindow", u"Caracteres Min\u00fasculos (a, b, c, d)", None))
        self.cbNum.setText(QCoreApplication.translate("MainWindow", u"N\u00fameros (0, 1, 2, 3)", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Embaralhar", None))
        self.btnGeraSen.setText(QCoreApplication.translate("MainWindow", u"GerarSenha", None))
        self.leSenha.setText("")
    # retranslateUi

