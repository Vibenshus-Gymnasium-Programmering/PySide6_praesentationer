# [[file:02_QtDesigner.org::*Selve logikken bag en trekantsberegner][Selve logikken bag en trekantsberegner:1]]
import math

def sidelaengde_vha_cosrel(side_1, side_2, vinkel_imellem):
    """Returnerer sidelængden i en trekant vha cosinusrelationen, hvis man anvender to sidelængder og den mellemliggende vinkel. Vinklen antages at være i grader."""
    return (side_1**2 + side_2**2 - 2 * side_1 * side_2 * math.cos(math.radians(vinkel_imellem)))**0.5

def sidelaengde_vha_sinrel(side_1, vinkel_1, vinkel_2):
    """Returnerer sidelængden i en trekant vha sinusrelationen, hvis man anvender en side og dens modstående vinkel, samt en anden kendt vinkel. Den returnerede sidelængde står overfor vinkel_2. Alle vinkler antages at være i grader."""
    return side_1 * math.sin(math.radians(vinkel_2)) / math.sin(math.radians(vinkel_1)) 

# Her fra må I selv finde på flere funktioner og en eller flere algoritmer, som kan løse en vilkårlig trekant.
# Selve logikken bag en trekantsberegner:1 ends here
