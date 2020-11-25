from enum import Enum

SEARCH_NAME = 'search_name'
SEARCH_CONTENT = 'search_content'
DOWNLOAD = 'download'
UPLOAD = 'upload'
LOGIN = 'login'
LOGOUT = 'logout'
LIST = 'list'

class STATE:
    def __init__(self):
        self.CONNECTED = 'CONNECTED'
        self.AUTHENTICATED = 'AUTHENTICATED'
        self.ADMIN = 'ADMIN'
        self.EXIT = 'EXIT'

class STATUS:
    def __init__(self):
        self.OK = 'OK'
        self.ERROR = 'ERROR'
        self.PARAMNULL = 'PARAMNULL'

class MESSAGES:
    def __init__(self):
        self.LOGIN = 'LOGIN'
        self.LOGINREPLY = 'LOGINREPLY'
        self.ADMINLOGINREPLY = 'ADMINLOGINREPLY'
        self.LOGOUT = 'LOGOUT'
        self.LOGOUTREPLY = 'LOGOUTREPLY'
        self.ADDCANDIDATO = 'ADDCANDIDATO'
        self.ADDCANDIDATOREPLY = 'ADDCANDIDATOREPLY'
        self.STARTVOTE = 'STARTVOTE'
        self.STARTVOTEREPLY = 'STARTVOTEREPLY'
        self.LISTCANDIDATOS = 'LISTCANDIDATOS'
        self.LISTCANDIDATOSREPLY = 'LISTCANDIDATOSREPLY'
        self.ENDVOTE = 'ENDVOTE'
        self.ENDVOTEREPLY = 'ENDVOTEREPLY'
        self.CONSULTRESULT = 'CONSULTRESULT'
        self.CONSULTRESULTREPLY = 'CONSULTRESULTREPLY'
        self.VOTE = 'VOTE'
        self.VOTEREPLY = 'VOTEREPLY'