# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'giris.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(712, 831)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(300, 0))
        self.frame.setMaximumSize(QSize(16777215, 100))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.kullanici_adi = QLabel(self.frame)
        self.kullanici_adi.setObjectName(u"kullanici_adi")
        self.kullanici_adi.setMinimumSize(QSize(150, 40))
        self.kullanici_adi.setMaximumSize(QSize(100, 50))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.kullanici_adi.setFont(font)
        self.kullanici_adi.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.kullanici_adi)

        self.adline = QLineEdit(self.frame)
        self.adline.setObjectName(u"adline")

        self.horizontalLayout_8.addWidget(self.adline)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(Dialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(300, 0))
        self.frame_2.setMaximumSize(QSize(16777215, 100))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.sifre = QLabel(self.frame_2)
        self.sifre.setObjectName(u"sifre")
        self.sifre.setMinimumSize(QSize(150, 40))
        self.sifre.setMaximumSize(QSize(100, 50))
        self.sifre.setFont(font)
        self.sifre.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.sifre)

        self.sifreline = QLineEdit(self.frame_2)
        self.sifreline.setObjectName(u"sifreline")
        self.sifreline.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_9.addWidget(self.sifreline)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.dou_logo = QLabel(Dialog)
        self.dou_logo.setObjectName(u"dou_logo")
        self.dou_logo.setPixmap(QPixmap(u"dogus.png"))
        self.dou_logo.setScaledContents(True)

        self.verticalLayout_2.addWidget(self.dou_logo)

        self.frame_3 = QFrame(Dialog)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(300, 0))
        self.frame_3.setMaximumSize(QSize(100, 100))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.vazgec_button = QPushButton(self.frame_3)
        self.vazgec_button.setObjectName(u"vazgec_button")
        self.vazgec_button.setMinimumSize(QSize(100, 40))
        self.vazgec_button.setMaximumSize(QSize(120, 50))
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(True)
        self.vazgec_button.setFont(font1)
        self.vazgec_button.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255,0, 0);\n"
"	border: 2px solid;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton::hover\n"
"{\n"
"	background-color: rgb(255, 255, 0);\n"
"\n"
"}")

        self.horizontalLayout_7.addWidget(self.vazgec_button)

        self.giris_button = QPushButton(self.frame_3)
        self.giris_button.setObjectName(u"giris_button")
        self.giris_button.setMinimumSize(QSize(100, 40))
        self.giris_button.setMaximumSize(QSize(120, 50))
        self.giris_button.setFont(font1)
        self.giris_button.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0, 255, 0);\n"
"	border: 2px solid;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton::hover\n"
"{\n"
"	background-color: rgb(255, 255, 0);\n"
"\n"
"}")

        self.horizontalLayout_7.addWidget(self.giris_button)


        self.verticalLayout_2.addWidget(self.frame_3)


        self.verticalLayout.addLayout(self.verticalLayout_2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"ROBDOU", None))
        self.kullanici_adi.setText(QCoreApplication.translate("Dialog", u"KULLANICI ADI: ", None))
        self.sifre.setText(QCoreApplication.translate("Dialog", u"\u015e\u0130FRE:       ", None))
        self.dou_logo.setText("")
        self.vazgec_button.setText(QCoreApplication.translate("Dialog", u"VAZGE\u00c7", None))
        self.giris_button.setText(QCoreApplication.translate("Dialog", u"G\u0130R\u0130\u015e YAP", None))
    # retranslateUi

