# [[file:01_Opsaetning_og_de_foerste_programmer.org::*Udskrivning til konsolen ved tryk på knap][Udskrivning til konsolen ved tryk på knap:1]]
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

import sys


class HovedVindue(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Et program med en knap")

        knap = QPushButton("Tryk på mig!")
        # Denne naeste linje er det nye.
        # clicked er signalet, mens knappen_blev_trykket_paa er slottet
        knap.clicked.connect(self.knappen_blev_trykket_paa)

        self.setCentralWidget(knap)

    # Denne metode et slot
    def knappen_blev_trykket_paa(self):
        print("Du trykkede paa knappen!")


program = QApplication(sys.argv)

vindue = HovedVindue()
vindue.show()

program.exec()
# Udskrivning til konsolen ved tryk på knap:1 ends here
