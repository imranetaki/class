class Rectangle :
    nbrRectangle=0
    def __init__(self,longueur,largeur):
        self.longueur = longueur
        self.largeur = largeur
        Rectangle.nbrRectangle += 1

    
    # def __init__(self):
    #     self.longueur=0
    #     self.largeur=0
    
    # def __init__(self,R1):
    #     self.longueur=R1.longueur
    #     self.largeur=R1.largueur
    def getLongueur(self) :
        return self.longueur
    def getLargeur(self) :
        return self.largeur
    def getNbrRectangle(self) :
        return self.nbrRectangle
    
    def perimetre(self) :
        perimetre = 2 * (self.longueur + self.largeur)
        return perimetre
    
    def aire(self) :
        aire =  (self.longueur * self.largeur)
        return aire
    

    def Equals(self,R) :
        if self.longueur == R.longueur and self.largeur == R.largeur :
            return True
        else :
            return False
        
    def ToString(self) :
        return print(f"longueur : {self.longueur} , la largeur est {self.largeur} ")
    
class parallélépipède(Rectangle) :
    nbrParallélépipède=0
    def __init__(self, longueur, largeur , hauteur ):
        super().__init__(longueur, largeur)
        self.hauteur = hauteur
        parallélépipède.nbrParallélépipède += 1

    def getHauteur(self) :
        return self.hauteur
    
    def getnbrparallélépipède(self) :
        return self.nbrParallélépipède
    
    def setHauteur(self , value ) :
        self.hauteur = value
    
    def ToString(self):
        return super().ToString() + f"la hauteur est : {self.hauteur}"
    
    def surface(self) :
        return 2 * self.hauteur * self.largeur + 2 * self.hauteur +self.longueur + 2 * self.longueur + self.largeur 
    
    def volume(self) :
        return super().aire() * self.hauteur

    def Equals(self, R):
        if self.longueur == R.getLongueur() and self.largeur == R.getLargeur() and self.hauteur == R.getHauteur()  :
            return True
        else :
            return False
        
rec = Rectangle(5,2)
print(rec.Equals(Rectangle(5,2)))
    

    
        