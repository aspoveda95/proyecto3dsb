listaCompradores = []
dicGeneral = {}
dic = {}
listaGeneral = []

def buscarPorNombre(nombreBuscar):
    for indice in range(len(listaCompradores)):
        if nombreBuscar.upper() in listaCompradores[indice].upper():
            return indice
        else:
            return -1

def buscarVentasPorUsuario():
    for ident in dic.keys():
        cont = 0
        for i in lineas[1:]:
            temp = i.rstrip('\n').split(';')
            identificacion = temp[37].strip('"')
            if ident == identificacion:
                cont = cont + 1
        dic[ident][-1] = cont

def buscarIdentificacion(ident):
    if ident in dic:
        return ident.rstrip(' ')
    else:
        return 0

def limpiar():
    for i in range(50):
        print('')

def buscarVentasPorIdentificacion():
    identi = buscarIdentificacion(input('Ingrese numero de identificacion: '))
    if identi != 0:
        print('{9}{0:16}{9} {9}{1:15}{9} {9}{2:120}{9} {9}{3:75}{9} {9}{4:20}{9} {9}{5:15}{9} {9}{6:150}{9} {9}{7:12}{9} {9}{8:30}{9}'.format('FECHA DE EMISION','CODIGO PRODUCTO','DESCRIPCION PRODUCTO','COMPRADOR',
                                                                               'TIPO IDENTIFICACION','IDENTIFICACION','DIRECCION','TELEFONO',
                                                                               'CORREO','|'))
        for i in lineas[1:]:
            temp = i.rstrip('\n').split(';')
            fecha = temp[1].strip('"')
            codigo = temp[3].strip('"')
            descripcion = temp[4].strip('"')
            comprador = temp[35].strip('"').upper()
            tipoIdentificacion = temp[36].strip('"')
            identificacion = temp[37].strip('"')
            direccion = temp[38].strip('"').upper()
            telefono = temp[39].strip('"')
            correo = temp[40].strip('"')

            if identi == identificacion:
                print('{9}{0:16}{9} {9}{1:15}{9} {9}{2:120}{9} {9}{3:75}{9} {9}{4:20}{9} {9}{5:15}{9} {9}{6:150}{9} {9}{7:12}{9} {9}{8:30}{9}'.format(fecha,codigo,descripcion, comprador, tipoIdentificacion, identificacion, direccion, telefono, correo,'|'))

    else:
        print('*** Identificacion no encontrada ***')

def hero():
    print('''
    ==========================================================================================================================================
    =======       =======          =========         ======           ========================================================================
    =====  ======   =====  ========  =====  ========  =====  =======  ========================================================================
    ====   =====   ======  ========= =====  ===============  ======   ========================================================================
    ===========  ========  ========= =======        =======       ============================================================================
    ====   =====   ======  ========= ===============  =====  ======  =========================================================================
    =====  ======   =====  ========  ======  =======  =====  ======   ========================================================================
    =======       =======           =======         =======          =========================================================================
    ==========================================================================================================================================
    ==============================         ==         ===  ==   ===  ==          ==  ==    ===  ===        ===================================
    ==============================  =====  ==  =====  ===  ==  = ==  ======  ======  ==  == ==  ==  ==========================================
    ==============================  =====  ==  ====  ====  ==  == =  ======  ======  ==  === =  ==  ==========================================
    ==============================  =========  =====  ===  ==  ===   ======  ======  ==  ====   ==  ======  ==================================
    ==============================  =========  ======  ==  ==  ====  ======  ======  ==  =====  ===       ====================================
    ==========================================================================================================================================
    ''')

validar = True

while validar:
    print('''
    ==========================================================================================================================================
    =       1.- Escribir nombre de archivo                                                                                                   =
    =       2.- Visualizar fecha de ultima compra de cada cliente y el numero de compras totales realizadas                                  =
    =       3.- Buscar ventas por nombre                                                                                                     = 
    =       4.- Buscar ventas por identificacion                                                                                             =
    =       5.- Salir                                                                                                                        =
    ===========================================================================================================================================
    ''')
    op = input('Ingresar opcion: ')
    if op.isdigit() and int(op) >= 0 and int(op) <= 5:
        op = int(op)
        if op == 1:
            try:
                nomArchivo = input('Ingrese el nombre del archivo a leer con su extension (Ej: facturacion.csv): ')
                archivo = open(nomArchivo, 'r', encoding='utf-8')
                lineas = archivo.readlines()
                encabezados = lineas[0].rstrip('\n').split(';')
                prueba = lineas[1].split(';')
                # print(encabezados[35:])

                for i in lineas[1:]:
                    temp = i.rstrip('\n').split(';')
                    fecha = temp[1].strip('"')
                    codigo = temp[3].strip('"')
                    descripcion = temp[4].strip('"')
                    comprador = temp[35].strip('"').upper()
                    tipoIdentificacion = temp[36].strip('"')
                    identificacion = temp[37].strip('"')
                    direccion = temp[38].strip('"').upper()
                    telefono = temp[39].strip('"')
                    correo = temp[40].strip('"')

                    if identificacion not in listaCompradores:
                        listaCompradores.append(identificacion)
                        lista = [fecha, comprador, tipoIdentificacion, identificacion, direccion, telefono, correo, 0]
                        dic[identificacion] = lista
                    # print(temp[35:])
                archivo.close()
            except:
                print("*** Nombre de archivo incorrecto ***")


        elif op == 2:
            buscarVentasPorUsuario()
            print(
                '{8}{0:22}{8} {8}{1:75}{8} {8}{2:20}{8} {8}{3:30}{8} {8}{4:150}{8} {8}{5:25}{8} {8}{6:50}{8} {8}{7:30}{8}'.format(
                    'FECHA DE ULTIMA COMPRA', 'COMPRADOR',
                    'TIPO IDENTIFICACION', 'IDENTIFICACION', 'DIRECCION', 'TELEFONO',
                    'CORREO','NUMERO DE COMPRAS TOTALES', '|'))
            for key in dic.keys():
                print(
                    '{8}{0:22}{8} {8}{1:75}{8} {8}{2:20}{8} {8}{3:30}{8} {8}{4:150}{8} {8}{5:25}{8} {8}{6:50}{8} {8}{7:30}{8}'.format(
                        dic[key][0], dic[key][1],
                        dic[key][2], dic[key][3], dic[key][4], dic[key][5],
                        dic[key][6], dic[key][7], '|'))
            input('*** Presione ENTER para continuar ***')
        elif op == 3:
            ind = buscarPorNombre(input('Ingresar nombre: '))
            if ind != -1:
                print(listaCompradores[ind])
            else:
                print('*** Usuario no encontrado ***')
        elif op == 4:
            buscarVentasPorIdentificacion()
        elif op == 5:
            validar = False
            print('*** Programo finalizado ***')
    else:
        print('*** Ingresa una opcion correcta ***')
