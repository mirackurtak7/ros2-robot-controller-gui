# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'anasayfa.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QTabWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
import ikonlar_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(792, 580)
        MainWindow.setMinimumSize(QSize(200, 200))
        MainWindow.setMaximumSize(QSize(15000, 15000))
        icon = QIcon()
        icon.addFile(u":/images/icons/optimak.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: rgb(186, 12, 47);\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_11 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.tabWidgetEtiketOzellikleri = QTabWidget(self.centralwidget)
        self.tabWidgetEtiketOzellikleri.setObjectName(u"tabWidgetEtiketOzellikleri")
        self.tabWidgetEtiketOzellikleri.setEnabled(True)
        font = QFont()
        font.setFamilies([u"DejaVu Sans"])
        font.setPointSize(10)
        font.setBold(True)
        self.tabWidgetEtiketOzellikleri.setFont(font)
        self.tabWidgetEtiketOzellikleri.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(27, 27, 36);\n"
"")
        self.tabWidgetEtiketOzellikleri.setTabPosition(QTabWidget.West)
        self.ANASAYFA = QWidget()
        self.ANASAYFA.setObjectName(u"ANASAYFA")
        self.ANASAYFA.setStyleSheet(u"")
        self.verticalLayout_7 = QVBoxLayout(self.ANASAYFA)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_ust = QFrame(self.ANASAYFA)
        self.frame_ust.setObjectName(u"frame_ust")
        self.frame_ust.setMinimumSize(QSize(0, 250))
        self.frame_ust.setMaximumSize(QSize(16777215, 250))
        self.frame_ust.setFrameShape(QFrame.StyledPanel)
        self.frame_ust.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_ust)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.frame_ust)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(250, 150))
        self.frame.setMaximumSize(QSize(300, 220))
        self.frame.setStyleSheet(u"background-color: rgb(230, 230, 230);\n"
"border-radius: 20px;\n"
"border: 3px solid  rgb(0, 120, 10);\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.text_10 = QLabel(self.frame)
        self.text_10.setObjectName(u"text_10")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_10.sizePolicy().hasHeightForWidth())
        self.text_10.setSizePolicy(sizePolicy)
        self.text_10.setMinimumSize(QSize(50, 30))
        self.text_10.setMaximumSize(QSize(100, 30))
        font1 = QFont()
        font1.setBold(True)
        self.text_10.setFont(font1)
        self.text_10.setStyleSheet(u"border:none;")
        self.text_10.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.text_10, 4, 0, 1, 1)

        self.agv_net_durumu = QLabel(self.frame)
        self.agv_net_durumu.setObjectName(u"agv_net_durumu")
        self.agv_net_durumu.setEnabled(True)
        sizePolicy.setHeightForWidth(self.agv_net_durumu.sizePolicy().hasHeightForWidth())
        self.agv_net_durumu.setSizePolicy(sizePolicy)
        self.agv_net_durumu.setMinimumSize(QSize(60, 30))
        self.agv_net_durumu.setMaximumSize(QSize(80, 30))
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(51, 209, 122, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(121, 255, 181, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(86, 232, 151, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(25, 104, 61, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(34, 139, 81, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        brush6 = QBrush(QColor(255, 255, 255, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush6)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush)
        brush7 = QBrush(QColor(153, 232, 188, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush7)
        brush8 = QBrush(QColor(255, 255, 220, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush8)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        brush9 = QBrush(QColor(0, 0, 0, 128))
        brush9.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush9)
#endif
        self.agv_net_durumu.setPalette(palette)
        font2 = QFont()
        font2.setFamilies([u"Ubuntu Mono"])
        font2.setPointSize(11)
        font2.setBold(True)
        self.agv_net_durumu.setFont(font2)
        self.agv_net_durumu.setStyleSheet(u"border:none;background-color:rgb(255,0,0);border-radius:12px;")
        self.agv_net_durumu.setAlignment(Qt.AlignCenter)
        self.agv_net_durumu.setWordWrap(True)
        self.agv_net_durumu.setIndent(1)

        self.gridLayout.addWidget(self.agv_net_durumu, 4, 2, 1, 1)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 30))
        font3 = QFont()
        font3.setFamilies([u"Ubuntu"])
        font3.setPointSize(11)
        font3.setBold(True)
        font3.setUnderline(True)
        self.label_4.setFont(font3)
        self.label_4.setStyleSheet(u"border:none;")

        self.gridLayout.addWidget(self.label_4, 2, 3, 1, 1)

        self.text_9 = QLabel(self.frame)
        self.text_9.setObjectName(u"text_9")
        self.text_9.setMaximumSize(QSize(16777215, 30))
        self.text_9.setFont(font3)
        self.text_9.setStyleSheet(u"border:none;")
        self.text_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.text_9, 2, 0, 1, 3)

        self.label_4.raise_()
        self.text_10.raise_()
        self.agv_net_durumu.raise_()
        self.text_9.raise_()

        self.horizontalLayout.addWidget(self.frame)


        self.verticalLayout_7.addWidget(self.frame_ust)

        self.frame_log = QFrame(self.ANASAYFA)
        self.frame_log.setObjectName(u"frame_log")
        self.frame_log.setFrameShape(QFrame.StyledPanel)
        self.frame_log.setFrameShadow(QFrame.Raised)
        self.bildiri_ekrani = QListWidget(self.frame_log)
        self.bildiri_ekrani.setObjectName(u"bildiri_ekrani")
        self.bildiri_ekrani.setGeometry(QRect(10, 10, 700, 241))
        sizePolicy.setHeightForWidth(self.bildiri_ekrani.sizePolicy().hasHeightForWidth())
        self.bildiri_ekrani.setSizePolicy(sizePolicy)
        self.bildiri_ekrani.setMinimumSize(QSize(700, 200))
        self.bildiri_ekrani.setMaximumSize(QSize(700, 700))
        self.bildiri_ekrani.setStyleSheet(u"border-radius:15px;\n"
"background-color: rgb(230, 230, 230);\n"
"border: 5px solid  rgb(0, 120, 10);\n"
"")

        self.verticalLayout_7.addWidget(self.frame_log)

        icon1 = QIcon()
        icon1.addFile(u":/images/icons/homepage.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidgetEtiketOzellikleri.addTab(self.ANASAYFA, icon1, "")
        self.KONTROL = QWidget()
        self.KONTROL.setObjectName(u"KONTROL")
        self.gridLayout_3 = QGridLayout(self.KONTROL)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame_2 = QFrame(self.KONTROL)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.widget = QWidget(self.frame_2)
        self.widget.setObjectName(u"widget")
        font4 = QFont()
        font4.setFamilies([u"Sans"])
        font4.setBold(True)
        self.widget.setFont(font4)
        self.gridLayout_19 = QGridLayout(self.widget)
        self.gridLayout_19.setObjectName(u"gridLayout_19")

        self.gridLayout_4.addWidget(self.widget, 0, 1, 1, 1)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.buton_ileri = QPushButton(self.frame_2)
        self.buton_ileri.setObjectName(u"buton_ileri")
        self.buton_ileri.setMinimumSize(QSize(0, 50))
        self.buton_ileri.setMaximumSize(QSize(16777215, 50))
        font5 = QFont()
        font5.setFamilies([u"Sans Serif"])
        font5.setPointSize(10)
        font5.setBold(True)
        self.buton_ileri.setFont(font5)
        self.buton_ileri.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(85, 170, 255);\n"
"	color: rgb(0, 0, 0);\n"
"	border: 3px solid;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton::hover\n"
"{\n"
"	background-color: rgb(0, 255, 0);\n"
"}\n"
"QPushButton::checked\n"
"{\n"
"	background-color: rgb(0, 255, 0);\n"
"}")
        self.buton_ileri.setCheckable(False)

        self.gridLayout_5.addWidget(self.buton_ileri, 1, 1, 1, 1)

        self.buton_geri = QPushButton(self.frame_2)
        self.buton_geri.setObjectName(u"buton_geri")
        self.buton_geri.setMinimumSize(QSize(0, 50))
        self.buton_geri.setMaximumSize(QSize(16777215, 50))
        self.buton_geri.setFont(font5)
        self.buton_geri.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(85, 170, 255);\n"
"	color: rgb(0, 0, 0);\n"
"	border: 3px solid;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton::hover\n"
"{\n"
"	background-color: rgb(0, 255, 0);\n"
"}\n"
"QPushButton::checked\n"
"{\n"
"	background-color: rgb(0, 255, 0);\n"
"}")
        self.buton_geri.setCheckable(False)

        self.gridLayout_5.addWidget(self.buton_geri, 3, 1, 1, 1)

        self.buton_dur = QPushButton(self.frame_2)
        self.buton_dur.setObjectName(u"buton_dur")
        self.buton_dur.setMinimumSize(QSize(0, 50))
        self.buton_dur.setMaximumSize(QSize(16777215, 50))
        self.buton_dur.setFont(font5)
        self.buton_dur.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 0, 0);\n"
"	color: rgb(0, 0, 0);\n"
"	border: 3px solid;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton::hover\n"
"{\n"
"	background-color: rgb(0, 255, 0);\n"
"}")
        self.buton_dur.setCheckable(True)

        self.gridLayout_5.addWidget(self.buton_dur, 2, 1, 1, 1)

        self.buton_sol = QPushButton(self.frame_2)
        self.buton_sol.setObjectName(u"buton_sol")
        self.buton_sol.setMinimumSize(QSize(0, 50))
        self.buton_sol.setMaximumSize(QSize(16777215, 50))
        self.buton_sol.setFont(font5)
        self.buton_sol.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(85, 170, 255);\n"
