import tkinter as tk
from tkinter import messagebox

fields = ('NOMBRE COMPLETO', 'IDENTIFICACION' , 'TELEFONO', 'DIRECCION', 'CORREO')
search = ('BUSCAR POR CEDULA\RUC', 'BUSCAR POR NOMBRE')
clientes = {}

def agregarCliente(entries):
    if entries['NOMBRE COMPLETO'].get() != '' and entries['IDENTIFICACION'].get() != '' and entries['TELEFONO'].get() != '' and entries['DIRECCION'].get() != '' and entries['CORREO'].get() != '':
        nombreCompleto = entries['NOMBRE COMPLETO'].get()
        if v.get() == 0:
            tipo = 'RUC'
        else:
            tipo = 'CEDULA'
        identi = entries['IDENTIFICACION'].get()
        telefono = entries['TELEFONO'].get()
        direccion = entries['DIRECCION'].get()
        correo = entries['CORREO'].get()
        if identi not in clientes:
            messagebox.showinfo("Aviso", 'Registro Exitoso.')
            clientes[identi] = [nombreCompleto, tipo, identi, telefono, direccion, correo]
            print(clientes)
        else:
            messagebox.showinfo("Aviso", 'Ya existe usuario registrado con {2}: {0} y nombres: {1}'.format(identi,clientes[identi][0].upper(),clientes[identi][1]))
    else:
        messagebox.showinfo("Aviso", 'Por favor verifique que todos los campos esten llenos.')


def editarCliente(entries):
    nombreCompleto = entries['NOMBRE COMPLETO'].get()

    print("r", nombreCompleto)

def eliminarCliente(entries):
    nombreCompleto = entries['NOMBRE COMPLETO'].get()

    print("r", nombreCompleto)


def busquedaCedula(cedula):
    cont = 0
    for key in clientes.keys():
        if cedula in clientes[key][2]:
            # NOMBRE COMPLETO, TIPO DE IDENTIFICACION , CEDULA/RUC , TELEFONO, DIRECCION, CORREO
            listbox.insert(tk.END,
                           '| NOMBRE COMPLETO: {0} | TIPO DE IDENTIFICACION: {1} | CEDULA/RUC: {2} | TELEFONO: {3} | DIRECCION: {4} | CORREO: {5} |'.format(
                               clientes[key][0], clientes[key][1], clientes[key][2], clientes[key][3], clientes[key][4],
                               clientes[key][5]))
            cont += 1
            print(clientes[key])
    messagebox.showinfo("Aviso", 'Numero de usuarios encontrados: ' + str(cont))

def busquedaNombre(nombre):
    cont = 0
    for key in clientes.keys():
        if nombre in clientes[key][0]:
            # NOMBRE COMPLETO, TIPO DE IDENTIFICACION , CEDULA/RUC , TELEFONO, DIRECCION, CORREO
            listbox.insert(tk.END, '| NOMBRE COMPLETO: {0} | TIPO DE IDENTIFICACION: {1} | CEDULA/RUC: {2} | TELEFONO: {3} | DIRECCION: {4} | CORREO: {5} |'.format(clientes[key][0],clientes[key][1],clientes[key][2],clientes[key][3],clientes[key][4],clientes[key][5]))
            cont +=1
            print(clientes[key])
    messagebox.showinfo("Aviso", 'Numero de usuarios encontrados: '+str(cont))

def busquedaTotal(nom,ced):
    if nom == '' and ced == '':
        for key in clientes.keys():
            listbox.insert(tk.END, '| NOMBRE COMPLETO: {0} | TIPO DE IDENTIFICACION: {1} | CEDULA/RUC: {2} | TELEFONO: {3} | DIRECCION: {4} | CORREO: {5} |'.format(clientes[key][0],clientes[key][1],clientes[key][2],clientes[key][3],clientes[key][4],clientes[key][5]))
            print(clientes[key])


def buscarClientes(entries):
    ced = entries['BUSCAR POR CEDULA\RUC'].get()
    nom = entries['BUSCAR POR NOMBRE'].get()
    listbox.delete(0,tk.END)

    if ced != '':
        busquedaCedula(ced)

    elif nom != '':
        busquedaNombre(nom)
    else:
        busquedaTotal(nom, ced)

def makeform(root, fields):
    entries = {}
    for field in fields:
        print(field)
        row = tk.Frame(root)
        lab = tk.Label(row, width=22, text=field + ": ", anchor='w')
        ent = tk.Entry(row)
        ent.winfo_name()
        ent.insert(0, "")
        row.pack(side=tk.TOP,
                 fill=tk.X,
                 padx=10,
                 pady=10)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.RIGHT,
                 expand=tk.YES,
                 fill=tk.X)
        entries[field] = ent

    return entries

