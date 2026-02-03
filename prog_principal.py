from f_decrypt import *
from f_crypt import *
from tkinter import *
from tkinter import filedialog

def decrypt_interface():
    root = Tk()
    root.title('Déchiffrement RSA')

    Label(root, text='Fichier chiffré:').grid(row=0, column=0)
    fichier_entry = Entry(root)
    fichier_entry.grid(row=0, column=1)
    Button(root, text='Parcourir', command=lambda: fichier_entry.insert(0, filedialog.askopenfilename())).grid(row=0, column=2)

    Label(root, text='Clé publique:').grid(row=1, column=0)
    keyPub_entry = Entry(root)
    keyPub_entry.grid(row=1, column=1)
    Button(root, text='Parcourir', command=lambda: keyPub_entry.insert(0, filedialog.askopenfilename())).grid(row=1, column=2)

    Label(root, text='Clé privée:').grid(row=2, column=0)
    keyPriv_entry = Entry(root)
    keyPriv_entry.grid(row=2, column=1)
    Button(root, text='Parcourir', command=lambda: keyPriv_entry.insert(0, filedialog.askopenfilename())).grid(row=2, column=2)

    def decrypt_action():
        fichier = fichier_entry.get()
        keyPub = keyPub_entry.get()
        keyPriv = keyPriv_entry.get()
        decrypted_text = decrypt(fichier, cléPub(keyPub), cléPriv(keyPriv))
        print(decrypted_text)

    Button(root, text='Déchiffrer', command=decrypt_action).grid(row=3, column=1)
    root.mainloop()

début = __name__ == '__main__'
if début:
    decrypt_interface()