"	color: rgb(0, 0, 0);\n"
"	border: 3px solid;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton::hover\n"
"{\n"
"	background-color: rgb(0, 255, 0);\n"
"}\n"
"QPushButton::checked\n"
"{\n"
"	background-color: rgb(0, 255, 0);\n"
"}")
        self.buton_sol.setCheckable(False)

        self.gridLayout_5.addWidget(self.buton_sol, 2, 0, 1, 1)

        self.buton_sag = QPushButton(self.frame_2)
        self.buton_sag.setObjectName(u"buton_sag")
        self.buton_sag.setMinimumSize(QSize(0, 50))
        self.buton_sag.setMaximumSize(QSize(16777215, 50))
        self.buton_sag.setFont(font5)
        self.buton_sag.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(85, 170, 255);\n"
"	color: rgb(0, 0, 0);\n"
"	border: 3px solid;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton::hover\n"
"{\n"
"	background-color: rgb(0, 255, 0);\n"
"}\n"
"QPushButton::checked\n"
"{\n"
"	background-color: rgb(0, 255, 0);\n"
"}")
        self.buton_sag.setCheckable(False)

        self.gridLayout_5.addWidget(self.buton_sag, 2, 2, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_5, 8, 1, 1, 1)

        self.text_2 = QLabel(self.frame_2)
        self.text_2.setObjectName(u"text_2")
        self.text_2.setMinimumSize(QSize(0, 38))
        self.text_2.setMaximumSize(QSize(16777215, 38))
        font6 = QFont()
        font6.setFamilies([u"Ubuntu"])
        font6.setPointSize(14)
        font6.setBold(True)
        self.text_2.setFont(font6)
        self.text_2.setStyleSheet(u"QLabel{\n"
"background-color: rgb(0, 120, 10);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 3px solid;\n"
"	border-radius: 10px ;\n"
"}")
        self.text_2.setScaledContents(True)
        self.text_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.text_2, 6, 1, 1, 1)

        self.tabWidget = QTabWidget(self.frame_2)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setFont(font5)
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.gridLayout_24 = QGridLayout(self.tab_1)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.linear_info = QLineEdit(self.tab_1)
        self.linear_info.setObjectName(u"linear_info")

        self.gridLayout_24.addWidget(self.linear_info, 0, 1, 1, 1)

        self.donus_aci_info = QLineEdit(self.tab_1)
        self.donus_aci_info.setObjectName(u"donus_aci_info")

        self.gridLayout_24.addWidget(self.donus_aci_info, 4, 1, 1, 1)

        self.position_y = QLabel(self.tab_1)
        self.position_y.setObjectName(u"position_y")
        font7 = QFont()
        font7.setFamilies([u"Sans Serif"])
        font7.setBold(True)
        font7.setItalic(False)
        self.position_y.setFont(font7)

        self.gridLayout_24.addWidget(self.position_y, 3, 0, 1, 1)

        self.y_info = QLineEdit(self.tab_1)
        self.y_info.setObjectName(u"y_info")

        self.gridLayout_24.addWidget(self.y_info, 3, 1, 1, 1)

        self.x_info = QLineEdit(self.tab_1)
        self.x_info.setObjectName(u"x_info")

        self.gridLayout_24.addWidget(self.x_info, 2, 1, 1, 1)

        self.rotation_angle = QLabel(self.tab_1)
        self.rotation_angle.setObjectName(u"rotation_angle")
        self.rotation_angle.setFont(font7)

        self.gridLayout_24.addWidget(self.rotation_angle, 4, 0, 1, 1)

        self.angular_vel = QLabel(self.tab_1)
        self.angular_vel.setObjectName(u"angular_vel")
        self.angular_vel.setFont(font7)

        self.gridLayout_24.addWidget(self.angular_vel, 1, 0, 1, 1)

        self.acisal_hiz_info = QLineEdit(self.tab_1)
        self.acisal_hiz_info.setObjectName(u"acisal_hiz_info")

        self.gridLayout_24.addWidget(self.acisal_hiz_info, 1, 1, 1, 1)

        self.linear_vel = QLabel(self.tab_1)
        self.linear_vel.setObjectName(u"linear_vel")
        self.linear_vel.setFont(font7)

        self.gridLayout_24.addWidget(self.linear_vel, 0, 0, 1, 1)

        self.position_x = QLabel(self.tab_1)
        self.position_x.setObjectName(u"position_x")
        self.position_x.setFont(font7)

        self.gridLayout_24.addWidget(self.position_x, 2, 0, 1, 1)

        self.sarj_durumu = QLabel(self.tab_1)
        self.sarj_durumu.setObjectName(u"sarj_durumu")
        font8 = QFont()
        font8.setFamilies([u"Sans"])
        font8.setPointSize(11)
        font8.setBold(True)
        font8.setItalic(False)
        self.sarj_durumu.setFont(font8)

        self.gridLayout_24.addWidget(self.sarj_durumu, 5, 0, 1, 1)

        self.sarj_info = QLineEdit(self.tab_1)
        self.sarj_info.setObjectName(u"sarj_info")

        self.gridLayout_24.addWidget(self.sarj_info, 5, 1, 1, 1)

        self.tabWidget.addTab(self.tab_1, "")

        self.gridLayout_4.addWidget(self.tabWidget, 3, 1, 1, 1)


        self.gridLayout_3.addWidget(self.frame_2, 1, 0, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.camera_info = QLabel(self.KONTROL)
        self.camera_info.setObjectName(u"camera_info")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.camera_info.sizePolicy().hasHeightForWidth())
        self.camera_info.setSizePolicy(sizePolicy2)
        self.camera_info.setMinimumSize(QSize(300, 300))
        self.camera_info.setMaximumSize(QSize(500, 405))
        self.camera_info.setFrameShape(QFrame.Box)
        self.camera_info.setScaledContents(True)
        self.camera_info.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.camera_info)

        self.camera_button = QPushButton(self.KONTROL)
        self.camera_button.setObjectName(u"camera_button")
        self.camera_button.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0, 120, 10);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 5px solid;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton::hover\n"
