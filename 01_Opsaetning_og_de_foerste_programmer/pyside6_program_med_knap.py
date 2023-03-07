# [[file:01_Opsaetning_og_de_foerste_programmer.org::*Et program med en knap][Et program med en knap:1]]
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

import sys

# HovedVindue nedarver fra QMainWindow
class HovedVindue(QMainWindow):
    def __init__(self):
        # super() er en reference til den klasse/de klasser, der nedarves fra
        # Den foelgende linje koerer altsaa initialiseringsmetoden for QMainWindow
        super().__init__()

        # Her saettes vinduestitlen for HovedVindue
        self.setWindowTitle("Et program med en knap")

        # Her oprettes en knap. knap er kun tilgaengelig inden for __init__
        knap = QPushButton("Tryk på mig!")

        # Her saettes knappen til at blive vist i vinduet
        self.setCentralWidget(knap)

# Resten er det samme som i forrige eksempel
program = QApplication(sys.argv)

vindue = HovedVindue()
vindue.show()

program.exec()
# Et program med en knap:1 ends here
