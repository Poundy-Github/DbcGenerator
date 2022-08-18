/********************************************************************************
** Form generated from reading UI file 'DbcGen.ui'
**
** Created by: Qt User Interface Compiler version 5.15.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef DBCGEN_H
#define DBCGEN_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QDialog>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_Dialog
{
public:
    QComboBox *comboBox_comSheet;
    QWidget *horizontalLayoutWidget;
    QHBoxLayout *horizontalLayout;
    QLabel *label;
    QLineEdit *matrix_path;
    QPushButton *matrix_choose;
    QWidget *horizontalLayoutWidget_2;
    QHBoxLayout *horizontalLayout_2;
    QLabel *label_2;
    QLineEdit *dbc_dem_path;
    QPushButton *matrix_choose_2;
    QWidget *horizontalLayoutWidget_3;
    QHBoxLayout *horizontalLayout_3;
    QLabel *label_3;
    QLineEdit *matrix_demo_path;
    QPushButton *matrix_choose_3;
    QLabel *label_4;
    QLabel *label_5;

    void setupUi(QDialog *Dialog)
    {
        if (Dialog->objectName().isEmpty())
            Dialog->setObjectName(QString::fromUtf8("Dialog"));
        Dialog->resize(748, 309);
        comboBox_comSheet = new QComboBox(Dialog);
        comboBox_comSheet->setObjectName(QString::fromUtf8("comboBox_comSheet"));
        comboBox_comSheet->setGeometry(QRect(170, 240, 101, 22));
        horizontalLayoutWidget = new QWidget(Dialog);
        horizontalLayoutWidget->setObjectName(QString::fromUtf8("horizontalLayoutWidget"));
        horizontalLayoutWidget->setGeometry(QRect(10, 70, 701, 51));
        horizontalLayout = new QHBoxLayout(horizontalLayoutWidget);
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        horizontalLayout->setContentsMargins(0, 0, 0, 0);
        label = new QLabel(horizontalLayoutWidget);
        label->setObjectName(QString::fromUtf8("label"));
        QFont font;
        font.setPointSize(14);
        label->setFont(font);

        horizontalLayout->addWidget(label);

        matrix_path = new QLineEdit(horizontalLayoutWidget);
        matrix_path->setObjectName(QString::fromUtf8("matrix_path"));

        horizontalLayout->addWidget(matrix_path);

        matrix_choose = new QPushButton(horizontalLayoutWidget);
        matrix_choose->setObjectName(QString::fromUtf8("matrix_choose"));

        horizontalLayout->addWidget(matrix_choose);

        horizontalLayoutWidget_2 = new QWidget(Dialog);
        horizontalLayoutWidget_2->setObjectName(QString::fromUtf8("horizontalLayoutWidget_2"));
        horizontalLayoutWidget_2->setGeometry(QRect(10, 120, 701, 51));
        horizontalLayout_2 = new QHBoxLayout(horizontalLayoutWidget_2);
        horizontalLayout_2->setObjectName(QString::fromUtf8("horizontalLayout_2"));
        horizontalLayout_2->setContentsMargins(0, 0, 0, 0);
        label_2 = new QLabel(horizontalLayoutWidget_2);
        label_2->setObjectName(QString::fromUtf8("label_2"));
        label_2->setFont(font);

        horizontalLayout_2->addWidget(label_2);

        dbc_dem_path = new QLineEdit(horizontalLayoutWidget_2);
        dbc_dem_path->setObjectName(QString::fromUtf8("dbc_dem_path"));

        horizontalLayout_2->addWidget(dbc_dem_path);

        matrix_choose_2 = new QPushButton(horizontalLayoutWidget_2);
        matrix_choose_2->setObjectName(QString::fromUtf8("matrix_choose_2"));

        horizontalLayout_2->addWidget(matrix_choose_2);

        horizontalLayoutWidget_3 = new QWidget(Dialog);
        horizontalLayoutWidget_3->setObjectName(QString::fromUtf8("horizontalLayoutWidget_3"));
        horizontalLayoutWidget_3->setGeometry(QRect(10, 170, 701, 51));
        horizontalLayout_3 = new QHBoxLayout(horizontalLayoutWidget_3);
        horizontalLayout_3->setObjectName(QString::fromUtf8("horizontalLayout_3"));
        horizontalLayout_3->setContentsMargins(0, 0, 0, 0);
        label_3 = new QLabel(horizontalLayoutWidget_3);
        label_3->setObjectName(QString::fromUtf8("label_3"));
        label_3->setFont(font);

        horizontalLayout_3->addWidget(label_3);

        matrix_demo_path = new QLineEdit(horizontalLayoutWidget_3);
        matrix_demo_path->setObjectName(QString::fromUtf8("matrix_demo_path"));

        horizontalLayout_3->addWidget(matrix_demo_path);

        matrix_choose_3 = new QPushButton(horizontalLayoutWidget_3);
        matrix_choose_3->setObjectName(QString::fromUtf8("matrix_choose_3"));

        horizontalLayout_3->addWidget(matrix_choose_3);

        label_4 = new QLabel(Dialog);
        label_4->setObjectName(QString::fromUtf8("label_4"));
        label_4->setGeometry(QRect(10, 240, 161, 21));
        label_4->setFont(font);
        label_5 = new QLabel(Dialog);
        label_5->setObjectName(QString::fromUtf8("label_5"));
        label_5->setGeometry(QRect(100, 10, 551, 51));
        QFont font1;
        font1.setFamily(QString::fromUtf8("MS Reference Sans Serif"));
        font1.setPointSize(20);
        label_5->setFont(font1);

        retranslateUi(Dialog);

        QMetaObject::connectSlotsByName(Dialog);
    } // setupUi

    void retranslateUi(QDialog *Dialog)
    {
        Dialog->setWindowTitle(QCoreApplication::translate("Dialog", "Dialog", nullptr));
        label->setText(QCoreApplication::translate("Dialog", "matrix path", nullptr));
        matrix_choose->setText(QCoreApplication::translate("Dialog", "\351\200\211\346\213\251", nullptr));
        label_2->setText(QCoreApplication::translate("Dialog", "Dbc Demo", nullptr));
        matrix_choose_2->setText(QCoreApplication::translate("Dialog", "\351\200\211\346\213\251", nullptr));
        label_3->setText(QCoreApplication::translate("Dialog", "Matrix Demo", nullptr));
        matrix_choose_3->setText(QCoreApplication::translate("Dialog", "\351\200\211\346\213\251", nullptr));
        label_4->setText(QCoreApplication::translate("Dialog", "\351\200\211\346\213\251matrix Sheet", nullptr));
        label_5->setText(QCoreApplication::translate("Dialog", "Continental Smart Core Dbc Generator", nullptr));
    } // retranslateUi

};

namespace Ui {
    class Dialog: public Ui_Dialog {};
} // namespace Ui

QT_END_NAMESPACE

#endif // DBCGEN_H