"{\n"
"	background-color: rgb(0, 255, 0);\n"
"	border-color: rgb(255, 0, 0);\n"
"\n"
"}")

        self.verticalLayout_3.addWidget(self.camera_button)

        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.butonKapat_5 = QPushButton(self.KONTROL)
        self.butonKapat_5.setObjectName(u"butonKapat_5")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.butonKapat_5.sizePolicy().hasHeightForWidth())
        self.butonKapat_5.setSizePolicy(sizePolicy3)
        self.butonKapat_5.setMinimumSize(QSize(0, 50))
        self.butonKapat_5.setMaximumSize(QSize(120, 16777215))
        font9 = QFont()
        font9.setPointSize(13)
        font9.setBold(True)
        self.butonKapat_5.setFont(font9)
        self.butonKapat_5.setStyleSheet(u"QPushButton{\n"
"    qproperty-icon: url(:/images/icons/close_icon.png);\n"
"\n"
"	background-color: rgb(255, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 5px solid;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton::hover\n"
"{\n"
"	background-color: rgb(0, 255, 0);\n"
"	border-color: rgb(255, 0, 0);\n"
"\n"
"}")
        self.butonKapat_5.setIconSize(QSize(30, 30))

        self.gridLayout_8.addWidget(self.butonKapat_5, 1, 1, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_12, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_8.addItem(self.verticalSpacer, 0, 0, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_8)


        self.gridLayout_3.addLayout(self.verticalLayout_3, 1, 1, 1, 1)

        icon2 = QIcon()
        icon2.addFile(u":/images/icons/agv_icons.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidgetEtiketOzellikleri.addTab(self.KONTROL, icon2, "")
        self.ISTASYON = QWidget()
        self.ISTASYON.setObjectName(u"ISTASYON")
        self.gridLayout_10 = QGridLayout(self.ISTASYON)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.text_8 = QLabel(self.ISTASYON)
        self.text_8.setObjectName(u"text_8")
        font10 = QFont()
        font10.setFamilies([u"Sans"])
        font10.setPointSize(20)
        font10.setBold(True)
        font10.setItalic(False)
        self.text_8.setFont(font10)
        self.text_8.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.text_8, 0, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.text_3 = QLabel(self.ISTASYON)
        self.text_3.setObjectName(u"text_3")
        self.text_3.setMinimumSize(QSize(0, 50))
        font11 = QFont()
        font11.setPointSize(10)
        font11.setBold(True)
        self.text_3.setFont(font11)
        self.text_3.setStyleSheet(u"border: 3px solid  rgb(0, 120, 10);\n"
"border-radius: 10px;\n"
"border-radius:15px;\n"
"background-color: rgb(230, 230, 230);\n"
"")
        self.text_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.text_3)

        self.durak_info = QTableWidget(self.ISTASYON)
        if (self.durak_info.columnCount() < 5):
            self.durak_info.setColumnCount(5)
        font12 = QFont()
        font12.setFamilies([u"Ubuntu"])
        font12.setPointSize(9)
        font12.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font12);
        self.durak_info.setHorizontalHeaderItem(0, __qtablewidgetitem)
        font13 = QFont()
        font13.setPointSize(9)
        font13.setBold(True)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font13);
        self.durak_info.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font13);
        self.durak_info.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font13);
        self.durak_info.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font13);
        self.durak_info.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.durak_info.setObjectName(u"durak_info")
        self.durak_info.setMinimumSize(QSize(0, 20))
        font14 = QFont()
        font14.setPointSize(10)
        self.durak_info.setFont(font14)
        self.durak_info.setStyleSheet(u"background-color: rgb(230, 230, 230);\n"
"border: 1px solid  rgb(0, 120, 10);\n"
"")
        self.durak_info.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.durak_info.setSortingEnabled(True)
        self.durak_info.horizontalHeader().setDefaultSectionSize(100)

        self.verticalLayout_9.addWidget(self.durak_info)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.kalan_durak = QLabel(self.ISTASYON)
        self.kalan_durak.setObjectName(u"kalan_durak")
        self.kalan_durak.setMinimumSize(QSize(100, 0))
        font15 = QFont()
        font15.setPointSize(14)
        font15.setBold(True)
        self.kalan_durak.setFont(font15)
        self.kalan_durak.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 3px solid;\n"
