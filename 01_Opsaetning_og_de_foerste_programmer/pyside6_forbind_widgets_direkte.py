# [[file:01_Opsaetning_og_de_foerste_programmer.org::*Forbind =widgets= direkte med hinanden][Forbind =widgets= direkte med hinanden:1]]
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QLineEdit,
    QVBoxLayout,
    QWidget,
)

import sys


class HovedVindue(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Direkte forbindelse")
        self.label = QLabel()

        self.inputlinje = QLineEdit()
        self.inputlinje.textChanged.connect(self.label.setText)

        layout = QVBoxLayout()
        layout.addWidget(self.inputlinje)
        layout.addWidget(self.label)

        central_widget = QWidget()
        central_widget.setLayout(layout)

        self.setCentralWidget(central_widget)


program = QApplication(sys.argv)

vindue = HovedVindue()
vindue.show()

program.exec()

# Forbind =widgets= direkte med hinanden:1 ends here
