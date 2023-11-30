class documentaire :
    
    

    _nbr_obj = 0 

    def __init__(self , date , titre ) :

        self._date = date 
        self._titre = titre 
        documentaire._nbr_obj += 1
        self.code = documentaire._nbr_obj 


    def get_date(self):
        return self._date
    
    def get_titre(self) :
        return self._titre
    
    def get_nbr_objet(self) :
        return self._nbr_obj
    
    def get_code(self) :
        return self.code
    
    def set_date(self , value) :
        self ._date = value
    
    def set_titre(self , value) :
        self ._titre = value
    
    def set_code(self , value) :
        self ._code = value

    def ToString(self) :
        return f" la date est : {self.get_date()} le titre est : {self.get_titre()} et le nombre d'objet est : {self.code}" 
    
    def Equals(self , doc  ) :
        if self.code == doc.get_code() :
            return True 
        else :
            return False

# doc1 = documentaire( 2021 , "titre" , 250)

# print(doc1.get__code() , doc1.get__date() , doc1.get__titre() , doc1.get__nbr_objet() , doc1.ToString() , doc1.Equals(documentaire(2021 , "titre" , 250 )))

class exemplaire (documentaire) :
    def __init__(self, date, titre , numéro , date_achat ):
        super().__init__(date, titre)
        self.__numéro = numéro
        self.__date_achat = date_achat 

    def get__numéro(self) :
        return self.__numéro
    
    def set__numéro(self , value) :
        self.__numéro = value
    
    def get__date_achat(self) :
        return self.__date_achat
    
    def set__numéro(self , value) :
        self.__date_achat = value
    
    def ToString(self):
        return super().ToString() + f" la date est : {self.get__date_achat()} le numéro est {self.get__numéro()}"
    
    def Equals(self, doc):
        if  self.__numéro == doc.get__numéro() :
            return True 
        else :
            return False


# exem = exemplaire(2021,"titre",5,2021)
# exem1 = exemplaire(2021,"titre",5,2021)
doc1 = documentaire(2021,"titre")
doc2 = documentaire(2021,"titre")
print(doc1.Equals(doc2))