"border-color: rgb(0, 0, 0);\n"
"border-radius: 10px;\n"
"")
        self.kalan_durak.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.kalan_durak)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_9)

        self.durak_liste_yenile = QPushButton(self.ISTASYON)
        self.durak_liste_yenile.setObjectName(u"durak_liste_yenile")
        self.durak_liste_yenile.setMinimumSize(QSize(180, 50))
        font16 = QFont()
        font16.setFamilies([u"Sans Serif"])
        font16.setPointSize(11)
        font16.setBold(True)
        self.durak_liste_yenile.setFont(font16)
        self.durak_liste_yenile.setStyleSheet(u"QPushButton{\n"
"	qproperty-icon: url(:/images/icons/refresh_icon.png);\n"
"    background-color: rgb(0, 120, 10);\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"	border: 3px solid;\n"
"	border-color: rgb(0, 0, 0);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton::hover\n"
"{\n"
"	background-color: rgb(0, 255, 0);\n"
"	border-color: rgb(255, 0, 0);\n"
"\n"
"}")
        self.durak_liste_yenile.setIconSize(QSize(30, 30))

        self.horizontalLayout_3.addWidget(self.durak_liste_yenile)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_10)


        self.verticalLayout_9.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_4.addLayout(self.verticalLayout_9)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.durak_info_2 = QLabel(self.ISTASYON)
        self.durak_info_2.setObjectName(u"durak_info_2")
        self.durak_info_2.setMinimumSize(QSize(0, 50))
        self.durak_info_2.setToolTipDuration(-3)
        self.durak_info_2.setTextFormat(Qt.AutoText)
        self.durak_info_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.durak_info_2)

        self.frame_7 = QFrame(self.ISTASYON)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"border: 3px solid  rgb(0, 120, 10);\n"
