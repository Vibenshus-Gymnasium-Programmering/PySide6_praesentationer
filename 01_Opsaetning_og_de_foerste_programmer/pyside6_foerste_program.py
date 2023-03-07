# [[file:01_Opsaetning_og_de_foerste_programmer.org::*Det første program][Det første program:1]]
from PySide6.QtWidgets import QApplication, QMainWindow

import sys

program = QApplication(sys.argv)

vindue = QMainWindow()
vindue.setWindowTitle("Mit foerste pyside6-program")
vindue.show()

program.exec()
# Det første program:1 ends here
