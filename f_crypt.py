
import os

def premier_entre_eux(a, b):
    """Vérifie si deux nombres sont premiers entre eux"""
    if a > b:
        a, b = b, a
    for i in range(2, a + 1):
        if a % i == 0 and b % i == 0:
            return False
    return True

def element_e(phi_n):
    """Trouve le plus petit e premiers avec phi_n"""
    for e in range(2, phi_n):
        if premier_entre_eux(e, phi_n):
            return e

def cryptage(m, e, n):
    """Chiffre un message avec RSA
        m : Le message à chiffrer
        e : L'exposant public
        n : Le module RSA
    """
    return pow(m, e, n)

def chiffrer_fichier(chemin_fichier, e, n, dossier_sortie):
    """Chiffre un fichier texte avec RSA
        e : L'exposant public
        n : Le module RSA
    """
    try:
        # Lire le contenu du fichier
        with open(chemin_fichier, 'r', encoding='utf-8') as f:
            contenu = f.read()
        
        # Convertir en nombre entier (ASCII)
        contenu_bytes = contenu.encode('utf-8')
        message = int.from_bytes(contenu_bytes, byteorder='big')
        
        # Chiffrer
        message_chiffré = cryptage(message, e, n)
        
        # Sauvegarder le message chiffré
        nom_fichier = os.path.basename(chemin_fichier)
        nom_sortie = f"chiffré_{nom_fichier}"
        chemin_sortie = os.path.join(dossier_sortie, nom_sortie)
        
        # Stocker: longueur_originale|message_chiffré
        with open(chemin_sortie, 'w') as f:
            f.write(f"{len(contenu_bytes)}|{message_chiffré}")
        
        return chemin_sortie
    
    except Exception as e:
        raise Exception(f"Erreur lors du chiffrement : {e}")