"border-radius: 10px;\n"
"background-color: rgb(230, 230, 230);\n"
"")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_12 = QGridLayout(self.frame_7)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.durak_adi = QLineEdit(self.frame_7)
        self.durak_adi.setObjectName(u"durak_adi")
        self.durak_adi.setMinimumSize(QSize(0, 22))
        self.durak_adi.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 2px solid;\n"
"border-color: rgb(0, 0, 0);\n"
"border-radius: 10px;\n"
"")

        self.gridLayout_12.addWidget(self.durak_adi, 11, 1, 1, 2)

        self.text_6 = QLabel(self.frame_7)
        self.text_6.setObjectName(u"text_6")
        self.text_6.setFont(font11)
        self.text_6.setStyleSheet(u"border : none;")
        self.text_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_12.addWidget(self.text_6, 12, 0, 1, 1)

        self.text_4 = QLabel(self.frame_7)
        self.text_4.setObjectName(u"text_4")
        self.text_4.setMinimumSize(QSize(0, 38))
        self.text_4.setFont(font11)
        self.text_4.setLayoutDirection(Qt.LeftToRight)
        self.text_4.setStyleSheet(u"border: none ;")
        self.text_4.setScaledContents(False)
        self.text_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_12.addWidget(self.text_4, 2, 0, 1, 1)

        self.mevcut_durak = QLabel(self.frame_7)
        self.mevcut_durak.setObjectName(u"mevcut_durak")
        self.mevcut_durak.setMinimumSize(QSize(0, 22))
        self.mevcut_durak.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 2px solid;\n"
