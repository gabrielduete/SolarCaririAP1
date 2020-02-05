from tkinter import *
def cad_cliente():
    janela_clientes = Tk()
    janela_clientes.title("Solar Cariri Simulator")
    janela_clientes.geometry('370x350+400+200')
    janela_clientes.resizable(width=False, height=False)
    bg_clientes = PhotoImage(file = r'bg_clientes.png')
    bgclientes = Label(janela_clientes, image=bg_clientes).pack()
    def novo_cliente():
        lista_clientes.insert(END, inserir_cliente.get())
    def ok_salvar():
        janela_clientes.destroy()
    lista_clientes = Listbox(janela_clientes, width = 56, cursor='hand2')
    lista_clientes.place(x=14, y=70)
    client = (ed_nome.get())
    clientes = [client]
    for clientes in clientes:
        lista_clientes.insert(END,clientes)
    inserir_cliente=StringVar()
    ed_ins_cliente=Entry(janela_clientes, textvariable=inserir_cliente)
    ed_ins_cliente.place(x=150, y=242)
    bt_cadastrar_clientes = Button(janela_clientes, text='Cadastrar', width=8, cursor='hand2', bg='#E6E6E6', bd='3', command=novo_cliente).place(x=287, y=238)
    bt_clientes_ok = Button(janela_clientes, text='OK', width=4, cursor='hand2', bg='#E6E6E6', bd='3', command=ok_salvar).place(x=170, y=310)
    janela_clientes.iconbitmap(r'solar_icon.ico')
    janela_clientes.mainloop()
cad_cliente()
