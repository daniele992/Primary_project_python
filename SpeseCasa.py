import tkinter as tk
from tkinter import *                   #importiamo tool per creazione interfacce grafiche


window = tk.Tk()                         #creiamo la finestra
window.geometry("600x600")               # personalizziamo la finestra
window.title("HOMEPAGE")                 #Titolo della nostra finestra
window.resizable(False, False)           #permette di non modificare grandezza finestra
window.configure(background="green")     #impostiamo sfondo della finestra

def formRegistrati():                    #creiamo la funzione per il form di registrazione
    windowRegistrati = tk.Tk()                    #creiamo la finestra inizializzando la varabile
    windowRegistrati.geometry("600x600")          #personalizziamo la finestra con larghezza e lunghezza

    #RIGHE (16-17) creazione titolo della pagina
    label_title = Label(windowRegistrati, text="REGISTRATION",width="20",font=("bold", 20))
    label_title.place(x=90,y=53)

    #(RIGHE 19-22) Creiamo campo inserimento per il Fullname
    label_fullname = Label(windowRegistrati, text="Fullname",width="20",font=("bold", 10))
    label_fullname.place(x=80,y=130)
    entry_fullname = Entry(windowRegistrati)
    entry_fullname.place(x=240,y=130)

    #(RIGHE 26-29) Creiamo campo inserimento per email
    label_email = Label(windowRegistrati, text="Email",width="20",font=("bold", 10))
    label_email.place(x=68,y=180)
    entry_email = Entry(windowRegistrati)
    entry_email.place(x=240,y=180)

    #(RIGHE 32-36) Creiamo radiobutton per scelta gender
    label_gender = Label(windowRegistrati, text="Gender",width="20",font=("bold", 10))
    label_gender.place(x=70,y=230)
    var = IntVar()
    Radiobutton(windowRegistrati, text="Male",padx = 5,variable = var, value = 1).place(x=235,y=230)
    Radiobutton(windowRegistrati, text="Female",padx = 20,variable=var, value = 2).place(x=290,y=230)

    #(RIGHE 39-42) Creiamo campo inserimento per la password
    label_password = Label(windowRegistrati, text="Password",width="20",font=("bold", 10))
    label_password.place(x=80,y=280)
    entry_password = Entry(windowRegistrati)
    entry_password.place(x=240,y=280)

    #creiamo il tasto per il submit, con width diamo la lunghezza, bg il colore del tasto, fg colore del testo
    Button(windowRegistrati, text="submit", width="30", bg="green", fg="white").place(x=180,y=380)

    #creiamo tasto per distruggere la pagina
    quitButtonRegistration = Button(windowRegistrati, text="quit", width="30", bg="red", fg="white",
    command=windowRegistrati.destroy)
    quitButtonRegistration.place(x=180,y=420)


    window2.mainloop() #avviamo la finestra
#fine della funzione registrati

def form_Login():                  #creiamo funzione per il login
    windowLogin = tk.Tk()              #creiamo la finestra login
    windowLogin.geometry("600x600")    #personalizziamo la finestra

    #(RIGHE 55-56)creiamo il titolo per la nostra finestra di login
    label_title = Label(windowLogin, text="LOGIN",width="20",font=("bold", 20))
    label_title.place(x=90,y=53)

    #(RIGHE 59-62) creiamo campo per inserimento email
    label_email = Label(windowLogin, text="Email",width="20",font=("bold", 10))
    label_email.place(x=80,y=130)
    entry_email = Entry(windowLogin)
    entry_email.place(x=240,y=130)

    #(RIGHE 65-68) creiamo campo inserimento password
    label_password = Label(windowLogin, text="Password",width="20",font=("bold", 10))
    label_password.place(x=68,y=180)
    entry_password = Entry(windowLogin)
    entry_password.place(x=240,y=180)

    #creiamo tasto per inviare i dati
    Button(windowLogin, text="submit", width="30", bg="green", fg="white").place(x=180,y=380)

    #creiamo tasto per distruggere la pagina
    quitButton = Button(windowLogin, text="quit", width="30", bg="red", fg="white", command=windowLogin.destroy)
    quitButton.place(x=180,y=420)

    windowLogin.mainloop()
#fine della funzione login

#(RIGHE 76-77) creiamo tasto registrati nella nostra homepage
buttonRegistrati = tk.Button(text="Registrati", command=formRegistrati)  #inizializzazione button login
buttonRegistrati.grid(row=0, column=0)

#(RIGHE 80-81) creiamo tasto login nella nostra homepage
buttonLogin = tk.Button(text="Login", command=form_Login)
buttonLogin.grid(row=0,column=2)

if __name__ == "__main__":
    window.mainloop()