"border-color: rgb(0, 0, 0);\n"
"border-radius: 10px;")
        self.mevcut_durak.setAlignment(Qt.AlignCenter)
        self.mevcut_durak.setWordWrap(True)

        self.gridLayout_12.addWidget(self.mevcut_durak, 2, 1, 1, 2)

        self.durak_notu = QLineEdit(self.frame_7)
        self.durak_notu.setObjectName(u"durak_notu")
        self.durak_notu.setMinimumSize(QSize(0, 22))
        self.durak_notu.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 2px solid;\n"
"border-color: rgb(0, 0, 0);\n"
"border-radius: 10px;\n"
"")

        self.gridLayout_12.addWidget(self.durak_notu, 12, 1, 1, 2)

        self.durak_kayit = QPushButton(self.frame_7)
        self.durak_kayit.setObjectName(u"durak_kayit")
        self.durak_kayit.setMinimumSize(QSize(180, 30))
        font17 = QFont()
        font17.setPointSize(11)
        font17.setBold(True)
        self.durak_kayit.setFont(font17)
        self.durak_kayit.setStyleSheet(u"QPushButton{\n"
"	qproperty-icon: url(:/images/icons/save-icon.png);\n"
"    background-color: rgb(0, 120, 10);\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid;\n"
"	border-color: rgb(0, 0, 0);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton::hover\n"
"{\n"
"	background-color: rgb(0, 255, 0);\n"
"	border-color: rgb(255, 0, 0);\n"
"\n"
"}")
        self.durak_kayit.setIconSize(QSize(30, 30))

        self.gridLayout_12.addWidget(self.durak_kayit, 13, 1, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_12.addItem(self.verticalSpacer_7, 9, 1, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_6, 13, 2, 1, 1)

        self.text_5 = QLabel(self.frame_7)
        self.text_5.setObjectName(u"text_5")
        self.text_5.setFont(font11)
        self.text_5.setStyleSheet(u"border : none;")
        self.text_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_12.addWidget(self.text_5, 10, 0, 2, 1)


        self.verticalLayout_10.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.ISTASYON)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"background-color: rgb(230, 230, 230);\n"
