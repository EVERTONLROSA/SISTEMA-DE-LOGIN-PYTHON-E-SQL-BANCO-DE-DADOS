index.py
#Importar as bibliotecas
from TKinter import *
from TKinter import messagebox 
from TKinter import ttk
import DataBaser 

#Criar nossa janela
jan = TK()
jan.title('#EVE>>> - Acess panel')
jan.geometry('600x300')
jan.configure(background='while')
jan.resizable(width=false,height=false)
jan.attributes("-alpha", 0.9)

#===== Carregando Imagens ============
logo = PhotoImage(file="Icons/logo.png")

#===== Widegts ==================
LeftFrame = Frame(jan, width=200, height=300, bg="MIDNIGHTBLUE", relief="raise")
LeftFrame.pack(side=LEFT)

Rightframe = Frame(jan, width=395, height=300, bg="MIDNIGHTBLUE", relief="raise")
Rightframe.pack(side=RIGHT)

LogoLabel = Label(Letframe, image=logo, bg="MIDNIGHTBLUE")
LogoLabel.place(x=50, y=100)

UserLabel = Label(Rightframe, Text="Username:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
UserLabel.place(x=5, y=100)

UserEntry = ttk.Entry(RightFrame, width=30)
UserEntry.place(x=150, y=110)

PassLabel = Label(Rightframe, Text="Password:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
PassLabel.place(x=5, y=200)

PassEntry = ttk.Entry(RightFrame, width=30, show= ".")
PassEntry.place(x=150, y=220)

def Login():
    User = UserEntry.get()
    Pass = PassEntry.get()

    DataBaser.cursor.execute("""
    SELECT * FROM Users
    WHERE (User = ? and Password = ?)
    """ , (User,Pass))
    print("Selecionou")
    VerifyLogin = DataBaser.cursor.fetchone 
    try:
    if (User in VerifyLogin and Pass in VerifyLogin):
         messagebox.showinfo(title="Login Info",message="Acesso Confirmado. Bem vindo!")
    except:
         messagebox.showinfo(title="Login Info",message="Acesso Negado. Verifique se está cadastrado no sistema")

#Botoes
LoginButton = ttk.Button(RightFrame, text="Login", width=30, command=login)
LoginButton.place(x=100, y=225)

def register():
    #Removendo Widegtes de Login
    LoginButton.place(x=5000)
    RegisterButton.place(x=5000)
    #Removendo Widegtes de Cadastro
    NomeLabel = Label(RightFrame, text="Name:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")  
    NomeLabel.place(x=5, y=5)

    NomeEntry = ttk.Entry(RightFrame, width=39)
    NomeEntry.place(x=100, y=10)
   
    EmailLabel = Label(RightFrame, text="Email:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
    EmailLabel.place(x=5, y=55)

    EmailEntry = Entry(RightFrame, width=39)
    EmailEntry.place(x=100, y=66)

    def RegisterToDataBase():
          Name = NomeEntry.get()
          Email = EmailEntry.get()
          User = UserEntry.get()
          Pass = PassEntry.get()

if (Name == "" and Email =="" and User =="" and Pass ==""):
          messagebox.showerror(title="Register Error", message="Não deixe Nenhum campo Vazio. Preencha Todos os Campos")
else:   
        DataBaser.cursor.execute("""
        INSERT INTO(Users(Name, Email, User, Password) VALUES(?,?,?,?)
        """, (Name, Email, User, Pass))
        DataBaser.conn.commit()
        Messagebox.showinfo(title="Register Info",message="Conta Criada Com Sucesso")
            
    Register = ttk.Button(RightFrame, text="Register", width=30, command =  RegisterToDataBase)
    Register.place(x=100, y=225)

    def BackToLogin():
         #Removendo Widegtes de Cadastro
         NomeLabel.place(x=5000)
         NomeEntry.place(x=5000)
         EmailLabel.place(x=5000)
         EmailEntry.place(x=5000)
         Register.place(x=5000)
         Back.place(x=5000)

    Back = ttk.Button(RightFrame, text="Register", width=30, command=BackToLogin)
    Back.place(x=125, y=260)
    #Trazendo de volta os Widegtes do Login
    LoginButton.place(x=100)
    RegisterButton.place(x=125)
  


RegisterButton = ttk.Button(RightFrame, text="Register", width=20, command = Register )
RegisterButton.place(x=125, y=260)



jan.mainloojan.mainloop()
