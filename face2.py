# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QTabWidget, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(918, 778)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.daka = QTabWidget(self.centralwidget)
        self.daka.setObjectName(u"daka")
        self.daka.setGeometry(QRect(0, 0, 901, 731))
        self.daka.setStyleSheet(u"")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.join = QGroupBox(self.tab)
        self.join.setObjectName(u"join")
        self.join.setGeometry(QRect(20, 120, 281, 471))
        self.join.setStyleSheet(u"")
        self.horizontalLayoutWidget = QWidget(self.join)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(20, 60, 211, 80))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_2.setFont(font)

        self.horizontalLayout.addWidget(self.label_2)

        self.name1 = QLineEdit(self.horizontalLayoutWidget)
        self.name1.setObjectName(u"name1")
        font1 = QFont()
        font1.setPointSize(12)
        self.name1.setFont(font1)

        self.horizontalLayout.addWidget(self.name1)

        self.horizontalLayoutWidget_2 = QWidget(self.join)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(20, 140, 211, 80))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.horizontalLayoutWidget_2)
        self.label_3.setObjectName(u"label_3")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(False)
        self.label_3.setFont(font2)
        self.label_3.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.id1 = QLineEdit(self.horizontalLayoutWidget_2)
        self.id1.setObjectName(u"id1")
        self.id1.setFont(font1)

        self.horizontalLayout_2.addWidget(self.id1)

        self.horizontalLayoutWidget_5 = QWidget(self.join)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(10, 240, 251, 141))
        self.horizontalLayout_5 = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.startbutton = QPushButton(self.horizontalLayoutWidget_5)
        self.startbutton.setObjectName(u"startbutton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startbutton.sizePolicy().hasHeightForWidth())
        self.startbutton.setSizePolicy(sizePolicy)
        self.startbutton.setFont(font1)

        self.horizontalLayout_5.addWidget(self.startbutton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.catchbutton = QPushButton(self.horizontalLayoutWidget_5)
        self.catchbutton.setObjectName(u"catchbutton")
        sizePolicy.setHeightForWidth(self.catchbutton.sizePolicy().hasHeightForWidth())
        self.catchbutton.setSizePolicy(sizePolicy)
        self.catchbutton.setFont(font1)
        self.catchbutton.setAutoRepeat(True)
        self.catchbutton.setAutoExclusive(True)
        self.catchbutton.setAutoDefault(False)
        self.catchbutton.setFlat(False)

        self.horizontalLayout_5.addWidget(self.catchbutton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.trainbutton = QPushButton(self.horizontalLayoutWidget_5)
        self.trainbutton.setObjectName(u"trainbutton")
        sizePolicy.setHeightForWidth(self.trainbutton.sizePolicy().hasHeightForWidth())
        self.trainbutton.setSizePolicy(sizePolicy)
        self.trainbutton.setFont(font1)

        self.horizontalLayout_5.addWidget(self.trainbutton)

        self.close = QPushButton(self.join)
        self.close.setObjectName(u"close")
        self.close.setGeometry(QRect(70, 410, 111, 41))
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(320, 0, 221, 121))
        font3 = QFont()
        font3.setPointSize(20)
        self.label.setFont(font3)
        self.label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label.setStyleSheet(u"background-color:rgb(0, 255, 255)\n"
"")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.showlable = QLabel(self.tab)
        self.showlable.setObjectName(u"showlable")
        self.showlable.setGeometry(QRect(310, 130, 571, 461))
        self.showlable.setStyleSheet(u"background-image: url(./R-C.png);\n"
" background-repeat: no-repeat;\n"
"\n"
" background-size: cover;")
        self.daka.addTab(self.tab, "")
        self.daka_2 = QWidget()
        self.daka_2.setObjectName(u"daka_2")
        self.time = QLabel(self.daka_2)
        self.time.setObjectName(u"time")
        self.time.setGeometry(QRect(80, 10, 201, 111))
        font4 = QFont()
        font4.setPointSize(18)
        self.time.setFont(font4)
        self.time.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.dakalabel = QLabel(self.daka_2)
        self.dakalabel.setObjectName(u"dakalabel")
        self.dakalabel.setGeometry(QRect(390, 20, 471, 711))
        self.dakalabel.setStyleSheet(u"background-image: url(./R-C.png);")
        self.go = QPushButton(self.daka_2)
        self.go.setObjectName(u"go")
        self.go.setGeometry(QRect(120, 510, 151, 51))
        font5 = QFont()
        font5.setPointSize(12)
        font5.setBold(True)
        self.go.setFont(font5)
        self.listWidget = QListWidget(self.daka_2)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(70, 140, 256, 351))
        self.stop = QPushButton(self.daka_2)
        self.stop.setObjectName(u"stop")
        self.stop.setGeometry(QRect(30, 560, 331, 151))
        font6 = QFont()
        font6.setPointSize(16)
        font6.setBold(True)
        self.stop.setFont(font6)
        self.stop.setStyleSheet(u"background-image: url(./r.png);")
        self.daka.addTab(self.daka_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 918, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.daka.setCurrentIndex(0)
        self.catchbutton.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.join.setTitle(QCoreApplication.translate("MainWindow", u"\u4fe1\u606f\u5f55\u5165", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u59d3\u540d\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"id\uff1a", None))
        self.startbutton.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u542f", None))
        self.catchbutton.setText(QCoreApplication.translate("MainWindow", u"\u91c7\u96c6", None))
        self.trainbutton.setText(QCoreApplication.translate("MainWindow", u"\u8bad\u7ec3", None))
        self.close.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u725b\u9a6c\u6253\u5361\u4e0a\u73ed", None))
        self.showlable.setText("")
        self.daka.setTabText(self.daka.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u5f55\u5165", None))
        self.time.setText("")
        self.dakalabel.setText("")
        self.go.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5361", None))
        self.stop.setText(QCoreApplication.translate("MainWindow", u"\u725b\u9a6c\u62d2\u7edd\u6253\u5361", None))
        self.daka.setTabText(self.daka.indexOf(self.daka_2), QCoreApplication.translate("MainWindow", u"\u6253\u5361", None))
    # retranslateUi

