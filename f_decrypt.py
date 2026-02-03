
def cléPub(fichier):
    with open(fichier, 'r') as f:
        keyPub = f.read()
    return keyPub

def cléPriv(fichier):
    with open(fichier, 'r') as f:
        keyPriv = f.read()
    return keyPriv

def decrypt(fichier, keyPub, keyPriv):
    with open(fichier, 'r') as f:
        texteChiffré = f.read()
    # Simuler le processus de déchiffrement
    texteDéchiffré = f"Déchiffré avec clé publique {keyPub} et clé privée {keyPriv}: {texteChiffré}"
    return texteDéchiffré