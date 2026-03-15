import tkinter as tk
from tkinter import filedialog, messagebox
import os
from f_cle import generer_clés_aléatoires, sauvegarder_clés, charger_clés
from f_crypt import chiffrer_fichier
from f_decrypt import dechiffrer_fichier

# Variables globales
fichier_selectionne = ""
dossier_selectionne = ""
dossier_clé = ""
public_key = None
private_key = None

def window_generer_clés():
    """Génère des clés RSA aléatoires"""
    global dossier_clé, public_key, private_key
    
    if not dossier_clé:
        messagebox.showwarning("Erreur", "Veuillez d'abord sélectionner un dossier pour les clés !")
        return
    
    try:
        # Générer les clés
        public_key, private_key = generer_clés_aléatoires(min_bits=1024, max_bits=2048)
        
        # Sauvegarder les clés
        sauvegarder_clés(public_key, private_key, dossier_clé)
        
        e, n = public_key
        d, _ = private_key
        
        messagebox.showinfo("Succès", 
            f"Clés générées et sauvegardées !\n\n")
           
        lbl_clés_status.config(text="✓ Clés générées avec succès", fg="green")
    
    except Exception as e:
        messagebox.showerror("Erreur", f"Erreur lors de la génération : {e}")

def window_crypt():
    """Chiffre un fichier"""
    global fichier_selectionne, dossier_selectionne, dossier_clé, public_key
    
    if not fichier_selectionne or not dossier_selectionne or not dossier_clé:
        messagebox.showwarning("Erreur", "Veuillez sélectionner un fichier, un dossier de sortie et un dossier pour les clés !")
        return
    
    try:
        # Charger la clé publique si pas déjà chargée
        if public_key is None:
            try:
                public_key, _ = charger_clés(dossier_clé)
            except:
                messagebox.showerror("Erreur", "Impossible de charger la clé publique. Générez d'abord les clés !")
                return
        
        e, n = public_key
        
        # Chiffrer le fichier
        fichier_crypte = chiffrer_fichier(fichier_selectionne, e, n, dossier_selectionne)
        messagebox.showinfo("Succès", f"Fichier chiffré enregistré sous :\n{fichier_crypte}")
        lbl_status.config(text="✓ Fichier chiffré avec succès", fg="green")
    
    except Exception as e:
        messagebox.showerror("Erreur", f"Erreur lors du chiffrement : {e}")

def window_uncrypt():
    """Déchiffre un fichier"""
    global fichier_selectionne, dossier_selectionne, dossier_clé, private_key
    
    if not fichier_selectionne or not dossier_selectionne or not dossier_clé:
        messagebox.showwarning("Erreur", "Veuillez sélectionner un fichier, un dossier de sortie et un dossier pour les clés !")
        return
    
    try:
        # Charger la clé privée si pas déjà chargée
        if private_key is None:
            try:
                _, private_key = charger_clés(dossier_clé)
            except:
                messagebox.showerror("Erreur", "Impossible de charger la clé privée. Générez d'abord les clés !")
                return
        
        d, n = private_key
        
        # Déchiffrer le fichier
        fichier_decrypte = dechiffrer_fichier(fichier_selectionne, d, n, dossier_selectionne)
        messagebox.showinfo("Succès", f"Fichier déchiffré enregistré sous :\n{fichier_decrypte}")
        lbl_status.config(text="✓ Fichier déchiffré avec succès", fg="green")
    
    except Exception as e:
        messagebox.showerror("Erreur", f"Erreur lors du déchiffrement : {e}")

def choisir_fichier():
    """Sélectionne un fichier"""
    global fichier_selectionne
    fichier_selectionne = filedialog.askopenfilename(title="Sélectionnez un fichier")
    if fichier_selectionne:
        nom = os.path.basename(fichier_selectionne)
        lbl_fichier.config(text=f"📂 Fichier : {nom}", fg="blue")

def choisir_dossier():
    """Sélectionne un dossier"""
    global dossier_selectionne
    dossier_selectionne = filedialog.askdirectory(title="Sélectionnez un dossier de sauvegarde")
    if dossier_selectionne:
        nom = os.path.basename(dossier_selectionne)
        lbl_dossier.config(text=f"📁 Dossier : {nom}", fg="blue")

