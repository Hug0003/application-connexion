

import tkinter
from tkinter import*
import os


def inscription_code():
    nom_inscrpition = Nom_inscription_Entry.get()
    pass_inscription = Pass_inscription_Entry.get()
    file_inscription_name = os.listdir()
    if str(nom_inscrpition)+".txt"in file_inscription_name:
        print("Erreur 3 : Le nom d'utilisteur est déja pris")
    else:
        file=open(str(nom_inscrpition)+".txt","w")
        file.write(str(nom_inscrpition)+":"+str(pass_inscription))
        file.close()
        print("Message 2 : votre compte a été créer avec succes")


def mdp_oublie ():
    indice_ps = Toplevel(fenetre)
    indice_ps.title("indice du mot de passe")
    indice_ps.config(bg="#454e78")
    indice_ps.geometry("1280x720+20+20")
    canevas= Canvas(indice_ps,width=1280, height=720,bg="#454e78")
    canevas.place(x=0,y=0)

    # si la case oui est coché faire ça( dans la variables "oui_indice"
    def oui_indice_ps():
        label_indice = Label(canevas, text="Non force à toi.",font=("Time Nex Roman", 15, "bold"), bg='white', fg='black')
        label_indice.place(x=370, y=300)

    # si la case non est coché faire ça(dans la variable "non_indice"
    def non_indice_ps():
        label_indice_non = Label(canevas,text="                                        Bon courage                                    ",font=("Time Nex Roman", 15, "bold"), bg='white', fg='black')
        label_indice_non.place(x=370, y=300)

    # bouton quitter la page canevas et fenetre
    def bouton_quitter_ps():
        exit()

    # afficher la question pour savoir si l utilisateur veut un indice
    indice_ps = Label(canevas, text="tu veux des indices pour trouver le mot de passe?",font=("Time Nex Roman", 15, "bold"), bg="white", fg="black")
    indice_ps.place(x=400, y=200)

    # afficher le bouton qui permet a l utilisateur de choisir s'il veut un indice("oui")
    oui_indice = Button(canevas, text=" oui ", font=("Time Nex Roman", 15, "bold"), bg="white", fg="black",justify="center", command=oui_indice_ps)
    oui_indice.place(x=520, y=250)

    # afficher le bouton qui permet a l utilisateur de choisir s'il ne veut pas d'un indice("non")
    non_indice = Button(canevas, text=" non ", font=("Time Nex Roman", 15, "bold"), bg="white", fg="black",justify="center", command=non_indice_ps)
    non_indice.place(x=700, y=250)

    bouton_exit = Button(canevas, text="quitter", font=("Time Nex Roman", 15, "bold"), bg="#white", fg="black",justify="center", command=bouton_quitter_ps)
    bouton_exit.place(x=100, y=600)

    indice_ps.mainloop()



def login_code():
    nom_login= Nom_Login_Entry.get()
    pass_login=Pass_Login_Entry.get()
    file_login_name=os.listdir()
    if str(nom_login)+".txt"in file_login_name:
        file1=open(str(nom_login)+".txt","r")
        list_info_login = file1.read().split(":")
        file1.close()
        if pass_login == list_info_login[1]:
            print("Message 1 : votre nom et mot de passe sont correct")
            fenetre_valider_login = Tk()
            fenetre_valider_login.title("login:")
            fenetre_valider_login.geometry("1280x720+20+20")
            fenetre_valider_login.config(bg="#99b2d1")

            acceder_au_compte = Label(fenetre_valider_login, text="bienvenue sur votre espace de surprise",font=("Time Nex Roman", 18, "bold"), bg="#8fb086")
            acceder_au_compte.place(x=400, y=20)
            decouvert_surprise=Label(fenetre_valider_login,text="bon comme t'es casses couilles tu as trouvé:",font=("Time Nex Roman", 14, "bold"), bg="#8fb086")
            decouvert_surprise_=Label(fenetre_valider_login,text="Juste bravo.",font=("Time Nex Roman", 16, "bold"), bg="#8fb086")
            _decouvert_surprise_=Label(fenetre_valider_login,text="Voila tu peux partir.",font=("Time Nex Roman", 13, "bold"), bg="#c70039")
            decouvert_surprise.place(x=10,y=340)
            decouvert_surprise_.place(x=10,y=370)
            _decouvert_surprise_.place(x=50,y=650)
        else:
            print("Erreur 2 : le mot de passe est incorrect")
    else:
        print("Erreur 1 : l'identifiant n'existe pas")




