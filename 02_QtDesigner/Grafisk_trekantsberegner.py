# [[file:02_QtDesigner.org::*Direkte indlæsning af designfil][Direkte indlæsning af designfil:1]]
# Grafisk_trekantsberegner.py
import sys

from PySide6.QtWidgets import QApplication
# QUiLoader skal bruges til at loade ui-filen
from PySide6.QtUiTools import QUiLoader

# Læg mærke tile at QMainWindow ikke importeres.
# I stedet importeres QObject i stedet for.
# QMainWindow er anvendt i Designer.
from PySide6.QtCore import QObject


# loader-objekt som bruges til at loade .ui-filen
loader = QUiLoader()


class Trekantsberegner(QObject):
    def __init__(self):
        super().__init__()
        # Brugerfladen kan tilgås gennem self.ui
        self.ui = loader.load("Grafisk_trekantsberegner_GUI.ui", None)
        self.ui.beregnknap.clicked.connect(self.beregn)
        # Skal bruges til at gemme værdierne for vinklerne og sidelængderne
        self.trekantsvaerdier = {}

    def beregn(self):
        # Her er et eksempel, som skal vise, hvordan værdier kan gemmes
        # I skal bruge funktionen beregn til noget andet end dette eksempel
        # Gemmer alle vinkler og længder i et dictionary
        for noegle, stoerrelse in zip(["A", "B", "C", "a", "b", "c"],[self.ui.vinkel_A, self.ui.vinkel_B, self.ui.vinkel_C, self.ui.side_a, self.ui.side_b, self.ui.side_c]):
            self.trekantsvaerdier[noegle] = stoerrelse.value()

        # Alternativ til for-løkken. Hvis der er mange værdier, der skal gemmes,
        # kan det hurtigt fylde for mange linjer.
        # self.trekantsvaerdier["A"] = self.ui.vinkel_A.value()
        # self.trekantsvaerdier["B"] = self.ui.vinkel_B.value()
        # self.trekantsvaerdier["C"] = self.ui.vinkel_C.value()
        # self.trekantsvaerdier["a"] = self.ui.side_a.value()
        # self.trekantsvaerdier["b"] = self.ui.side_b.value()
        # self.trekantsvaerdier["c"] = self.ui.side_c.value()

        # Sletter indholdet i outputfeltet
        self.ui.outputfelt.clear()
        # Skriver følgende til outputfeltet
        self.ui.outputfelt.append("Følgende værdier er gemt.")
        # Udprinter alle værdierne for indtastede vinkler og sider
        for navn, vaerdi in self.trekantsvaerdier.items():
                self.ui.outputfelt.append(f"{navn} = {vaerdi}")


program = QApplication.instance()
if program == None:
    program = QApplication(sys.argv)
trekantsberegner = Trekantsberegner()
trekantsberegner.ui.show()
program.exec()
# Direkte indlæsning af designfil:1 ends here
