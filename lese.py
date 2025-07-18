# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lese.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QGridLayout, QGroupBox,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(968, 767)
        MainWindow.setStyleSheet(u"background-image: url(./picture/1.png);\n"
"\n"
" ")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(220, 30, 481, 31))
        font = QFont()
        font.setFamilies([u"Microsoft Sans Serif"])
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.showlabel = QLabel(self.centralwidget)
        self.showlabel.setObjectName(u"showlabel")
        self.showlabel.setGeometry(QRect(100, 80, 411, 381))
        self.showlabel.setStyleSheet(u"background-image: url(./picture/2.png);\n"
" background-size: cover;      \n"
"   background-position: center; \n"
"")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(590, 70, 341, 181))
        self.formLayoutWidget = QWidget(self.groupBox)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(20, 20, 291, 150))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout.setItem(2, QFormLayout.ItemRole.LabelRole, self.verticalSpacer_2)

        self.video = QPushButton(self.formLayoutWidget)
        self.video.setObjectName(u"video")
        icon = QIcon()
        icon.addFile(u"picture/wen.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.video.setIcon(icon)

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.video)

        self.videoedit = QLineEdit(self.formLayoutWidget)
        self.videoedit.setObjectName(u"videoedit")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.videoedit)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout.setItem(4, QFormLayout.ItemRole.LabelRole, self.verticalSpacer)

        self.cameraedit = QLineEdit(self.formLayoutWidget)
        self.cameraedit.setObjectName(u"cameraedit")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.cameraedit)

        self.horizontalSpacer = QSpacerItem(3, 3, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.formLayout.setItem(0, QFormLayout.ItemRole.FieldRole, self.horizontalSpacer)

        self.photoedit = QLineEdit(self.formLayoutWidget)
        self.photoedit.setObjectName(u"photoedit")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.photoedit)

        self.camera = QPushButton(self.formLayoutWidget)
        self.camera.setObjectName(u"camera")
        icon1 = QIcon()
        icon1.addFile(u"picture/favicon.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.camera.setIcon(icon1)

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.camera)

        self.photo = QPushButton(self.formLayoutWidget)
        self.photo.setObjectName(u"photo")
        icon2 = QIcon()
        icon2.addFile(u"picture/pic.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.photo.setIcon(icon2)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.photo)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(590, 260, 351, 241))
        self.groupBox_2.setStyleSheet(u"font: 9pt \"Microsoft New Tai Lue\";")
        self.gridLayoutWidget = QWidget(self.groupBox_2)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(30, 30, 281, 108))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.numlabel = QLabel(self.gridLayoutWidget)
        self.numlabel.setObjectName(u"numlabel")

        self.gridLayout.addWidget(self.numlabel, 0, 4, 1, 1)

        self.x1 = QLabel(self.gridLayoutWidget)
        self.x1.setObjectName(u"x1")

        self.gridLayout.addWidget(self.x1, 2, 1, 1, 1)

        self.timelabel = QLabel(self.gridLayoutWidget)
        self.timelabel.setObjectName(u"timelabel")

        self.gridLayout.addWidget(self.timelabel, 0, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_4, 1, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_3, 1, 0, 1, 1)

        self.time = QLabel(self.gridLayoutWidget)
        self.time.setObjectName(u"time")
        self.time.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.time, 0, 0, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.y1 = QLabel(self.gridLayoutWidget)
        self.y1.setObjectName(u"y1")

        self.gridLayout.addWidget(self.y1, 3, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(10, 10, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 0, 3, 1, 1)

        self.label_6 = QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 3, 1, 1)

        self.x2 = QLabel(self.gridLayoutWidget)
        self.x2.setObjectName(u"x2")

        self.gridLayout.addWidget(self.x2, 2, 4, 1, 1)

        self.label_7 = QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 3, 3, 1, 1)

        self.y2 = QLabel(self.gridLayoutWidget)
        self.y2.setObjectName(u"y2")

        self.gridLayout.addWidget(self.y2, 3, 4, 1, 1)

        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 160, 54, 16))
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.conflabel = QLabel(self.groupBox_2)
        self.conflabel.setObjectName(u"conflabel")
        self.conflabel.setGeometry(QRect(90, 160, 61, 16))
        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(30, 190, 54, 16))
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.idname = QLabel(self.groupBox_2)
        self.idname.setObjectName(u"idname")
        self.idname.setGeometry(QRect(100, 190, 111, 16))
        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(590, 520, 351, 121))
        self.save = QPushButton(self.groupBox_3)
        self.save.setObjectName(u"save")
        self.save.setGeometry(QRect(40, 40, 101, 41))
        icon3 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentSave))
        self.save.setIcon(icon3)
        self.save.setIconSize(QSize(20, 20))
        self.exit = QPushButton(self.groupBox_3)
        self.exit.setObjectName(u"exit")
        self.exit.setGeometry(QRect(200, 40, 111, 41))
        icon4 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ApplicationExit))
        self.exit.setIcon(icon4)
        self.groupBox_4 = QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(90, 490, 481, 181))
        self.response = QTextEdit(self.groupBox_4)
        self.response.setObjectName(u"response")
        self.response.setGeometry(QRect(30, 20, 421, 111))
        self.question = QLineEdit(self.groupBox_4)
        self.question.setObjectName(u"question")
        self.question.setGeometry(QRect(30, 140, 421, 31))
        self.clear = QPushButton(self.centralwidget)
        self.clear.setObjectName(u"clear")
        self.clear.setGeometry(QRect(710, 23, 121, 41))
        self.ai = QPushButton(self.centralwidget)
        self.ai.setObjectName(u"ai")
        self.ai.setGeometry(QRect(10, 540, 75, 111))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 968, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u5783\u573e\u5206\u7c7b\u7cfb\u7edf", None))
        self.showlabel.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u64cd\u4f5c", None))
        self.video.setText("")
        self.camera.setText("")
        self.photo.setText("")
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u68c0\u6d4b\u7ed3\u679c", None))
        self.numlabel.setText("")
        self.x1.setText(QCoreApplication.translate("MainWindow", u"\u3001", None))
        self.timelabel.setText("")
        self.time.setText(QCoreApplication.translate("MainWindow", u"\u7528\u65f6\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"ymin", None))
        self.y1.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u76ee\u6807\u6570\u76ee\uff1a", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"xmin\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"xmax", None))
        self.x2.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"ymax", None))
        self.y2.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u7f6e\u4fe1\u5ea6\uff1a", None))
        self.conflabel.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u79cd\u7c7b\uff1a", None))
        self.idname.setText("")
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u4e0e\u9000\u51fa", None))
        self.save.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.exit.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"\u4eba\u673a\u4fe1\u606f", None))
        self.clear.setText(QCoreApplication.translate("MainWindow", u"clear", None))
        self.ai.setText(QCoreApplication.translate("MainWindow", u"\u4eba\u673a", None))
    # retranslateUi

