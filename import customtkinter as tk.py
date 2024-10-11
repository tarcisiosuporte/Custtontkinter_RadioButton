import customtkinter as ctk

 
tela=ctk.CTk()
tela.title("Minha Aplicação Tkinter")  
tela.geometry("300x200")  
tela.resizable(False,False)
_font = ('Arial',14)


#varbut = ctk.StringVar(value="")
#varbut = True
#varbut1=StringVar()
#varbut2=StringVar()


def radio_event():
    v = varbut.get()    
    
    #if v == "":
    print(f"a opção é: {v}")
 #   else:
  #      print(f"a opção é: {v}")
    #print(varbut.get())
    pass
varbut = ctk.StringVar(value="")
radiobutton=ctk.CTkRadioButton(tela, text='teste1',command=radio_event, variable=varbut, value='radiobutton', font=_font)
#raciobutton.pack(pady=200, padx=200)    
#radiobutton.place(x=10, y=10)
radiobutton2=ctk.CTkRadioButton(tela, text='teste2', command=radio_event, variable=varbut,value='radiobutton2', font=_font)


#radiobutton2=Radiobutton(tela, text='teste3', variable=varbut, value="opção3", font=_font)
#CTkRadiobutton2.pack()
#radiobutton.place(x=10, y=10)
    # Definindo o tamanho da janela  
 
radiobutton.pack()
radiobutton2.pack()
    
radiobutton.    
print(f"{varbut.get()}")   
    
tela.mainloop()  
