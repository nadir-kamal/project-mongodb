import tkinter
from subprocess import call
from tkinter import ttk, Tk
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import tkinter as tk
from PIL import Image, ImageTk
import mysql.connector
from tkinter import filedialog

import requests
import json

# URLs
url_find = "https://eu-west-2.aws.data.mongodb-api.com/app/data-fxpru/endpoint/data/v1/action/findOne"

# Database and collection names
database_name = "students"
collection_name = "colstud"

# Common headers for MongoDB API requests
headers = {
    'Content-Type': 'application/json',
    'Access-Control-Request-Headers': '*',
    'api-key': 'r6sCYqd6LJ0PDvhq6zuS02zeeI8U9KKKWQs2RscJCQZnrlGj0uhIdd8mkeUE6YD5',
}

def get_document_by_employee_id(employee_id):
    try:
        # Payload for MongoDB API request (find)
        filter_criteria = {"tag_data": employee_id}
        find_payload = {
            "collection": collection_name,
            "database": database_name,
            "dataSource": "Cluster0",
            "filter": filter_criteria
        }

        # Find a document in MongoDB
        find_response = requests.post(url_find, headers=headers, json=find_payload)

        if find_response.status_code == 200:
            found_document = find_response.json().get("document", {})
            return found_document
        else:
            print(f"Error querying MongoDB. Status Code: {find_response.status_code}")
            return None

    except KeyboardInterrupt:
        print("\nScript interrupted by user.")
        return None

# Example usage of the function
employee_id_to_search = "123456789"  # Replace with the employee_id you want to search
found_document = get_document_by_employee_id(employee_id_to_search)

# Remplir data_list avec les données du document trouvé
data_list = [
    (
        found_document.get("tag_data", ""),
        found_document.get("user_name", ""),
        found_document.get("employee_id", ""),
        found_document.get("department", ""),
        found_document.get("position", ""),
        found_document.get("email", ""),
        found_document.get("attendance_time", "")
    )
]

#actualiser
def actualiser():
    root.destroy()
    call(["python", "gestion.py"])

#ajouter

def Ajouter():
    pass

#Modifier
def Modifer():
    pass


#Supprimer
def Supprimer():
    pass


#Ma fenetre
root = Tk()

root.title('Fenetre de connexion')
root.geometry('1400x930+100+50')
root.configure(bg="#091821")
root.resizable(True, True)

# Charger l'image que vous souhaitez utiliser pour l'icône
icon = tkinter.PhotoImage(file="images\\back.png")

# Définir l'icône de la fenêtre principale
root.iconphoto(True, icon)

img=Image.open("images\\emp.jpg")
img = img.resize((1400,930), resample=Image.LANCZOS)

root.photoimg=ImageTk.PhotoImage(img)

f_lbl=Label(root,image=root.photoimg)
f_lbl.place(x=0,y=0,width=1400,height=930)

#Ajouter le titre

title_lbl = Label(root, text="Gestion Des Etudiants ", font=("Microsoft Himalaya", 40, "bold"),
                          bg="#091821", fg="#57a1f8")
title_lbl.place(x=0, y=50, width=1400, height=50)


#details des personnes

#Matricule
LblNumero=Label(root, text="MATRICULE", font=("Arial", 18), bg="#091821", fg="white")
LblNumero.place (x=20, y=150, width=180)
txtNumero= Entry(root, bd=4, font=("Arial", 14))
txtNumero.place (x=220, y=150, width=300)

#Nom

lblnom =Label(root, text="NOM", font=("Arial", 18), bg="#091821", fg="white")
lblnom.place(x=20, y=200, width=180)
txtnom =Entry(root, bd=4, font=("Arial", 14))
txtnom.place(x=220, y=200, width=300)

#Prenom
lblprenom=Label(root, text="PRENOM", font=("Arial", 18), bg="#091821", fg="white")
lblprenom.place (x=20, y=250, width=180, )
txtprenom = Entry (root, bd=4, font=("Arial", 14))
txtprenom.place (x=220, y=250, width=300)

#sexe

valeurSexe = StringVar()
lblSexeMasculin = Radiobutton (root, text="MASCULIN", value="M", variable=valeurSexe, indicatoron=0, font=("Arial", 14), cursor="hand2", bg="#091821", fg="#57a1f8")
lblSexeMasculin.place(x=220, y=300, width=130)
txtSexeFeminin =Radiobutton(root, text="FEMININ", value="F", variable=valeurSexe, indicatoron=0, font=("Arial", 14), cursor="hand2", bg="#091821", fg="#57a1f8")
txtSexeFeminin.place(x=390, y=300, width=130)

#Departement
lblClasse = Label(root, text="DEPARTEMENT", font=("Arial", 18), bg="#091821", fg="white")
lblClasse.place(x=20, y=350, width=180, )

comboClasse = ttk.Combobox (root, font=("Arial", 14))
comboClasse['values'] = ['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9']
comboClasse.place(x=220, y=350, width=300)

#Specialite
lblmatiere = Label(root, text="SPECIALITE", font=("Arial", 18), bg="#091821", fg="white")
lblmatiere.place (x=20, y=400, width=180, )
txtmatiere =Entry(root,bd=4, font=("Arial", 14))
txtmatiere.place(x=220, y=400, width=300)

btnenregistrer = Button(root, text="AJOUTER PERSONNE", font=("Microsoft Himalaya", 20, "bold"), cursor="hand2",bg='#57a1f8', fg='white',command=Ajouter)
btnenregistrer.place(x=220, y=500, width=300, height=30)

btnmodifier = Button(root, text="MODIFIER PERSONNE", font=("Microsoft Himalaya", 20, "bold"), cursor="hand2", bg='#57a1f8', fg='white',command=Modifer)
btnmodifier.place(x=220, y=550, width=300, height=30)

btnsupprimmer = Button(root, text="SUPPRIMER PERSONNE", font=("Microsoft Himalaya", 20, "bold"), cursor="hand2", bg='#57a1f8', fg='white',command=Supprimer)
btnsupprimmer.place(x=220, y=600, width=300, height=30)



title_table = Label(root, text="Liste Des Etudiants ",font=("Microsoft Himalaya", 20, "bold"),bg='#57a1f8', fg='white',)
title_table.place(x=620, y=150, width=720, height=35)


#Table
table=ttk. Treeview (root, columns = (1, 2, 3, 4, 5, 6,7), height=5,show="headings")
table.place(x=620, y = 190, width = 720, height = 450)


#Entete
table.heading(1 ,text = "tag_data")
table.heading(2 , text = "user_name")
table.heading(3 , text = "employee_id")
table.heading(4 , text = "department")
table.heading(5 , text = "position")
table.heading(6 , text = "email")
#table.heading(7 , text = "image")
table.heading(7 , text = "attendance_time")

#definir les dimentions des colonnes
table.column(1, width = 80)
table.column(2, width = 100)
table.column(3, width = 100)
table.column(4, width = 50)
table.column(5, width = 100)
table.column(6, width = 100)
#table.column(7, width = 50)
table.column(7, width = 80)


# afficher les informations de la table

# Boucle pour ajouter chaque ligne de données au tableau
for data in data_list:
    table.insert("", "end", values=data)


#Execution
root.mainloop()