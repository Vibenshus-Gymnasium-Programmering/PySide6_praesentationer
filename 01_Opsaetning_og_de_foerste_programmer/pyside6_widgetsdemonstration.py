# [[file:01_Opsaetning_og_de_foerste_programmer.org::*Widgets i Qt og PySide6][Widgets i Qt og PySide6:1]]
import sys

from PySide6.QtWidgets import QVBoxLayout, QWidget
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
)


class HovedVindue(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Demonstration af forskellige widgets")

        layout = QVBoxLayout()

        self.widgets = [
            QCheckBox(),
            QComboBox(),
            QDateEdit(),
            QDateTimeEdit(),
            QDial(),
            QDoubleSpinBox(),
            QFontComboBox(),
            QLCDNumber(),
            QLabel(text="Dette er en QLabel"),
            QLineEdit("Dette er en QLineEdit"),
            QProgressBar(),
            QPushButton(text="Dette er en QPushButton"),
            QRadioButton(),
            QSlider(),
            QSpinBox(),
            QTimeEdit(),
        ]

        for widget in self.widgets:
            layout.addWidget(widget)

        central_widget = QWidget()
        central_widget.setLayout(layout)

        self.setCentralWidget(central_widget)


program = QApplication(sys.argv)

vindue = HovedVindue()
vindue.show()

program.exec()


# Widgets i Qt og PySide6:1 ends here
