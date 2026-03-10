class Employe:
    def __init__(self, numeroPermis, nom, prenom):
        self.numeroPermis = numeroPermis
        self.nom = nom
        self.prenom = prenom
        self.voitureService = None
    def afficherInformations(self):
        return (self.numeroPermis, self.nom, self.prenom, self.voitureService)
    def affecterVoiture(self, voiture):
        if self.voitureService is None and voiture.chauffeur is None:
            self.voitureService = voiture
            voiture.chauffeur = self
    def retirerVoiture(self):
        if self.voitureService is not None:
            self.voitureService.chauffeur = None
            self.voitureService = None
class Voiture:

    def __init__(self, matricule, annee, marque, kilometrage):
        self.matricule = matricule
        self.annee = annee
        self.marque = marque
        self.kilometrage = kilometrage
        self.chauffeur = None

        def afficherInformations(self):
            return (self.matricule, self.annee, self.marque, self.kilometrage, self.chauffeur)
e1 = Employe("I270520", "lounis", "younes")
e2 = Employe("B120399", "Bousekin", "Noureddine")
e3 = Employe("K150800", "Ali", "boukhalfa")
v1 = Voiture("AA123BB", 2025, "ford", 11000)
v2 = Voiture("CC456DD", 2025, "Honda", 8000)
v3 = Voiture("EE789FF", 2024, "dodge", 15000)
print(e1.afficherInformations())
print(e2.afficherInformations())
print(e3.afficherInformations())
print(v1.afficherInformations())
print(v2.afficherInformations())
print(v3.afficherInformations())
e1.affecterVoiture(v1)
e2.affecterVoiture(v2)
print(e1.afficherInformations())
print(e2.afficherInformations())
print(v1.afficherInformations())
print(v2.afficherInformations())
e1.retirerVoiture()
print(e1.afficherInformations())
print(v1.afficherInformations())
e3.affecterVoiture(v2)
print(e2.afficherInformations())
print(e3.afficherInformations())
print(v2.afficherInformations())