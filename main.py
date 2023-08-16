#Elean Rivas 19062
#Redes 2023
'''
Client Main class, implement the rest of the classes and make the calls
Implementation through CLI
'''

from XmppProtocol import RyE, Roster, MSG, Grupo, Archivos, Noti, Del, Agregar
from getpass import getpass

#Menu
def menu():
    print("+------------------------------------+")
    print("|    Bienvendio ¿que deseas hacer?   |")
    print("|    ░░░░░░░░░▄░░░░░░░░░░░░░░▄░░░░   |")
    print("|    ░░░░░░░░▌▒█░░░░░░░░░░░▄▀▒▌░░░   |")
    print("|    ░░░░░░░░▌▒▒█░░░░░░░░▄▀▒▒▒▐░░░   |")
    print("|    ░░░░░░░▐▄▀▒▒▀▀▀▀▄▄▄▀▒▒▒▒▒▐░░░   |")
    print("|    ░░░░░▄▄▀▒░▒▒▒▒▒▒▒▒▒█▒▒▄█▒▐░░░   |")
    print("|    ░░░▄▀▒▒▒░░░▒▒▒░░░▒▒▒▀██▀▒▌░░░   |")
    print("|    ░░▐▒▒▒▄▄▒▒▒▒░░░▒▒▒▒▒▒▒▀▄▒▒▌░░   |")
    print("|    ░░▌░░▌█▀▒▒▒▒▒▄▀█▄▒▒▒▒▒▒▒█▒▐░░   |")
    print("|    ░▐░░░▒▒▒▒▒▒▒▒▌██▀▒▒░░░▒▒▒▀▄▌░   |")
    print("|    ░▌░▒▄██▄▒▒▒▒▒▒▒▒▒░░░░░░▒▒▒▒▌░   |")
    print("|    ▐▒▀▐▄█▄█▌▄░▀▒▒░░░░░░░░░░▒▒▒▐░   |")
    print("|    ▐▒▒▐▀▐▀▒░▄▄▒▄▒▒▒▒▒▒░▒░▒░▒▒▒▒▌░  |")
    print("|    ▐▒▒▒▀▀▄▄▒▒▒▄▒▒▒▒▒▒▒▒░▒░▒░▒▒▐░░  |")
    print("|    ░▌▒▒▒▒▒▒▀▀▀▒▒▒▒▒▒░▒░▒░▒░▒▒▒▌░░  |")
    print("|    ░▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒░▒░▒▒▄▒▒▐░    |")
    print("|    ░░▀▄▒▒▒▒▒▒▒▒▒▒▒░▒░▒░▒▄▒▒▒▒▌░    |")
    print("|    ░░░░▀▄▒▒▒▒▒▒▒▒▒▒▄▄▄▀▒▒▒▒▄▀░░    |")
    print("|    ░░░░░░▀▄▄▄▄▄▄▀▀▀▒▒▒▒▒▄▄▀░░░░    |")
    print("|    ░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▀▀░░░░░░░░   |")
    print("+------------------------------------+")
    print("+------------------------------------+")
    print("PRESIONE 1 PARA INGRESAR EN EL SERVIDOR DE ALUMCHAT")
    print("PRESIONE 2 PARA REGISTRARSE EN EL SERVIDOR DE ALUMCHAT")
    print("PRESIONE 3 PARA SALIR")
    print("")
    op = input("Opcion: ")
    print("======================================================")
    print("")
    print("")
    print("")

    usu = ""
    psd = ""


    #inicio de ciclo solicitud de usuario y contrasenia
    while (op != "3"):
        #login
        if(op== "1"):
            usu = input("Ingrese usuario: ")
            psd = getpass("Ingrese contraseña: ")
        #registro
        elif(op == "2"):
            usu = input("Ingrese nuevo usuario: ")
            psd = getpass("Ingrese contraseña: ")
            xmpp = RyE(usu, psd)
            xmpp.register_plugin('xep_0030') ### Service Discovery
            xmpp.register_plugin('xep_0004') ### Data Forms
            xmpp.register_plugin('xep_0066') ### Band Data
            xmpp.register_plugin('xep_0077') ### Band Registration
            xmpp.connect()
            xmpp.process(forever=False)
            print("Registro Completado\n")
        else:
            print("Opcion invalida intente denuevo")
        #opciones
        print("")
        print("-----------------------------------------------")
        print("Presione 1 para mostrar contactos")
        print("Presione 2 para agregar contactos")
        print("Presione 3 para mostrar detalles de un contacto")
        print("Presione 4 para entrar a un chat 1 a 1")
        print("Presione 5 para entrar a un chat grupal")
        print("Presione 6 para cambiar mensaje de presencia")
        print("Presione 7 para enviar y recibir archivos")
        print("Presione 8 para notificaciones")
        print("Presione 9 para eliminar cuenta")
        print("Presione 10 para cerrar sesion")
        print("-----------------------------------------------")
        print("")

        op2  = input("")

        #ciclo de login     
        while(op2 != "10"):
            #get contacts
            if(op2 =="1"):
                xmpp = Roster(usu, psd)
                xmpp.register_plugin('xep_0030') # Service Discovery
                xmpp.register_plugin('xep_0199') # XMPP Ping
                xmpp.register_plugin('xep_0045') # Mulit-User Chat (MUC)
                xmpp.register_plugin('xep_0096') # Jabber Search
                xmpp.connect()
                xmpp.process(forever=False)
            #add contacts
            elif(op2 == "2"):
                con = input("Escriba el Usuario del contacto: ") 
                xmpp = Agregar(usu, psd, con)
                xmpp.register_plugin('xep_0030') # Service Discovery
                xmpp.register_plugin('xep_0199') # XMPP Ping
                xmpp.register_plugin('xep_0045') # Mulit-User Chat (MUC)
                xmpp.register_plugin('xep_0096') # Jabber Search
                xmpp.connect()
                xmpp.process(forever=False)

            #contact details
            elif(op2 == "3"):
                con = input("Escriba el Usuario del contacto: ") 
                xmpp = Roster(usu, psd, con)
                xmpp.register_plugin('xep_0030') # Service Discovery
                xmpp.register_plugin('xep_0199') # XMPP Ping
                xmpp.register_plugin('xep_0045') # Mulit-User Chat (MUC)
                xmpp.register_plugin('xep_0096') # Jabber Search
                xmpp.connect()
                xmpp.process(forever=False)

            #1 on 1
            elif(op2 == "4"):
                try:
                        cont = input("Ingrese el recipiente: ") 
                        msg = input("Mensaje: ")
                        xmpp = MSG(usu, psd, cont, msg)
                        xmpp.register_plugin('xep_0030') # Service Discovery
                        xmpp.register_plugin('xep_0199') # XMPP Ping
                        xmpp.register_plugin('xep_0045') # Mulit-User Chat (MUC)
                        xmpp.register_plugin('xep_0096') # Jabber Search
                        xmpp.connect()
                        xmpp.process(forever=False)
                except KeyboardInterrupt as e:
                        print('Conversacion finalizada')
                        xmpp.disconnect()
            #grupo chat
            elif(op2 == "5"):

                try:
                        gr = input("Escriba el JID del grupo: ") 
                        nom = input("Escriba su alias en el grupo: ")
                        if '@conference.alumchat.xyz' in gr:
                            xmpp = Grupo(usu, psd, gr, nom)
                            xmpp.register_plugin('xep_0030')
                            xmpp.register_plugin('xep_0045')
                            xmpp.register_plugin('xep_0199')
                            xmpp.connect()
                            xmpp.process(forever=False)
                except KeyboardInterrupt as e:
                        print('Chat Grupal Finalizado')
                        xmpp.disconnect()
                        
            #presence
            elif(op2 == "6"):
                msg = input("indique su mensaje de presencia: ") 
                xmpp = Roster(usu, psd, show=False, message=msg)
                xmpp.register_plugin('xep_0030') # Service Discovery
                xmpp.register_plugin('xep_0199') # XMPP Ping
                xmpp.register_plugin('xep_0045') # Mulit-User Chat (MUC)
                xmpp.register_plugin('xep_0096') # Jabber Search
                xmpp.connect()
                xmpp.process(forever=False)
            #Files. NOt working
            elif(op2 == "7"):
                para = input("Indique el usuario al que quiere enviar: ") 
                file = input("Direccion del archivo: ") 
                xmpp = Archivos(usu, psd, para, file)
                xmpp.register_plugin('xep_0030') # Service Discovery
                xmpp.register_plugin('xep_0065') # SOCKS5 Bytestreams
                xmpp.connect()
                xmpp.process(forever=False)

            #notifications
            elif(op2 == "8"):
                
                try:
                        
                        para = input("Ingrese el recipiente: ") 
                        msg = input("Mensaje: ")
                        ty = input("Type: ")
                        xmpp = Noti(usu, psd, para, msg, ty)
                        xmpp.register_plugin('xep_0030') # Service Discovery
                        xmpp.register_plugin('xep_0199') # XMPP Ping
                        xmpp.register_plugin('xep_0045') # Mulit-User Chat (MUC)
                        xmpp.register_plugin('xep_0096') # Jabber Search
                        xmpp.connect()
                        xmpp.process(forever=False)
                except KeyboardInterrupt as e:
                        print('Notificaciones finalizadas')
                        xmpp.disconnect()
            #eliminar cuenta
            elif(op2 == "9"):
                
                xmpp = Del(usu, psd)
                xmpp.register_plugin('xep_0030') # Service Discovery
                xmpp.register_plugin('xep_0004') # Data forms
                xmpp.register_plugin('xep_0066') # Out-of-band Data
                xmpp.register_plugin('xep_0077') # In-band Registration
                xmpp.connect()
                xmpp.process()
                xmpp = None
                control = False
                break


            else:
                print("Opcion invalida intente denuevo")


            print("")
            print("-----------------------------------------------")
            print("Presione 1 para mostrar contactos")
            print("Presione 2 para agregar contactos")
            print("Presione 3 para mostrar detalles de un contacto")
            print("Presione 4 para entrar a un chat 1 a 1")
            print("Presione 5 para entrar a un chat grupal")
            print("Presione 6 para cambiar mensaje de presencia")
            print("Presione 7 para enviar y recibir archivos")
            print("Presione 8 para notificaciones")
            print("Presione 9 para eliminar cuenta")
            print("Presione 10 para cerrar sesion")
            print("-----------------------------------------------")
            print("")
            

            op2  = input("")
            
        print("")
        print("======================================================")
        print("BIENVENIDO AL CHAT")
        print("PRESIONE 1 PARA INGRESAR EN EL SERVIDOR DE ALUMCHAT")
        print("PRESIONE 2 PARA REGISTRARSE EN EL SERVIDOR DE ALUMCHAT")
        print("PRESIONE 3 PARA SALIR")
        print("")
        op = input("Opcion: ")
        print("======================================================")
        print("")
        print("")
        print("")

    print("GRACIAS HASTA LUEGO")

menu()
