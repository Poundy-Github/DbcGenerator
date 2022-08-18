# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DbcGenBaseWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(960, 385)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(11, 11, 581, 35))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_7)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        font = QFont()
        font.setFamilies([u"MS Reference Sans Serif"])
        font.setPointSize(20)
        self.label_5.setFont(font)

        self.horizontalLayout.addWidget(self.label_5)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_8)

        self.widget1 = QWidget(Dialog)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(11, 52, 581, 26))
        self.horizontalLayout_2 = QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.matrix_choose = QPushButton(self.widget1)
        self.matrix_choose.setObjectName(u"matrix_choose")

        self.horizontalLayout_2.addWidget(self.matrix_choose)

        self.matrix_path = QLineEdit(self.widget1)
        self.matrix_path.setObjectName(u"matrix_path")

        self.horizontalLayout_2.addWidget(self.matrix_path)

        self.widget2 = QWidget(Dialog)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(11, 84, 581, 26))
        self.horizontalLayout_3 = QHBoxLayout(self.widget2)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.dbc_demo_choose = QPushButton(self.widget2)
        self.dbc_demo_choose.setObjectName(u"dbc_demo_choose")

        self.horizontalLayout_3.addWidget(self.dbc_demo_choose)

        self.dbc_demo_path = QLineEdit(self.widget2)
        self.dbc_demo_path.setObjectName(u"dbc_demo_path")

        self.horizontalLayout_3.addWidget(self.dbc_demo_path)

        self.widget3 = QWidget(Dialog)
        self.widget3.setObjectName(u"widget3")
        self.widget3.setGeometry(QRect(11, 116, 581, 26))
        self.horizontalLayout_4 = QHBoxLayout(self.widget3)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.matrix_demo_choose = QPushButton(self.widget3)
        self.matrix_demo_choose.setObjectName(u"matrix_demo_choose")

        self.horizontalLayout_4.addWidget(self.matrix_demo_choose)

        self.matrix_demo_path = QLineEdit(self.widget3)
        self.matrix_demo_path.setObjectName(u"matrix_demo_path")

        self.horizontalLayout_4.addWidget(self.matrix_demo_path)

        self.widget4 = QWidget(Dialog)
        self.widget4.setObjectName(u"widget4")
        self.widget4.setGeometry(QRect(11, 148, 581, 23))
        self.horizontalLayout_5 = QHBoxLayout(self.widget4)
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.widget4)
        self.label_4.setObjectName(u"label_4")
        font1 = QFont()
        font1.setPointSize(11)
        self.label_4.setFont(font1)

        self.horizontalLayout_5.addWidget(self.label_4)

        self.comboBox_comSheet = QComboBox(self.widget4)
        self.comboBox_comSheet.setObjectName(u"comboBox_comSheet")

        self.horizontalLayout_5.addWidget(self.comboBox_comSheet)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.label = QLabel(self.widget4)
        self.label.setObjectName(u"label")

        self.horizontalLayout_5.addWidget(self.label)

        self.cur_node_combox = QComboBox(self.widget4)
        self.cur_node_combox.setObjectName(u"cur_node_combox")

        self.horizontalLayout_5.addWidget(self.cur_node_combox)

        self.widget5 = QWidget(Dialog)
        self.widget5.setObjectName(u"widget5")
        self.widget5.setGeometry(QRect(11, 179, 581, 36))
        self.horizontalLayout_6 = QHBoxLayout(self.widget5)
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)

        self.start_generate = QPushButton(self.widget5)
        self.start_generate.setObjectName(u"start_generate")
        font2 = QFont()
        font2.setPointSize(14)
        self.start_generate.setFont(font2)

        self.horizontalLayout_6.addWidget(self.start_generate)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Continental Smart Core Dbc Generator", None))
        self.matrix_choose.setText(QCoreApplication.translate("Dialog", u"Choose source matrix  ", None))
        self.dbc_demo_choose.setText(QCoreApplication.translate("Dialog", u"Choose Dbc Demo", None))
        self.matrix_demo_choose.setText(QCoreApplication.translate("Dialog", u"Choose Matrix Demo", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Com matrix Sheet", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Current network node", None))
        self.start_generate.setText(QCoreApplication.translate("Dialog", u"Start", None))
    # retranslateUi

