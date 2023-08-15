#Elean Rivas 19062
#Redes 2023
'''
Class with the functionalities of an XMPP protocol
Call of libraries and plugins
'''


#Import of libraries
import sys
import logging
from slixmpp.exceptions import IqError, IqTimeout
from slixmpp.xmlstream.stanzabase import ET, ElementBase 
import slixmpp
import base64, time
import threading
#----------------------------------------------
#Register class
#----------------------------------------------
class RyE(slixmpp.ClientXMPP):
    def __init__(self, jid, password):
        slixmpp.ClientXMPP.__init__(self, jid, password)

        self.user = jid
        self.add_event_handler("session_start", self.start)
        self.add_event_handler("register", self.register)

    def start(self, event):
        self.send_presence()
        self.get_roster()
        self.disconnect()

    def register(self, iq):
        iq = self.Iq()
        iq['type'] = 'set'
        iq['register']['username'] = self.boundjid.user
        iq['register']['password'] = self.password

        try:
            iq.send()
            print("Nueva Cuenta Creada", self.boundjid,"\n")
        except IqError as e:
            print("Error en Registro ", e,"\n")
            self.disconnect()
        except IqTimeout:
            print("Timeout en el servidor")
            self.disconnect()
        except Exception as e:
            print(e)
            self.disconnect()
#Clase hecha con la ayuda de copilot



#----------------------------------------------
#Login class
#----------------------------------------------

#----------------------------------------------
#Delete account class
#----------------------------------------------
class Del(slixmpp.ClientXMPP):
    def __init__(self, jid, password):
        slixmpp.ClientXMPP.__init__(self, jid, password)

        self.user = jid
        self.add_event_handler("session_start", self.start)

    def start(self, event):
  
        self.send_presence()
        self.get_roster()

        delete = self.Iq()
        delete['type'] = 'set'
        delete['from'] = self.user
        fragment = ET.fromstring("<query xmlns='jabber:iq:register'><remove/></query>")
        delete.append(fragment)

        try:
            delete.send()
            print("Cuenta Borrada")
        except IqError as e:
           
            print("Error", e)
        except IqTimeout:

            print("timeout del server")
        except Exception as e:
     
            print(e)  

        self.disconnect()


#----------------------------------------------
#Contacts and information class
#----------------------------------------------
class Roster(slixmpp.ClientXMPP):
    def __init__(self, jid, password, user=None, show=True, message=""):
        slixmpp.ClientXMPP.__init__(self, jid, password)
        self.add_event_handler("session_start", self.start)
        self.presences = threading.Event()
        self.contacts = []
        self.user = user
        self.show = show
        self.message = message

    async def start(self, event):
        self.send_presence()
        await self.get_roster()

        my_contacts = []
        try:
            self.get_roster()
        except IqError as e:
            print("Error", e)
        except IqTimeout:
            print("Timeout en el Server")
        
        self.presences.wait(3)

        my_roster = self.client_roster.groups()
        for group in my_roster:
            for user in my_roster[group]:
                status = show = answer = priority = ''
                self.contacts.append(user)
                subs = self.client_roster[user]['subscription']
                conexions = self.client_roster.presence(user)
                username = self.client_roster[user]['name'] 
                for answer, pres in conexions.items():
                    if pres['show']:
                        show = pres['show']
                    if pres['status']:
                        status = pres['status']
                    if pres['priority']:
                        status = pres['priority']

                my_contacts.append([
                    user,
                    subs,
                    status,
                    username,
                    priority
                ])
                self.contacts = my_contacts

        if(self.show):
            if(not self.user):
                if len(my_contacts)==0:
                    print('No hay usuarios conectados')
                else:
                    print('Usuarios: \n')
                for contact in my_contacts:
                    print('\tusuario:' , contact[0] , '\t\tStatus:' , contact[2])
            else:
                print('\n\n')
                for contact in my_contacts:
                    if(contact[0]==self .user):
                        print('\tUsuario:' , contact[0] , '\n\tStatus:' , contact[2] , '\n\tNombre:' , contact[3])
        else:
            for JID in self.contacts:
                self.notification_(JID, self.message, 'active')

        self.disconnect()

    def notification_(self, to, body, my_type):

        message = self.Message()
        message['to'] = to
        message['type'] = 'chat'
        message['body'] = body

        if (my_type == 'active'):
            fragmentStanza = ET.fromstring("<active xmlns='http://jabber.org/protocol/chatstates'/>")
        elif (my_type == 'composing'):
            fragmentStanza = ET.fromstring("<composing xmlns='http://jabber.org/protocol/chatstates'/>")
        elif (my_type == 'inactive'):
            fragmentStanza = ET.fromstring("<inactive xmlns='http://jabber.org/protocol/chatstates'/>")
        message.append(fragmentStanza)

        try:
            message.send()
        except IqError as e:
            print("Error", e)
        except IqTimeout:
            print("Timeout en el servidor")

#----------------------------------------------
#Add contacts class
#----------------------------------------------

#----------------------------------------------
#Send messages class
#----------------------------------------------


#----------------------------------------------
#grupal chat class
#----------------------------------------------


#----------------------------------------------
#send files class
#----------------------------------------------


#----------------------------------------------
#Notifications class
#----------------------------------------------