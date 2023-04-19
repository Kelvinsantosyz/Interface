import customtkinter
from banco import DatabaseConnection, UserDados
from tkinter import messagebox


customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')


class TelaCadastro:
    def __init__(self, master):
        self.master = master
        self.db = DatabaseConnection()
        self.master.geometry('1000x850')
        self.texto = customtkinter.CTkLabel(self.master, text='Buscar o id')
        self.texto.pack(padx=10, pady=10)

        self.buscar = customtkinter.CTkButton(self.master, text='Buscar', command=self.buscar_id)
        self.buscar.pack(padx=20, pady=12)

        self.entry_id = customtkinter.CTkEntry(self.master, placeholder_text='Digite o ID')
        self.entry_id.pack(padx=20, pady=12)

        self.texto = customtkinter.CTkLabel(self.master, text='Fazer Cadastro')
        self.texto.pack(padx=10, pady=10)
        
        self.nome = customtkinter.CTkEntry(self.master, placeholder_text='Nome')
        self.nome.pack(padx=20, pady=12)
        
        self.email = customtkinter.CTkEntry(self.master, placeholder_text='E-mail')
        self.email.pack(padx=20, pady=12)

        self.senha = customtkinter.CTkEntry(self.master, placeholder_text='senha', show='*')
        self.senha.pack(padx=20, pady=12)

        self.telefone = customtkinter.CTkEntry(self.master, placeholder_text='Telefone')
        self.telefone.pack(padx=20, pady=12)

        self.usuario = customtkinter.CTkEntry(self.master, placeholder_text='Usuario')
        self.usuario.pack(padx=20, pady=12)

        self.inserir = customtkinter.CTkButton(self.master, text='Inserir', command=self.inserir)
        self.inserir.pack(padx=20, pady=7)

        self.alterar = customtkinter.CTkButton(self.master, text='Alterar', command=self.alterar)
        self.alterar.pack(padx=20, pady=14)

        self.excluir = customtkinter.CTkButton(self.master, text='Excluir', command=self.excluir)
        self.excluir.pack(padx=20, pady=14)

    def buscar_id(self):
        id_usuario = self.entry_id.get()
        user = UserDados()
        result = user.selectUser(id_usuario)
        if result == "Usuário não encontrado.":
            messagebox.showinfo('Erro', 'ID não encontrado')
            
        if result == 'Busca feita com sucesso':
            messagebox.showinfo(f'{self.entry_id},{self.nome},{self.telefone},{self.email,self.usuario}')
            
        else:
            self.nome.delete(0, 'end')
            self.nome.insert(0, user.nome)
            self.telefone.delete(0, 'end')
            self.telefone.insert(0, user.telefone)
            self.email.delete(0, 'end')
            self.email.insert(0, user.email)


    def inserir(self):
        self.user = UserDados()
        self.user.nome = self.nome.get()
        self.user.email = self.email.get()
        self.user.senha = self.senha.get()
        self.user.telefone = self.telefone.get()
        self.user.usuario = self.usuario.get()
        self.user.create_user()
        # ...

  
    def alterar(self):
        self.user = UserDados()
        self.user.id_usuario = self.id_entry.get()
        self.user.nome = self.nome.get()
        self.user.telefone = self.telefone.get()
        self.user.email = self.email.get()
        self.user.usuario = self.usuario.get()
        self.user.senha = self.senha.get()
        message = self.user.update_user()
        # ...

    def excluir(self):
        self.user = UserDados()
        self.user.id_usuario = self.id_entry.get()
        message = self.user.delete_user()
        # ...

root = customtkinter.CTk()
TelaCadastro(root)
root.mainloop()
