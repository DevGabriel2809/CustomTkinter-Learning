import customtkinter as ctk
from tkinter import *
from PIL import *

window = ctk.CTk(fg_color="teal")
window.title("Teste")
window.geometry("700x450")
window.maxsize(width=900, height=550)
window.minsize(width=500, height=350)
window._set_appearance_mode("system")

texto = ctk.CTkLabel(window, text="Teste de função do botão para colar", font=("Arial", 20, 'bold'))
texto.place(x=30, y=15)

def colar():
    texto_copiado = window.clipboard_get() #Pegar texto da caixa de trasferência
    entrada.insert("insert", texto_copiado)
    entrada.focus()
    # entrada = texto_copiado
    saida.configure(text="O número do processo é:" + str(texto_copiado))
    pass

entrada = ctk.CTkEntry(window,
                        placeholder_text="Nº Processo",
                        width=350,height=35, 
                        corner_radius=7,
                        text_color="black",
                        fg_color="#d7dcde")
entrada.place(x=30,y=50)

img_paste = ctk.CTkImage(light_image=Image.open("./colagem.png"), dark_image=Image.open("./colagem.png"), size=(30,30))

paste = ctk.CTkButton(window,
                        command=colar,
                        width=20,
                        height=20,
                        text="",
                        font=("arial",12,'bold'),
                        image=(img_paste),
                        fg_color="transparent")
paste.place(x=300,y=1)

saida = ctk.CTkLabel(window, text='', width=200)
saida.place(x=30, y=90)

window.mainloop()