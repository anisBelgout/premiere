# geométrie sur les rectangles

def aire(longueur, largeur):
    aire = (longueur * largeur)/ 2
    return aire
 
    
    
def perimetre(longueur, largeur):
    perimetre = (longueur + largeur)*2
    return perimetre
   
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()