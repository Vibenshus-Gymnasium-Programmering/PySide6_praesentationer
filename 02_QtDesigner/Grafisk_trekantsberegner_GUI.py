# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Grafisk_trekantsberegner_GUI.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QDoubleSpinBox,
    QGridLayout,
    QLabel,
    QMainWindow,
    QMenuBar,
    QPushButton,
    QSizePolicy,
    QStatusBar,
    QTextBrowser,
    QVBoxLayout,
    QWidget,
)


class Ui_TrekantsberegnerVindue(object):
    def setupUi(self, TrekantsberegnerVindue):
        if not TrekantsberegnerVindue.objectName():
            TrekantsberegnerVindue.setObjectName("TrekantsberegnerVindue")
        TrekantsberegnerVindue.resize(328, 402)
        self.centralwidget = QWidget(TrekantsberegnerVindue)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.vinkel_C_label = QLabel(self.centralwidget)
        self.vinkel_C_label.setObjectName("vinkel_C_label")
        self.vinkel_C_label.setMinimumSize(QSize(20, 20))
        self.vinkel_C_label.setMaximumSize(QSize(20, 20))

        self.gridLayout.addWidget(self.vinkel_C_label, 4, 0, 1, 1)

        self.side_b_label = QLabel(self.centralwidget)
        self.side_b_label.setObjectName("side_b_label")
        self.side_b_label.setMinimumSize(QSize(10, 10))
        self.side_b_label.setMaximumSize(QSize(20, 20))

        self.gridLayout.addWidget(self.side_b_label, 3, 2, 1, 1)

        self.beregnknap = QPushButton(self.centralwidget)
        self.beregnknap.setObjectName("beregnknap")

        self.gridLayout.addWidget(self.beregnknap, 5, 0, 1, 4)

        self.vinkler_label = QLabel(self.centralwidget)
        self.vinkler_label.setObjectName("vinkler_label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.vinkler_label.sizePolicy().hasHeightForWidth()
        )
        self.vinkler_label.setSizePolicy(sizePolicy)
        self.vinkler_label.setMaximumSize(QSize(16777215, 20))
        self.vinkler_label.setAlignment(
            Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter
        )

        self.gridLayout.addWidget(self.vinkler_label, 1, 0, 1, 2)

        self.sider_label = QLabel(self.centralwidget)
        self.sider_label.setObjectName("sider_label")
        sizePolicy.setHeightForWidth(self.sider_label.sizePolicy().hasHeightForWidth())
        self.sider_label.setSizePolicy(sizePolicy)
        self.sider_label.setMaximumSize(QSize(16777215, 20))
        self.sider_label.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.gridLayout.addWidget(self.sider_label, 1, 2, 1, 2)

        self.output_label = QLabel(self.centralwidget)
        self.output_label.setObjectName("output_label")

        self.gridLayout.addWidget(self.output_label, 6, 0, 1, 4)

        self.vinkel_A_label = QLabel(self.centralwidget)
        self.vinkel_A_label.setObjectName("vinkel_A_label")
        self.vinkel_A_label.setMinimumSize(QSize(20, 20))
        self.vinkel_A_label.setMaximumSize(QSize(20, 20))

        self.gridLayout.addWidget(self.vinkel_A_label, 2, 0, 1, 1)

        self.vinkel_C = QDoubleSpinBox(self.centralwidget)
        self.vinkel_C.setObjectName("vinkel_C")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.vinkel_C.sizePolicy().hasHeightForWidth())
        self.vinkel_C.setSizePolicy(sizePolicy1)
        self.vinkel_C.setMaximum(180.000000000000000)

        self.gridLayout.addWidget(self.vinkel_C, 4, 1, 1, 1)

        self.side_a = QDoubleSpinBox(self.centralwidget)
        self.side_a.setObjectName("side_a")
        sizePolicy1.setHeightForWidth(self.side_a.sizePolicy().hasHeightForWidth())
        self.side_a.setSizePolicy(sizePolicy1)
        self.side_a.setMinimumSize(QSize(20, 20))
        self.side_a.setMaximum(9999999999999.000000000000000)

        self.gridLayout.addWidget(self.side_a, 2, 3, 1, 1)

        self.side_c_label = QLabel(self.centralwidget)
        self.side_c_label.setObjectName("side_c_label")
        self.side_c_label.setMinimumSize(QSize(10, 10))
        self.side_c_label.setMaximumSize(QSize(20, 20))

        self.gridLayout.addWidget(self.side_c_label, 4, 2, 1, 1)

        self.side_b = QDoubleSpinBox(self.centralwidget)
        self.side_b.setObjectName("side_b")
        sizePolicy1.setHeightForWidth(self.side_b.sizePolicy().hasHeightForWidth())
        self.side_b.setSizePolicy(sizePolicy1)
        self.side_b.setMinimumSize(QSize(20, 20))
        self.side_b.setMaximum(9999999999999.000000000000000)

        self.gridLayout.addWidget(self.side_b, 3, 3, 1, 1)

        self.side_c = QDoubleSpinBox(self.centralwidget)
        self.side_c.setObjectName("side_c")
        sizePolicy1.setHeightForWidth(self.side_c.sizePolicy().hasHeightForWidth())
        self.side_c.setSizePolicy(sizePolicy1)
        self.side_c.setMinimumSize(QSize(20, 20))
        self.side_c.setMaximum(9999999999999.000000000000000)

        self.gridLayout.addWidget(self.side_c, 4, 3, 1, 1)

        self.vinkel_B_label = QLabel(self.centralwidget)
        self.vinkel_B_label.setObjectName("vinkel_B_label")
        self.vinkel_B_label.setMinimumSize(QSize(20, 20))
        self.vinkel_B_label.setMaximumSize(QSize(20, 20))

        self.gridLayout.addWidget(self.vinkel_B_label, 3, 0, 1, 1)

        self.vinkel_A = QDoubleSpinBox(self.centralwidget)
        self.vinkel_A.setObjectName("vinkel_A")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.vinkel_A.sizePolicy().hasHeightForWidth())
        self.vinkel_A.setSizePolicy(sizePolicy2)
        self.vinkel_A.setMaximum(180.000000000000000)

        self.gridLayout.addWidget(self.vinkel_A, 2, 1, 1, 1)

        self.side_a_label = QLabel(self.centralwidget)
        self.side_a_label.setObjectName("side_a_label")
        self.side_a_label.setMinimumSize(QSize(10, 10))
        self.side_a_label.setMaximumSize(QSize(20, 20))

        self.gridLayout.addWidget(self.side_a_label, 2, 2, 1, 1)

        self.vinkel_B = QDoubleSpinBox(self.centralwidget)
        self.vinkel_B.setObjectName("vinkel_B")
        sizePolicy1.setHeightForWidth(self.vinkel_B.sizePolicy().hasHeightForWidth())
        self.vinkel_B.setSizePolicy(sizePolicy1)
        self.vinkel_B.setMaximum(180.000000000000000)

        self.gridLayout.addWidget(self.vinkel_B, 3, 1, 1, 1)

        self.outputfelt = QTextBrowser(self.centralwidget)
        self.outputfelt.setObjectName("outputfelt")
        self.outputfelt.setFocusPolicy(Qt.NoFocus)
        self.outputfelt.setAcceptRichText(False)

        self.gridLayout.addWidget(self.outputfelt, 7, 0, 1, 4)

        self.verticalLayout_2.addLayout(self.gridLayout)

        TrekantsberegnerVindue.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(TrekantsberegnerVindue)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 328, 23))
        TrekantsberegnerVindue.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(TrekantsberegnerVindue)
        self.statusbar.setObjectName("statusbar")
        TrekantsberegnerVindue.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.vinkel_A, self.vinkel_B)
        QWidget.setTabOrder(self.vinkel_B, self.vinkel_C)
        QWidget.setTabOrder(self.vinkel_C, self.side_a)
        QWidget.setTabOrder(self.side_a, self.side_b)
        QWidget.setTabOrder(self.side_b, self.side_c)
        QWidget.setTabOrder(self.side_c, self.beregnknap)
        QWidget.setTabOrder(self.beregnknap, self.outputfelt)

        self.retranslateUi(TrekantsberegnerVindue)

        QMetaObject.connectSlotsByName(TrekantsberegnerVindue)

    # setupUi

    def retranslateUi(self, TrekantsberegnerVindue):
        TrekantsberegnerVindue.setWindowTitle(
            QCoreApplication.translate(
                "TrekantsberegnerVindue", "Trekantsberegner", None
            )
        )
        self.vinkel_C_label.setText(
            QCoreApplication.translate("TrekantsberegnerVindue", "C:", None)
        )
        self.side_b_label.setText(
            QCoreApplication.translate("TrekantsberegnerVindue", "b:", None)
        )
        self.beregnknap.setText(
            QCoreApplication.translate("TrekantsberegnerVindue", "Beregn", None)
        )
        self.vinkler_label.setText(
            QCoreApplication.translate("TrekantsberegnerVindue", "Vinkler:", None)
        )
        self.sider_label.setText(
            QCoreApplication.translate(
                "TrekantsberegnerVindue", "Sidel\u00e6ngder:", None
            )
        )
        self.output_label.setText(
            QCoreApplication.translate("TrekantsberegnerVindue", "Output:", None)
        )
        self.vinkel_A_label.setText(
            QCoreApplication.translate("TrekantsberegnerVindue", "A:", None)
        )
        self.side_c_label.setText(
            QCoreApplication.translate("TrekantsberegnerVindue", "c:", None)
        )
        self.vinkel_B_label.setText(
            QCoreApplication.translate("TrekantsberegnerVindue", "B:", None)
        )
        self.side_a_label.setText(
            QCoreApplication.translate("TrekantsberegnerVindue", "a:", None)
        )

    # retranslateUi
