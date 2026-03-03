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
    
    Args:
        m_crypté (int): Le message chiffré
        d (int): L'exposant privé
        n (int): Le module RSA
        
    Returns:
        int: Le message en clair
    """
    return pow(m_crypté, d, n)

def decrypt(fichier, keyPriv):
    """Déchiffre un fichier contenant un message chiffré
    
    Args:
        fichier (str): Chemin du fichier chiffré
        keyPriv (str): La clé privée au format 'd,n'
        
    Returns:
        int: Le message déchiffré
    """
    with open(fichier, 'r') as f:
        texteChiffré = int(f.read().strip())
    
    # Parser la clé privée au format 'd,n'
    d, n = map(int, keyPriv.split(','))
    
    # Déchiffrer le message
    texteDéchiffré = decryptage(texteChiffré, d, n)
    return texteDéchiffré

def dechiffrer_fichier(chemin_fichier, d, n, dossier_sortie):
    """Déchiffre un fichier chiffré avec RSA
    
    Args:
        chemin_fichier (str): Chemin du fichier chiffré
        d (int): L'exposant privé
        n (int): Le module RSA
        dossier_sortie (str): Dossier de sauvegarde
        
    Returns:
        str: Chemin du fichier déchiffré
    """
    try:
        # Lire le message chiffré
        with open(chemin_fichier, 'r') as f:
            message_chiffré = int(f.read().strip())
        
        # Déchiffrer
        message_décrypté = decryptage(message_chiffré, d, n)
        
        # Convertir de nouveau en texte
        # Calculer le nombre de bytes nécessaires
        contenu = message_décrypté.to_bytes(
            (message_décrypté.bit_length() + 7) // 8, 
            byteorder='big'
        ).decode('utf-8')
        
        # Sauvegarder le fichier déchiffré
        nom_fichier = os.path.basename(chemin_fichier)
        nom_sortie = nom_fichier.replace('chiffré_', 'déchiffré_')
        chemin_sortie = os.path.join(dossier_sortie, nom_sortie)
        
        with open(chemin_sortie, 'w', encoding='utf-8') as f:
            f.write(contenu)
        
        return chemin_sortie
    
    except Exception as e:
        raise Exception(f"Erreur lors du déchiffrement : {e}")