import os

def cléPub(fichier):
    """Charge la clé publique depuis un fichier"""
    with open(fichier, 'r') as f:
        keyPub = f.read().strip()
    return keyPub

def cléPriv(fichier):
    """Charge la clé privée depuis un fichier"""
    with open(fichier, 'r') as f:
        keyPriv = f.read().strip()
    return keyPriv

def decryptage(m_crypté, d, n):
    """Déchiffre un message en utilisant RSA asymétrique
        m_crypté : Le message chiffré
        d : L'exposant privé
        n : Le module RSA
    """
    return pow(m_crypté, d, n) #= m_crypté^d mod n

def dechiffrer_fichier(chemin_fichier, d, n, dossier_sortie):
    """Déchiffre un fichier chiffré avec RSA
        d (int): L'exposant privé
        n (int): Le module RSA
    """
    try:
        # Lire le message chiffré avec sa longueur
        with open(chemin_fichier, 'r') as f:
            contenu_fichier = f.read().strip()
        
        # Séparer la longueur originale et le message chiffré
        longueur_str, message_chiffré_str = contenu_fichier.split('|')
        longueur_originale = int(longueur_str)
        message_chiffré = int(message_chiffré_str)
        
        # Déchiffrer
        message_décrypté = decryptage(message_chiffré, d, n)
        
        # Convertir de nouveau en texte avec la bonne longueur
        contenu = message_décrypté.to_bytes(longueur_originale, byteorder='big').decode('utf-8') # Décode en UTF-8 
        
        # Sauvegarder le fichier déchiffré
        nom_fichier = os.path.basename(chemin_fichier)
        nom_sortie = nom_fichier.replace('chiffré_', 'déchiffré_')
        chemin_sortie = os.path.join(dossier_sortie, nom_sortie)
        
        with open(chemin_sortie, 'w', encoding='utf-8') as f:
            f.write(contenu)

        #os.remove(chemin_fichier) # Supprimer le fichier chiffré après déchiffrement
        
        return chemin_sortie
    
    except Exception as e:
        raise Exception(f"Erreur lors du déchiffrement : {e}")