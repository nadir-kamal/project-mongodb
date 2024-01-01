from subprocess import call
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter
import customtkinter as ctk


#ctk.set_appearance_mode("dark")
#ctk.set_default_color_theme("dark-blue")


class Face_Recognition_System:
    def __init__(self, root):
        self.root = root

        self.root.geometry('1400x930+100+50')
        self.root.title('Système de présence intelligent')
        self.root.configure(bg="#fff")
        self.root.resizable(True, True)




        def gestion():
            #root.destroy()
            call(["python", "gestion.py"])

        def presence():
            #root.destroy()
            call(["python", "presence.py"])


        # Charger l'image que vous souhaitez utiliser pour l'icône
        icon = tkinter.PhotoImage(file="images\\back.png")

        # Définir l'icône de la fenêtre principale
        root.iconphoto(True, icon)


        '''#self.menu.entryconfig(0, bg="blue", fg="white")

        # Créer un menu pour les connexions
        self.menu_connexion = Menu(self.root, bg='#57a1f8', fg='white')
        self.menu_connexion.entryconfig = Menu(0, bg='#57a1f8', fg='white')
        self.root.config(menu=self.menu_connexion)

        # Ajouter un menu de connexion pour les administrateurs
        self.menu_admin = Menu(self.menu_connexion, tearoff=0, bg='#57a1f8', fg='white')
        self.menu_connexion.add_cascade(label="Responsable de presnce", menu=self.menu_admin)
        self.menu_admin.add_command(label="Se connecter", command=open_singIn_admin)

        # Ajouter un menu de connexion pour les techniciens
        self.menu_tech = Menu(self.menu_connexion, tearoff=0, bg='#57a1f8', fg='white')
        self.menu_connexion.add_cascade(label="Technicien (gestion des personnes) ", menu=self.menu_tech)
        self.menu_tech.add_command(label="Se connecter", command=open_singIn_tech)'''





        ###########################################################################################################################

        img = Image.open("images\\po\\bnbn.jpg")
        img = img.resize((1400, 930),  resample=Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)



        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=1400, height=930)

        title_lbl = Label(self.root, text="SYSTEME DE PRESENCE INTELLIGENT ", font=("Microsoft Himalaya", 40, "bold"),
                          bg="#091821", fg="#57a1f8")
        title_lbl.place(x=0, y=50, width=1400, height=50)

        img1 = Image.open("images\\po\\yara.png")
        img1 = img1.resize((220, 200),  resample=Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        b1 = Button(self.root,border=0, image=self.photoimg1)
        b1.place(x=250, y=250, width=220, height=200)

        #Button(frame, width=39, pady=7, text='Sign in', bg='#57a1f8', fg='white', border=0, command=signin).place(x=35,y=204)

        b1_1 = Button(self.root, width=39, pady=7,border=0, text="gestion des etudiants", cursor="hand2",
                       bg='#57a1f8', fg='white', font=(0, 10,"bold"), command=gestion)
        b1_1.place(x=250, y=460, width=220, height=50)

        img3 = Image.open("images\\po\\this.jpg")
        img3 = img3.resize((220, 200), resample=Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        b2 = Button(self.root, border=0, image=self.photoimg3)
        b2.place(x=970, y=250, width=220, height=200)

        b2_1 = Button(self.root, width=39, pady=7, border=0, text="présence", cursor="hand2",
                       bg='#57a1f8', fg='white',  font=(0, 10, "bold"),command=presence)
        b2_1.place(x=970, y=460, width=220, height=50)

        ##########################################################################################################

        '''img6 = Image.open("images\\aide.jpg")
        img6 = img6.resize((220, 200), resample=Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b2 = Button(self.root, border=0, image=self.photoimg6)
        b2.place(x=970, y=450, width=220, height=200)

        b2_1 = Button(self.root, width=39, pady=7, border=0, text="Aide ?", cursor="hand2",
                      bg='#57a1f8', fg='white', font=(0, 10, "bold"), command=aide)
        b2_1.place(x=970, y=660, width=220, height=50)

        ##########################################################################################################

        img2 = Image.open("images\\emp.jpg")
        img2 = img2.resize((220, 200), resample=Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        b2 = Button(self.root,border=0, image=self.photoimg2)
        b2.place(x=330, y=450, width=220, height=200)

        b2_1 = Button(self.root, width=39, pady=7,border=0, text="Connexion en tant que technicien\n (gestion des personnes)", cursor="hand2",
                      bg='#57a1f8', fg='white', font=(0, 10, "bold"), command=open_singIn_tech)
        b2_1.place(x=330, y=660, width=220, height=50)'''

        #####################################################


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()