def makeformSearch(root, fields):
    entries = {}
    for field in fields:
        print(field)
        row = tk.Frame(root)
        lab = tk.Label(row, width=22, text=field + ": ", anchor='w')
        ent = tk.Entry(row)

        ent.insert(0, "")
        row.pack(side=tk.TOP,
                 fill=tk.X,
                 padx=10,
                 pady=10)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.RIGHT,
                 expand=tk.YES,
                 fill=tk.X)
        entries[field] = ent

    return entries

def ShowChoice():
    print(v.get())


def CurSelet(event):
    w = event.widget
    index = list(w.curselection())
    if len(index) != 0:
        value = w.get(index[0])
        tipo = value.strip('|').split('|')[1].split(':')[1].strip(' ')
        if tipo == 'CEDULA':
            v.set(1)
        else:
            v.set(0)
        cedula = value.strip('|').split('|')[2].split(':')[1].strip(' ')

        lista = clientes[cedula]

        ents['NOMBRE COMPLETO'].delete(0, 'end')
        ents['IDENTIFICACION'].delete(0, 'end')
        ents['TELEFONO'].delete(0, 'end')
        ents['DIRECCION'].delete(0, 'end')
        ents['CORREO'].delete(0, 'end')

        ents['NOMBRE COMPLETO'].insert(0, lista[0])
        ents['IDENTIFICACION'].insert(0, lista[2])
        ents['TELEFONO'].insert(0, lista[3])
        ents['DIRECCION'].insert(0, lista[4])
        ents['CORREO'].insert(0, lista[5])
        print(cedula)


if __name__ == '__main__':
    root = tk.Tk()
    root.title('3DSBPRINTING SYSTEM')
    root.geometry('800x700')

    languages = [("RUC"), ("CEDULA")]



    v = tk.IntVar()
    v.set(1)
    row = tk.Frame(root)
    tk.Label(row,
             text='TIPO DE IDENTIFICACION: ',
             width=22,anchor='w').pack(side=tk.LEFT)

    for val, language in enumerate(languages):
        tk.Radiobutton(row,
                       text=language,
                       padx=20,
                       variable=v,
                       command=ShowChoice,
                       value=val).pack(anchor=tk.W)
    row.pack(side=tk.TOP,
             fill=tk.X,
             padx=10,
             pady=10)


    def nuevoCliente(entries):
        entries['NOMBRE COMPLETO'].delete(0,'end')
        v.set(1)
        identi = entries['IDENTIFICACION'].delete(0,'end')
        telefono = entries['TELEFONO'].delete(0,'end')
        direccion = entries['DIRECCION'].delete(0,'end')
        correo = entries['CORREO'].delete(0,'end')

    ents = makeform(root, fields)

    row3 = tk.Frame(root)
    row3.pack(side=tk.TOP,
             fill=tk.X,
             padx=10,
             pady=10)

    #Nuevo
    b1 = tk.Button(row3, text='Nuevo',
           command=(lambda e=ents: nuevoCliente(e)))
    b1.pack(side=tk.LEFT, padx=5, pady=5)

    #Agregar
    b2 = tk.Button(row3, text='Agregar',
           command=(lambda e=ents: agregarCliente(e)))
    b2.pack(side=tk.LEFT, padx=5, pady=5)

    #Editar
    b3 = tk.Button(row3, text='Editar',
                   command=(lambda e=ents: monthly_payment(e)))
    b3.pack(side=tk.LEFT, padx=5, pady=5)

    #Eliminar
    b4 = tk.Button(row3, text='Eliminar',
                   command=(lambda e=ents: monthly_payment(e)))
    b4.pack(side=tk.LEFT, padx=5, pady=5)

    #Salir del programa
    b5 = tk.Button(row3, text='Quit', command=root.quit)
    b5.pack(side=tk.LEFT, padx=5, pady=5)

    row2 = tk.Frame(root)
    entsSearch = makeformSearch(row2, search)

    scrollbar = tk.Scrollbar(row2, orient="vertical")
    scrollbarx = tk.Scrollbar(row2, orient="horizontal")

    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    scrollbarx.pack(side=tk.BOTTOM, fill=tk.X)

    listbox = tk.Listbox(row2,background="Black",  yscrollcommand=scrollbar.set,xscrollcommand=scrollbarx.set,fg="white", selectbackground="Blue", highlightcolor="Blue")
    listbox.pack(side=tk.BOTTOM, fill=tk.X,
             padx=10,
             pady=10)
    listbox.bind('<<ListboxSelect>>',CurSelet)

    scrollbar.config(command=listbox.yview)
    scrollbarx.config(command=listbox.xview)

    b6 = tk.Button(row2, text='Buscar', command=(lambda e=entsSearch: buscarClientes(e)))
    b6.pack(side=tk.RIGHT, padx=5, pady=5)
    row2.pack(
             fill=tk.X,
             padx=10,
             pady=10)
    root.mainloop()
#NOMBRE COMPLETO, TIPO DE IDENTIFICACION , CEDULA/RUC , TELEFONO, DIRECCION, CORREO
