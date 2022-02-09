from tkinter import *

# creer une premier fenetre
window = Tk()

# personnaliser cette fenetre

window.title("My Application")
window.geometry("1080x720")
window.minsize(250, 250)
window.iconbitmap("chef.ico")

window.config(background='#41B77F')

# ajouter un premier texte
label_title = Label(window, text="Bienvenue sur l application", font=("Arial", 40), bg='#41B77F', fg='white')
label_title.pack()

# afficher
window.mainloop()