def choisir_d_clé():
    """Sélectionne le dossier pour les clés"""
    global dossier_clé
    dossier_clé = filedialog.askdirectory(title="Sélectionnez le dossier pour les clés")
    if dossier_clé:
        nom = os.path.basename(dossier_clé)
        lbl_clé.config(text=f"🔑 Dossier clés : {nom}", fg="blue")

# Création de la fenêtre principale
root = tk.Tk()
root.title("RSA : Cryptage & Décryptage")
root.geometry("650x700")
root.config(bg="lightgray")

# Titre principal
titre = tk.Label(root, text="Système RSA", font=("Arial", 18, "bold"), bg="lightgray")
titre.pack(pady=15)

# === Partie 1: SÉLECTIONS ===
frame_selection = tk.Frame(root, bg="white", relief="sunken", bd=2)
frame_selection.pack(padx=10, pady=10, fill="both", expand=False)

tk.Label(frame_selection, text="1. SÉLECTIONS", font=("Arial", 12, "bold"), bg="white").pack(anchor="w", padx=10, pady=(10, 5))

# Sélection de fichier
lbl_fichier = tk.Label(frame_selection, text="Aucun fichier sélectionné", fg="red", wraplength=400, bg="white")
lbl_fichier.pack(anchor="w", padx=10, pady=5)
tk.Button(frame_selection, text="📂 Choisir un fichier", command=choisir_fichier, bg="skyblue").pack(anchor="w", padx=10, pady=2)

# Sélection de dossier sortie
lbl_dossier = tk.Label(frame_selection, text="Aucun dossier sélectionné", fg="red", wraplength=400, bg="white")
lbl_dossier.pack(anchor="w", padx=10, pady=5)
tk.Button(frame_selection, text="📁 Choisir un dossier de sauvegarde", command=choisir_dossier, bg="skyblue").pack(anchor="w", padx=10, pady=2)

# Sélection du dossier clé
lbl_clé = tk.Label(frame_selection, text="Aucun dossier clé sélectionné", fg="red", wraplength=400, bg="white")
lbl_clé.pack(anchor="w", padx=10, pady=5)
tk.Button(frame_selection, text="🔑 Choisir un dossier pour les clés", command=choisir_d_clé, bg="skyblue").pack(anchor="w", padx=10, pady=(2, 10))

# === Partie 2: GESTION DES CLÉS ===
frame_clés = tk.Frame(root, bg="white", relief="sunken", bd=2)
frame_clés.pack(padx=10, pady=10, fill="both", expand=False)

tk.Label(frame_clés, text="2. GESTION DES CLÉS", font=("Arial", 12, "bold"), bg="white").pack(anchor="w", padx=10, pady=(10, 5))

lbl_clés_status = tk.Label(frame_clés, text="❌ Aucune clé générée", fg="red", bg="white")
lbl_clés_status.pack(anchor="w", padx=10, pady=5)

tk.Button(frame_clés, text="🔐 Générer les clés RSA", command=window_generer_clés, bg="lightgreen", 
          font=("Arial", 10, "bold")).pack(padx=10, pady=(5, 10), fill="x")

# === Partie 3: CRYPTAGE/DÉCRYPTAGE ===
frame_crypto = tk.Frame(root, bg="white", relief="sunken", bd=2)
frame_crypto.pack(padx=10, pady=10, fill="both", expand=True)

tk.Label(frame_crypto, text="3. CRYPTAGE & DÉCRYPTAGE", font=("Arial", 12, "bold"), bg="white").pack(anchor="w", padx=10, pady=(10, 5))

lbl_status = tk.Label(frame_crypto, text="En attente", fg="gray", bg="white")
lbl_status.pack(anchor="w", padx=10, pady=5)

# Boutons d'action
button_frame = tk.Frame(frame_crypto, bg="white")
button_frame.pack(padx=10, pady=(5, 10), fill="x")

tk.Button(button_frame, text="🔒 Chiffrer", command=window_crypt, bg="orange", 
          font=("Arial", 10, "bold"), width=20).pack(side="left", padx=5)

tk.Button(button_frame, text="🔓 Déchiffrer", command=window_uncrypt, bg="lightblue", 
          font=("Arial", 10, "bold"), width=20).pack(side="left", padx=5)

# Bouton quitter
tk.Button(root, text="❌ Quitter", command=root.quit, bg="red", fg="white", 
          font=("Arial", 10, "bold")).pack(pady=10, fill="x", padx=10)

# Lancer l'interface graphique
root.mainloop()