"border: 3px solid  rgb(0, 120, 10);\n"
"border-radius: 10px;\n"
"")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_13 = QGridLayout(self.frame_8)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_8, 7, 0, 1, 1)

        self.text_7 = QLabel(self.frame_8)
        self.text_7.setObjectName(u"text_7")
        self.text_7.setMinimumSize(QSize(0, 50))
        font18 = QFont()
        font18.setPointSize(10)
        font18.setBold(True)
        font18.setItalic(False)
        self.text_7.setFont(font18)
        self.text_7.setStyleSheet(u"border: none;")
        self.text_7.setAlignment(Qt.AlignCenter)

        self.gridLayout_13.addWidget(self.text_7, 1, 1, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_7, 7, 2, 1, 1)

        self.durak_sil = QPushButton(self.frame_8)
        self.durak_sil.setObjectName(u"durak_sil")
        self.durak_sil.setMinimumSize(QSize(180, 50))
        self.durak_sil.setFont(font17)
        self.durak_sil.setStyleSheet(u"QPushButton{\n"
"	qproperty-icon: url(:/images/icons/delete.png);\n"
"    background-color: rgb(0, 120, 10);\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"	border: 3px solid;\n"
"	border-color: rgb(0, 0, 0);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton::hover\n"
"{\n"
"	background-color: rgb(0, 255, 0);\n"
"	border-color: rgb(255, 0, 0);\n"
"\n"
"}")
        self.durak_sil.setIconSize(QSize(30, 30))

        self.gridLayout_13.addWidget(self.durak_sil, 7, 1, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_13.addItem(self.verticalSpacer_8, 6, 1, 1, 1)

        self.sil_durak_sec = QComboBox(self.frame_8)
        self.sil_durak_sec.setObjectName(u"sil_durak_sec")
        self.sil_durak_sec.setMinimumSize(QSize(0, 30))
        self.sil_durak_sec.setFont(font17)
        self.sil_durak_sec.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 3px solid;\n"
"border-color: rgb(0, 0, 0);\n"
"border-radius: 10px;\n"
"")

        self.gridLayout_13.addWidget(self.sil_durak_sec, 2, 0, 1, 3)


        self.verticalLayout_10.addWidget(self.frame_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_11)


        self.verticalLayout_10.addLayout(self.horizontalLayout_9)


        self.horizontalLayout_4.addLayout(self.verticalLayout_10)


        self.gridLayout_10.addLayout(self.horizontalLayout_4, 2, 0, 1, 1)

        icon3 = QIcon()
        icon3.addFile(u":/images/icons/data.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidgetEtiketOzellikleri.addTab(self.ISTASYON, icon3, "")

        self.horizontalLayout_11.addWidget(self.tabWidgetEtiketOzellikleri)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidgetEtiketOzellikleri.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"RobDou-ANA PENCERE", None))
        self.text_10.setText(QCoreApplication.translate("MainWindow", u"AGV 1", None))
        self.agv_net_durumu.setText(QCoreApplication.translate("MainWindow", u"ONLINE", None))
        self.label_4.setText("")
        self.text_9.setText(QCoreApplication.translate("MainWindow", u"CONNECTION STATUS", None))
        self.tabWidgetEtiketOzellikleri.setTabText(self.tabWidgetEtiketOzellikleri.indexOf(self.ANASAYFA), QCoreApplication.translate("MainWindow", u"HOME PAGE", None))
        self.buton_ileri.setText(QCoreApplication.translate("MainWindow", u"FORWARD", None))
        self.buton_geri.setText(QCoreApplication.translate("MainWindow", u"BACK", None))
        self.buton_dur.setText(QCoreApplication.translate("MainWindow", u"STOP", None))
        self.buton_sol.setText(QCoreApplication.translate("MainWindow", u"LEFT", None))
        self.buton_sag.setText(QCoreApplication.translate("MainWindow", u"RIGHT", None))
        self.text_2.setText(QCoreApplication.translate("MainWindow", u"ROBOT CONTROL", None))
        self.linear_info.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.donus_aci_info.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.position_y.setText(QCoreApplication.translate("MainWindow", u"Position Y(m):", None))
        self.y_info.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.x_info.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.rotation_angle.setText(QCoreApplication.translate("MainWindow", u"Rotation AngleX:", None))
        self.angular_vel.setText(QCoreApplication.translate("MainWindow", u"Angular Velocity(rad/s):", None))
        self.acisal_hiz_info.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.linear_vel.setText(QCoreApplication.translate("MainWindow", u"Linear Velocity(m/s):", None))
        self.position_x.setText(QCoreApplication.translate("MainWindow", u"Position X(m):", None))
        self.sarj_durumu.setText(QCoreApplication.translate("MainWindow", u"State of Charge:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), QCoreApplication.translate("MainWindow", u"AGV", None))
        self.camera_info.setText("")
        self.camera_button.setText(QCoreApplication.translate("MainWindow", u"OPEN  THE CAMERA", None))
        self.butonKapat_5.setText(QCoreApplication.translate("MainWindow", u"CLOSE", None))
        self.tabWidgetEtiketOzellikleri.setTabText(self.tabWidgetEtiketOzellikleri.indexOf(self.KONTROL), QCoreApplication.translate("MainWindow", u"CONTROL", None))
        self.text_8.setText(QCoreApplication.translate("MainWindow", u"VEHICLE STATION TRACKING", None))
        self.text_3.setText(QCoreApplication.translate("MainWindow", u"STATION LIST", None))
        ___qtablewidgetitem = self.durak_info.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"STATION NAME", None));
        ___qtablewidgetitem1 = self.durak_info.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"POSITION X", None));
        ___qtablewidgetitem2 = self.durak_info.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"POSITION Y", None));
        ___qtablewidgetitem3 = self.durak_info.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"POSITION Z", None));
        ___qtablewidgetitem4 = self.durak_info.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"NOTE", None));
        self.kalan_durak.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.durak_liste_yenile.setText(QCoreApplication.translate("MainWindow", u"REFRESH LIST", None))
        self.durak_info_2.setText(QCoreApplication.translate("MainWindow", u"No error", None))
        self.text_6.setText(QCoreApplication.translate("MainWindow", u"STATION NOTE:", None))
        self.text_4.setText(QCoreApplication.translate("MainWindow", u"CURRENT LOCATION AGV 1 :", None))
        self.mevcut_durak.setText("")
        self.durak_kayit.setText(QCoreApplication.translate("MainWindow", u"SAVE STATION", None))
        self.text_5.setText(QCoreApplication.translate("MainWindow", u"STATION NAME", None))
        self.text_7.setText(QCoreApplication.translate("MainWindow", u"DELETE STATION", None))
        self.durak_sil.setText(QCoreApplication.translate("MainWindow", u"DELETE STATION", None))
        self.tabWidgetEtiketOzellikleri.setTabText(self.tabWidgetEtiketOzellikleri.indexOf(self.ISTASYON), QCoreApplication.translate("MainWindow", u"STATION", None))
    # retranslateUi

