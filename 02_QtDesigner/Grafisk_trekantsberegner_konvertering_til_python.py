# [[file:02_QtDesigner.org::*Fra ui-fil til pythonfil][Fra ui-fil til pythonfil:1]]
import sys

# Import af de almindelige elementer i pyside6
from PySide6.QtWidgets import QApplication, QMainWindow
# Import af brugerfladen, som netop er konverteret til en pythonfil hva pyside6-uic
from Grafisk_trekantsberegner_GUI import Ui_TrekantsberegnerVindue

# Vores trekantsberegner starter med at nedarve fra QMainWindow, da det var det,
# vi valgte, da vi designede vores applikation
class Trekantsberegner(QMainWindow):
    def __init__(self):
        super().__init__()
        # Her oprettes self.ui ud fra den klasse som er i den genererede pythonfil
        # altså den samme klasse, som er importeret i starten af denne fil
        self.ui = Ui_TrekantsberegnerVindue()
        # Nedenfor sætte selve brugerfladen op. Metoden kan man finde i GUI-pythonfilen.
        self.ui.setupUi(self)

        # Her sættes signal og slot op for beregn knappen.
        self.ui.beregnknap.clicked.connect(self.beregn)

        # Skal bruges til at gemme værdierne for vinklerne og sidelængderne
        self.trekantsvaerdier = {}

    def beregn(self):
        # Indholdet i denne metode er det samme som i forrige eksempel med indlæsning af ui-filen.

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
# Læg mærke til at det nu er trekantsberegner, som har metoden show,
# og ikke trekantsberegner.ui.
trekantsberegner.show()
program.exec()
# Fra ui-fil til pythonfil:1 ends here
