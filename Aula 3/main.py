import customtkinter as ctk
from tkinter import *

window = ctk.CTk()
window.title("Teste")
window.geometry("900x550")
window.maxsize(width=900, height=550)
window.minsize(width=500, height=350)
window._set_appearance_mode("system")


def meses(escolha):
    print(f'O seu mês de nascimento é: {escolha}')

def new_window():
    new_win = ctk.CTkToplevel(window, fg_color="teal") 
    new_win.geometry("500x450")
    new_win.maxsize(width=900, height=550)
    new_win.minsize(width=500, height=350)

    # Aguardar alguns milissegundos antes de tentar trazer à frente e focar
    def bring_to_front():
        new_win.lift()

    new_win.after(100, bring_to_front)  # Executa após 100ms

# btn = ctk.CTkButton(window, text='Abrir nova janela', command=new_window)
# btn.place(x=290, y=200)

# aula 5 frame

# frame_master = ctk.CTkFrame(window, width=650, height=350, fg_color="blue")
# frame_master.place(x=50, y=170)

# frame1 = ctk.CTkFrame(frame_master, width=150, height=300, fg_color="teal")
# frame1.place(x=10, y=10)

# frame2 = ctk.CTkFrame(frame_master, width=150, height=300, fg_color="teal")
# frame2.place(x=250, y=10)  # Isso vai ultrapassar o frame_master, cuidado

# frame3 = ctk.CTkFrame(frame_master, width=150, height=300, fg_color="teal")
# frame3.place(x=460, y=10)  # Também pode sair para fora

#aula 6 tabview

# Tabview = ctk.CTkTabview(window, width=300, corner_radius=10, height=300,border_color="red", border_width=1,segmented_button_fg_color="teal",segmented_button_unselected_hover_color="red")
# Tabview.pack()
# Tabview.add("Nomes")
# Tabview.add("Idades")
# Tabview.add("Sexo")
# Tabview.tab("Nomes").grid_columnconfigure(0,weight=1)
# Tabview.tab("Idades").grid_columnconfigure(0,weight=1)
# Tabview.tab("Sexo").grid_columnconfigure(0,weight=1)

# # Adicionando elementos
# Nomes_Tabview = ctk.CTkLabel(Tabview.tab("Nomes"), text="Gabriel\nMarília")
# Nomes_Tabview.pack()

# Idades_Tabview = ctk.CTkLabel(Tabview.tab("Idades"), text="19\n17")
# Idades_Tabview.pack()

# Sexo_Tabview = ctk.CTkLabel(Tabview.tab("Sexo"), text="Gosta\nNão Gosta")
# Sexo_Tabview.pack()]

# Aula 7 textbox

# Caixa_Texto = ctk.CTkTextbox(window, width=300,height=150, scrollbar_button_color="teal",scrollbar_button_hover_color="blue" )
# Caixa_Texto.pack()
# Caixa_Texto.insert("0.0", "PlaceHolder\n" + "Sou gay\n"*20)

# Aula 9 menu 
""" 
ctk.CTkLabel(window, text='Menu de Opções', font=("arial light", 20)).pack(pady=20)

ctk.CTkLabel(window, text="Escolha seu mês de nascimento", font=("arial light", 20)).pack(pady=10)


mes = ctk.CTkOptionMenu(window, 
                values=["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outrubro","Novembro","Dezembro"], height=25, command=meses)

mes.pack(pady=10)
mes.set("Mês")


mes_var = ctk.StringVar(value="Mês")

mes = ctk.CTkComboBox(window, 
                values=["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outrubro","Novembro","Dezembro"] *30, height=30,width=150, command=meses,
                variable=mes_var,
                corner_radius=5,
                dropdown_font=('new times bold',14))

mes.pack(pady=10)
# """

# Aula 10

# ctk.CTkLabel(window, text='Teste', font=("Arial bolder", 20)).pack(pady=10)

# Label dinamico

# def Enviar():
#     entrada = entry.get()
#     resposta.configure(text='Seu nome é: ' + str(entrada),fg_color="#616363", corner_radius=5, anchor="w",font=("Arial", 15, "bold"))
#     pass
# lab = ctk.CTkLabel(window,
#                     text="Digite seu nome",
#                     width=200,
#                     height=25,
#                     font=("Arial bolda", 16))
# lab.pack(pady=10)
# entry = ctk.CTkEntry(window, width=200)
# entry.pack()

# ctk.CTkButton(window,text='Enviar', width=200, command=Enviar).pack(pady=10)


# resposta = ctk.CTkLabel(window, text="",width=200)
# resposta.pack()

# AULA 11

# entrada = ctk.CTkEntry(window,
#                     placeholder_text="Digite seu nome",
#                     width=200,
#                     )

# entrada.pack(pady=20)

# def catch():
#     print(entrada.get())
#     entrada.delete(0, END)



# ctk.CTkButton(window, width=50, text='Pegar texto', command=catch).pack()

# Aula 12

def evento():
    print('gay')

def new_window():
    new_win = ctk.CTkToplevel(window, fg_color="teal") 
    new_win.geometry("500x450")
    new_win.maxsize(width=900, height=550)
    new_win.minsize(width=500, height=350)

    # Aguardar alguns milissegundos antes de tentar trazer à frente e focar
    def bring_to_front():
        new_win.lift()

    new_win.after(100, bring_to_front)  # Executa após 100ms

ctk.CTkButton(window,
                text="Clique-me",
                command=new_window,
                width=70).pack(pady=10)

window.mainloop()
