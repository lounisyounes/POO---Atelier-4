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