def login_fenetre_open():
#prenom
    fenetre_login=Tk()
    fenetre_login.title("login:")
    fenetre_login.geometry("1280x720+20+20")
    fenetre_login.config(bg="#99b2d1")
    login_frame=Frame(fenetre_login,bg="#99b2d1")
    Nom=Label(login_frame,text="prénom:",font=("Time Nex Roman", 15, "bold"),width=15,height=1,bg="#b7af94",fg="black")
    Nom.grid(row=0,column=0)
    global Nom_Login_Entry
    Nom_Login_Entry=Entry(login_frame,font=("Time Nex Roman", 15, "bold"),bg="white",fg="black",width=25)
    Nom_Login_Entry.grid(row=0,column=1)



    mainmenu = tkinter.Menu(fenetre_login)  # changer en login_bouton

    proposition = tkinter.Menu(mainmenu)
    proposition.add_radiobutton(label="1234")
    proposition.add_radiobutton(label="le gogo 3000")
    proposition.add_radiobutton(label="différent")
    proposition.add_radiobutton(label="faut qu'on se bouge le cul")
    proposition.add_radiobutton(label="le sport c est trop génial")
    proposition.add_radiobutton(label="I love doing legs")
    proposition.add_radiobutton(label="mot de passe")
    proposition.add_radiobutton(label="i'm fucking rich!!")
    proposition.add_radiobutton(label="Non")


    mainmenu.add_cascade(label="proposition mot de passe", menu=proposition)

    fenetre_login.config(menu=mainmenu)


#Space
    Space=Label(login_frame,text="",bg="#99b2d1",height=1)
    Space.grid(row=1,column=0)


#mot de passe
    Pass=Label(login_frame,text="mot de passe:",font=("Time Nex Roman", 15, "bold"),width=15,height=1,bg="#b7af94",fg="black")
    Pass.grid(row=2,column=0)
    global Pass_Login_Entry
    Pass_Login_Entry=Entry(login_frame,font=("Time Nex Roman", 15, "bold"),bg="white",fg="black",width=25)
    Pass_Login_Entry.grid(row=2,column=1)

#Space
    Space=Label(login_frame,text="",bg="#99b2d1",height=1)
    Space.grid(row=4,column=0)


#bouton_login
    valider_bouton=Button(login_frame,text="valider",font=("Time Nex Roman", 15, "bold"),bg="white",fg="black",command=login_code)
    valider_bouton.grid(row=4,column=1)


    oublier_boutotn=Button(login_frame,text="mot de passe oublié",font=("Time Nex Roman", 15, "bold"),bg="white",fg="black",command= mdp_oublie)
    oublier_boutotn.grid(row=5,column=1)


    login_frame.pack(expand=YES)
    login_bouton.mainloop()





def inscription_fenetre_open():
#prenom
    inscription_login=Tk()
    inscription_login.title("inscription:")
    inscription_login.geometry("1280x720+20+20")
    inscription_login.config(bg="#99b2d1")
    inscription_frame=Frame(inscription_login,bg="#99b2d1")
    Nom=Label(inscription_frame,text="prénom:",font=("Time Nex Roman", 15, "bold"),width=15,height=1,bg="#b7af94",fg="black")
    Nom.grid(row=0,column=0)
    global Nom_inscription_Entry
    Nom_inscription_Entry=Entry(inscription_frame,font=("Time Nex Roman", 15, "bold"),bg="white",fg="black",width=25)
    Nom_inscription_Entry.grid(row=0,column=1)

#Space
    Space=Label(inscription_frame,text="",bg="#99b2d1",height=1)
    Space.grid(row=1,column=0)


#mot de passe
    Pass=Label(inscription_frame,text="mot de passe:",font=("Time Nex Roman", 15, "bold"),width=15,height=1,bg="#b7af94",fg="black")
    Pass.grid(row=2,column=0)
    global Pass_inscription_Entry
    Pass_inscription_Entry=Entry(inscription_frame,font=("Time Nex Roman", 15, "bold"),bg="white",fg="black",width=25)
    Pass_inscription_Entry.grid(row=2,column=1)

#Space
    Space=Label(inscription_frame,text="",bg="#99b2d1",height=1)
    Space.grid(row=4,column=0)


#bouton_inscriptiion
    bouton_inscription=Button(inscription_frame,text="inscription",font=("Time Nex Roman", 15, "bold"),bg="white",fg="black",command=inscription_code)
    bouton_inscription.grid(row=4,column=1)

    quitter=Button(inscription_login,text="quitter",font=("Time Nex Roman", 15, "bold"),bg="white",fg="black",command=exit)
    quitter.place(x=50,y=600)

    inscription_frame.pack(expand=YES)
    inscription_login.mainloop()






fenetre=Tk()
fenetre.title("st valentin")
fenetre.geometry("1280x720+20+20")
fenetre.config(bg="#007082")
fenetre_frame= Frame(fenetre,width=1000,height=600,bg="black")
mainmenu=tkinter.Menu(fenetre)#changer en login_bouton
#creation du bouton Login
login_bouton= Button(fenetre_frame,text="connexion",font=("Time Nex Roman", 15, "bold"), bg="white", fg='black',width=8,height=3,command=login_fenetre_open)
login_bouton.grid(row=0,column=0)

inscription_bouton= Button(fenetre_frame,text="inscription",font=("Time Nex Roman", 15, "bold"), bg="white", fg='black',width=8,height=3,command=inscription_fenetre_open)
inscription_bouton.grid(row=0,column=1)




fenetre_frame.pack(expand=YES)
fenetre.mainloop()
















































