#Elean Rivas 19062
#Redes 2023
'''
Class with the functionalities of an XMPP protocol
Call of libraries and plugins
'''


#Import of libraries
from slixmpp.exceptions import IqError, IqTimeout
from slixmpp.xmlstream.stanzabase import ET, ElementBase 
import slixmpp


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




#----------------------------------------------
#Login class
#----------------------------------------------

#----------------------------------------------
#Delete account class
#----------------------------------------------


#----------------------------------------------
#Contacts and information class
#----------------------------------------------


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