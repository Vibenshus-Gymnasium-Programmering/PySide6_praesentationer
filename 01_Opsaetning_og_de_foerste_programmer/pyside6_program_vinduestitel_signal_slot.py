# [[file:01_Opsaetning_og_de_foerste_programmer.org::*Ændring af vinduestitlen][Ændring af vinduestitlen:1]]
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

import sys

from random import choice

vinduestitler = [
    "Tryk på knappen!",
    "Suprise!",
    "Noget gik galt! Hvad har du nu gjort?!",
    "Poprorogogroramommomerorinongog",
]


class HovedVindue(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tryk på knappen!")

        self.knap = QPushButton("Tryk på mig!")
        self.knap.clicked.connect(self.aendr_vinduestitlen)

        self.setCentralWidget(self.knap)

    def aendr_vinduestitlen(self):
        ny_titel = choice(vinduestitler)
        self.setWindowTitle(ny_titel)
        if ny_titel == "Noget gik galt! Hvad har du nu gjort?!":
            self.knap.setDisabled(True)


program = QApplication(sys.argv)

vindue = HovedVindue()
vindue.show()

program.exec()
# Ændring af vinduestitlen:1 ends here
