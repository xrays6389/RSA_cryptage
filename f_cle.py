import random
import os
from sympy import isprime, mod_inverse

def nombre_premier_aleatoire(min_val, max_val):
    """Génère un nombre premier aléatoire entre min_val et max_val
        min_val (int): Valeur minimale
        max_val (int): Valeur maximale
    """
    while True:
        n = random.randint(min_val, max_val)
        if isprime(n):
            return n

def generer_clés_aléatoires(min_bits=10, max_bits=20):
    """Génère des clés RSA avec des nombres premiers aléatoires
        min_bits (int): Nombre minimum de bits pour les nombres premiers
        max_bits (int): Nombre maximum de bits pour les nombres premiers
    """
    min_val = 2 ** min_bits
    max_val = 2 ** max_bits
    
    # Générer deux nombres premiers aléatoires et distincts
    p = nombre_premier_aleatoire(min_val, max_val)
    while True:
        q = nombre_premier_aleatoire(min_val, max_val)
        if q != p:
            break
    
    # Calculer n
    n = p * q
    
    # Calculer la fonction d'Euler
    phi = (p - 1) * (q - 1)
    
    # Choisir e (exposant public)
    e = 65537  # Choix commun pour e
    
    # Calculer d (exposant privé)
    d = mod_inverse(e, phi)
    
    # Clés publique et privée
    public_key = (e, n)
    private_key = (d, n)
    
    return public_key, private_key

def generate_keys(p, q):
    """Genere les clés RSA.
        p (int): nombre premier.
        q (int): second nombre premier."""

    # Calculate n
    n = p * q

    # Calculate Euler's totient function
    phi = (p - 1) * (q - 1)

    # Choose e
    e = 65537  # Common choice for e

    # Calculate d
    d = mod_inverse(e, phi)

    # Public key (e, n) and private key (d, n)
    public_key = (e, n)
    private_key = (d, n)

    return public_key, private_key

def sauvegarder_clés(public_key, private_key, dossier):
    """Sauvegarde les clés dans des fichiers
        public_key (tuple): Clé publique (e, n)
        private_key (tuple): Clé privée (d, n)
    """
    # Créer le dossier s'il n'existe pas
    os.makedirs(dossier, exist_ok=True)
    
    e, n = public_key
    d, n_priv = private_key
    
    # Sauvegarder la clé publique
    chemin_pub = os.path.join(dossier, "cle_publique.txt")
    with open(chemin_pub, 'w') as f:
        f.write(f"{e},{n}")
    
    # Sauvegarder la clé privée
    chemin_priv = os.path.join(dossier, "cle_privee.txt")
    with open(chemin_priv, 'w') as f:
        f.write(f"{d},{n_priv}")
    
    return chemin_pub, chemin_priv

def charger_clés(dossier):
    """Charge les clés depuis les fichiers"""
    
    # Charger la clé publique
    chemin_pub = os.path.join(dossier, "cle_publique.txt")
    with open(chemin_pub, 'r') as f:
        e, n = map(int, f.read().strip().split(','))
    public_key = (e, n)
    
    # Charger la clé privée
    chemin_priv = os.path.join(dossier, "cle_privee.txt")
    with open(chemin_priv, 'r') as f:
        d, n_priv = map(int, f.read().strip().split(','))
    private_key = (d, n_priv)
    
    return public_key, private_key