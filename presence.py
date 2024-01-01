import os
import tkinter
from subprocess import call
from tkinter import ttk, Tk
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from PIL import Image, ImageTk
import csv
import mysql.connector
from datetime import datetime
from tkinter import filedialog
import pandas as pd
from mysql.connector import Error

from datetime import datetime

def open_folder():
    folder_path = r'C:\Users\viet\Desktop\comparaison\presence'
    if os.path.exists(folder_path):
        os.startfile(folder_path)
    else:
        messagebox.showerror("erreur", "Le dossier spécifié n'existe pas")
        #print("Le dossier spécifié n'existe pas")

def rapport():
    # Créer un tableau Tkinter
    presence_dir = 'presence'
    # obtenir la date d'aujourd'hui au format 'dd-mm-yyyy'
    today = datetime.today().strftime('%Y-%m-%d')

    # créer le nom de fichier avec la date d'aujourd'hui
    #now = datetime.now()
    file_name =  f"presence_{today}.csv"

    title_table = Label(root, text="Rapport ", font=("Microsoft Himalaya", 20, "bold"), bg='#57a1f8',
                                    fg='white', )
    title_table.place(x=400, y=150, width=780, height=35)
    table = ttk.Treeview(root, columns=("Nom_Prénom", "Présence", "Date"), show="headings")
    table.heading("Nom_Prénom", text="Identité: Matricule_Prénom_Nom")
    table.heading("Présence", text="Statut: Présence")
    table.heading("Date", text="Horodatage: Date de présence")
    table.place(x=400, y=200, width=780, height=450)
        # table.pack()

    with open(os.path.join(presence_dir, file_name), "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                    table.insert("", "end", values=(row["Matricule_Prénom_Nom"], row["Présence"], row["Date"]))

def import_csv():
    title_table = Label(root, text="Liste Des Personnes ", font=("Microsoft Himalaya", 20, "bold"), bg='#57a1f8',
                        fg='white', )
    title_table.place(x=400, y=150, width=780, height=35)

    table = ttk.Treeview(root, columns=(1, 2, 3, 4, 5, 6, 7), height=5, show="headings")
    table.place(x=400, y=200, width=780, height=450)

    # Entete
    table.heading(1, text="MAT")
    table.heading(2, text="NOM")
    table.heading(3, text="PRENOM")
    table.heading(4, text="SEXE")
    table.heading(5, text="DEPARTEMENT")
    table.heading(6, text="SPECIALITE")
    # table.heading(7 , text = "image")
    # table.heading(7 , text = "photo")

    # definir les dimentions des colonnes
    table.column(1, width=120)
    table.column(2, width=120)
    table.column(3, width=120)
    table.column(4, width=120)
    table.column(5, width=120)
    table.column(6, width=180)
    # table.column(7, width = 50)
    # table.column(7, width = 150)

    # afficher les informations de la table
    maBase = mysql.connector.connect(host="localhost", user="root", password="souadouth2002", database="personnes")
    meConnect = maBase.cursor()
    meConnect.execute("select * from gestperson")
    for row in meConnect:
        table.insert('', END, value=row)
    maBase.close()

'''
def import_csv():
    # Ouvrir une boîte de dialogue pour sélectionner le fichier CSV
    file_path = filedialog.askopenfilename()

    # Charger le fichier CSV dans un DataFrame pandas
    df = pd.read_csv("C:\\Users\\viet\\Desktop\\comparaison\\presence.csv")

    # Afficher le DataFrame dans la console
    print(df)

'''
#Ma fenetre
root = Tk()

root.title('Fenetre de connexion')
root.geometry('1530x790+0+0')
root.configure(bg="#091821")
root.resizable(False, False)

# Charger l'image que vous souhaitez utiliser pour l'icône
icon = tkinter.PhotoImage(file="images\\back.png")

# Définir l'icône de la fenêtre principale
root.iconphoto(True, icon)

img=Image.open("images\\po\\back-presence.png")
img = img.resize((1530,790), resample=Image.LANCZOS)

root.photoimg=ImageTk.PhotoImage(img)

f_lbl=Label(root,image=root.photoimg)
f_lbl.place(x=0,y=0,width=1530,height=790)

#Ajouter le titre

title_lbl = Label(root, text="Espace Administratif : Rappots de presence", font=("Microsoft Himalaya", 30, "bold"),
                          bg="#091821", fg="#57a1f8")
title_lbl.place(x=0, y=50, width=1530, height=50)



# Ajouter un bouton pour fermer la fenêtre
#button = tk.Button(root, text="OK", command=root.destroy)
#button.pack()

########################################################################################################################
'''now = datetime.now()
#presence_file = 'presence_{}.csv'.format(now.strftime('%Y-%m-%d'))

directory = 'images\\presence'

for filename in os.listdir(directory):
    if now.strftime('%Y-%m-%d') in filename:
        messagebox.showinfo("Présence enregistrée", "Rapport de présence disponible pour aujourd\'hui. Consulter votre rapport ici.")
        #print('Rapport de présence disponible pour aujourd\'hui')
        # code pour envoyer un e-mail au responsable avec le rapport de présence
        break
else:
    messagebox.showinfo("Présence non enregistrée", "Aucune présence détectée aujourd\'hui")
    #print('Aucune présence détectée aujourd\'hui')
    # code pour envoyer un e-mail au responsable indiquant que la présence n'a pas été détectée
########################################################################################################################
# Afficher une boîte de dialogue
#messagebox.showinfo("Présence enregistrée", "La présence a été bien marquée. Consulter votre rapport ici.")'''


img1 = Image.open("images\\q.jpg")
img1 = img1.resize((220, 200), resample=Image.LANCZOS)
photoimg1 = ImageTk.PhotoImage(img1)

b1 = Button(root,border=0, image=photoimg1)
b1.place(x=30, y=150, width=220, height=200)

img2 = Image.open("images\\po\\top.jpg")
img2 = img2.resize((220, 200),  resample=Image.LANCZOS)
photoimg2 = ImageTk.PhotoImage(img2)

b1 = Button(root,border=0, image=photoimg2)
b1.place(x=30, y=450, width=220, height=200)

#title_lbl = Label(root, text="Bienvenus sur votre espace ",font=("Microsoft Himalaya", 40), bg="#B5DEF2", fg="#004dcf")
#title_lbl.place(x=280, y=150, width=780, height=450)


#boutons

btnlisteperson = Button(root, text="Liste Des Personnes", font=(0, 10, "bold"),  bg='#57a1f8', fg='white',cursor="hand2",command=import_csv)
btnlisteperson.place(x=30, y=360, width=220, height=50)
btnrapport = Button(root, text="Rapport d'Aujourd'hui",  font=(0, 10, "bold"),  bg='#57a1f8', fg='white',cursor="hand2",command=rapport)
btnrapport.place(x=30, y=660, width=220, height=50)

img5 = Image.open("images\\po\\bro.jpg")
img5 = img5.resize((220, 200), resample=Image.LANCZOS)
root.photoimg5 = ImageTk.PhotoImage(img5)

b2 = Button(root, border=0, image=root.photoimg5)
b2.place(x=1270, y=150, width=220, height=200)

b2_1 = Button(root, width=39, pady=7, border=0, text="Archive Des Rapports", cursor="hand2",
                       bg='#57a1f8', fg='white',  font=(0, 10, "bold"),command=open_folder)
b2_1.place(x=1270, y=360, width=220, height=50)

'''
# Créer un tableau Tkinter
table = ttk.Treeview(root, columns=("Nom_Prénom", "Présence", "Date"), show="headings")
table.heading("Nom_Prénom", text="Identité: Nom_Prénom")
table.heading("Présence", text="Statut: Présence")
table.heading("Date", text="Horodatage: Date de présence")
table.place(x =280, y=  150, width = 780, height = 450)
#table.pack()

with open("presence.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        table.insert("", "end", values=(row["Nom_Prénom"], row["Présence"], row["Date"]))


#Table
table=ttk. Treeview (root, columns = (1, 2, 3, 4, 5, 6,7), height=5,show="headings")
table.place(x =280, y=  150, width = 780, height = 450)


#Entete
table.heading(1 ,text = "MAT")
table.heading(2 , text = "NOM")
table.heading(3 , text = "PRENOM")
table.heading(4 , text = "SEXE")
table.heading(5 , text = "DEPARTEMENT")
table.heading(6 , text = "SPECIALITE")
#table.heading(7 , text = "image")
#table.heading(7 , text = "photo")

#definir les dimentions des colonnes
table.column(1, width = 50)
table.column(2, width = 150)
table.column(3, width = 150)
table.column(4, width = 100)
table.column(5, width = 50)
table.column(6, width = 100)
#table.column(7, width = 50)
#table.column(7, width = 150)


# afficher les informations de la table
maBase= mysql.connector.connect(host="localhost", user="root", password="souadouth2002", database="personnes")
meConnect = maBase.cursor()
meConnect.execute("select * from gestperson")
for row in meConnect:
    table.insert('', END, value=row)
maBase.close()
'''

#Execution
root.mainloop()